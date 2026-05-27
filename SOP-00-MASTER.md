# SOP-00: MASTER OVERVIEW
## American Survey II — Revision Site

---

## Project Identity

**Name:** American Survey II Revision Hub  
**Mascot:** Kiwi — a round green parakeet sitting with kiwi fruits (provided image, white background removed)  
**Purpose:** iPad-first study tool for ENGL3215 final exam at Sultan Qaboos University  
**Target user:** One student, studying alone, needs fast, clear, exam-focused content  

---

## Tech Stack

- **Single HTML file** — no build tools, no frameworks, no dependencies except CDN imports
- **Vanilla JS + CSS** — for maximum portability and iPad compatibility
- **LocalStorage** — for progress tracking, checkmarks, MCQ scores
- **Anthropic API** — for the Essay Models section (AI feedback, see SOP-05)
- **No backend** — everything runs client-side

---

## Color System

Colors sampled directly from the Kiwi parrot image:

```css
/* FROM THE PARROT */
--deep-feather: #2d5a27;        /* darkest feather shadows — deep forest green */
--vivid-feather: #7bc043;       /* bright mid-feather — vivid lime green */
--highlight-feather: #c8e84a;   /* top highlight on bird — yellow-lime */
--kiwi-flesh: #d4e84a;          /* kiwi fruit interior — bright yellow-green */
--kiwi-skin: #8b6914;           /* kiwi fruit skin — warm brown */
--beak-coral: #e8956d;          /* beak — soft salmon coral */

/* PALETTE (non-green accents kept from original) */
--champagne: #f2e8cf;           /* background cards, sidebar */
--brick: #bc4749;               /* wrong answers, danger states */

/* DERIVED USAGE — mapped from parrot colors */
--bg-primary: #faf7f2;          /* near-white warm base */
--bg-secondary: #f2e8cf;        /* champagne — sidebar, cards */
--text-primary: #1a2e18;        /* near-black, green-tinted (from deep feather) */
--text-secondary: #4a6b3a;      /* muted mid-green (between vivid and deep feather) */
--accent-primary: #2d5a27;      /* deep feather — headings, active sidebar, borders */
--accent-mid: #7bc043;          /* vivid feather — hover states, tags, badges */
--accent-light: #c8e84a;        /* highlight feather — highlights, correct answer glow */
--danger: #bc4749;              /* brick — wrong answers, warnings */
--border: #b8d98a;              /* light green border (desaturated vivid feather) */
--confetti-colors: ["#c8e84a", "#2d5a27", "#7bc043", "#f2e8cf", "#bc4749", "#e8956d"]
```

---

## Typography

- **Display/Headings:** `Playfair Display` (Google Fonts) — literary, elegant, fits American literature context
- **Body/UI:** `DM Sans` (Google Fonts) — clean, readable, modern, not generic
- **Monospace/Quotes:** `Lora` (Google Fonts) — serif warmth for literary quotes

---

## Layout (iPad First)

- **Viewport target:** 768px–1024px (iPad portrait and landscape)
- **Sidebar:** Fixed left, always visible, 240px wide
- **Main content area:** Remaining width, scrollable, padded
- **Mobile fallback:** Sidebar collapses to icon-only at <768px

---

## Sections (Sidebar Order)

1. **Home** — welcome screen with Kiwi mascot, exam date, quick stats
2. **Works** — individual pages per literary work (see SOP-02)
3. **Schools** — literary schools/movements (see SOP-03)
4. **Terms** — flip-card flashcard glossary (see SOP-03)
5. **MCQ** — multiple choice quiz with confetti (see SOP-04)
6. **Essay Models** — model paragraph breakdown + AI (see SOP-05)
7. **Quote ID** — identify which work a quote is from (see SOP-06)

---

## Progress System

- Every section item (work page, flashcard, MCQ set, quote) has a checkmark
- Checkmarks stored in `localStorage` under key `amsII_progress`
- Sidebar shows completion count per section (e.g. "Works 3/6")
- Home screen shows overall % complete with a progress ring around Kiwi

---

## Global Rules

1. No em dashes anywhere — use commas, colons, or new sentences instead
2. No semicolons — break into separate sentences
3. Use "because" over "thus/therefore/hence" where possible
4. Emojis allowed and encouraged in work pages and section headers
5. Language is clear, direct, not dumbed down but not academic-stiff
6. Every section has a unique visual identity (see per-section SOPs)
7. Animations must feel fast and satisfying, never slow or loading-heavy
8. No Lorem Ipsum — all content is real exam content

---

## File Structure

Single file: `index.html`  
All CSS in `<style>` block  
All JS in `<script>` block at bottom  
Parrot image embedded as base64 OR loaded from relative path `kiwi.png`

---

## SOP Index

| File | Covers |
|------|--------|
| SOP-00-MASTER.md | This file — architecture, palette, rules |
| SOP-01-LAYOUT.md | Sidebar, navigation, home screen, progress system |
| SOP-02-WORKS.md | All 6 literary works, their content and page designs |
| SOP-03-SCHOOLS-TERMS.md | Literary schools + flip-card terms |
| SOP-04-MCQ.md | MCQ bank, scoring, confetti system |
| SOP-05-ESSAY.md | Model paragraph breakdown + AI feedback integration |
| SOP-06-QUOTEID.md | Quote identification game |
| SOP-07-CONTENT.md | All raw exam content (themes, quotes, devices, etc.) |
