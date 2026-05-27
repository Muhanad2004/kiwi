# SOP-08: AGENT INSTRUCTIONS & BUILD ORDER

This file tells a coding agent exactly how to build the site. Read all SOP files before writing a single line of code.

---

## Files to Read First (in order)

1. SOP-00-MASTER.md — palette, typography, rules, file structure
2. SOP-01-LAYOUT.md — sidebar, navigation, home screen, progress
3. SOP-02-WORKS.md — all 6 works content and visual identity per work
4. SOP-03-SCHOOLS-TERMS.md — schools content + term bank
5. SOP-04-MCQ.md — MCQ bank and confetti system
6. SOP-05-ESSAY.md — essay model breakdown
7. SOP-06-QUOTEID.md — quote ID game and quote bank
8. SOP-07-CONTENT.md — flat content reference for all sections

---

## Output

Single file: `index.html`
Self-contained — all CSS in `<style>`, all JS in `<script>` at bottom.
Parrot image: embed as base64 (the provided webp image, white background removed via CSS `mix-blend-mode: multiply` or similar — do not require a separate image file).

---

## CDN Imports (include in `<head>`)

```html
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=DM+Sans:wght@300;400;500;600&family=Lora:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">

<!-- canvas-confetti -->
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>
```

---

## Build Order

Build in this sequence. Each phase should be testable before moving to the next.

### Phase 1: Shell and Navigation
- HTML structure: sidebar + main content area
- All 7 section divs (hidden by default)
- Sidebar with nav items, emoji icons, labels
- `showSection(id)` JS function
- Active state styling
- localStorage: save/restore last section
- Home screen: Kiwi image, progress ring (static first), exam date
- Color variables, typography applied globally
- Responsive: sidebar collapses to icon-only below 768px

### Phase 2: Progress System
- `amsII_progress` localStorage object initialized on first load
- `markDone(section, key)` function
- Sidebar badge counts update dynamically
- Home screen stats update dynamically
- Progress ring animates based on real % on home screen

### Phase 3: Works Section
- Sub-nav pill tabs for 6 works
- Each work page rendered with its unique visual identity (see SOP-02)
- All content blocks populated from SOP-02 and SOP-07
- Checkmark per work stored in progress system
- Mark as Done button at bottom of each work page

### Phase 4: Schools + Terms
- Schools: sub-nav pill tabs for 5 schools
- Each school page fully populated from SOP-03
- Terms: flip card grid (3 columns iPad, 2 columns mobile)
- CSS 3D flip on click
- Checkmark per card in localStorage
- Filter buttons: All / Literary Devices / Schools / Concepts

### Phase 5: MCQ
- Shuffle function (Fisher-Yates)
- One question at a time card
- 4 answer options, immediate feedback on click
- Correct: sage green + confetti
- Wrong: brick red + reveal correct in hunter green
- Streak tracking (3 correct = bigger confetti)
- End screen: score, personal best
- Progress stored in localStorage

### Phase 6: Essay Models
- Three sub-pages: The Model / Applied / Cheat Sheet
- Collapsible step blocks for The Model page
- Full formatted paragraph for Applied page (Lora serif for paragraph text)
- Clean cheat sheet card

### Phase 7: Quote ID
- Quote card display in Lora serif
- 4 work title pill buttons
- Confetti on correct
- Score tracker
- End screen with restart

### Phase 8: Polish
- Staggered fade-in on page load (sidebar items)
- Hover animations on all cards (translateY -2px)
- Section transition fade (200ms)
- Progress ring animation (800ms ease-out)
- Ensure all content is real (no placeholders)
- Test localStorage persistence
- iPad viewport check (768px–1024px)

---

## Design Rules (repeat for emphasis)

1. Each work page in the Works section must have a visually distinct identity — different color treatment, different mood. Do not use the same card layout for all 6 works. See SOP-02 for the unique identity spec per work.
2. Every section has its own visual character — MCQ feels different from Works, which feels different from Terms.
3. Light theme only. Background: #faf7f0. No dark mode.
4. No em dashes. No semicolons.
5. Playfair Display for headings. DM Sans for body and UI. Lora for quotes and poem text.
6. Confetti colors: #a7c957, #386641, #6a994e, #f2e8cf, #bc4749.
7. Parrot image appears in sidebar header and on home screen. Use `mix-blend-mode: multiply` to remove white background.
8. All content must come from SOP-07 and section SOPs — no invented or generalized content.
9. Language: clear, direct, uses "because" over formal connectors, has emojis in work pages and section headers, not childish.

---

## Kiwi Parrot Image Handling

File provided: `green-parakeet-bird-sitting-kiwi-fruit-cute-sits-surrounded-vibrant-illustration-any-project-tropical-birds-372156237.webp`

Usage:
```css
.kiwi-img {
  mix-blend-mode: multiply; /* removes white background */
  width: 60px;
  height: auto;
}
```

The image has a white background — `mix-blend-mode: multiply` on a light background makes white transparent. This works well on the champagne sidebar background.

Embed as base64 in the HTML so the site is fully self-contained, OR reference as a relative path if the image file will sit alongside index.html.

---

## Common Mistakes to Avoid

- Do not make all work pages look the same — each one has a unique spec in SOP-02
- Do not use placeholder content — all MCQ, quotes, and content must come from the SOP files
- Do not break localStorage by writing conflicting keys — use the schema in SOP-01
- Do not make animations longer than 400ms for content (except the progress ring which is 800ms)
- Do not use Inter, Roboto, or Arial — use the specified fonts only
- Do not use purple, blue, or grey as primary colors — the palette is hunter green, sage, yellow-green, champagne, brick only
- Do not use semicolons or em dashes in any displayed text
