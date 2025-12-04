from lookbook.models import Item
from lookbook.generator import generate_outfit


def fake_item(id, category):
    return Item(
        id=id,
        name=f"Item{id}",
        category=category,
        color="black",
        brand="TestBrand",
        season="winter",
        vibe="streetwear",
        tags=[],
    )


def test_generate_success():
    items = [
        fake_item(1, "top"),
        fake_item(2, "bottom"),
        fake_item(3, "shoes"),
    ]

    outfit = generate_outfit(items, season="winter", vibe="streetwear")
    assert outfit is not None
    assert outfit.top_id == 1
    assert outfit.bottom_id == 2
    assert outfit.shoes_id == 3


def test_generate_fails_without_required_categories():
    items = [
        fake_item(1, "top"),
        fake_item(2, "bottom"),
        # missing shoes → should fail
    ]

    outfit = generate_outfit(items)
    assert outfit is None
