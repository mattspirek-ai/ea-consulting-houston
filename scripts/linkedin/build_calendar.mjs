#!/usr/bin/env node
/**
 * build_calendar.mjs — generate a posting calendar from the post bank,
 * rotating pillars per the playbook's weekly rhythm (docs/linkedin/playbook.md §8).
 *
 * Usage:
 *   node build_calendar.mjs --start YYYY-MM-DD --weeks N [--posts-per-week 4] [--exclude P001,P002] [--json]
 *
 * Behavior:
 *   - Skips weekends.
 *   - Never repeats a post id within the generated calendar; --exclude removes already-published ids.
 *   - Prints a markdown table (default) or JSON (--json).
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

// Weekly rhythm (playbook §8). getUTCDay(): 1=Mon ... 5=Fri.
// Where a day lists multiple pillars, they alternate by week index.
const DAY_PILLARS = {
  1: ['delegation_craft'],
  2: ['houston_executive_life'],
  3: ['radical_transparency', 'industry_dirty_laundry'],
  4: ['behind_the_bench', 'founders_build_log'],
  5: ['founders_build_log', 'delegation_craft']
};

// Peak days first (Tue-Thu strongest across 2025-2026 B2B studies), then Mon, then Fri.
const DAY_PRIORITY = [2, 3, 4, 1, 5];

const ENGAGEMENT_TASKS = [
  '30 connects + 10 comments; reply <2h',
  '30 connects + 10 comments; focus: this week\'s sector list',
  '30 connects + 10 comments; paste source links as first comment',
  '30 connects + 10 comments; stay 45 min post-publish',
  'Engagement block + WEEKLY REVIEW: fill scorecard, prune target list, pick next week\'s posts'
];

function parseArgs(argv) {
  const args = {};
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (!a.startsWith('--')) continue;
    const key = a.slice(2).replace(/-/g, '_');
    const next = argv[i + 1];
    if (next !== undefined && !next.startsWith('--')) { args[key] = next; i++; }
    else args[key] = true;
  }
  return args;
}

function fail(msg) {
  console.error(msg);
  console.error('\nUsage: node build_calendar.mjs --start YYYY-MM-DD --weeks N [--posts-per-week 4] [--exclude P001,P002] [--json]');
  process.exit(1);
}

const args = parseArgs(process.argv);

if (!args.start || !/^\d{4}-\d{2}-\d{2}$/.test(String(args.start))) fail('Missing or invalid --start (expected YYYY-MM-DD).');
const start = new Date(String(args.start) + 'T00:00:00Z');
if (Number.isNaN(start.getTime())) fail(`Invalid date: ${args.start}`);

const weeks = parseInt(args.weeks, 10);
if (!Number.isInteger(weeks) || weeks < 1 || weeks > 52) fail('Missing or invalid --weeks (1-52).');

const postsPerWeek = args.posts_per_week === undefined ? 4 : parseInt(args.posts_per_week, 10);
if (!Number.isInteger(postsPerWeek) || postsPerWeek < 1 || postsPerWeek > 5) fail('--posts-per-week must be 1-5 (weekends are skipped).');

const excluded = new Set(
  String(args.exclude || '')
    .split(',')
    .map(s => s.trim())
    .filter(Boolean)
);

let bank;
try {
  bank = JSON.parse(readFileSync(BANK_PATH, 'utf8'));
} catch (e) {
  fail(`Could not read post bank at ${BANK_PATH}: ${e.message}`);
}

// Posting days for the chosen volume, sorted chronologically within the week.
const activeDays = DAY_PRIORITY.slice(0, postsPerWeek).sort((a, b) => a - b);

const used = new Set(excluded);

function nextPost(pillar) {
  // First unused bank post for the pillar (bank order = intended order),
  // falling back to any unused post, then to null.
  let p = bank.find(x => x.pillar === pillar && !used.has(x.id));
  if (!p) p = bank.find(x => !used.has(x.id));
  if (!p) return null;
  used.add(p.id);
  return p;
}

const DAY_NAMES = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const rows = [];

// Walk day by day from the Monday of the start week? No — from the start date itself.
const cursor = new Date(start.getTime());
const endExclusive = new Date(start.getTime());
endExclusive.setUTCDate(endExclusive.getUTCDate() + weeks * 7);

let weekIndex = 0;
let lastWeekStamp = null;

while (cursor < endExclusive) {
  const dow = cursor.getUTCDay();
  if (dow >= 1 && dow <= 5) {
    // week index relative to start date (calendar weeks beginning at start)
    const daysFromStart = Math.floor((cursor - start) / 86400000);
    weekIndex = Math.floor(daysFromStart / 7);

    if (activeDays.includes(dow)) {
      const options = DAY_PILLARS[dow];
      const pillar = options[weekIndex % options.length];
      const post = nextPost(pillar);
      rows.push({
        date: cursor.toISOString().slice(0, 10),
        day: DAY_NAMES[dow],
        week: weekIndex + 1,
        pillar: post ? post.pillar : pillar,
        post_id: post ? post.id : null,
        hook: post ? post.hook : '(bank exhausted - write new or repurpose oldest)',
        format: post ? post.format : '-',
        sources_in_comments: post ? post.sources.length > 0 : false,
        has_placeholders: post ? post.placeholders.length > 0 : false,
        engagement: dow === 5 ? ENGAGEMENT_TASKS[4] : ENGAGEMENT_TASKS[(weekIndex + dow) % 4],
        review: false
      });
    } else if (dow === 5) {
      // Friday with no post still carries the weekly review
      rows.push({
        date: cursor.toISOString().slice(0, 10),
        day: 'Fri',
        week: weekIndex + 1,
        pillar: null,
        post_id: null,
        hook: '(no post)',
        format: '-',
        sources_in_comments: false,
        has_placeholders: false,
        engagement: ENGAGEMENT_TASKS[4],
        review: true
      });
    }
  }
  cursor.setUTCDate(cursor.getUTCDate() + 1);
}

// mark Friday rows as review checkpoints
for (const r of rows) if (r.day === 'Fri') r.review = true;

if (args.json) {
  console.log(JSON.stringify({
    start: args.start,
    weeks,
    posts_per_week: postsPerWeek,
    excluded: [...excluded],
    entries: rows
  }, null, 2));
  process.exit(0);
}

// ---------- markdown output ----------
const postCount = rows.filter(r => r.post_id).length;
console.log(`# LinkedIn Calendar — ${args.start} for ${weeks} week(s), ${postsPerWeek} posts/week (${postCount} posts)\n`);
if (excluded.size) console.log(`Excluded ids: ${[...excluded].join(', ')}\n`);
console.log('| Date | Day | Wk | Pillar | Post | Format | Hook | Notes | Engagement |');
console.log('|---|---|---|---|---|---|---|---|---|');
for (const r of rows) {
  const notes = [];
  if (r.sources_in_comments) notes.push('sources -> 1st comment');
  if (r.has_placeholders) notes.push('FILL PLACEHOLDERS first');
  if (r.review) notes.push('weekly review');
  console.log(`| ${r.date} | ${r.day} | ${r.week} | ${r.pillar || '-'} | ${r.post_id || '-'} | ${r.format} | ${r.hook.replace(/\|/g, '/')} | ${notes.join('; ') || '-'} | ${r.engagement} |`);
}
console.log('\nRules: weekends skipped; no post id repeats; posts with [INSERT] placeholders publish only when real content exists (swap otherwise).');
console.log('Time slot: 7:30-9:00 AM CT (weak-evidence lever - consistency beats timing; playbook section 8).');
