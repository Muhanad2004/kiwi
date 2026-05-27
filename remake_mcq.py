"""Remake MCQ tab: replace HTML, JS (MCQ_BANK + engine), add CSS, update progress."""
import re

with open(r'C:/Users/Muhanad/Desktop/AS2_Revision/index.html', encoding='utf-8') as f:
    content = f.read()

# ── 1. ADD topicBests to DEFAULT_PROGRESS ────────────────────────────────────
content = content.replace(
    "  quoteId: { correct: 0, total: 0 }\n};",
    "  quoteId: { correct: 0, total: 0 },\n  topicBests: {}\n};"
)

# ── 2. ADD CSS after .mcq-end-best line ──────────────────────────────────────
NEW_CSS = """
/* MCQ Topic Hub */
.mcq-section-label {
  font-size: 12px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--text-secondary); margin-bottom: 12px; margin-top: 4px;
}
.topic-card-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(148px, 1fr));
  gap: 12px; margin-bottom: 8px;
}
.topic-card {
  background: white; border-radius: 10px; padding: 16px 14px; cursor: pointer;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
  box-shadow: 0 1px 4px rgba(0,0,0,0.08);
}
.topic-card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.12); }
.topic-card.quiz-done { background: rgba(45,90,39,0.06); }
.topic-card-emoji { font-size: 22px; margin-bottom: 8px; }
.topic-card-title { font-size: 13px; font-weight: 600; color: var(--text-primary); margin-bottom: 3px; line-height: 1.35; }
.topic-card-meta { font-size: 11px; color: var(--text-secondary); }
.topic-card-best { font-size: 11px; color: var(--accent-primary); font-weight: 700; margin-top: 5px; }
.mcq-back-btn {
  background: none; border: none; color: var(--accent-primary); font-size: 13px;
  font-weight: 600; cursor: pointer; padding: 0; margin-bottom: 16px; font-family: 'DM Sans', sans-serif;
}
.mcq-back-btn:hover { text-decoration: underline; }
.mcq-topic-title {
  font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700;
  color: var(--text-primary); margin-bottom: 20px;
}"""

content = content.replace(
    ".mcq-end-best { font-size: 13px; color: var(--text-secondary); font-style: italic; }",
    ".mcq-end-best { font-size: 13px; color: var(--text-secondary); font-style: italic; }" + NEW_CSS
)

# ── 3. REPLACE MCQ HTML SECTION ──────────────────────────────────────────────
OLD_MCQ_HTML = '''  <!-- MCQ ──────────────────────────────────────────────────── -->
  <div class="section" id="section-mcq">
    <div class="section-inner">
      <div class="section-header">
        <h1>❓ MCQ</h1>
        <div class="subtitle">40 questions, shuffled each session — confetti for correct answers</div>
        <div class="section-divider"></div>
      </div>

      <!-- START SCREEN -->
      <div id="mcq-start">
        <div class="mcq-start-card">
          <div class="mcq-start-emoji">❓</div>
          <h2 class="mcq-start-title">Practice MCQ</h2>
          <p class="mcq-start-desc">40 questions covering all works, literary schools, devices, and deeper analytical thinking. Questions and options shuffle every session.</p>
          <div class="mcq-best-row" id="mcq-best-row" style="display:none">
            <span>Personal best:</span>
            <span class="mcq-best-score" id="mcq-best-display">–</span>
          </div>
          <button class="mcq-start-btn" onclick="startMCQ()">Start Quiz</button>
        </div>
      </div>

      <!-- QUIZ SCREEN -->
      <div id="mcq-quiz" style="display:none">
        <div class="mcq-card">
          <div class="mcq-meta-row">
            <div class="mcq-progress-bar-wrap"><div class="mcq-progress-bar" id="mcq-progress-bar"></div></div>
            <div class="mcq-qnum" id="mcq-qnum">Q1 / 25</div>
          </div>
          <div class="mcq-question" id="mcq-question"></div>
          <div class="mcq-options" id="mcq-options"></div>
          <div class="mcq-feedback" id="mcq-feedback" style="display:none"></div>
          <div class="mcq-next-row" id="mcq-next-row" style="display:none">
            <button class="mcq-next-btn" onclick="nextMCQ()">Next →</button>
          </div>
        </div>
      </div>

      <!-- END SCREEN -->
      <div id="mcq-end" style="display:none">
        <div class="mcq-end-card">
          <div class="mcq-end-score-label">Your score</div>
          <div class="mcq-end-score" id="mcq-end-score"></div>
          <div class="mcq-end-sub" id="mcq-end-sub"></div>
          <div class="mcq-end-best" id="mcq-end-best"></div>
          <button class="mcq-start-btn" onclick="startMCQ()" style="margin-top:24px">Try Again</button>
          <button class="mcq-ghost-btn" onclick="showSection(\'home\')" style="margin-top:10px">Back to Home</button>
        </div>
      </div>

    </div>
  </div>'''

NEW_MCQ_HTML = '''  <!-- MCQ ──────────────────────────────────────────────────── -->
  <div class="section" id="section-mcq">
    <div class="section-inner">
      <div class="section-header">
        <h1>❓ MCQ</h1>
        <div class="subtitle">Quiz by topic — pick a work or literary school to drill</div>
        <div class="section-divider"></div>
      </div>

      <!-- HUB -->
      <div id="mcq-hub">
        <div class="mcq-section-label">📖 By Work</div>
        <div class="topic-card-grid" id="mcq-work-cards"></div>
        <div class="mcq-section-label" style="margin-top:28px">🏫 By School</div>
        <div class="topic-card-grid" id="mcq-school-cards"></div>
      </div>

      <!-- TOPIC QUIZ PANEL -->
      <div id="mcq-topic-quiz" style="display:none">
        <button class="mcq-back-btn" onclick="backToMcqHub()">← All Topics</button>
        <div class="mcq-topic-title" id="mcq-topic-title"></div>
        <div id="tq-quiz">
          <div class="mcq-card">
            <div class="mcq-meta-row">
              <div class="mcq-progress-bar-wrap"><div class="mcq-progress-bar" id="tq-progress-bar"></div></div>
              <div class="mcq-qnum" id="tq-qnum">Q1 / 7</div>
            </div>
            <div class="mcq-question" id="tq-question"></div>
            <div class="mcq-options" id="tq-options"></div>
            <div class="mcq-feedback" id="tq-feedback" style="display:none"></div>
            <div class="mcq-next-row" id="tq-next-row" style="display:none">
              <button class="mcq-next-btn" onclick="nextTopicQ()">Next →</button>
            </div>
          </div>
        </div>
        <div id="tq-end" style="display:none">
          <div class="mcq-end-card">
            <div class="mcq-end-score-label">Your score</div>
            <div class="mcq-end-score" id="tq-end-score"></div>
            <div class="mcq-end-sub" id="tq-end-sub"></div>
            <button class="mcq-start-btn" onclick="retryTopicQuiz()" style="margin-top:24px">Try Again</button>
            <button class="mcq-ghost-btn" onclick="backToMcqHub()" style="margin-top:10px">← All Topics</button>
          </div>
        </div>
      </div>

    </div>
  </div>'''

