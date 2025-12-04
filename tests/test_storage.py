import json
from pathlib import Path
from lookbook.storage import save_items, load_items
from lookbook.models import Item


def test_save_and_load_items(tmp_path, monkeypatch):
    # Redirect data directory to temp folder
    monkeypatch.setattr("lookbook.storage.DATA_DIR", tmp_path)
    monkeypatch.setattr("lookbook.storage.ITEMS_PATH", tmp_path / "items.json")

    items = [
        Item(
            id=1,
            name="Test Top",
            category="top",
            color="black",
            brand="Brand",
            season="winter",
            vibe="streetwear",
            tags=[],
        )
    ]

    save_items(items)
    loaded = load_items()

    assert len(loaded) == 1
    assert loaded[0].id == 1
    assert loaded[0].name == "Test Top"
import json
from pathlib import Path
from lookbook.storage import save_items, load_items
from lookbook.models import Item


def test_save_and_load_items(tmp_path, monkeypatch):
    # Redirect data directory to temp folder
    monkeypatch.setattr("lookbook.storage.DATA_DIR", tmp_path)
    monkeypatch.setattr("lookbook.storage.ITEMS_PATH", tmp_path / "items.json")

    items = [
        Item(
            id=1,
            name="Test Top",
            category="top",
            color="black",
            brand="Brand",
            season="winter",
            vibe="streetwear",
            tags=[],
        )
    ]

    save_items(items)
    loaded = load_items()

    assert len(loaded) == 1
    assert loaded[0].id == 1
    assert loaded[0].name == "Test Top"
