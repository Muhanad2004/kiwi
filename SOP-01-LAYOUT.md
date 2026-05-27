# SOP-01: LAYOUT, NAVIGATION & HOME SCREEN

---

## Sidebar

**Width:** 240px, fixed left, full height  
**Background:** `--bg-secondary` (#f2e8cf champagne)  
**Border-right:** 1px solid `--border`  
**Box-shadow:** subtle right shadow to lift it from content

### Sidebar Top
- Kiwi mascot image, ~60px, centered
- Site name: "Kiwi Reads" or "Survey II" in Playfair Display, hunter green
- Thin divider

### Sidebar Nav Items

Each item has:
- An emoji icon (fixed, not icon font)
- Label in DM Sans medium
- A completion badge (e.g. "3/6") in sage green pill
- Active state: hunter green left border (4px), bg tint, text goes bold
- Hover state: bg `--yellow-green` at 15% opacity, smooth transition 150ms

Nav items and their emojis:
```
🏠 Home
📖 Works          [x/6]
🏫 Schools        [x/5]
🃏 Terms          [x/N]
❓ MCQ            [x/N]
✍️ Essay Models   [x/3]
💬 Quote ID       [x/N]
```

### Sidebar Bottom
- Small text: "Final: May 26 · 11:30–13:30"
- Exam countdown (days remaining) — computed from today's date in JS

---

## Main Content Area

**Left margin:** 240px (sidebar width)  
**Padding:** 40px top, 48px horizontal  
**Max content width:** 800px centered in available space  
**Background:** `--bg-primary` (#faf7f0)  
**Scroll behavior:** smooth  

### Section Header Pattern (used in all sections)
```
[emoji] Section Title          ← Playfair Display, 28px, hunter green
Subtitle or context line       ← DM Sans, 14px, text-secondary
────────────────────────────   ← thin border line, sage green
```

---

## Home Screen

The home screen is the landing page. It should feel welcoming and motivating, not like a dashboard.

### Layout (top to bottom):

**1. Hero block**
- Large Kiwi image, centered, ~140px
- Progress ring around Kiwi (SVG circle, animated on load)
- Ring color: hunter green filling clockwise based on overall % done
- Below Kiwi: "Ready to ace it, Muhanad." in Playfair Display, 24px
- Subtext: "Final exam · May 26 · 11:30–13:30" in DM Sans, muted

**2. Quick Stats Row**
Three small cards side by side:
- "Works covered" — X/6
- "Terms learned" — X/N  
- "MCQ score" — X% (last session average)

Card style: champagne bg, sage border, rounded-12px, subtle shadow

**3. Exam Focus Callout**
A warm champagne card with hunter green left border:
```
📌 What the exam will test
• Essay on "To Build a Fire" — prepare themes + characteristics
• Quote identification — know your works cold
• MCQ — literary schools, authors, analytical links
• Short answers — terms, devices, specific details
• Naturalism + Determinism — core of everything
```

**4. Quick Jump Grid**
Six cards, 2 columns, each linking to a section:
- Works, Schools, Terms, MCQ, Essay Models, Quote ID
- Each card shows section emoji, title, completion badge
- Hover: slight lift (transform: translateY(-2px)), shadow deepens
- Click: navigates to section (JS section switching)

---

## Navigation System (JS)

All navigation is JS-driven, single page app style:
- Each section is a `<div class="section" id="section-name">` — hidden by default
- Active section: `display: block` (or flex)
- Sidebar clicks call `showSection(id)` which:
  1. Hides all sections
  2. Shows target section
  3. Updates sidebar active state
  4. Scrolls main area to top
  5. Saves `localStorage.amsII_lastSection`

On page load: restore last visited section, or show Home.

---

## Progress System (JS + LocalStorage)

Storage key: `amsII_progress`  
Structure:
```json
{
  "works": {
    "to-build-a-fire": false,
    "the-open-boat": false,
    "doc-hill": false,
    "abel-melveny": false,
    "richard-cory": false,
    "the-mill": false
  },
  "schools": {
    "naturalism": false,
    "impressionism": false,
    "realism": false,
    "modernism": false,
    "regionalism": false
  },
  "terms": {},
  "mcq": { "highScore": 0, "attempts": 0 },
  "essay": { "viewed": [] },
  "quoteId": { "correct": 0, "total": 0 }
}
```

Each checkmark (checkbox or toggle) calls `markDone(section, key)` which:
1. Updates the progress object
2. Saves to localStorage
3. Updates sidebar badge counts
4. Updates home screen stats

---

## Animations (Global)

- **Section transition:** fade in 200ms ease on section show
- **Card hover:** translateY(-2px) + shadow deepens, 150ms
- **Page load:** staggered fade-in on sidebar items (animation-delay 50ms per item)
- **Progress ring:** SVG stroke-dashoffset animates on load, 800ms ease-out
- No animations longer than 400ms for content reveals (keeps it snappy)
