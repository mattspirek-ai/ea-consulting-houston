#!/usr/bin/env node
/**
 * post_scaffold.mjs — print a ready-to-edit LinkedIn post scaffold.
 *
 * Usage:
 *   node post_scaffold.mjs --pillar <name> [--format <name>] [--sector <name>] [--seed <n>]
 *   node post_scaffold.mjs --list
 *
 * Node >= 18, zero dependencies. Reads post-bank.json (env POST_BANK, or a sibling copy, or ../../docs/linkedin/post-bank.json).
 */

import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
import { existsSync } from 'node:fs';
// Bank resolution: env override -> sibling copy (skill layout) -> repo layout ../../docs/linkedin/
const BANK_PATH = process.env.POST_BANK
  || (existsSync(join(__dirname, 'post-bank.json')) ? join(__dirname, 'post-bank.json') : join(__dirname, '..', '..', 'docs', 'linkedin', 'post-bank.json'));

// ---------- static maps ----------

const PILLARS = {
  delegation_craft: 'Delegation craft — what to hand off first, playbook excerpts, failure modes',
  houston_executive_life: 'Houston executive life — energy/TMC/legal/PE week-in-the-life, local logistics',
  radical_transparency: 'Radical transparency — pricing math, contract terms, why we publish',
  industry_dirty_laundry: "The industry's dirty laundry — sourced fine print; competitors named only with sourced facts",
  behind_the_bench: 'Behind the bench — vetting, EA craft, tools, confidentiality, coverage',
  founders_build_log: "Founder's build log — building in public; honest numbers only when real"
};

const HOOKS = {
  delegation_craft: [
    'Delegate your calendar before your inbox.',
    'The only-you list is smaller than you fear.',
    'Track one week. Sort it into three lists.',
    "Approvals queue at your name? You're the bottleneck.",
    'Delegation is a system, not a personality trait.',
    "Your EA's first week decides the next year.",
    'Board prep at 9pm is a systems gap.'
  ],
  houston_executive_life: [
    'OTC week is won in February.',
    "A docket doesn't care about your calendar.",
    'Hurricane season is an executive continuity problem.',
    'Central Time is an underrated operating advantage.',
    'TMC parking is a calendar problem.',
    'NAPE fills a February calendar in one afternoon.',
    'Schedule around I-10, not through it.'
  ],
  radical_transparency: [
    'Our pricing is on the website. All of it.',
    "Publishing prices costs us deals. We'll take the trade.",
    'Our contract fits in ten plain-English lines.',
    'Expiring hours are a quiet margin trick.',
    'The honest math on a full-time Houston EA.',
    'Six questions to ask any EA service. Including us.',
    'If you hire your EA away from us, we did our job.'
  ],
  industry_dirty_laundry: [
    "The biggest name in EA services won't tell you the price.",
    'Twelve months is a long time to be wrong.',
    'The $10,000 fee nobody mentions on the sales call.',
    'Your unused hours may be their best product.',
    '"Hit or miss" shouldn\'t describe a premium service.',
    'The invoice is not the total cost.',
    "Offshore VAs aren't the problem. The mismatch is."
  ],
  behind_the_bench: [
    'How we vet an EA before you ever meet them.',
    'What "senior" means when we say it.',
    'AI drafts. Your EA decides.',
    'Discretion has a checklist.',
    'The best EAs spend week one mostly listening.',
    'One document decides whether an EA match survives.'
  ],
  founders_build_log: [
    "I'm building Houston's fractional EA firm. In public.",
    'We published pricing before we had a single client.',
    'We set public kill criteria for this firm.',
    'Month-to-month means clients can fire us monthly.',
    'Build log: the real numbers, dated.',
    "The firm we're building was written in complaint threads."
  ]
};

