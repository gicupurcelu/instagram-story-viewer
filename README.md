# Instagram Story Viewer Automation

This repository is a developer-focused template for building tools that work with Instagram story viewing workflows.
It emphasizes a clear architecture (loader → parser → viewer) and includes safe, minimal examples for working with
public profile pages and browser-based viewing.

## What this repo does
- Provides a structured codebase to build an Instagram story viewer tool
- Supports username-based public profile URL handling
- Includes a small downloader utility for direct media URLs you are permitted to download
- Includes example scripts and basic tests

## What this repo does NOT do
- It does not bypass login, private access controls, or platform restrictions
- It does not implement scraping for private stories or accounts

## Quickstart

### Install
```bash
pip install -r requirements.txt
```

### Run examples
```bash
python examples/basic_view.py
python examples/username_view.py
```

### Run tests
```bash
pytest -q
```

## Notes on responsible use
Use this code only with content you are allowed to access and download. Always comply with platform terms and applicable rules.

## License
MIT (see LICENSE).
