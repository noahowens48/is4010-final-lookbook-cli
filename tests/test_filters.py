from lookbook.filters import filter_items
from lookbook.models import Item


def fake_item(id, category, season="winter", vibe="streetwear"):
    return Item(
        id=id,
        name=f"Item{id}",
        category=category,
        color="black",
        brand="TestBrand",
        season=season,
        vibe=vibe,
        tags=[],
    )


def test_filter_by_category():
    items = [
        fake_item(1, "top"),
        fake_item(2, "bottom"),
        fake_item(3, "shoes"),
    ]

    tops = filter_items(items, category="top")
    assert len(tops) == 1
    assert tops[0].id == 1


def test_filter_by_season():
    items = [
        fake_item(1, "top", season="winter"),
        fake_item(2, "bottom", season="summer"),
    ]

    winter_items = filter_items(items, season="winter")
    assert len(winter_items) == 1
    assert winter_items[0].id == 1


def test_filter_by_vibe():
    items = [
        fake_item(1, "top", vibe="streetwear"),
        fake_item(2, "top", vibe="campus"),
    ]

    streetwear_items = filter_items(items, vibe="streetwear")
    assert len(streetwear_items) == 1
    assert streetwear_items[0].id == 1
