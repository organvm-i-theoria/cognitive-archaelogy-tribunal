"""
File utilities for the Cognitive Tribunal project.
Provides file hashing, classification, and deduplication capabilities.
"""

import os
import hashlib
import mimetypes
from pathlib import Path
from typing import Dict, List, Set, Optional
from datetime import datetime


class FileClassifier:
    """Classifies files by type and purpose."""
    
    FILE_CATEGORIES = {
        'code': ['.py', '.js', '.java', '.cpp', '.c', '.h', '.cs', '.go', '.rs', '.rb', '.php'],
        'document': ['.txt', '.md', '.doc', '.docx', '.pdf', '.odt', '.rtf'],
        'spreadsheet': ['.xlsx', '.xls', '.csv', '.ods'],
        'presentation': ['.ppt', '.pptx', '.odp', '.key'],
        'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'],
        'video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
        'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
        'archive': ['.zip', '.tar', '.gz', '.bz2', '.7z', '.rar', '.xz'],
        'data': ['.json', '.xml', '.yaml', '.yml', '.toml', '.ini', '.cfg'],
        'database': ['.db', '.sqlite', '.sqlite3', '.mdb'],
        'notebook': ['.ipynb'],
        'config': ['.conf', '.config', '.env', '.properties'],
    }
    
    @classmethod
    def classify(cls, file_path: Path) -> str:
        """Classify a file based on its extension."""
        ext = file_path.suffix.lower()
        
        for category, extensions in cls.FILE_CATEGORIES.items():
            if ext in extensions:
                return category
        
        return 'other'
    
    @classmethod
    def get_mime_type(cls, file_path: Path) -> Optional[str]:
        """Get MIME type for a file."""
        mime_type, _ = mimetypes.guess_type(str(file_path))
        return mime_type


class FileHasher:
    """Handles file hashing for deduplication."""
    
    @staticmethod
    def compute_hash(file_path: Path, algorithm: str = 'sha256') -> str:
        """
        Compute hash of a file.
        
        Args:
            file_path: Path to the file
            algorithm: Hash algorithm to use (sha256, md5, etc.)
            
        Returns:
            Hexadecimal hash string
        """
        hash_func = hashlib.new(algorithm)
        
        try:
            with open(file_path, 'rb') as f:
                # Read in chunks to handle large files
                for chunk in iter(lambda: f.read(8192), b''):
                    hash_func.update(chunk)
            return hash_func.hexdigest()
        except (IOError, OSError) as e:
            return f"ERROR: {str(e)}"
    
    @staticmethod
    def compute_quick_hash(file_path: Path) -> str:
        """
        Compute a quick hash based on file size and name.
        Useful for initial deduplication pass.
        """
        try:
            stat = file_path.stat()
            quick_id = f"{file_path.name}_{stat.st_size}_{stat.st_mtime}"
            return hashlib.md5(quick_id.encode()).hexdigest()
        except (IOError, OSError) as e:
            return f"ERROR: {str(e)}"


class Deduplicator:
    """Identifies duplicate files."""
    
    def __init__(self):
        self.hash_to_files: Dict[str, List[Path]] = {}
        self.quick_hash_to_files: Dict[str, List[Path]] = {}
    
    def add_file(self, file_path: Path, compute_full_hash: bool = False):
        """
        Add a file to the deduplication index.
        
        Args:
            file_path: Path to the file
            compute_full_hash: Whether to compute full content hash
        """
        # Quick hash first
        quick_hash = FileHasher.compute_quick_hash(file_path)
        if quick_hash not in self.quick_hash_to_files:
            self.quick_hash_to_files[quick_hash] = []
        self.quick_hash_to_files[quick_hash].append(file_path)
        
        # Full hash if requested or if quick hash collision
        if compute_full_hash or len(self.quick_hash_to_files[quick_hash]) > 1:
            full_hash = FileHasher.compute_hash(file_path)
            if full_hash not in self.hash_to_files:
                self.hash_to_files[full_hash] = []
            self.hash_to_files[full_hash].append(file_path)
    
    def find_duplicates(self) -> Dict[str, List[Path]]:
        """
        Find all duplicate files.
        
        Returns:
            Dictionary mapping hash to list of duplicate file paths
        """
        duplicates = {}
        
        # First check quick hash collisions
        for quick_hash, files in self.quick_hash_to_files.items():
            if len(files) > 1:
                # Verify with full hash
                file_groups: Dict[str, List[Path]] = {}
                for file_path in files:
                    full_hash = FileHasher.compute_hash(file_path)
                    if full_hash not in file_groups:
                        file_groups[full_hash] = []
                    file_groups[full_hash].append(file_path)
                
                # Add groups with actual duplicates
                for full_hash, duplicate_files in file_groups.items():
                    if len(duplicate_files) > 1:
                        duplicates[full_hash] = duplicate_files
        
        return duplicates
    
    def get_stats(self) -> Dict:
        """Get deduplication statistics."""
        total_files = sum(len(files) for files in self.quick_hash_to_files.values())
        unique_quick = len(self.quick_hash_to_files)
        
        duplicates = self.find_duplicates()
        duplicate_count = sum(len(files) - 1 for files in duplicates.values())
        
        return {
            'total_files': total_files,
            'unique_quick_hashes': unique_quick,
            'duplicate_groups': len(duplicates),
            'duplicate_files': duplicate_count,
        }


def extract_file_metadata(file_path: Path) -> Dict:
    """
    Extract metadata from a file.
    
    Args:
        file_path: Path to the file
        
    Returns:
        Dictionary containing file metadata
    """
    try:
        stat = file_path.stat()
        return {
            'name': file_path.name,
            'path': str(file_path.absolute()),
            'size': stat.st_size,
            'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
            'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
            'accessed': datetime.fromtimestamp(stat.st_atime).isoformat(),
            'category': FileClassifier.classify(file_path),
            'mime_type': FileClassifier.get_mime_type(file_path),
            'extension': file_path.suffix.lower(),
        }
    except (IOError, OSError) as e:
        return {
            'name': file_path.name,
            'path': str(file_path.absolute()),
            'error': str(e),
        }
