from __future__ import annotations

import webbrowser
from urllib.parse import urlparse

from ..utils.logger import get_logger


class BrowserAdapter:
    """A thin wrapper around the OS browser to open public URLs."""

    def __init__(self):
        self._log = get_logger(__name__)

    def open_url(self, url: str) -> None:
        if not url or not url.strip():
            raise ValueError("url is required")

        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            raise ValueError("only http/https URLs are supported")

        self._log.info("Opening URL in browser: %s", url)
        webbrowser.open(url)
