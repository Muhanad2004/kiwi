# SOP-04: MCQ SECTION

---

## Layout

- One question displayed at a time, full card
- Question number + total shown top right (e.g. "Q4 / 20")
- 4 answer options as pill buttons
- On selection: immediate feedback (no submit button)
  - Correct: button turns sage green, brief confetti burst
  - Wrong: button turns brick red, correct answer revealed in hunter green
- "Next" arrow appears after answering
- End screen shows score, breakdown, and restart option
- Progress bar at top of card tracks through the set

---

## Confetti System

- Trigger: correct answer only
- Library: use `canvas-confetti` from CDN (https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js)
- Colors: pulled from palette — #a7c957 (yellow-green), #386641 (hunter green), #6a994e (sage), #f2e8cf (champagne), #bc4749 (brick for fun contrast)
- On correct: `confetti({ particleCount: 60, spread: 70, origin: { y: 0.6 }, colors: [...] })`
- On streak of 3 correct in a row: bigger burst — `particleCount: 120, spread: 100`
- On perfect score: full fireworks sequence (multiple confetti calls with spread and angle variation)
- No confetti on wrong answers — just the red highlight

---

## Scoring

- Track current session score in JS state
- Store in localStorage: `amsII_progress.mcq.highScore` and `amsII_progress.mcq.attempts`
- End screen shows:
  - "X / Y correct"
  - "Personal best: Z / Y"
  - Color coded: 90%+ hunter green, 70-89% sage, below 70% brick

---

## Shuffle

- Questions shuffled on every new session (Fisher-Yates shuffle)
- Answer options also shuffled per question
- So MCQ feels different each time even with the same bank

---

## MCQ Bank

### Category 1: School to Work/Author

**Q1.** Which literary school does "To Build a Fire" most clearly belong to?
- A) Impressionism
- B) Regionalism
- C) **Naturalism** ✓
- D) Modernism

**Q2.** Stephen Crane's "The Open Boat" combines which two literary schools?
- A) Realism and Regionalism
- B) **Naturalism and Impressionism** ✓
- C) Modernism and Naturalism
- D) Realism and Modernism

**Q3.** The Spoon River Anthology by Edgar Lee Masters belongs to which school(s)?
- A) Naturalism and Impressionism
- B) Regionalism and Realism
- C) **Modernism and Realism** ✓
- D) Impressionism and Modernism

**Q4.** Edwin Arlington Robinson is best associated with which literary movement?
- A) Naturalism
- B) Regionalism
- C) Impressionism
- D) **Modernism / Realism** ✓

**Q5.** Which author is primarily associated with Naturalism and survival narratives set in the American wilderness?
- A) Stephen Crane
- B) Edwin Arlington Robinson
- C) **Jack London** ✓
- D) Edgar Lee Masters

**Q6.** Which literary school focuses on how individual perception and emotion shape the experience of reality?
- A) Naturalism
- B) Regionalism
- C) **Impressionism** ✓
- D) Determinism

---

### Category 2: Concept and Device Identification

**Q7.** A character dies because the environment and forces of nature made survival impossible, regardless of what choices they made. This best illustrates which concept?
- A) Hubris
- B) Materialism
- C) Impressionism
- D) **Determinism** ✓

**Q8.** In "To Build a Fire," the dog survives while the man dies. This contrast most directly illustrates which theme?
- A) Materialism vs. Poverty
- B) Hubris vs. Humility
- C) **Instinct vs. Intellect** ✓
- D) Fate vs. Free Will

**Q9.** "None of them knew the colour of the sky." This opening line of "The Open Boat" is primarily an example of which technique?
- A) Foreshadowing
- B) Symbolism
- C) **Impressionism — limited, subjective perception** ✓
- D) Dramatic irony

**Q10.** A poem ends with a complete reversal of everything established in its previous lines. What is this structural device called?
- A) Free verse
- B) Dramatic monologue
- C) Foreshadowing
- D) **Volta** ✓

**Q11.** All speakers in the Spoon River Anthology are dead and speak from the grave. What literary form does this use?
- A) Stream of consciousness
- B) Free indirect discourse
- C) **Dramatic monologue** ✓
- D) First-person plural narration

**Q12.** In "Richard Cory," the narrator is:
- A) Richard Cory himself
- B) An omniscient third-person narrator
- C) A close friend of Richard Cory
- D) **The collective working-class townspeople ("we")** ✓

**Q13.** "The Mill" ends without directly stating that the miller's wife died. What technique is this?
- A) Dramatic irony
- B) Understatement
- C) Symbolism
- D) **Narrative ellipsis (implication)** ✓

**Q14.** What does the mill symbolize in Robinson's poem "The Mill"?
- A) The beauty of rural American life
- B) The power of nature over humans
- C) **Industrial obsolescence and lost livelihood** ✓
- D) The American dream

**Q15.** What does the dog represent in "To Build a Fire"?
- A) Loyalty and friendship
- B) The cruelty of nature
- C) **Instinct and natural law** ✓
- D) The human desire for companionship

---

### Category 3: Work Identification and Details

**Q16.** Which work features four men in a lifeboat who can see shore but cannot reach it?
- A) To Build a Fire
- B) Richard Cory
- C) The Mill
- D) **The Open Boat** ✓

**Q17.** In which work does the most physically capable character die while weaker characters survive?
- A) To Build a Fire
- B) Richard Cory
- C) **The Open Boat** ✓
- D) The Mill

**Q18.** Abel Melveny is best described as a character who:
- A) Gave everything to his community and died with dignity
- B) Was destroyed by industrial competition
- C) Drowned himself in despair after losing his trade
- D) **Collected machines and tools but never used them, dying with regret** ✓

**Q19.** Which character in this course's works serves as the clearest contrast to Abel Melveny?
- A) Richard Cory
- B) The miller's wife
- C) **Doc Hill** ✓
- D) Billie the oiler

**Q20.** The old-timer in "To Build a Fire" warns the protagonist not to travel alone in extreme cold. His warning goes unheeded. This is an example of:
- A) Dramatic monologue
- B) Volta
- C) **Foreshadowing** ✓
- D) Narrative ellipsis

---

### Category 4: Analytical Connections

**Q21.** Both "Richard Cory" and "The Mill" share which Modernist technique?
- A) Dramatic monologue with dead speaker
- B) First-person plural narration
- C) Free verse with no rhyme scheme
- D) **Understatement and restrained emotional description of tragedy** ✓

**Q22.** The Naturalist belief that nature is indifferent to human suffering is demonstrated by which specific event in "The Open Boat"?
- A) The men forming a bond during their ordeal
- B) The lighthouse keeper failing to see the men
- C) **Billie the oiler's death despite being the most hardworking and capable** ✓
- D) The correspondent's anger at the sea

**Q23.** Which of the following best explains why "To Build a Fire" is considered Determinist?
- A) The man makes many bad decisions that lead to his death
- B) The dog deliberately abandons the man to save itself
- C) The story is told from the perspective of nature itself
- D) **The man's death was inevitable given the environmental conditions — no choice could have saved him** ✓

**Q24.** Impressionism in literature is most similar to which concept in visual art?
- A) Painting every detail of a scene with photographic accuracy
- B) Using geometric shapes to represent reality
- C) **Capturing the fleeting impression, mood, and light of a moment rather than objective reality** ✓
- D) Depicting the harsh, brutal facts of working-class life

**Q25.** The Second Industrial Revolution is most directly relevant to which work in this course?
- A) To Build a Fire
- B) Doc Hill
- C) Richard Cory
- D) **The Mill** ✓
