## 2024-05-23 - Initial Setup
**Vulnerability:** None
**Learning:** Initial setup
**Prevention:** None
## 2024-05-23 - Path Traversal Prevention in Archive Scanner
**Vulnerability:** The `ArchiveScanner` allowed scanning of the filesystem root (/) and critical system directories (e.g., /etc, C:\Windows), which could lead to resource exhaustion or unintentional scanning of sensitive system files.
**Learning:** Relied on `pathlib.Path.resolve()` to normalize paths, but missed explicit checks against known unsafe anchors and system paths.
**Prevention:** Implemented `is_unsafe_path` method with platform-specific blocklists (`UNSAFE_PATHS_POSIX`, `UNSAFE_PATHS_NT`) and a check against the path anchor.
