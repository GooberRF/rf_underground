# Tabletop Simulator Mod

This folder contains a build script that creates Tabletop Simulator (TTS) deck sheets and a ready-to-import mod JSON for **Red Faction: Underground**.

## Build the Mod

```bash
python tts/build_mod.py
```

The script will:

- Generate `tts/output/main_deck_sheet_1.png`, `tts/output/main_deck_sheet_2.png`, and `tts/output/room_deck_sheet.png` from the card PNGs.
- Generate a `tts/output/card_back.png` back image.
- Write `tts/output/RedFactionUnderground.json` with **local file URLs** pointing at the generated deck sheets.

## Import into Tabletop Simulator

1. Run the build script.
2. Open Tabletop Simulator.
3. Go to **Objects → Saved Objects**.
4. Choose **Import** and select `tts/output/RedFactionUnderground.json`.

The mod will load **Main Deck 1**, **Main Deck 2**, and the Room Deck on the table. Combine the two main decks in Tabletop Simulator after importing.

## Notes

- The generated JSON uses `file://` URLs that point to your local files. If you move the deck sheets, re-run the script so the URLs update.
- If you want to host the deck sheets on the web instead, replace the `FaceURL` and `BackURL` values in the JSON with hosted URLs.