if OLD_MCQ_HTML in content:
    content = content.replace(OLD_MCQ_HTML, NEW_MCQ_HTML)
    print('OK: MCQ HTML replaced')
else:
    print('MISS: MCQ HTML not found — check exact whitespace')

# ── 4. REPLACE MCQ_BANK + JS ENGINE ──────────────────────────────────────────
# Find the block from "const MCQ_BANK" to end of "function initMCQStartScreen() {...}"
bank_start = content.find('const MCQ_BANK = [')
init_fn_start = content.find('function initMCQStartScreen()')
init_fn_end = content.find('\n}', init_fn_start) + 2  # end of that function

OLD_JS_BLOCK = content[bank_start:init_fn_end]

NEW_JS_BLOCK = r"""const TOPIC_BANKS = {
  tbf: {
    title: 'To Build a Fire', emoji: '🔥', type: 'work',
    questions: [
      { q: 'Which literary school does "To Build a Fire" most clearly belong to?', options: ['Impressionism', 'Regionalism', 'Naturalism', 'Modernism'], correct: 2, explanation: 'London shows nature as an indifferent, deterministic force. The cold and terrain seal the man\'s fate regardless of his choices — that is Naturalism.' },
      { q: 'The dog survives while the man dies. This contrast most directly illustrates which theme?', options: ['Materialism vs Poverty', 'Hubris vs Humility', 'Instinct vs Intellect', 'Fate vs Free Will'], correct: 2, explanation: 'The dog cannot reason but survives by following instinct. The man can reason but dies because he trusts intellect over instinct. London\'s argument: in nature, instinct beats intelligence.' },
      { q: 'Why is it significant that the man in "To Build a Fire" has no name?', options: ['London forgot to name him', 'It creates mystery', 'It universalizes him — he represents any human who overestimates intellect against nature', 'It is a common short story convention'], correct: 2, explanation: 'A nameless man becomes every man. London removes his identity so he becomes a universal symbol of human pride against natural indifference.' },
      { q: 'The old-timer\'s warning that the man should not travel alone in extreme cold is an example of:', options: ['Dramatic monologue', 'Volta', 'Foreshadowing', 'Narrative ellipsis'], correct: 2, explanation: 'The old-timer predicts exactly what will happen. The man ignores it — making the foreshadowing even more pointed and ironic.' },
      { q: 'A student argues: "The man dies because he made bad decisions." A Naturalist critic would most likely respond:', options: ['"He should have listened to the old-timer"', '"His death was inevitable — the environment determined the outcome regardless of his choices"', '"He lacked wilderness survival skills"', '"He should have built the fire in a more sheltered location"'], correct: 1, explanation: 'Naturalism says environment and biology determine outcomes, not individual choices. The cold was simply too extreme. His decisions were irrelevant once he entered those conditions.' },
      { q: 'What does the dog represent in "To Build a Fire"?', options: ['Loyalty and companionship', 'The cruelty of the wilderness', 'Pure instinct and natural law', 'The human desire for belonging'], correct: 2, explanation: 'The dog represents pure instinct and natural law — it knows the cold is deadly without reasoning. It has what the man lacks: a direct, honest relationship with nature.' },
      { q: 'The man\'s repeated failed attempts to light a fire after his hands go numb illustrate which Naturalist idea?', options: ['Human ingenuity triumphs over adversity', 'Nature forces humans to adapt', 'Human intelligence is helpless once biological conditions deteriorate beyond a threshold', 'Persistence is always rewarded'], correct: 2, explanation: 'No amount of cleverness or effort can overcome the biological reality of frozen hands. The body\'s deterioration is a condition outside human control — determinism in action.' },
      { q: 'This story is considered Determinist because:', options: ['The man chooses to ignore the old-timer\'s advice', 'The dog chooses to abandon the man', 'The man\'s death was inevitable given the extreme environmental conditions — no choice could have changed it', 'London believed in fate and destiny'], correct: 2, explanation: 'Determinism: outcomes are fixed by conditions. The cold was already fatal before the man made any choices. His fate was sealed by environment, not free will.' }
    ]
  },
  tob: {
    title: 'The Open Boat', emoji: '⛵', type: 'work',
    questions: [
      { q: '"The Open Boat" combines which two literary schools?', options: ['Realism and Regionalism', 'Naturalism and Impressionism', 'Modernism and Naturalism', 'Realism and Modernism'], correct: 1, explanation: 'Naturalism: Billie\'s death proves nature cares nothing for human survival. Impressionism: the story is told through the crew\'s shifting emotions and subjective perceptions, not objective narration.' },
      { q: '"None of them knew the colour of the sky." This opening line is primarily an example of:', options: ['Foreshadowing', 'Symbolism', 'Impressionism — the men\'s limited, subjective perception of their environment', 'Dramatic irony'], correct: 2, explanation: 'Crane opens with what the men cannot see — too focused on surviving to look up. This limited, subjective perception is Impressionism in its purest form.' },
      { q: 'Which character\'s death is the most ironic Naturalist statement in the story?', options: ['The captain', 'The cook', 'The correspondent', 'Billie the oiler — the strongest man, who dies'], correct: 3, explanation: 'Billie is the strongest, most capable of the four men. He is also the one who drowns. Nature rewards no one — this brutal irony is Crane\'s clearest Naturalist statement.' },
      { q: 'The correspondent asks: "If I am going to be drowned, why was I allowed to come thus far?" His inability to answer reveals:', options: ['He is confused from exhaustion', 'The universe offers no meaning or justice — a core Naturalist idea', 'He blames the captain for their situation', 'He is starting to accept his fate'], correct: 1, explanation: 'The correspondent wants the universe to explain or justify his possible death. There is no answer — Naturalism says the universe has no interest in individual human lives or fates.' },
      { q: 'The correspondent feels strange calm and even humor at moments despite being in mortal danger. This shifting emotional state is most characteristic of:', options: ['Naturalism', 'Impressionism', 'Realism', 'Determinism'], correct: 1, explanation: 'Impressionism tracks shifting, illogical emotional states. The calm and humor in the face of death makes no rational sense — and that is exactly the point. Inner states don\'t follow logic.' },
      { q: 'Crane\'s story is based on his real shipwreck, yet he presented it as fiction rather than journalism. This choice suggests:', options: ['He wanted legal protection', 'He wanted to use Impressionist technique to capture the subjective emotional truth of the experience', 'He changed the events so much it could no longer be called journalism', 'Fiction sold better than journalism'], correct: 1, explanation: 'Crane could have written journalism. Instead he fictionalized the experience to use Impressionist technique — capturing how it felt subjectively, not just what factually occurred.' },
      { q: 'What is Crane\'s clearest Naturalist statement in "The Open Boat"?', options: ['The men bond and cooperate to survive', 'The lighthouse keeper fails to see them in time', 'Billie the oiler dies despite being the most capable — nature rewards no one', 'The correspondent survives because he is the protagonist'], correct: 2, explanation: 'Billie is strongest; he dies. Weaker men survive. This random, unjust outcome demonstrates nature\'s indifference most directly.' }
    ]
  },
  dochill: {
    title: 'Doc Hill', emoji: '🩺', type: 'work',
    questions: [
      { q: 'Doc Hill is part of which major work?', options: ['To Build a Fire', 'The Open Boat', 'Spoon River Anthology', 'Richard Cory'], correct: 2, explanation: 'Doc Hill is one of the many poems in Edgar Lee Masters\' Spoon River Anthology — a collection of dead speakers reviewing their own lives.' },
      { q: 'Doc Hill speaks from the grave. What does this narrative device most effectively achieve?', options: ['It creates suspense about whether he survived', 'It removes motivation to lie or self-deceive — the dead have nothing left to prove, so the account feels honest', 'It is a religious reference to the afterlife', 'It makes the poem easier to write'], correct: 1, explanation: 'Dead speakers have nothing left to prove. The grave-speaking device strips away social pretense and allows honest, unfiltered reflection on a life.' },
      { q: 'Doc Hill treated the poor for free throughout his life. In the context of Realism, this detail is significant because:', options: ['It makes Doc Hill appear saintly', 'It shows class inequality and economic hardship in ordinary American life, without romanticizing or heroizing it', 'It proves doctors in this era were poorly paid', 'It illustrates the theme of divine reward for good deeds'], correct: 1, explanation: 'Realism shows life as it is without sentimentalizing. Doc Hill\'s quiet service is an honest depiction of class, poverty, and economic hardship — no heroic framing.' },
      { q: 'Doc Hill\'s life is best contrasted with which other Spoon River character?', options: ['Richard Cory', 'The miller\'s wife', 'Abel Melveny', 'Billie the oiler'], correct: 2, explanation: 'Doc Hill gave everything and is remembered with love. Abel Melveny owned everything and is remembered with pity. Action and giving vs accumulation and regret.' },
      { q: 'What broader human truth does Masters argue through Doc Hill?', options: ['That doctors live better lives than craftsmen', 'That a meaningful life comes from what you give and do, not from what you own or collect', 'That small towns produce both generous and selfish people equally', 'That regret is an inevitable part of human experience'], correct: 1, explanation: 'Doc Hill gave everything; Abel Melveny owned everything. The contrast argues: what you give and do gives life meaning — what you accumulate does not.' },
      { q: 'Which literary school does Doc Hill belong to?', options: ['Naturalism', 'Impressionism', 'Realism', 'Modernism'], correct: 2, explanation: 'Doc Hill depicts ordinary small-town American life — a doctor\'s quiet service, class realities, and community relationships — without romanticizing. That is Realism.' },
      { q: 'The literary form used in Doc Hill — one dead character speaking directly to the reader reviewing their own life — is called:', options: ['Stream of consciousness', 'Free indirect discourse', 'Dramatic monologue', 'First-person plural narration'], correct: 2, explanation: 'Each Spoon River poem is a dramatic monologue: one speaker addresses the reader directly from a specific persona and point of view.' }
    ]
  },
  abel: {
    title: 'Abel Melveny', emoji: '⚙️', type: 'work',
    questions: [
      { q: 'Abel Melveny is best described as a character who:', options: ['Gave everything to his community and died content', 'Was destroyed by industrial competition', 'Collected tools and machines throughout his life but never used them, dying with regret', 'Drowned himself in despair'], correct: 2, explanation: 'Abel spent his life accumulating machines and tools — sewing machines, grinders, cranes — but never actually used any of them. His life was potential that was never realized.' },
      { q: 'As the list of Abel\'s machines grows longer in the poem, what emotional effect does this catalogue create?', options: ['Excitement and admiration for his ambition', 'A growing sense of absurdity and sadness — each machine represents one more dream never pursued', 'Respect for his knowledge of technology', 'Confusion about what Abel actually wanted to build'], correct: 1, explanation: 'The list of machines becomes absurd and sad because none were ever used. The longer it gets, the more pitiful Abel becomes. Each machine = one more plan, one more dream, never pursued.' },
      { q: 'What does Abel Melveny\'s collection of unused machines symbolize?', options: ['The promise of the industrial revolution', 'Material success in small-town America', 'Unfulfilled potential — a life of accumulation with no action', 'The dangers of industrialization'], correct: 2, explanation: 'Abel\'s machines are symbols of intention without execution. They represent everything he meant to do, start, or build — but never did. Potential that dies with him.' },
      { q: 'Abel Melveny uses the same narrative device as Doc Hill. What is this form called?', options: ['Stream of consciousness', 'Free indirect discourse', 'Dramatic monologue — a dead speaker addressing the reader directly', 'First-person plural narration'], correct: 2, explanation: 'Like all Spoon River poems, Abel Melveny is a dramatic monologue: one dead speaker addresses the reader directly, reviewing their own life.' },
      { q: 'Abel Melveny contrasts most sharply with Doc Hill. What is the key difference?', options: ['Abel was rich; Doc Hill was poor', 'Abel accumulated without acting; Doc Hill gave and acted throughout his life', 'Abel was industrious; Doc Hill was lazy', 'Abel died young; Doc Hill lived to old age'], correct: 1, explanation: 'Abel accumulated (machines, things) but never acted. Doc Hill acted (served the community) but accumulated nothing. Masters uses this contrast to argue that action and giving give life meaning.' },
      { q: 'What argument does Masters make through the character of Abel Melveny?', options: ['That the industrial revolution destroyed traditional crafts', 'That accumulating wealth and possessions without using them or giving makes a life meaningless', 'That small-town American life was characterized by regret', 'That machines are inherently dehumanizing'], correct: 1, explanation: 'Abel\'s regret is total. His life was full of potential (machines, plans) but empty of action. Masters\' argument: a life measured in things owned rather than things done is a wasted life.' }
    ]
  },
  cory: {
    title: 'Richard Cory', emoji: '👑', type: 'work',
    questions: [
      { q: 'Who narrates "Richard Cory"?', options: ['Richard Cory himself', 'An omniscient third-person narrator', 'A close friend of Richard Cory', 'The collective working-class townspeople ("we")'], correct: 3, explanation: 'Robinson uses "we" throughout — the collective voice of the working-class town. We only hear what the town perceived: Cory\'s polished exterior. His inner life is never accessible.' },
      { q: 'The ending of "Richard Cory" — where Cory goes home and shoots himself — is an example of which poetic device?', options: ['Free verse', 'Dramatic monologue', 'Foreshadowing', 'Volta — a sudden reversal of everything the poem has established'], correct: 3, explanation: 'Volta (Italian for "turn") is a sudden reversal in a poem\'s direction. Richard Cory builds a golden image for seven stanzas, then the volta destroys it in two lines.' },
      { q: 'Robinson presents the tragedy of Richard Cory\'s death in flat, emotionless language. This technique is called:', options: ['Dramatic irony', 'Symbolism', 'Understatement', 'Narrative ellipsis'], correct: 2, explanation: 'The most devastating moment — Cory\'s suicide — is described with the same quiet tone as his elegant appearance. Stating tragedy without drama or emotional commentary is understatement.' },
      { q: 'The most important literary effect of Robinson\'s choice to use "we" as narrator is:', options: ['It makes the poem feel intimate', 'We only ever see Cory\'s surface — we never access his inner life, which is the entire point of the poem', 'It shows that everyone in town liked Cory', 'It creates a sense of class solidarity'], correct: 1, explanation: 'The "we" narrator means the reader only ever sees what the town saw: Cory\'s polished exterior. His inner pain is completely hidden. The irony: nobody actually knew him.' },
      { q: '"Richard Cory" belongs to which literary school(s)?', options: ['Naturalism and Impressionism', 'Regionalism and Realism', 'Modernism and Realism', 'Impressionism and Modernism'], correct: 2, explanation: 'Modernism: irony, unconventional form, hidden inner lives, disillusionment. Realism: small-town American life depicted honestly without romanticizing.' },
      { q: 'Both "Richard Cory" and "The Mill" deal with suicide presented quietly and without melodrama. What technique do they share?', options: ['Dramatic monologue with dead speaker', 'First-person plural narration', 'Free verse', 'Understatement — tragedy described in restrained, flat language'], correct: 3, explanation: 'Both poems present the most devastating moments with quiet, restrained language. The deaths are described flatly, without dramatic commentary. This is understatement.' },
      { q: 'What is the key narrative difference between how Cory\'s death is revealed vs the miller\'s death in "The Mill"?', options: ['Cory\'s death is expected; the miller\'s is a surprise', 'Cory\'s death is a sudden shock at the poem\'s end; the miller\'s is discovered slowly through the wife\'s grief and domestic detail', 'The Mill is more emotionally dramatic', 'Cory\'s death is implied; the miller\'s is explicit'], correct: 1, explanation: 'Richard Cory: seven stanzas build him up, then one flat line destroys it — sudden shock. The Mill: the wife discovers her husband\'s death slowly through cold tea, dead fire, and then walking toward the pond.' },
      { q: 'The fact that the whole town envied Richard Cory while he was secretly in despair is an example of:', options: ['Foreshadowing', 'Dramatic irony — the audience recognizes a painful gap between what the townspeople believe and reality', 'Narrative ellipsis', 'Volta'], correct: 1, explanation: 'The town envies Cory\'s perfect life while he is secretly miserable enough to shoot himself. This gap between what observers believe and the real situation is dramatic irony.' }
    ]
  },
  mill: {
    title: 'The Mill', emoji: '⚒️', type: 'work',
    questions: [
      { q: 'What does the mill symbolize in Robinson\'s poem?', options: ['The beauty of rural American life', 'The power of nature over humans', 'Industrial obsolescence — a trade and an identity made worthless by the machine age', 'The American dream'], correct: 2, explanation: 'The mill represents the miller\'s identity, livelihood, and purpose. The industrial revolution made his craft obsolete. When the trade dies, so does he — his identity was inseparable from his work.' },
      { q: '"The tea was cold, the fire was dead." These details at the start of "The Mill" function primarily as:', options: ['Realistic description of a poor household', 'Symbols of comfort contrasting with what follows', 'Foreshadowing — cold and dead details signal that the miller is dead and warmth has left their life', 'A Naturalist description of rural poverty'], correct: 2, explanation: 'The cold tea and dead fire are domestic symbols of warmth that is gone. They signal something is wrong before we are told what. This is foreshadowing — and symbolism of death entering the household.' },
      { q: 'Robinson leaves the wife\'s death unstated at the poem\'s end. What technique is this?', options: ['Dramatic irony', 'Understatement', 'Symbolism', 'Narrative ellipsis — leaving key events out for the reader to infer'], correct: 3, explanation: 'Robinson never states that the wife dies. We infer it from cold/dead imagery and the fact that she walks toward the pond. Leaving key events out for the reader to complete is narrative ellipsis.' },
      { q: 'The miller is not lazy or incompetent — his trade has simply been replaced by machines. How does this connect to Naturalist ideas?', options: ['It shows humans can overcome any obstacle', 'External economic forces destroyed him regardless of his personal worth or effort — like how nature destroys characters in Naturalism', 'It proves the industrial revolution was harmful to workers', 'It shows that the miller should have learned a new trade'], correct: 1, explanation: 'Like Naturalism\'s determinism, the miller is destroyed by forces entirely outside his control. His worth and effort are irrelevant — the economic environment determined his fate.' },
      { q: 'Which historical period is most directly relevant to understanding "The Mill"?', options: ['The Civil War era', 'The Second Industrial Revolution — which replaced traditional crafts with machines', 'The Great Depression', 'The Reconstruction era'], correct: 1, explanation: 'The Second Industrial Revolution replaced traditional trades and crafts with machines. The miller\'s entire occupation becomes obsolete — the historical backdrop is essential to his tragedy.' },
      { q: '"Richard Cory" and "The Mill" share which Modernist technique?', options: ['Dead speaker reviewing their own life', 'First-person plural narrator', 'Free verse with no rhyme scheme', 'Understatement — the most devastating moments described in flat, restrained language'], correct: 3, explanation: 'Both poems present tragedy through quiet, restrained language. The most devastating moments are described flatly, without drama. This is understatement — a key Modernist technique.' },
      { q: 'Who wrote "The Mill"?', options: ['Jack London', 'Stephen Crane', 'Edgar Lee Masters', 'Edwin Arlington Robinson'], correct: 3, explanation: 'Edwin Arlington Robinson wrote both "Richard Cory" and "The Mill." He is associated with Modernism and Realism, and is known for portraits of hidden inner lives in realistic small-town settings.' }
    ]
  },
  naturalism: {
    title: 'Naturalism', emoji: '🌿', type: 'school',
    questions: [
      { q: 'What is the core belief of Naturalism?', options: ['Humans shape their own destiny through free will', 'Individual choices always determine outcomes', 'Environment, biology, and external forces determine outcomes — human choice is secondary or irrelevant', 'Nature is a source of beauty and spiritual renewal'], correct: 2, explanation: 'Naturalism holds that environment and biology determine outcomes, not individual choice. Characters are shaped by forces outside their control — nature, heredity, social conditions.' },
      { q: 'Which works in this course are Naturalist?', options: ['Doc Hill and Richard Cory', 'The Open Boat and Richard Cory', 'To Build a Fire and The Open Boat', 'Abel Melveny and The Mill'], correct: 2, explanation: 'To Build a Fire (London) and The Open Boat (Crane) are the two Naturalist works in this course. Both show nature as an indifferent force that determines human fate.' },
      { q: 'What is Determinism as it applies to Naturalism?', options: ['The belief that God controls all outcomes', 'The idea that individual effort determines success', 'The belief that outcomes are fixed by environmental and biological conditions — not by human choice', 'The idea that nature has a plan for each person'], correct: 2, explanation: 'Determinism says the outcome was determined before the story began. The cold was too extreme, the sea too powerful — no choice the characters made could have changed the result.' },
      { q: 'In Naturalist literature, nature\'s attitude toward humans is best described as:', options: ['Nurturing and protective', 'Actively hostile and punishing', 'Indifferent — nature does not care whether humans survive or die', 'Neutral but predictable'], correct: 2, explanation: 'Nature in Naturalism is not cruel — it simply does not care. It has no interest in human survival or suffering. This indifference is the central horror of Naturalism.' },
      { q: 'Why does the dog survive while the man dies in "To Build a Fire"? What does this prove about Naturalism?', options: ['Dogs are physically better suited to cold', 'London wanted to show animals are superior to humans', 'The dog follows instinct (Naturalist truth) while the man relies on intellect — nature rewards instinct over reasoning', 'It was random chance'], correct: 2, explanation: 'The dog follows instinct — it knows the cold is dangerous without reasoning about it. The man trusts his intellect and overrides the body\'s signals. Naturalism: instinct is aligned with natural law; intellectual confidence is not.' },
      { q: 'Billie the oiler\'s death in "The Open Boat" proves which Naturalist idea?', options: ['Hard work always leads to survival', 'The strongest always perish first in nature', 'Nature is indifferent — it does not reward strength, effort, or moral worth', 'The sea is a symbol of human ambition'], correct: 2, explanation: 'Billie is strongest and most capable — he dies. Nature does not award survival based on merit. This random, unjust outcome is exactly what Naturalist indifference looks like.' },
      { q: 'What is the key difference between Naturalism and Realism?', options: ['Naturalism is set in nature; Realism is set in cities', 'Naturalism adds determinism — the idea that environmental forces control outcomes; Realism simply depicts life accurately without that deterministic framework', 'Realism is earlier than Naturalism', 'There is no significant difference'], correct: 1, explanation: 'Both schools depict life honestly — but Naturalism adds the idea that forces beyond human control determine outcomes. Realism shows life accurately; Naturalism adds determinism and environmental power.' },
      { q: 'A Naturalist critic is told: "The man in To Build a Fire died because of bad decisions." The critic most likely responds:', options: ['"He should have listened to the old-timer"', '"His death was inevitable — the environmental conditions determined the outcome regardless of any decisions he made"', '"He lacked wilderness survival training"', '"He should have turned back sooner"'], correct: 1, explanation: 'Naturalism: environment determines outcome. The cold was too extreme before he started. No decision could have changed the result. His choices were irrelevant to the deterministic forces at work.' }
    ]
  },
  impressionism: {
    title: 'Impressionism', emoji: '🎨', type: 'school',
    questions: [
      { q: 'What is the core focus of Literary Impressionism?', options: ['Depicting the harsh biological and environmental forces controlling humans', 'Showing life as it honestly is, without romanticizing', 'Capturing reality as filtered through a character\'s subjective perception, emotion, and moment-to-moment experience', 'Rejecting traditional verse forms and embracing irony'], correct: 2, explanation: 'Impressionism filters reality through what characters can perceive and feel in the moment, not through objective facts. Experience is subjective and shifting.' },
      { q: 'Which work in this course uses Impressionist technique?', options: ['To Build a Fire', 'The Open Boat', 'Richard Cory', 'The Mill'], correct: 1, explanation: 'The Open Boat uses Impressionism — the story is told through the crew\'s shifting perceptions and emotional states, not through objective narration. "None of them knew the colour of the sky."' },
      { q: '"None of them knew the colour of the sky." This opening line is Impressionist because:', options: ['It shows the men are confused after the shipwreck', 'It sets up symbolism about blindness', 'It places the reader inside the men\'s limited, subjective viewpoint — they can only perceive what their immediate survival allows them to notice', 'It is an example of foreshadowing'], correct: 2, explanation: 'Crane opens with what the men cannot see — too focused on surviving to look up. This limited, subjective perception is Impressionism in its purest form.' },
      { q: 'Literary Impressionism is most similar to which concept in visual art?', options: ['Painting every detail with photographic accuracy', 'Using geometric shapes to represent reality abstractly', 'Capturing the fleeting impression, mood, and light of a moment rather than objective visual reality', 'Depicting the harsh facts of working-class life'], correct: 2, explanation: 'Literary Impressionism takes its name from the Impressionist painting movement (Monet, Renoir). Both prioritize capturing the fleeting, subjective experience of a moment over accurate objective representation.' },
      { q: 'The correspondent feels strange calm and humor at moments in "The Open Boat" despite mortal danger. This is Impressionist because:', options: ['Naturalism explains human adaptation to threats', 'Impressionism tracks shifting, illogical inner emotional states — they do not follow rational patterns', 'Realism depicts practical behavior under pressure', 'Determinism means the correspondent accepts his fate'], correct: 1, explanation: 'Impressionism tracks shifting, illogical emotional states. The calm and humor in the face of death makes no rational sense — and that is exactly the point. Inner states in Impressionism don\'t follow logic.' },
      { q: 'Crane fictionalized his real 1896 shipwreck instead of writing journalism. His purpose was to:', options: ['Protect himself legally by claiming it was fiction', 'Use Impressionist technique to capture the subjective emotional truth of the experience, not just the factual record', 'Change the events so much it could no longer be called journalism', 'Publish the story in a literary magazine that only accepted fiction'], correct: 1, explanation: 'Crane could have written journalism. He chose fiction to use Impressionist technique — capturing how the experience felt subjectively from inside the boat, not just what objectively occurred.' },
      { q: 'What does Impressionism prioritize over objective facts?', options: ['The environmental forces shaping the character', 'The character\'s subjective, felt, emotional experience of the moment', 'Accurate historical and social context', 'Universal moral truths'], correct: 1, explanation: 'Impressionism\'s central principle: reality is what a character perceives and feels in the moment — not objective, external facts. The "impression" of an experience matters more than its accurate record.' }
    ]
  },
  realism: {
    title: 'Realism', emoji: '🏘️', type: 'school',
    questions: [
      { q: 'What is the core principle of Realism?', options: ['Environment and biology determine human outcomes', 'Capture the subjective emotional experience of a moment', 'Depict life as it actually is — ordinary people, real situations, without romanticizing or idealizing', 'Reject traditional verse forms and express modern fragmentation'], correct: 2, explanation: 'Realism: show life honestly. Ordinary people in recognizable situations, without heroizing, sentimentalizing, or idealizing. It is the literary equivalent of a documentary lens.' },
      { q: 'Which works in this course are Realist?', options: ['To Build a Fire and The Open Boat', 'Doc Hill, Abel Melveny, Richard Cory, The Mill (Spoon River Anthology)', 'To Build a Fire and The Mill', 'The Open Boat and Doc Hill'], correct: 1, explanation: 'The Spoon River poems (Doc Hill, Abel Melveny) and Robinson\'s poems (Richard Cory, The Mill) all depict ordinary small-town American life honestly — without romanticizing. That is Realism.' },
      { q: 'Doc Hill treated the poor for free. In the context of Realism, this is significant because:', options: ['It makes Doc Hill appear saintly and heroic', 'It shows class inequality and economic hardship in ordinary American life without romanticizing or heroizing it', 'It proves doctors in this period were underpaid', 'It illustrates the theme of divine reward for good deeds'], correct: 1, explanation: 'Realism shows life as it is without sentimentalizing. Doc Hill\'s quiet service is an honest depiction of class, poverty, and economic hardship in small-town America — no heroic framing.' },
      { q: 'Realism differs from Romanticism primarily because:', options: ['Realism is set in more recent time periods', 'Realism depicts ordinary life honestly without idealization; Romanticism sentimentalizes, idealizes, and heightens emotional experience', 'Realism is politically conservative; Romanticism is radical', 'Realism uses plain language; Romanticism uses elevated diction'], correct: 1, explanation: 'The core difference: Romantics idealize, sentimentalize, and heighten experience. Realists show things as they actually are — the ordinary, the unglamorous, the class realities.' },
      { q: 'Spoon River Anthology is Realist because:', options: ['It features dead speakers who lived extraordinary lives', 'It depicts ordinary small-town American life honestly — failures, regrets, quiet services, class realities — without romanticizing', 'It uses free verse which is a Realist technique', 'It takes place in a small town, which is a Realist setting'], correct: 1, explanation: 'Spoon River depicts ordinary lives — a doctor who served the poor, a man who collected unused machines, a mill owner. These are real, unheroic lives shown honestly. That is Realism.' },
      { q: 'Which two authors are most associated with Realism in this course?', options: ['Jack London and Stephen Crane', 'Edgar Lee Masters and Edwin Arlington Robinson', 'Mark Twain and Jack London', 'Stephen Crane and Edwin Arlington Robinson'], correct: 1, explanation: 'Edgar Lee Masters (Spoon River Anthology) and Edwin Arlington Robinson (Richard Cory, The Mill) both depict ordinary American small-town life with Realist honesty.' },
      { q: 'What does Realism reject that Romanticism embraced?', options: ['Narrative structure and plot', 'Strong emotional expression', 'Idealization, sentimentalization, and the heroizing of ordinary experience', 'Natural settings and rural themes'], correct: 2, explanation: 'Realism rejects the Romantic tendency to idealize, sentimentalize, and romanticize experience. Realists insist on showing things — including hardship, class inequality, and failure — as they actually are.' }
    ]
  },
  modernism: {
    title: 'Modernism', emoji: '🔮', type: 'school',
    questions: [
      { q: 'Which features most define Modernism as a literary school?', options: ['Survival narratives, determinism, and environmental force', 'Subjective perception and shifting emotional states', 'Free verse, irony, fragmentation, unconventional forms, and exploration of hidden inner lives', 'Depicting local color, dialect, and regional customs'], correct: 2, explanation: 'Modernism: free verse (rejecting traditional meter/rhyme), irony, fragmentation, unconventional forms, disillusionment, and a focus on hidden inner lives beneath social surfaces.' },
      { q: 'Which works in this course are Modernist?', options: ['To Build a Fire and The Open Boat', 'Doc Hill, Abel Melveny, Richard Cory, The Mill (Spoon River Anthology + Robinson)', 'To Build a Fire and Richard Cory', 'The Open Boat and The Mill'], correct: 1, explanation: 'The Spoon River poems and Robinson\'s poems are Modernist: free verse (Masters), irony, unconventional dead-speaker form, disillusionment, and the gap between surface and hidden reality.' },
      { q: 'Modernist poets like Edgar Lee Masters reject traditional rhyme and meter in favor of free verse. What does this formal choice communicate?', options: ['That they are unskilled or lazy', 'That they believe traditional forms are artificial structures that cannot honestly represent the fragmentation and complexity of modern experience', 'That they are following a French poetic tradition', 'That they prefer the sound of free verse'], correct: 1, explanation: 'Free verse rejects imposed poetic order. Modernists believed rhyme and meter were artificial structures that could not honestly represent the fragmentation and complexity of modern experience.' },
      { q: 'Robinson\'s poems ("Richard Cory," "The Mill") are Modernist because:', options: ['They are set in modern cities', 'They use scientific language to describe nature', 'They explore hidden inner lives, disillusionment, and the gap between surface reality and inner truth — all Modernist concerns', 'They depict the struggle between humans and nature'], correct: 2, explanation: 'Robinson\'s Modernism: irony (Cory appears perfect, is suicidal), disillusionment (the mill\'s obsolescence), and the gap between what others see (Cory\'s surface) and inner reality (his despair).' },
      { q: 'The dead-speaker dramatic monologue used throughout Spoon River Anthology is a Modernist technique because:', options: ['Only Modernists write about death', 'It is a conventional poetic form going back to ancient Greece', 'It breaks conventional poetic form — no living narrator, no traditional structure — to give unfiltered, ironic voice to ordinary lives', 'It creates emotional distance from the subject matter'], correct: 2, explanation: 'The dead speaker is a radical, unconventional form. It deconstructs the traditional poetic voice, giving ironic, unvarnished self-assessment to ordinary people — a Modernist move.' },
      { q: 'Modernism most directly rejects which earlier literary tradition?', options: ['Realism\'s focus on ordinary life', 'Romanticism\'s idealization, traditional verse forms, and Victorian optimism about human progress', 'Naturalism\'s focus on environmental forces', 'Regionalism\'s local color detail'], correct: 1, explanation: 'Modernism reacts against Romanticism and Victorian optimism. Modernists reject idealization, traditional verse forms, and the belief in human progress — replacing them with irony, fragmentation, and disillusionment.' },
      { q: 'Understatement in "Richard Cory" and "The Mill" is a Modernist technique because:', options: ['Modernism always avoids emotional language', 'Modernist irony and restraint convey deeper truth than melodrama — the gap between flat language and devastating content creates the impact', 'Modernist poets were trained to avoid adjectives', 'Understatement makes poems easier to understand'], correct: 1, explanation: 'Modernist understatement: the gap between the flatness of the language and the horror of the content is where the impact lives. More devastating than melodrama — the restraint forces the reader to feel it.' }
    ]
  },
  regionalism: {
    title: 'Regionalism', emoji: '🗺️', type: 'school',
    questions: [
      { q: 'What is the core focus of Regionalism as a literary school?', options: ['Determinism and environmental force', 'Subjective emotional experience of place', 'A specific geographic region — its dialect, local color, customs, and community spirit', 'The inner psychological lives of characters in a specific location'], correct: 2, explanation: 'Regionalism centers on a specific American place — its unique dialect, local customs, folk culture, and geographic character. The region itself becomes as important as the characters.' },
      { q: 'Which author is most associated with American Regionalism in this course?', options: ['Jack London', 'Stephen Crane', 'Mark Twain', 'Edwin Arlington Robinson'], correct: 2, explanation: 'Mark Twain is the canonical American Regionalist — his Mississippi River setting, Southern dialect, and folk culture are textbook Regionalism. Know this for MCQ matching.' },
      { q: 'For exam purposes, the most important thing to know about Regionalism is:', options: ['Its complex relationship with Naturalism and Determinism', 'MCQ matching: "Which school focuses on local color, dialect, and a specific American region?" → Regionalism', 'Its connection to Impressionist technique', 'How it relates to the Second Industrial Revolution'], correct: 1, explanation: 'Regionalism has the smallest footprint in this course. Know it for MCQ identification: which school focuses on local color and dialect of a specific American region? Answer: Regionalism.' },
      { q: 'What distinguishes Regionalism from Realism?', options: ['Regionalism is earlier than Realism', 'Regionalism focuses on a specific geographic place with its unique dialect and local color; Realism is broader — honest depiction of any ordinary American life', 'Realism is more politically engaged', 'There is no meaningful distinction between them'], correct: 1, explanation: 'Realism is broader: honest depiction of ordinary life anywhere. Regionalism narrows to a specific place with its local dialect, customs, and community character. Setting becomes central in Regionalism.' },
      { q: '"Local color" writing — capturing the speech patterns, customs, and feel of a specific American place — is characteristic of:', options: ['Naturalism', 'Impressionism', 'Modernism', 'Regionalism'], correct: 3, explanation: '"Local color" is the defining phrase for Regionalism. It refers to capturing the dialect, customs, folk culture, and geographic character of a specific American region.' },
      { q: 'If an exam question asks: "Which literary school captures the spirit, dialect, and customs of a specific American region?" — the answer is:', options: ['Realism', 'Naturalism', 'Impressionism', 'Regionalism'], correct: 3, explanation: 'Regionalism. This is the core MCQ-ready definition. Dialect + local customs + specific geographic region = Regionalism. Mark Twain is the associated author.' }
    ]
  }
};

/* ── TOPIC QUIZ ENGINE ───────────────────────────────────── */
let topicState = { id: null, questions: [], current: 0, score: 0, streak: 0, answered: false };

function initMcqHub() {
  const workIds = ['tbf', 'tob', 'dochill', 'abel', 'cory', 'mill'];
  const schoolIds = ['naturalism', 'impressionism', 'realism', 'modernism', 'regionalism'];
  const workGrid = document.getElementById('mcq-work-cards');
  const schoolGrid = document.getElementById('mcq-school-cards');
  if (!workGrid || !schoolGrid) return;
  workGrid.innerHTML = '';
  schoolGrid.innerHTML = '';
  workIds.forEach(id => workGrid.appendChild(makeTopicCard(id)));
  schoolIds.forEach(id => schoolGrid.appendChild(makeTopicCard(id)));
}

function makeTopicCard(id) {
  const t = TOPIC_BANKS[id];
  const bests = progress.topicBests || {};
  const best = bests[id];
  const div = document.createElement('div');
  div.className = 'topic-card' + (best >= 80 ? ' quiz-done' : '');
  div.onclick = () => startTopicQuiz(id);
  div.innerHTML = `<div class="topic-card-emoji">${t.emoji}</div>` +
    `<div class="topic-card-title">${t.title}</div>` +
    `<div class="topic-card-meta">${t.questions.length} questions</div>` +
    (best != null ? `<div class="topic-card-best">Best: ${best}%</div>` : '');
  return div;
}

function startTopicQuiz(id) {
  const t = TOPIC_BANKS[id];
  const qs = shuffle(t.questions).map(q => {
    const opts = [...q.options];
    const correctText = opts[q.correct];
    const shuffled = shuffle(opts);
    return { ...q, options: shuffled, correct: shuffled.indexOf(correctText) };
  });
  topicState = { id, questions: qs, current: 0, score: 0, streak: 0, answered: false };
  document.getElementById('mcq-hub').style.display = 'none';
  document.getElementById('mcq-topic-quiz').style.display = 'block';
  document.getElementById('tq-end').style.display = 'none';
  document.getElementById('tq-quiz').style.display = 'block';
  document.getElementById('mcq-topic-title').textContent = t.emoji + ' ' + t.title;
  renderTopicQuestion();
}

function renderTopicQuestion() {
  const { questions, current } = topicState;
  const q = questions[current];
  const total = questions.length;
  document.getElementById('tq-progress-bar').style.width = `${(current / total) * 100}%`;
  document.getElementById('tq-qnum').textContent = `Q${current + 1} / ${total}`;
  document.getElementById('tq-question').textContent = q.q;
  document.getElementById('tq-options').innerHTML = q.options.map((opt, i) =>
    `<button class="mcq-opt" onclick="answerTopicQ(${i})">${opt}</button>`
  ).join('');
  const fb = document.getElementById('tq-feedback');
  fb.style.display = 'none'; fb.className = 'mcq-feedback'; fb.innerHTML = '';
  document.getElementById('tq-next-row').style.display = 'none';
  topicState.answered = false;
}

function answerTopicQ(chosen) {
  if (topicState.answered) return;
  topicState.answered = true;
  const q = topicState.questions[topicState.current];
  const correct = q.correct;
  const isCorrect = chosen === correct;
  document.querySelectorAll('#tq-options .mcq-opt').forEach((btn, i) => {
    btn.disabled = true;
    if (i === correct) btn.classList.add('correct');
    else if (i === chosen && !isCorrect) btn.classList.add('wrong');
  });
  const fb = document.getElementById('tq-feedback');
  fb.style.display = 'block';
  if (isCorrect) {
    topicState.score++;
    topicState.streak++;
    fb.className = 'mcq-feedback correct-fb';
    const streakMsg = topicState.streak >= 3 ? `🔥 ${topicState.streak} in a row! Correct.` : '✓ Correct!';
    fb.innerHTML = `<strong>${streakMsg}</strong>`;
    if (topicState.streak >= 3) {
      confetti({ particleCount: 120, spread: 100, origin: { y: 0.55 }, colors: ['#c8e84a','#2d5a27','#7bc043','#f2e8cf','#bc4749'] });
    } else {
      confetti({ particleCount: 60, spread: 70, origin: { y: 0.6 }, colors: ['#c8e84a','#2d5a27','#7bc043','#f2e8cf','#bc4749'] });
    }
    if (q.explanation) fb.insertAdjacentHTML('beforeend', `<div class="mcq-explanation">💡 ${q.explanation}</div>`);
  } else {
    topicState.streak = 0;
    fb.className = 'mcq-feedback wrong-fb';
    fb.innerHTML = `<strong>✗ Incorrect. Correct answer: ${q.options[correct]}</strong>`;
    if (q.explanation) fb.insertAdjacentHTML('beforeend', `<div class="mcq-explanation">💡 ${q.explanation}</div>`);
  }
  document.getElementById('tq-next-row').style.display = 'flex';
}

function nextTopicQ() {
  topicState.current++;
  if (topicState.current >= topicState.questions.length) {
    endTopicQuiz();
  } else {
    renderTopicQuestion();
  }
}

function endTopicQuiz() {
  const total = topicState.questions.length;
  const score = topicState.score;
  const pct = Math.round((score / total) * 100);
  if (!progress.topicBests) progress.topicBests = {};
  if (progress.topicBests[topicState.id] == null || pct > progress.topicBests[topicState.id]) {
    progress.topicBests[topicState.id] = pct;
  }
  // update overall mcq tracking for home bar
  if (pct > (progress.mcq.highScore || 0)) { progress.mcq.highScore = pct; }
  progress.mcq.attempts = (progress.mcq.attempts || 0) + 1;
  saveProgress(progress);
  updateUI();
  document.getElementById('tq-quiz').style.display = 'none';
  document.getElementById('tq-end').style.display = 'block';
  const scoreEl = document.getElementById('tq-end-score');
  scoreEl.textContent = `${score} / ${total}`;
  scoreEl.className = 'mcq-end-score ' + (pct >= 90 ? 'green' : pct >= 70 ? 'sage' : 'red');
  document.getElementById('tq-end-sub').textContent = `${pct}% — ${pct >= 90 ? 'Excellent!' : pct >= 70 ? 'Good work.' : 'Keep revising.'}`;
  if (pct === 100) {
    const end = Date.now() + 2500;
    const colors = ['#c8e84a','#2d5a27','#7bc043','#bc4749','#e8956d'];
    (function frame() {
      confetti({ particleCount: 6, angle: 60, spread: 55, origin: { x: 0 }, colors });
      confetti({ particleCount: 6, angle: 120, spread: 55, origin: { x: 1 }, colors });
      if (Date.now() < end) requestAnimationFrame(frame);
    }());
  }
}

function retryTopicQuiz() { startTopicQuiz(topicState.id); }

function backToMcqHub() {
  document.getElementById('mcq-topic-quiz').style.display = 'none';
  document.getElementById('mcq-hub').style.display = 'block';
  initMcqHub();
}

function initMCQStartScreen() { /* legacy stub — replaced by initMcqHub */ }"""

