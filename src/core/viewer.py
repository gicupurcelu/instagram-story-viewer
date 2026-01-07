from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .loader import StoryLoader, FetchResult
from .parser import StoryParser, StoryItem


class StoryViewerError(Exception):
    """Base exception for viewer-level errors."""


@dataclass(frozen=True)
class ViewOptions:
    """Runtime options for viewing workflows."""
    user_agent: Optional[str] = None
    timeout_seconds: int = 20


class StoryViewer:
    """
    High-level orchestrator for story viewing workflows.

    Design goals:
    - Keep fetching concerns in StoryLoader
    - Keep parsing concerns in StoryParser
    - Keep this class focused on orchestration and safety controls

    Notes:
    - This template intentionally does NOT implement any bypass of authentication,
      private content access, or platform restrictions.
    - Use only with content you are permitted to access.
    """

    def __init__(self, loader: StoryLoader | None = None, parser: StoryParser | None = None):
        self.loader = loader or StoryLoader()
        self.parser = parser or StoryParser()

    def get_profile_snapshot(self, username: str, *, options: ViewOptions | None = None) -> List[StoryItem]:
        """
        Fetches and parses a public profile page into a minimal snapshot.

        This is a safe placeholder that demonstrates architecture.
        """
        opts = options or ViewOptions()
        fetch: FetchResult = self.loader.fetch_public_profile(username=username, user_agent=opts.user_agent, timeout=opts.timeout_seconds)
        try:
            return self.parser.parse_profile_page(fetch)
        except Exception as e:
            raise StoryViewerError(str(e)) from e
