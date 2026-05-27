# SOP-06: QUOTE ID SECTION

---

## Overview

The instructor will give excerpts and ask "which work is this from?" This section drills exactly that skill. It is a game — one quote at a time, tap to guess the work.

---

## Layout

- One quote displayed per round, styled in Lora serif, large, centered on a champagne card
- Below the quote: 4 work title buttons (pill buttons)
- On selection: immediate reveal
  - Correct: button turns sage green, brief confetti
  - Wrong: button turns brick red, correct answer shown in hunter green
- Score tracked: "X correct / Y attempted" shown at top
- "Next Quote" button appears after each answer
- Progress stored in localStorage

---

## Game Mechanics

- Quotes pulled from the bank below, shuffled each session
- Wrong options are always from the same author or same school when possible (to make it harder and more useful for the exam)
- After completing all quotes: end screen with score + option to restart

---

## Quote Bank

Format: Quote text | Correct work | Why it's distinctive

---

**QUOTE 1**
"When it occurs to a man that nature does not regard him as important, and that she feels she would not maim the universe by disposing of him, he at first wishes to throw bricks at the temple."
**Work:** The Open Boat (Stephen Crane)
**Why distinctive:** Classic Naturalism/Impressionism blend — nature's indifference + the correspondent's emotional reaction

---

**QUOTE 2**
"None of them knew the colour of the sky."
**Work:** The Open Boat (Stephen Crane)
**Why distinctive:** The famous opening line — Impressionism, limited perception, immediately disorienting

---

**QUOTE 3**
"The dog did not know anything about thermometers, but the brute had its instinct."
**Work:** To Build a Fire (Jack London)
**Why distinctive:** Direct contrast between the man's knowledge and the dog's instinct — core Naturalist theme

---

**QUOTE 4**
"He was a gentleman from sole to crown, clean favored, and imperially slim."
**Work:** Richard Cory (Edwin Arlington Robinson)
**Why distinctive:** The build-up of Richard Cory's perfection — makes the ending more devastating

---

**QUOTE 5**
"And Richard Cory, one calm summer night, went home and put a bullet through his head."
**Work:** Richard Cory (Edwin Arlington Robinson)
**Why distinctive:** The volta — the most shocking ending in the course

---

**QUOTE 6**
"So on we worked, and waited for the light, and went without the meat, and cursed the bread."
**Work:** Richard Cory (Edwin Arlington Robinson)
**Why distinctive:** The townspeople's poverty — class contrast with Cory's wealth

---

**QUOTE 7**
"The miller's wife had waited long, the tea was cold, the fire was dead."
**Work:** The Mill (Edwin Arlington Robinson)
**Why distinctive:** Opens with quiet domestic dread — the cold tea and dead fire signal something is wrong

---

**QUOTE 8**
"I went up and down the streets here living on little, saving all I could."
**Work:** Doc Hill (Edgar Lee Masters)
**Why distinctive:** Doc Hill's voice — quiet service, no self-pity

---

**QUOTE 9**
"I bought every kind of machine that's known — Sewing machines, grinders, cranes."
**Work:** Abel Melveny (Edgar Lee Masters)
**Why distinctive:** The list of machines — Abel's defining characteristic, materialism over action

---

**QUOTE 10**
"The cold of space smote the unprotected tip of the planet, and he, being on that unprotected tip, received the full force of the blow."
**Work:** To Build a Fire (Jack London)
**Why distinctive:** Naturalistic, cosmic-scale description of cold — the man is insignificant against geological/planetary forces

---

**QUOTE 11**
"He was a sight to see. A sight for sore eyes and a blistered heart."
**Work:** Doc Hill (Edgar Lee Masters)
**Why distinctive:** The community's affection for Doc Hill — his value is in what he gave

---

**QUOTE 12**
"The oiler swam strongly and rapidly. He was ahead in the race. But the oiler was drowned."
**Work:** The Open Boat (Stephen Crane)
**Why distinctive:** The brutal irony of Billie's death — the strongest man dies, proving nature's indifference

---

**QUOTE 13**
"Fifty degrees below zero was to him just precisely fifty degrees below zero. That there should be anything more to it than that was a thought that never entered his head."
**Work:** To Build a Fire (Jack London)
**Why distinctive:** Captures the man's fatal flaw — his purely rational, unimaginative relationship with danger

---

**QUOTE 14**
"He had never had a chance to go, but if he'd gone, I know he'd have seen the world."
**Work:** Abel Melveny (Edgar Lee Masters)
**Why distinctive:** The regret of unlived potential — Abel as a type for wasted human ambition

---

## Difficulty Grouping (for display purposes)

**Easier** (very distinctive lines):
- Quotes 2, 5, 9, 13

**Medium** (need context to be sure):
- Quotes 1, 4, 7, 10, 12

**Harder** (could be confused between works or authors):
- Quotes 3, 6, 8, 11, 14

---

## Wrong Answer Generation Logic

When generating wrong options for a quote:
- Always include the correct work
- Include 1-2 works from the same author (e.g. for a Crane quote, include "The Open Boat" and potentially a non-Crane work)
- Include 1 work from the same literary school
- Never include works that are obviously wrong (e.g. don't include "Richard Cory" as a wrong option for a clearly naturalistic wilderness passage)

Hardcoded wrong options per quote are acceptable — see the bank above for the "Why distinctive" field to inform which works would be plausible distractors.