const FORMATS = {
  short_text_insight: {
    label: 'Short text insight',
    when: 'Single sharp idea. The workhorse (~2/week). 120-200 words.',
    template: [
      'HOOK (first line, <=12 words, declarative)',
      'CONTEXT (1-2 lines: why this matters now)',
      'THE INSIGHT (2-4 lines, concrete, no abstractions)',
      'ONE WORKED EXAMPLE or checklist fragment',
      'SOFT CTA / genuine question'
    ]
  },
  story_lesson: {
    label: 'Story then lesson',
    when: 'Failure modes, objection stories, craft. Composite must be labeled in-body.',
    template: [
      'HOOK (the tension in one line)',
      'SCENE (labeled composite or permissioned real story - never unlabeled)',
      'THE TURN (what went wrong / what changed)',
      'LESSON (1-2 lines that survive without the story)',
      'CTA (invite their version of the story)'
    ]
  },
  listicle_checklist: {
    label: 'Listicle / checklist',
    when: 'Sequences and save-worthy lists: handoffs, contract clauses, storm prep. 4-8 items.',
    template: [
      'HOOK (state the payoff)',
      'ITEMS 1-N (one line each + one specific detail; specificity is the product)',
      'WHO THIS IS FOR (one line)',
      'CTA ("save this" / "what did I miss?")'
    ]
  },
  contrarian_take: {
    label: 'Contrarian take with evidence',
    when: 'Dirty laundry, transparency, AI takes. Requires a citation or clearly-flagged reasoning.',
    template: [
      'THE COMMON BELIEF (stated fairly - steelman it)',
      "WHY IT FAILS (the actual problem)",
      'EVIDENCE (sourced: "(source in comments)" + URL in sources array)',
      'OUR POSITION (one clean line)',
      'WHAT TO DO INSTEAD',
      'CTA (invite disagreement genuinely)'
    ]
  },
  document_carousel_outline: {
    label: 'Document carousel (PDF)',
    when: 'Flagship ideas 1-2x/month: pricing math, playbook, fine print. 8-12 slides, <=25 words/slide.',
    template: [
      'POST BODY: 2-3 line setup + why it is worth the swipe',
      'SLIDE 1: title (the promise)',
      'SLIDES 2-N: one idea per slide; sourced facts get on-slide citations',
      'FINAL SLIDE: CTA',
      'FIRST COMMENT: all source links with dates'
    ]
  },
  poll_follow_up: {
    label: 'Poll + follow-up',
    when: 'Max 1-2/month. Only questions we genuinely cannot answer. Follow-up post is mandatory.',
    template: [
      'SETUP (2-3 lines: why we are actually asking)',
      'OPTIONS x4 (no obvious winner - obvious-answer polls are penalized bait)',
      'PROMISE (results + full post on the winner within a week)',
      'CTA (invite the fifth option in comments)',
      'CALENDAR: schedule the follow-up post NOW'
    ]
  },
  week_with_ea_vignette: {
    label: '"A week with your EA" vignette',
    when: 'Sector storytelling with sector vocabulary (AFE, credentialing, docket, LP letters). Label illustrative.',
    template: [
      'HOOK (name the persona)',
      'LABEL ("illustrative - built from what [sector] leaders tell us, not a specific client")',
      'MON-FRI (one beat per day; the sector vocabulary does the persuading)',
      'CLOSER ("none of this needs you / all of it currently has you")',
      'CTA (ask the persona what you left off)'
    ]
  },
  build_log_update: {
    label: 'Founder build-log update',
    when: 'Pillar 6. Real numbers only, dated; [INSERT] placeholders until reality fills them.',
    template: [
      'WHAT HAPPENED (real, or [INSERT: ... - do not invent])',
      'THE DECISION + the actual reasoning',
      'WHAT IT COSTS US / WHAT IT BUYS (both sides, honestly)',
      "WHAT'S NEXT",
      'ASK (input, introductions, or a hard question)'
    ]
  }
};

const CTAS = [
  'Pricing and terms are on the site - no call required.',
  'If this sounds like your week, a fit call is 20 minutes.',
  'The 30-Day Delegation Playbook is free - link in the comments.',
  'Sources in the comments. Compare freely - that is the point.',
  'What would you add? (Genuine question.)',
  'Save this for the week you finally hire support.',
  'Follow the build log - real numbers, dated, corrections included.'
];

const CHECKLIST = [
  '[ ] No invented clients, testimonials, or metrics. Composites labeled "composite" in the body.',
  '[ ] Every competitor claim has a source URL -> goes in the FIRST COMMENT ("source in comments" in body).',
  '[ ] Pricing matches the brief exactly: $1,200/20h, $2,300/40h, $3,300/60h (+ $450 in-person day, $65/hr extra, $79/hr specialist, $299 onboarding waived on Chief of Staff).',
  '[ ] All [INSERT: ...] placeholders filled with real, dated facts - or the post does not ship.',
  '[ ] Banned words absent: hustle, crush, game-changer, rocket emoji, "humbled", rage-bait, fake vulnerability.',
  '[ ] Hook <= 12 words, declarative, no clickbait. Value in the first ~150 characters.',
  '[ ] 0-1 hashtags. Links in first comment (or bare in body without preview card if the link IS the point).',
  '[ ] Reads like the founder wrote it. Edit until it does.',
  '[ ] Post in the 7:30-9:00 AM CT window Tue-Thu when possible; never skip a post over timing.',
  '[ ] Stay 30-60 minutes after posting; reply to every comment within 2 working hours.'
];

// ---------- helpers ----------

function parseArgs(argv) {
  const args = {};
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--list') { args.list = true; continue; }
    if (a.startsWith('--')) {
      const key = a.slice(2).replace(/-/g, '_');
      const next = argv[i + 1];
      if (next !== undefined && !next.startsWith('--')) { args[key] = next; i++; }
      else args[key] = true;
    }
  }
  return args;
}

