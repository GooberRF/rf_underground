#!/usr/bin/env python3
"""Build Tabletop Simulator assets and mod JSON for Red Faction: Underground."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable, List, Tuple

from PIL import Image, ImageDraw, ImageFont

CARD_SIZE = (750, 1050)


def load_cards(card_dir: Path) -> List[Path]:
    return sorted([p for p in card_dir.iterdir() if p.suffix.lower() == ".png"])


def build_sheet(cards: List[Path], columns: int, rows: int, output_path: Path) -> None:
    width, height = CARD_SIZE
    sheet = Image.new("RGBA", (columns * width, rows * height), (0, 0, 0, 0))

    for idx, card_path in enumerate(cards):
        if idx >= columns * rows:
            raise ValueError("Not enough room on sheet for all cards.")
        card = Image.open(card_path).convert("RGBA")
        if card.size != CARD_SIZE:
            card = card.resize(CARD_SIZE)
        x = (idx % columns) * width
        y = (idx // columns) * height
        sheet.paste(card, (x, y))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path)


def build_back_image(output_path: Path) -> None:
    width, height = CARD_SIZE
    back = Image.new("RGBA", CARD_SIZE, (18, 18, 24, 255))
    draw = ImageDraw.Draw(back)
    accent_color = (190, 30, 30, 255)
    draw.rectangle([40, 40, width - 40, height - 40], outline=accent_color, width=8)

    title = "RED FACTION\nUNDERGROUND"
    font = ImageFont.load_default()
    text_w, text_h = draw.multiline_textbbox((0, 0), title, font=font, align="center")[2:]
    draw.multiline_text(
        ((width - text_w) / 2, (height - text_h) / 2),
        title,
        font=font,
        fill=(235, 235, 235, 255),
        align="center",
    )
    back.save(output_path)


def format_card_name(filename: str) -> str:
    stem = Path(filename).stem
    if "_" in stem:
        _, name = stem.split("_", 1)
    else:
        name = stem
    return name.replace("_", " ")


def build_deck_objects(
    cards: List[Path],
    deck_id: int,
    face_url: str,
    back_url: str,
    columns: int,
    rows: int,
) -> Tuple[dict, List[int]]:
    deck_key = str(deck_id)
    custom_deck = {
        deck_key: {
            "FaceURL": face_url,
            "BackURL": back_url,
            "NumWidth": columns,
            "NumHeight": rows,
            "BackIsHidden": True,
            "UniqueBack": False,
        }
    }

    deck_ids = []
    contained = []
    for idx, card_path in enumerate(cards):
        card_id = deck_id * 100 + idx
        deck_ids.append(card_id)
        contained.append(
            {
                "Name": "Card",
                "CardID": card_id,
                "Nickname": format_card_name(card_path.name),
                "Transform": {
                    "posX": 0,
                    "posY": 1,
                    "posZ": 0,
                    "rotX": 0,
                    "rotY": 180,
                    "rotZ": 0,
                    "scaleX": 1,
                    "scaleY": 1,
                    "scaleZ": 1,
                },
            }
        )

    deck_obj = {
        "Name": "Deck",
        "Nickname": "",
        "Description": "",
        "Transform": {
            "posX": 0,
            "posY": 1,
            "posZ": 0,
            "rotX": 0,
            "rotY": 180,
            "rotZ": 0,
            "scaleX": 1,
            "scaleY": 1,
            "scaleZ": 1,
        },
        "DeckIDs": deck_ids,
        "CustomDeck": custom_deck,
        "ContainedObjects": contained,
    }

    return deck_obj, deck_ids


def build_mod(
    output_dir: Path,
    asset_dir: Path,
    repo_root: Path,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    main_cards = load_cards(asset_dir / "MainDeck")
    room_cards = load_cards(asset_dir / "RoomDeck")

    main_cols = 10
    main_rows = 7
    main_chunk_size = main_cols * main_rows
    main_chunks = [
        main_cards[i : i + main_chunk_size]
        for i in range(0, len(main_cards), main_chunk_size)
    ]
    room_cols = 8
    room_rows = math.ceil(len(room_cards) / room_cols)

    main_sheets = [
        output_dir / f"main_deck_sheet_{index + 1}.png"
        for index in range(len(main_chunks))
    ]
    room_sheet = output_dir / "room_deck_sheet.png"
    back_image = output_dir / "card_back.png"

    for chunk, sheet_path in zip(main_chunks, main_sheets):
        build_sheet(chunk, main_cols, main_rows, sheet_path)
    build_sheet(room_cards, room_cols, room_rows, room_sheet)
    build_back_image(back_image)

    def file_url(path: Path) -> str:
        return path.resolve().as_uri()

    main_faces = [file_url(path) for path in main_sheets]
    room_face = file_url(room_sheet)
    back_url = file_url(back_image)

    main_decks = []
    for index, (chunk, face_url) in enumerate(zip(main_chunks, main_faces), start=1):
        deck, _ = build_deck_objects(
            chunk, index, face_url, back_url, main_cols, main_rows
        )
        deck["Nickname"] = f"Main Deck {index}"
        deck["Transform"].update({"posX": -4.5 + (index - 1) * 3.0, "posZ": 0})
        main_decks.append(deck)
    room_deck, _ = build_deck_objects(
        room_cards, 100, room_face, back_url, room_cols, room_rows
    )
    room_deck["Nickname"] = "Room Deck"
    room_deck["Transform"].update({"posX": 3.0, "posZ": 0})

    mod = {
        "SaveName": "Red Faction: Underground",
        "GameMode": "",
        "Date": "",
        "Gravity": 0.5,
        "PlayArea": 0.5,
        "Table": "",
        "Sky": "",
        "ObjectStates": [*main_decks, room_deck],
        "TabStates": {},
    }

    mod_path = output_dir / "RedFactionUnderground.json"
    mod_path.write_text(json.dumps(mod, indent=2))
    return mod_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build Tabletop Simulator assets for Red Faction: Underground."
    )
    parser.add_argument(
        "--assets",
        type=Path,
        default=Path("docs/CardImages"),
        help="Path to card image assets.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tts/output"),
        help="Output directory for deck sheets and mod JSON.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    asset_dir = (repo_root / args.assets).resolve()
    output_dir = (repo_root / args.output).resolve()

    mod_path = build_mod(output_dir, asset_dir, repo_root)
    print(f"Wrote {mod_path}")


if __name__ == "__main__":
    main()
