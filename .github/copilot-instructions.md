---
description: AI rules derived by SpecStory from the project AI interaction history
globs: *
---

## HEADERS

## PROJECT RULES

### General Guidelines
- Follow the principle of least astonishment.
- Write code that is easy to understand and maintain.
- Ensure code is well-documented.

### Code Style
- Adhere to PEP 8 style guidelines for Python.
- Use clear and descriptive names for variables, functions, and classes.
- Keep functions short and focused.

### Markdown Linting
- Fenced code blocks should always have a language specified for syntax highlighting and accessibility. Use `text`, `bash`, or `plaintext` for directory structures.
- Reduce multiple consecutive blank lines to one.
- Ensure lists are surrounded by blank lines.
- Ensure fenced code blocks are surrounded by blank lines.
- Ensure correct spacing after list markers.
- Ensure headings are surrounded by blank lines.
- Avoid multiple headings with the same content.
- The first line should be a top-level heading.
- Use spaces instead of hard tabs.

## TECH STACK

### Core Languages
- Python (version 3.14.0)

### Libraries
- argparse
- pathlib
- setuptools

### Tools
- Trunk
- VS Code

## PROJECT DOCUMENTATION & CONTEXT SYSTEM

### Documentation Guidelines
- All code must be documented with docstrings.
- Use Markdown for all documentation files.
- Diagrams and visual aids should be included where appropriate.

### File Structure
- Configuration files should reside in the root directory.
- Automatically generated configuration files (e.g., `.venv`, `.trunk`, `.vscode`, `.history`, `.github`, `.specstory`) should reside in the root directory.
- All config dot files/folders (`.venv`, `.trunk`, `.vscode`, `.history`, `.github`, `.specstory`) should be gitignored.

## WORKFLOW & RELEASE RULES

### Version Control
- Use Git for version control.
- Follow the branching strategy.
- All changes must be reviewed before merging.

### Branching Strategy
- Use feature branches for new development.
- Merge feature branches into the develop branch.
- Tag releases with version numbers.

### Commit Messages
- Write clear and concise commit messages.
- Use imperative mood in commit messages.

## DEBUGGING

### General Debugging
- Use logging for debugging.
- Use a debugger to step through code.
- Write unit tests to catch errors early.

### VS Code
- To restore a hidden folder in VS Code:
  1. Using Command Palette (⇧⌘P): Press `Cmd+Shift+P`, type "Files: Exclude", select "Preferences: Open User Settings", search for `files.exclude`, and remove or uncheck the pattern for the folder.
  2. Using Settings UI: `Cmd+,` to open Settings, search for "files exclude", look for the hidden folder pattern, and click the X to remove it.
  3. Using Workspace Settings: Open `settings.json` in your project, look for `files.exclude` configuration, and remove the folder pattern.
  4. Show All Files Temporarily: In the Explorer sidebar, click the "..." menu and look for filter options or "Show Excluded Files".

### GitLens Launchpad
- Common GitLens Launchpad issues and solutions:
  1. Sign in to GitHub through GitLens: Open Command Palette (⇧⌘P), type "GitLens: Sign in to GitLens+", and authenticate with GitHub.
  2. Check GitLens is enabled: Open Command Palette (⇧⌘P), type "GitLens: Show Launchpad", and if it doesn't appear, enable GitLens extension.
  3. Refresh connection: Open Command Palette (⇧⌘P), type "GitLens: Reset Stored AI Key", and re-authenticate.
  4. Check for pull requests/issues: Launchpad shows your assigned PRs, reviews, and issues. If you have none, the Launchpad may appear empty.

### Local History Extension
- Local History should be disabled. If it's still generating `` folders:
  1. Uninstall the extension: Open Extensions (⇧⌘X), search "Local History", and click "Uninstall".
  2. Configure it properly:
     - Disabled
     - 0 days limit (no retention)
     - 0 save delay (no auto-save)
     - Path to `` if it does activate
- If `` still regenerates, uninstall the extension entirely.

## CODING TOOLS

### Linters
- Trunk
- markdownlint
- black
- ruff
- bandit
- isort

### VS Code Extensions
- GitLens
- markdownlint

## BEST PRACTICES

- All config dot files/folders (`.venv`, `.trunk`, `.vscode`, `.history`, `.github`, `.specstory`) should be gitignored, tools auto-generate them as needed, and they're hidden from view via VS Code settings. Just let them exist and regenerate naturally.