if bank_start != -1 and init_fn_end != -1:
    content = content[:bank_start] + NEW_JS_BLOCK + content[init_fn_end:]
    print('OK: MCQ_BANK + JS replaced')
else:
    print('MISS: Could not find MCQ_BANK or initMCQStartScreen')

# ── 5. UPDATE showSection MCQ block ──────────────────────────────────────────
OLD_SHOW_MCQ = """  if (id === 'mcq') {
    document.getElementById('mcq-start').style.display = 'block';
    document.getElementById('mcq-quiz').style.display = 'none';
    document.getElementById('mcq-end').style.display = 'none';
    initMCQStartScreen();
  }"""

NEW_SHOW_MCQ = """  if (id === 'mcq') {
    document.getElementById('mcq-hub').style.display = 'block';
    document.getElementById('mcq-topic-quiz').style.display = 'none';
    initMcqHub();
  }"""

if OLD_SHOW_MCQ in content:
    content = content.replace(OLD_SHOW_MCQ, NEW_SHOW_MCQ)
    print('OK: showSection MCQ block updated')
else:
    print('MISS: showSection MCQ block not found')

# ── 6. UPDATE DOMContentLoaded init ──────────────────────────────────────────
content = content.replace(
    '  initMCQStartScreen();\n  initQIDStartScreen();',
    '  initMcqHub();\n  initQIDStartScreen();'
)

# Write output
with open(r'C:/Users/Muhanad/Desktop/AS2_Revision/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done — saved index.html')
