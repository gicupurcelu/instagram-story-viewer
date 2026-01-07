from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .browser_adapter import BrowserAdapter
from ..tools.username_lookup import UsernameLookup


@dataclass(frozen=True)
class OnlineViewOptions:
    open_in_browser: bool = True


class OnlineViewer:
    """
    Convenience layer for web-based viewing workflows.

    This does not scrape stories. It builds a public profile URL and can open it
    in the user's browser.
    """

    def __init__(self, *, browser: BrowserAdapter | None = None, lookup: UsernameLookup | None = None):
        self.browser = browser or BrowserAdapter()
        self.lookup = lookup or UsernameLookup()

    def view_profile(self, username: str, *, options: Optional[OnlineViewOptions] = None) -> str:
        opts = options or OnlineViewOptions()
        url = self.lookup.profile_url(username)
        if opts.open_in_browser:
            self.browser.open_url(url)
        return url
