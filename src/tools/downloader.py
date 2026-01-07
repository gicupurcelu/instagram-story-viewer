from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import requests

from ..utils.logger import get_logger


class DownloadError(Exception):
    """Raised when a download fails."""


@dataclass(frozen=True)
class DownloadResult:
    url: str
    saved_to: str
    bytes_written: int


class Downloader:
    """
    Downloads a file from a *direct* URL.

    IMPORTANT:
    - This downloader does NOT discover or extract Instagram story URLs.
    - Provide only URLs you are permitted to download.
    """

    def __init__(self):
        self._log = get_logger(__name__)

    def download(self, url: str, *, output_dir: str = "downloads", filename: Optional[str] = None, timeout: int = 30) -> DownloadResult:
        if not url or not url.strip():
            raise DownloadError("url is required")

        parsed = urlparse(url.strip())
        if parsed.scheme not in ("http", "https"):
            raise DownloadError("only http/https URLs are supported")

        out_dir = Path(output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        if not filename:
            name = Path(parsed.path).name or "media.bin"
            filename = name

        target = out_dir / filename

        try:
            with requests.get(url, stream=True, timeout=timeout) as r:
                r.raise_for_status()
                bytes_written = 0
                with open(target, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024 * 64):
                        if not chunk:
                            continue
                        f.write(chunk)
                        bytes_written += len(chunk)

            self._log.info("Downloaded %s -> %s (%d bytes)", url, str(target), bytes_written)
            return DownloadResult(url=url, saved_to=str(target), bytes_written=bytes_written)
        except requests.RequestException as e:
            raise DownloadError(f"download failed: {e}") from e
