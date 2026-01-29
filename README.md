# Red Faction: Underground — Rulebook

View card gallery: https://gooberrf.github.io/rf_underground/

**Players:** 2–4  
**Play Time:** ~30 minutes  
**Game Type:** Competitive multiplayer card/board game inspired by *Boss Monster*, set in the *Red Faction* universe.

In **Red Faction: Underground**, you use room cards to construct a base, and defend against attacking characters from the barracks. Survive the attacks, score points by defeating attackers, and outlast your rivals.

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

---

## 1. How You Win

You win immediately when either condition is met:

1. **Score 7 Points** (by defeating attacking characters), or  
2. **Be the Last Surviving Player**  
   - A player is eliminated when they reach **3 Wounds**.

---

## 2. Components

### Main Deck (Shared)
Contains:
- **Characters**
- **Events**
- **Interrupts**
- **Nano Enhancements**

**Main Discard Pile:** When the Main Deck runs out, **shuffle the Main Discard Pile** to form a new Main Deck.

---

### Room Deck (Shared)
Contains:
- **Rooms**

**Room Discard Pile:** When the Room Deck runs out, **shuffle the Room Discard Pile** to form a new Room Deck.

---

### Areas
- **Each player’s Base** (starts empty; max **5** rooms)
- **Barracks** (central area where characters wait before attacking)
- **Each player’s Hand** (secret information)

---

## 3. Card Types

### Rooms
Rooms appear in the **Room Deck** and in players’ **Bases**.

Each Room has:
- **Name**
- **Alignment:** RF, Ultor, EDF, RC, or Neutral
- **Room Stat + Check Number:** STR, DEX, or INT with a required value
- **Type:** Underground / Surface / Sky
- **Rule/Effect** (always follow the card text)

**Entrance:** The first room of your base (the one attackers enter first).

---

### Characters
Characters appear in the **Main Deck**, players’ **Hands**, the **Barracks**, and as **Attackers**.

Each Character has:
- **Name**
- **Types:** Soldier, Support, Creature, Leader (any number)
- **Attacks:** What it attacks
- **Stats:** STR, DEX, INT, CON

Characters can only be played during the **Play** phase.

---

### Events
Events appear in the **Main Deck**, players’ **Hands**, and the **Stack** (while resolving).

Each Event has:
- **Name**
- **Rule/Effect**

**Cost to play an Event:** **Discard 1 card** from your hand.

Events can only be played during the **Play** phase.

---

### Interrupts
Interrupts appear in the **Main Deck**, players’ **Hands**, and the **Stack** (while resolving).

Each Interrupt has:
- **Name**
- **Play Condition**
- **Rule/Effect**

**Cost to play an Interrupt:** **Discard 1 card** from your hand.

Inerrupts can be played at the specific time printed on the card.

---

### Nano Enhancements
Nano Enhancements appear in the **Main Deck**, players’ **Hands**, and **attached** to characters.

Each Nano Enhancement has:
- **Name**
- **Rule/Effect**

**Cost to play a Nano Enhancement:** **Discard 1 card** from your hand.

---

## 4. Setup

1. Place the **Main Deck** and **Room Deck** in the center of the play area, within reach of all players.
2. Note a central **Barracks** area. 
3. Each player notes a **Base area** in front of them (begins with **0 rooms**).
4. Choose a starting player at random.
5. Each player draws up to their **Hand Size** (see [Hand Size](#5-hand-size)).
6. The first player takes their turn

---

## 5. Hand Size

Your **Hand Size** is:

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

Starting with the player with the most points, each player takes their **Play Phase**. If multiple players are tied for the most points, randomly select the starting player from among the players tied for the most points.

During each player's Play Phase, that player may:

1. **Play up to 1 Character** from hand into the **Barracks**  
   - Place it at the end of the barracks line (newest goes last).
2. **Play any number of Events and/or Nano Enhancements**  
   - Each costs **discard 1 card**.
   
After each player has completed their Play Phase, proceed to the Build Phase.

---

## 6.3 Build Phase

Starting with the player with the most points, each player takes their **Build Phase**. If multiple players are tied for the most points, randomly select the starting player from among the players tied for the most points.

During each player's Build Phase, they:

1. Look at the **top 3 cards** of the **Room Deck**.  
2. If your base has **fewer than 5 rooms**:
   - Choose **1** and add it to your **Entrance** (front of your base).
3. If your base already has **5 rooms**:
   - You **may** choose **1** and **replace** any single room in your base with it.  
   - The replaced room is **destroyed** and goes to the **Room Discard Pile**.
4. Put the other room cards you looked at into the **Room Discard Pile**.

After each player has completed their Build Phase, proceed to the Target Phase.

---

## 6.4 Target Phase

Determine attacks in the **order that characters entered the barracks** (oldest first).

For each character, select their target based on:

- **Non-Neutral characters** target the base with the **highest number of matching Attack Alignment symbols**.  
- **Neutral characters** target a base using their **special targeting rule**.

### Tie Rule
If **more than one** base is tied for best target, that character **does not attack** and **stays in the barracks**, keeping its position, then move on to the next character and pick their target.

Characters that select a target become **Attackers**.

---

## 6.5 Combat Phase

Combat resolves in two layers of order:

1. **In turn order** (player with the most points resolves first, then clockwise), then  
2. For each base, resolve attackers in **attacking order** (the order in which they selected that base as their target).

### Resolving an Attack
When a character attacks a base:

1. The attacker enters at the **Entrance** and moves **room by room**.  
2. In each room, compare the room’s stat/check (STR/DEX/INT) to the attacker’s matching stat:
   - If **attacker stat exceeds or equals the room check** → pass safely and take **0 damage**.
   - If **attacker stat is less than room check** → take **damage equal to the difference** (room check minus attacker stat).
3. If total damage **exceeds or equals CON**, the attacker **dies immediately**:
   - The defending player takes that character card as **1 Point** (keep it face down).
4. If the attacker survives and passes through **all rooms in the base**:
   - The defending player takes that character card as **1 Wound** (keep it face up).

After combat in each base resolved, the next round begins at **Draw Phase**.

---

## 7. Tracking Points and Wounds

### Points
- **When a character dies in your base, you gain 1 Point.** Keep those character cards face down.

### Wounds
- **When a character survives your entire base, you take 1 Wound.** Keep those character cards face up.
- At **3 Wounds**, you are immediately eliminated.

---
