import json
from pathlib import Path
from typing import List
from .models import Item, Outfit

# Root of the project (folder that contains "lookbook")
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
ITEMS_PATH = DATA_DIR / "items.json"
OUTFITS_PATH = DATA_DIR / "outfits.json"


def _ensure_data_dir() -> None:
    """Make sure the data directory exists."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_items() -> List[Item]:
    """Load all items from the JSON file. Return [] if it doesn't exist."""
    _ensure_data_dir()
    if not ITEMS_PATH.exists():
        return []
    data = json.loads(ITEMS_PATH.read_text())
    return [Item(**item) for item in data]


def save_items(items: List[Item]) -> None:
    """Save all items to the JSON file."""
    _ensure_data_dir()
    payload = [item.__dict__ for item in items]
    ITEMS_PATH.write_text(json.dumps(payload, indent=2))


def load_outfits() -> List[Outfit]:
    """Load all outfits from the JSON file. Return [] if it doesn't exist."""
    _ensure_data_dir()
    if not OUTFITS_PATH.exists():
        return []
    data = json.loads(OUTFITS_PATH.read_text())
    return [Outfit(**entry) for entry in data]


def save_outfits(outfits: List[Outfit]) -> None:
    """Save all outfits to the JSON file."""
    _ensure_data_dir()
    payload = [o.__dict__ for o in outfits]
    OUTFITS_PATH.write_text(json.dumps(payload, indent=2))


def next_item_id(items: List[Item]) -> int:
    """Return the next available ID for a new item."""
    return max((i.id for i in items), default=0) + 1


def next_outfit_id(outfits: List[Outfit]) -> int:
    """Return the next available ID for a new outfit."""
    return max((o.id for o in outfits), default=0) + 1
