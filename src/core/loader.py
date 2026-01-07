from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional
import time
import random

import requests

from ..utils.logger import get_logger


class LoaderError(Exception):
    """Raised when fetching fails."""


@dataclass(frozen=True)
class FetchResult:
    """Represents a fetched document."""
    url: str
    status_code: int
    headers: Dict[str, str]
    text: str


class StoryLoader:
    """
    Fetch layer for public pages.

    This is deliberately conservative:
    - No login flows
    - No private content access
    - Basic pacing to reduce accidental aggressive usage
    """

    def __init__(self, *, min_delay_s: float = 0.8, max_delay_s: float = 1.6):
        self._min_delay_s = float(min_delay_s)
        self._max_delay_s = float(max_delay_s)
        self._log = get_logger(__name__)

    def _pace(self) -> None:
        time.sleep(random.uniform(self._min_delay_s, self._max_delay_s))

    def fetch_public_profile(self, *, username: str, user_agent: Optional[str] = None, timeout: int = 20) -> FetchResult:
        if not username or not username.strip():
            raise LoaderError("username is required")

        self._pace()

        url = f"https://www.instagram.com/{username.strip().lstrip('@')}/"
        headers = {"Accept": "text/html,application/xhtml+xml"}
        if user_agent:
            headers["User-Agent"] = user_agent

        try:
            resp = requests.get(url, headers=headers, timeout=timeout)
            return FetchResult(
                url=url,
                status_code=int(resp.status_code),
                headers={k: v for k, v in resp.headers.items()},
                text=resp.text or "",
            )
        except requests.RequestException as e:
            self._log.warning("Fetch failed for %s: %s", url, e)
            raise LoaderError(f"failed to fetch public profile page: {e}") from e
