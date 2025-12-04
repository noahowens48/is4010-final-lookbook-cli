import argparse
from .models import Item, Outfit
from .storage import (
    load_items,
    save_items,
    load_outfits,
    save_outfits,
    next_item_id,
    next_outfit_id,
)
from .filters import filter_items
from .generator import generate_outfit


def handle_add_item(args: argparse.Namespace) -> None:
    items = load_items()
    new_id = next_item_id(items)

    tags = []
    if args.tags:
        tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    item = Item(
        id=new_id,
        name=args.name,
        category=args.category,
        color=args.color,
        brand=args.brand or "",
        season=args.season or "all",
        vibe=args.vibe or "streetwear",
        tags=tags,
    )
    items.append(item)
    save_items(items)
    print(f"✅ Added item #{item.id}: {item.name}")


def handle_list_items(args: argparse.Namespace) -> None:
    items = load_items()
    filtered = filter_items(
        items,
        season=args.season,
        vibe=args.vibe,
        category=args.category,
    )
    if not filtered:
        print("No items found.")
        return

    for item in filtered:
        tags = ", ".join(item.tags) if item.tags else "-"
        print(
            f"[{item.id}] {item.name} | {item.category} | {item.color} | "
            f"{item.brand} | season={item.season} | vibe={item.vibe} | tags={tags}"
        )


def handle_generate(args: argparse.Namespace) -> None:
    items = load_items()
    outfit = generate_outfit(
        items,
        season=args.season,
        vibe=args.vibe,
    )
    if outfit is None:
        print("⚠️ Could not generate an outfit. Add more items or relax filters.")
        return

    # Build a quick lookup from id -> Item
    item_by_id = {item.id: item for item in items}

    def describe(item_id: int | None) -> str:
        if item_id is None:
            return "None"
        item = item_by_id.get(item_id)
        if not item:
            return f"Item {item_id} (not found)"
        return f"{item.name} ({item.color}, {item.brand or 'no brand'})"

    print("🎲 Generated outfit:")
    print(f"- Top:      {describe(outfit.top_id)}")
    print(f"- Bottom:   {describe(outfit.bottom_id)}")
    print(f"- Shoes:    {describe(outfit.shoes_id)}")
    if outfit.outerwear_id:
        print(f"- Outerwear:{describe(outfit.outerwear_id)}")


def handle_save_outfit(args: argparse.Namespace) -> None:
    items = load_items()
    outfits = load_outfits()
    new_id = next_outfit_id(outfits)

    outfit = Outfit(
        id=new_id,
        name=args.name,
        season=args.season or "all",
        vibe=args.vibe or "any",
        top_id=args.top_id,
        bottom_id=args.bottom_id,
        shoes_id=args.shoes_id,
        outerwear_id=args.outerwear_id,
        accessory_ids=args.accessory_ids or [],
    )

    # Optional: validate that IDs exist
    item_ids = {i.id for i in items}
    needed_ids = [outfit.top_id, outfit.bottom_id, outfit.shoes_id] + outfit.accessory_ids
    missing = [i for i in needed_ids if i is not None and i not in item_ids]
    if missing:
        print(f"⚠️ Warning: Some item IDs do not exist: {missing}")

    outfits.append(outfit)
    save_outfits(outfits)
    print(f"💾 Saved outfit #{outfit.id}: {outfit.name}")


def handle_list_outfits(args: argparse.Namespace) -> None:
    outfits = load_outfits()
    filtered = outfits
    if args.season:
        filtered = [o for o in filtered if o.season == args.season]
    if args.vibe:
        filtered = [o for o in filtered if o.vibe == args.vibe]

    if not filtered:
        print("No outfits found.")
        return

    for o in filtered:
        print(
            f"[{o.id}] {o.name} | season={o.season} | vibe={o.vibe} | "
            f"top={o.top_id} bottom={o.bottom_id} shoes={o.shoes_id} outerwear={o.outerwear_id}"
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="lookbook",
        description="Outfit & Lookbook Generator CLI",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add-item
    p_add = subparsers.add_parser("add-item", help="Add a wardrobe item")
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--category", required=True)
    p_add.add_argument("--color", required=True)
    p_add.add_argument("--brand")
    p_add.add_argument("--season")
    p_add.add_argument("--vibe")
    p_add.add_argument("--tags", help="Comma-separated tags", default="")
    p_add.set_defaults(func=handle_add_item)

    # list-items
    p_list = subparsers.add_parser("list-items", help="List wardrobe items")
    p_list.add_argument("--season")
    p_list.add_argument("--vibe")
    p_list.add_argument("--category")
    p_list.set_defaults(func=handle_list_items)

    # generate
    p_gen = subparsers.add_parser("generate", help="Generate an outfit")
    p_gen.add_argument("--season")
    p_gen.add_argument("--vibe")
    p_gen.set_defaults(func=handle_generate)

    # save-outfit
    p_save = subparsers.add_parser("save-outfit", help="Save an outfit by item IDs")
    p_save.add_argument("--name", required=True)
    p_save.add_argument("--season")
    p_save.add_argument("--vibe")
    p_save.add_argument("--top-id", type=int, required=True)
    p_save.add_argument("--bottom-id", type=int, required=True)
    p_save.add_argument("--shoes-id", type=int, required=True)
    p_save.add_argument("--outerwear-id", type=int)
    p_save.add_argument(
        "--accessory-ids",
        nargs="*",
        type=int,
        help="Optional accessory item IDs",
        default=[],
    )
    p_save.set_defaults(func=handle_save_outfit)

    # list-outfits
    p_lo = subparsers.add_parser("list-outfits", help="List saved outfits")
    p_lo.add_argument("--season")
    p_lo.add_argument("--vibe")
    p_lo.set_defaults(func=handle_list_outfits)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
