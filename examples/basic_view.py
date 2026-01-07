from src.core.viewer import StoryViewer, ViewOptions
from src.utils.config import Settings

def main():
    settings = Settings()
    viewer = StoryViewer()
    items = viewer.get_profile_snapshot(
        "instagram",
        options=ViewOptions(user_agent=settings.default_user_agent, timeout_seconds=settings.timeout_seconds),
    )
    for item in items:
        print("Source:", item.source_url)
        print("Caption:", item.caption)
        print("Media items:", len(item.media))

if __name__ == "__main__":
    main()
