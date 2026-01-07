from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Configuration loaded from environment variables."""
    default_user_agent: str = os.getenv("ISV_USER_AGENT", "")
    timeout_seconds: int = int(os.getenv("ISV_TIMEOUT_SECONDS", "20"))
