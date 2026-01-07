from src.core.parser import StoryParser
from src.core.loader import FetchResult

def test_parse_profile_page_returns_item():
    parser = StoryParser()
    fetch = FetchResult(
        url="https://www.instagram.com/example/",
        status_code=200,
        headers={},
        text="<html><head><title>Example • Instagram photos and videos</title></head><body></body></html>",
    )
    items = parser.parse_profile_page(fetch)
    assert len(items) == 1
    assert "Example" in (items[0].caption or "")
