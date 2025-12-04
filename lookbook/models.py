from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Item:
    id: int
    name: str
    category: str   # "top", "bottom", "shoes", "outerwear", "accessory"
    color: str
    brand: str
    season: str     # "winter", "summer", "spring", "fall", "all"
    vibe: str       # "streetwear", "campus", etc.
    tags: List[str] = field(default_factory=list)


@dataclass
class Outfit:
    id: int
    name: str
    season: str
    vibe: str
    top_id: Optional[int] = None
    bottom_id: Optional[int] = None
    shoes_id: Optional[int] = None
    outerwear_id: Optional[int] = None
    accessory_ids: List[int] = field(default_factory=list)
