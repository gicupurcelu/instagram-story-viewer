from src.core.viewer import StoryViewer
from src.core.loader import FetchResult
from src.core.parser import StoryItem

class FakeLoader:
    def fetch_public_profile(self, *, username, user_agent=None, timeout=20):
        return FetchResult(url="https://www.instagram.com/example/", status_code=200, headers={}, text="<title>Example</title>")

class FakeParser:
    def parse_profile_page(self, fetch):
        return [StoryItem(source_url=fetch.url, caption="Example", media=[])]

def test_viewer_orchestrates_loader_and_parser():
    viewer = StoryViewer(loader=FakeLoader(), parser=FakeParser())
    items = viewer.get_profile_snapshot("example")
    assert len(items) == 1
    assert items[0].caption == "Example"