function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function pick(arr, n, rnd) {
  const copy = [...arr];
  const out = [];
  while (copy.length && out.length < n) {
    out.push(copy.splice(Math.floor(rnd() * copy.length), 1)[0]);
  }
  return out;
}

function loadBank() {
  try {
    return JSON.parse(readFileSync(BANK_PATH, 'utf8'));
  } catch (e) {
    console.error(`Could not read post bank at ${BANK_PATH}: ${e.message}`);
    process.exit(1);
  }
}

function counts(bank, key) {
  const c = {};
  for (const p of bank) c[p[key]] = (c[p[key]] || 0) + 1;
  return c;
}

// ---------- main ----------

const args = parseArgs(process.argv);
const bank = loadBank();

if (args.list) {
  console.log('PILLARS (posts in bank):');
  const pc = counts(bank, 'pillar');
  for (const [k, desc] of Object.entries(PILLARS)) {
    console.log(`  ${k.padEnd(24)} ${String(pc[k] || 0).padStart(2)}  ${desc}`);
  }
  console.log('\nFORMATS (posts in bank):');
  const fc = counts(bank, 'format');
  for (const [k, f] of Object.entries(FORMATS)) {
    console.log(`  ${k.padEnd(26)} ${String(fc[k] || 0).padStart(2)}  ${f.when}`);
  }
  console.log('\nSECTORS (posts in bank):');
  const sc = counts(bank, 'sector');
  for (const [k, v] of Object.entries(sc).sort()) console.log(`  ${k.padEnd(16)} ${v}`);
  const houston = bank.filter(p => p.houston_specific).length;
  console.log(`\nTotal posts: ${bank.length} (Houston-specific: ${houston})`);
  process.exit(0);
}

const pillar = args.pillar;
if (!pillar || !PILLARS[pillar]) {
  console.error('Usage: node post_scaffold.mjs --pillar <name> [--format <name>] [--sector <name>] [--seed <n>]');
  console.error('       node post_scaffold.mjs --list');
  console.error(`\nPillars: ${Object.keys(PILLARS).join(', ')}`);
  process.exit(pillar ? 1 : 0);
}
if (args.format && !FORMATS[args.format]) {
  console.error(`Unknown format "${args.format}". Formats: ${Object.keys(FORMATS).join(', ')}`);
  process.exit(1);
}

const seed = Number.isFinite(Number(args.seed)) ? Number(args.seed) : Date.now() % 100000;
const rnd = mulberry32(seed);

// candidate example post from the bank: pillar (+format) (+sector), relaxing filters if needed
let pool = bank.filter(p => p.pillar === pillar);
if (args.format) {
  const f = pool.filter(p => p.format === args.format);
  if (f.length) pool = f;
}
if (args.sector) {
  const s = pool.filter(p => p.sector === args.sector);
  if (s.length) pool = s;
  else console.log(`(note: no ${pillar} post with sector "${args.sector}" in the bank - showing closest match)\n`);
}
const example = pool[Math.floor(rnd() * pool.length)];
const format = FORMATS[args.format || example.format];

const hr = '='.repeat(72);
console.log(hr);
console.log(`POST SCAFFOLD  ·  pillar: ${pillar}  ·  format: ${args.format || example.format}${args.sector ? `  ·  sector: ${args.sector}` : ''}  ·  seed: ${seed}`);
console.log(hr);
console.log(`\nPillar brief: ${PILLARS[pillar]}`);
console.log(`Format brief: ${format.when}`);

console.log(`\n--- 3 CANDIDATE HOOKS (edit, don't worship) ---`);
for (const h of pick(HOOKS[pillar], 3, rnd)) console.log(`  * ${h}`);

console.log(`\n--- STRUCTURE TEMPLATE (${format.label}) ---`);
format.template.forEach((line, i) => console.log(`  ${i + 1}. ${line}`));

console.log(`\n--- EXAMPLE FROM THE BANK (${example.id}${example.houston_specific ? ', Houston' : ''}, sector: ${example.sector}) ---`);
console.log(example.body.split('\n').map(l => '  | ' + l).join('\n'));
console.log(`  | \n  | CTA: ${example.cta}`);
if (example.sources.length) {
  console.log(`  | First comment (sources): ${example.sources.join(' · ')}`);
}
if (example.placeholders.length) {
  console.log(`  | PLACEHOLDERS in this example (fill before ever publishing):`);
  for (const ph of example.placeholders) console.log(`  |   - ${ph}`);
}

console.log(`\n--- CTA OPTIONS ---`);
for (const c of pick(CTAS, 3, rnd)) console.log(`  * ${c}`);

console.log(`\n--- PRE-PUBLISH CHECKLIST ---`);
for (const c of CHECKLIST) console.log(`  ${c}`);
console.log('');
