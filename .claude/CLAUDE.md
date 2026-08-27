# Tech Leadership Deep Dives - project notes

Hugo site for the YouTube series / podcast by Raphael Bauer and Marco Melas. Read
`README.md` first - it covers running the site and the full "add an episode" procedure.
This file records the conventions and the reasoning behind them.

## Content rules

- **Episode deep dives are written from the transcript**, never from the YouTube
  description. Descriptions run from ~450 to ~2,400 characters and are unusable as a source
  for half the episodes.
- **Never invent content.** If something was not said in the episode, it does not go on the
  page. If a transcript is unavailable, say so rather than filling the gap.
- **Attribution:** the auto-generated transcripts have no reliable speaker labels. Write
  neutrally - "the hosts", "one host argues, the other counters". Do not assign an opinion
  to Raphael or Marco unless the transcript makes it unambiguous.
- **Disagreements are content.** The hosts disagree on air regularly (team lead vs tech
  lead; whether bugs belong in the engineering or product budget). Present both sides -
  those passages are the most useful parts of the episodes.
- **Employer names** mentioned in passing on air are deliberately left off the site. Host
  bios are `<!-- TODO -->` markers in `content/about/index.md` for the hosts to fill in.

## Episode front matter contract

Every episode needs all of: `title`, `season`, `episode`, `date`, `youtube_id`, `duration`,
`summary`, `topics`, `references`. The layouts read all of them. `apple_url` and
`spotify_url` are optional per-episode deep links; without them the listen row falls back to
the show-level params.

- `episode` drives ordering everywhere - `sort (where .Site.RegularPages "Type" "episodes")
  "Params.episode"` - and the previous/next chain. Do not rely on date ordering; Hugo's
  `.Next`/`.Prev` run newest-first and would reverse the meaning of "previous episode".
- `references` render from front matter via `layouts/episodes/single.html`. Do not write a
  references section into the markdown body.
- `summary` is used three times: episode cards, the page lede, and the meta description.
  Keep it to one or two sentences.
- The thumbnail path is derived from the bundle directory name
  (`static/img/episodes/<ContentBaseName>.jpg`), so the directory name and the image
  filename must match.

## Body structure

`## In this episode` → `## Deep dive` (one `###` per concept, in the order the episode
covers it) → `## Key takeaways`. The table of contents is generated from the `##`/`###`
headings, so keep headings descriptive.

Transcripts live as a `transcript.md` page resource in the same bundle with
`headless: true`. The layout picks it up with `.Resources.GetMatch "transcript.md"` and
wraps it in a collapsed `<details>`.

## Styling conventions

- One stylesheet, `assets/css/main.css`, no framework and no build step beyond Hugo's own
  pipes.
- All colours are CSS custom properties on `:root`, redefined once under
  `@media (prefers-color-scheme: dark)`. Never hard-code a colour in a rule.
- Mobile first. Only two breakpoints: `40em` and `64em`. The card grid uses
  `repeat(auto-fill, minmax(280px, 1fr))` so it reflows on its own.
- No web fonts, no CDN, no analytics, no external requests of any kind before the visitor
  clicks play.

The landing-page hero is a two-column grid (`.hero-inner`): copy left, the photo of the two
hosts right, stacking below `64em`. The photo lives at `static/img/hosts/raphael-marco.jpg`
(1600x1000 JPEG, downscaled from the source PNG so the hero stays under ~150 KB) and is
referenced with `relURL "img/hosts/..."` - no leading slash, see the subpath gotcha below.
Its alt text names both hosts without saying who sits where; the transcripts give no
reliable speaker labels and the photo should not be the thing that assigns them.

## Listen links

`layouts/partials/listen-links.html` is the single source for the platform row - called with
`(dict "page" . "label" "..." "class" "...")`. Passing a page makes YouTube, Apple and
Spotify resolve to that *episode*; omitting it falls back to the show-level params. Apple,
Spotify and RSS render conditionally, so adding a platform means adding one param plus one
line in the partial. The show is not on Amazon Music, so there is deliberately no link or
placeholder for it.

Keep the platform links attached to Season 1 (where the episodes actually are), not to the
Season 2 callout - Season 2 does not exist yet, and putting subscribe links there was
confusing.

`podcastRss` is the show's real feed (Anchor/Spotify), which is *not* the same thing as
Hugo's `/index.xml`. The footer links both, labelled distinctly.

## The video facade

`layouts/partials/video-embed.html` + `assets/js/video.js`. The page ships a locally hosted
thumbnail and a link to YouTube; the click handler replaces it with a
`youtube-nocookie.com` iframe. This keeps YouTube from setting anything on page load - the
show is German-hosted and this matters. Without JavaScript the play button degrades to a
plain link. Do not replace this with a bare `<iframe>`.

## Gotchas

- `hugo.toml` uses `locale`, not the deprecated `languageCode`; templates use
  `.Site.Language.Lang`.
- `markup.goldmark.renderer.unsafe = true` is required for the `<div class="hosts">` blocks
  on the about page.
- `sort` must be called as `sort SEQ "Params.x"`, not piped - piping the sequence in fails
  with "can't sort string" on Hugo 0.164.
- Taxonomies are switched off deliberately (`[taxonomies]` left empty). Topics are labels,
  not browsable term pages; enabling them generated 60+ unlinked pages.
- `hugo --gc` does not delete stale output. After changing what gets generated, `rm -rf
  public` before rebuilding.
- **Leading slashes break subpath deploys.** `relURL "/episodes/"` returns `/episodes/`
  unchanged - Hugo reads a leading slash as "already final" and skips the baseURL subpath;
  `absURL "/episodes/"` drops the subpath too. Written without the slash,
  `relURL "episodes/"` resolves correctly. Site root is `site.Home.RelPermalink`. In
  content, cross-link with `relref`, never a bare `/episodes/...` path. Menu URLs and
  `.RelPermalink` are already handled by Hugo.
- The Pages workflow passes `--baseURL` from the Pages config, so `baseURL` in `hugo.toml`
  is a local-development placeholder only. Verify link changes against a subpath build,
  not just the root one - see the check in README's deployment section.
