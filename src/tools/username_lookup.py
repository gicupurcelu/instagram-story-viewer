from __future__ import annotations

import re


class UsernameLookup:
    """Validates usernames and generates public Instagram profile URLs."""

    _USERNAME_RE = re.compile(r"^[A-Za-z0-9._]{1,30}$")

    def normalize(self, username: str) -> str:
        if not username or not username.strip():
            raise ValueError("username is required")
        u = username.strip()
        if u.startswith("@"):
            u = u[1:]
        if not self._USERNAME_RE.match(u):
            raise ValueError("invalid username format")
        return u

    def profile_url(self, username: str) -> str:
        u = self.normalize(username)
        return f"https://www.instagram.com/{u}/"
