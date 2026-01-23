# Red Faction: Underground — Rulebook

**Players:** 2–4  
**Play Time:** ~30 minutes  
**Game Type:** Competitive multiplayer card/board game inspired by *Boss Monster*, set in the *Red Faction* universe.

In **Red Faction: Underground**, you build a **base of rooms** to defend yourself while **characters gather in the barracks** and then attack players’ bases. Survive the raids, score points by defeating attackers, and outlast your rivals.

---

## Table of Contents
- [1. How You Win](#1-how-you-win)
- [2. Components](#2-components)
- [3. Card Types](#3-card-types)
- [4. Setup](#4-setup)
- [5. Hand Size](#5-hand-size)
- [6. Turn Structure](#6-turn-structure)
  - [6.1 Draw Phase](#61-draw-phase)
  - [6.2 Play Phase](#62-play-phase)
  - [6.3 Build Phase](#63-build-phase)
  - [6.4 Target Phase](#64-target-phase)
  - [6.5 Combat Phase](#65-combat-phase)
- [7. Tracking Points and Wounds](#7-tracking-points-and-wounds)
- [8. Quick Glossary](#8-quick-glossary)
- [9. Example Attack](#9-example-attack)

---

## 1. How You Win

You win immediately when **either** condition is met:

1. **Score 10 Points** (most commonly by defeating attacking characters in your base), or  
2. **Be the Last Surviving Player**  
   - A player is eliminated when they reach **3 Wounds**.

> **If multiple players would win at the same time:** resolve the current round fully, then determine the winner by:
> 1) any player at **10+ Points**, otherwise  
> 2) the **last surviving** player.

---

## 2. Components

### Main Deck (Shared)
Contains:
- **Characters**
- **Actions**
- **Nano Enhancements**

**Main Discard Pile:** When the Main Deck runs out, **shuffle the Main Discard Pile** to form a new Main Deck.

---

### Room Deck (Shared)
Contains:
- **Room Cards**

**Room Discard Pile:** When the Room Deck runs out, **shuffle the Room Discard Pile** to form a new Room Deck.

---

### Battlefield Areas
- **Each player’s Base** (starts empty; max **5** rooms)
- **Barracks** (central area where characters wait before attacking)
- **Each player’s Hand** (secret information)

---

## 3. Card Types

### Rooms
Rooms appear in the **Room Deck** and in players’ **Bases**.

Each Room has:
- **Name**
- **Alignment:** RF, Ultor, EDF, RC, or **Neutral**
- **Room Stat + Check Number:** STR, DEX, or INT with a required value
- **Type:** Underground / Ground Level / Above Ground
- **Rule/Effect** (always follow the card text)

**Entrance:** The first room of your base (the one attackers enter first).

---

### Characters
Characters appear in the **Main Deck**, players’ **Hands**, the **Barracks**, and as **Attackers**.

Each Character has:
- **Name**
- **Types:** Soldier, Support, Creature, Leader (any number)
- **Attack Alignment:** RF, Ultor, EDF, RC, or **Neutral**
- **Stats:** STR, DEX, INT, CON
- **Rule/Effect**

**CON** is a character’s health. Damage reduces CON until the character dies.

---

### Actions
Actions appear in the **Main Deck**, players’ **Hands**, and the **Stack** (while resolving).

Each Action has:
- **Name**
- **Type:**
  - **Utility** (played during the Play Phase)
  - **Trap** (played when its trigger condition is met)
- **Rule/Effect**

**Cost to play an Action:** **Discard 1 card** from your hand (unless the Action says otherwise).

---

### Nano Enhancements
Nano Enhancements appear in the **Main Deck**, players’ **Hands**, and **attached** to other cards as instructed.

Each Nano Enhancement has:
- **Name**
- **Rule/Effect**

**Cost to play a Nano Enhancement:** **Discard 1 card** from your hand (unless the card says otherwise).

---

## 4. Setup

1. Place the **Main Deck** and **Room Deck** within reach of all players.  
2. Create a **Main Discard Pile** and a **Room Discard Pile** beside their decks.  
3. Create a central **Barracks** area.  
4. Each player creates a **Base area** in front of them (it begins with **0 rooms**).  
5. Choose a starting player at random.  
6. Each player draws up to their **Max Hand Size** (see [Hand Size](#5-hand-size)).

---

## 5. Hand Size

Your **Max Hand Size** is:

**4 + number of other players**

So:
- **2 players:** 5 cards
- **3 players:** 6 cards
- **4 players:** 7 cards

---

## 6. Turn Structure

Each round has **five phases**, completed in this order:

1. **Draw Phase**  
2. **Play Phase**  
3. **Build Phase**  
4. **Target Phase**  
5. **Combat Phase**  

Then the next round begins.

---

## 6.1 Draw Phase

Each player draws from the **Main Deck** until they reach their **Max Hand Size**.

---

## 6.2 Play Phase

Starting with the first player and continuing clockwise, each player takes a Play Phase turn.

On your Play Phase turn, you may:

1. **Play up to 1 Character** from your hand into the **Barracks**  
   - Place it at the end of the barracks line (newest goes last).
2. **Play any number of Utility Actions and Nano Enhancements**  
   - Each costs **discard 1 card** (unless stated otherwise).
3. **Play Trap Actions** only when their trigger condition is true  
   - Traps may be played outside your Play Phase if their trigger happens (still pay the discard cost unless stated otherwise).

> **Card text overrides the rulebook.** If a card contradicts this document, follow the card.

---

## 6.3 Build Phase

Starting with the first player and continuing clockwise, each player takes a Build Phase turn:

1. Look at the **top 3 cards** of the **Room Deck**.  
2. If your base has **fewer than 5 rooms**:
   - Choose **1** and add it to your **Entrance** (front of your base).
3. If your base already has **5 rooms**:
   - You **may** choose **1** and **replace** any single room in your base with it.  
   - The replaced room is **destroyed** and goes to the **Room Discard Pile**.  
   - Any Nano Enhancements on the replaced room are **discarded** (unless the card says otherwise).
4. Put the other room cards you looked at into the **Room Discard Pile**.

---

## 6.4 Target Phase

Determine attacks in the **exact order characters entered the barracks** (oldest first).

For each character:

- **Non-Neutral characters** target the base with the **highest number of matching Attack Alignment symbols**.  
- **Neutral characters** target a base using their **special targeting rule**.

### Tie Rule
If **more than one** base is tied for best target, that character **does not attack** and **stays in the barracks**, keeping its position.

Characters that select a target become **Attackers**.

---

## 6.5 Combat Phase

Combat resolves in two layers of order:

1. **In turn order** (first player’s base resolves first, then clockwise), then  
2. For each base, resolve attackers in **attacking order** (based on their barracks order).

### Resolving an Attack
When a character attacks a base:

1. The attacker enters at the **Entrance** and moves **room by room**.  
2. In each room, compare the room’s stat/check (STR/DEX/INT) to the attacker’s matching stat:
   - If **attacker stat ≥ room check** → pass safely.
   - If **attacker stat < room check** → take **1 damage**.
3. If total damage is **≥ CON**, the attacker **dies immediately**:
   - The defending player takes that character card as **1 Point**.
4. If the attacker survives and passes through **all rooms**:
   - The defending player takes **1 Wound** and keeps the character card as a reminder (or place it in a Wound area—your choice, as long as it’s tracked clearly).

After all combat resolves, follow any cleanup on card text, then the next round begins at **Draw Phase**.

---

## 7. Tracking Points and Wounds

### Points
- By default: **When a character dies in your base, you gain 1 Point**.  
  Keep those character cards in a **scored pile**.

### Wounds
- **When a character survives your entire base, you take 1 Wound.**
- At **3 Wounds**, you are eliminated.

---

## 8. Quick Glossary

- **Base:** Your line of up to **5 rooms**.
- **Entrance:** The first room attackers enter.
- **Barracks:** Where played characters wait before targeting.
- **Attack Alignment:** The faction symbol used to select a target base (or Neutral with special rules).
- **Check Number:** The required value on a room’s listed stat.
- **Damage:** Taken when a character fails a room check. Damage ≥ CON = death.

---

## 9. Example Attack

A character with **DEX 2** and **CON 3** attacks a base with 3 rooms:

1) Room 1: **DEX check 1** → 2 ≥ 1, passes.  
2) Room 2: **DEX check 3** → 2 < 3, takes 1 damage.  
3) Room 3: **STR check 2** → compare STR; if the attacker fails, it takes 1 more damage.  

If total damage reaches **3**, the character dies and the defender scores **1 Point**.  
If it survives through the last room, the defender takes **1 Wound** instead.
