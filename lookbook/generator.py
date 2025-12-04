import random
from typing import List, Optional
from .models import Item, Outfit
from .filters import filter_items


def generate_outfit(
    items: List[Item],
    season: Optional[str] = None,
    vibe: Optional[str] = None,
) -> Optional[Outfit]:
    """
    Try to build an outfit with at least:
    - top
    - bottom
    - shoes

    Optionally outerwear.
    Returns None if it can't.
    """
    tops = filter_items(items, season=season, vibe=vibe, category="top")
    bottoms = filter_items(items, season=season, vibe=vibe, category="bottom")
    shoes = filter_items(items, season=season, vibe=vibe, category="shoes")
    outerwear = filter_items(items, season=season, vibe=vibe, category="outerwear")

    if not (tops and bottoms and shoes):
        return None

    top = random.choice(tops)
    bottom = random.choice(bottoms)
    shoe = random.choice(shoes)
    coat = random.choice(outerwear) if outerwear else None

    return Outfit(
        id=-1,  # will be set when saved
        name="Generated Outfit",
        season=season or "all",
        vibe=vibe or "any",
        top_id=top.id,
        bottom_id=bottom.id,
        shoes_id=shoe.id,
        outerwear_id=coat.id if coat else None,
    )
