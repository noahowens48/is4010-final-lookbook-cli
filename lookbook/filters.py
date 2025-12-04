from typing import List, Optional
from .models import Item


def filter_items(
    items: List[Item],
    season: Optional[str] = None,
    vibe: Optional[str] = None,
    category: Optional[str] = None,
) -> List[Item]:
    """Filter items by optional season, vibe, and category."""
    result = items

    if season:
        # allow items marked "all" to show up in any season
        result = [i for i in result if i.season == season or i.season == "all"]

    if vibe:
        result = [i for i in result if i.vibe == vibe]

    if category:
        result = [i for i in result if i.category == category]

    return result
