from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional
import re

from .loader import FetchResult


class ParseError(Exception):
    """Raised when parsing fails."""


@dataclass(frozen=True)
class StoryMedia:
    """Represents a media item (image/video)."""
    media_url: str
    media_type: str  # "image" | "video" | "unknown"


@dataclass(frozen=True)
class StoryItem:
    """Represents a story-like item derived from public content."""
    source_url: str
    caption: Optional[str]
    media: List[StoryMedia]


class StoryParser:
    """
    Parses fetched public pages.

    This parser is intentionally lightweight and conservative. It demonstrates
    where parsing would happen, without implementing scraping logic aimed at
    restricted content.
    """

    _TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)

    def parse_profile_page(self, fetch: FetchResult) -> List[StoryItem]:
        if fetch.status_code >= 400:
            raise ParseError(f"received HTTP {fetch.status_code} for {fetch.url}")

        title_match = self._TITLE_RE.search(fetch.text or "")
        caption = None
        if title_match:
            caption = re.sub(r"\s+", " ", title_match.group(1)).strip()

        return [StoryItem(source_url=fetch.url, caption=caption, media=[])]
