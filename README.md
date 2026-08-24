# Tech Leadership Deep Dives - website

The website for the [Tech Leadership Deep Dives](https://www.youtube.com/@TechLeadershipDeepDives)
YouTube series and podcast by Raphael Bauer and Marco Melas.

Every episode gets its own page with the video embedded, a short summary, a long-form deep
dive covering the concepts discussed, the references mentioned, and the full transcript.

## Requirements

- [Hugo](https://gohugo.io/) **extended**, v0.158 or newer (developed against v0.164)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - only when adding a new episode, to fetch the
  transcript
- Python 3 - only for the transcript conversion script

No Node, no theme, no npm. The whole site is plain Hugo templates plus one CSS file and one
small JS file.

## Running it

```sh
hugo server          # http://localhost:1313, live reload
hugo --gc --minify   # production build into public/
```

Before deploying, set the real domain in `hugo.toml`:

```toml
baseURL = "https://your-domain.example/"
```

## Directory layout

```
hugo.toml                       site config, menu, external links
content/
  _index.md                     "why we made this" text shown on the home page
  about/index.md                about page (host bios live here)
  episodes/_index.md            season intro shown above the episode list
  episodes/NN-slug/
    index.md                    episode front matter + deep dive
    transcript.md               cleaned transcript (headless page resource)
layouts/
  index.html                    home page
  episodes/single.html          episode page
  episodes/list.html            season overview
  _default/                     baseof, and fallbacks for other pages
  partials/                     head, header, footer, video-embed, episode-card, schema
assets/
  css/main.css                  the entire stylesheet
  js/video.js                   click-to-load YouTube facade
static/img/episodes/NN-slug.jpg episode thumbnails (served locally, see below)
static/img/hosts/               host photos - add raphael.jpg / marco.jpg here
scripts/vtt2txt.py              YouTube auto-caption VTT -> readable paragraphs
```

Host bios on the about page are marked with `<!-- TODO ... -->` comments - roles, links and
photos still need to be filled in by Raphael and Marco.

## Adding an episode

### 1. Get the transcript

```sh
VIDEO_ID=xxxxxxxxxxx
yt-dlp --write-auto-sub --sub-lang en --sub-format vtt --skip-download \
       -o '%(id)s' -P /tmp/transcripts "https://www.youtube.com/watch?v=$VIDEO_ID"

python3 scripts/vtt2txt.py /tmp/transcripts/$VIDEO_ID.en.vtt
```

`vtt2txt.py` turns YouTube's rolling auto-captions into readable paragraphs. It writes two
files next to the input: `<id>.txt` (plain, what goes on the site) and `<id>.timed.txt`
(with timestamps, handy while writing the summary).

Note: YouTube's caption URLs cannot be fetched directly any more, which is why `yt-dlp` is
required rather than `curl`.

### 2. Save the thumbnail locally

```sh
curl -o static/img/episodes/07-slug.jpg \
     "https://i.ytimg.com/vi/$VIDEO_ID/maxresdefault.jpg"
```

The thumbnail is served from this site so that nothing is requested from YouTube before the
visitor clicks play.

### 3. Create the page bundle

```
content/episodes/07-slug/
  index.md
  transcript.md
```

`transcript.md` is the contents of `<id>.txt` with this front matter on top:

```yaml
---
headless: true
---
```

`index.md` front matter - all fields are used by the layouts:

```yaml
---
title: "Episode title"
season: 1
episode: 7
date: 2027-01-15          # the YouTube publish date
youtube_id: "xxxxxxxxxxx"
duration: "48 min"
apple_url: "https://podcasts.apple.com/us/podcast/.../id1885344238?i=..."
spotify_url: "https://podcasters.spotify.com/pod/show/raphael716/episodes/..."
summary: "One or two sentences. Shown on cards, as the page lede, and as the meta description."
topics: ["a topic", "another topic"]
references:
  - title: "Book or tool name"
    authors: "Author names"      # optional
    url: "https://..."           # optional
    note: "Why it came up"       # optional
---
```

The body follows a fixed shape:

- `## In this episode` - 3-6 bullets
- `## Deep dive` - the long writeup, one `###` per concept, in the order the episode
  covers them
- `## Key takeaways` - a numbered list

References are rendered by the layout from front matter - do not write them into the body.
The transcript section is added automatically when `transcript.md` exists.

**Write the deep dive from the transcript**, not from the YouTube description. The
descriptions are thin for some episodes and the point of these pages is that everything
discussed on air is findable in text.

`apple_url` and `spotify_url` are optional. When present, the listen row on the episode page
deep-links to that episode; when absent it falls back to the show-level links in
`hugo.toml`. To find them for a new episode:

```sh
# Apple episode URLs (trackViewUrl per episode)
curl -s "https://itunes.apple.com/lookup?id=1885344238&entity=podcastEpisode&limit=20" \
  | python3 -m json.tool | grep -E '"trackName"|"trackViewUrl"'

# Spotify episode URLs (the <link> of each item in the podcast feed)
curl -s https://anchor.fm/s/10f086064/podcast/rss | grep -E '<title>|<link>'
```

### 4. Check it

```sh
hugo server
```

Verify the video plays, the previous/next links chain correctly, and the transcript renders
without stray timestamps.

## Listen / subscribe links

`layouts/partials/listen-links.html` renders the platform row and is used in three places:
the episode page, the Season 1 section of the home page, and the episodes list header.
Show-level URLs live in `[params]` in `hugo.toml`:

| Param | What it is |
|---|---|
| `youtube` | the channel (episode pages use the episode's watch URL instead) |
| `applePodcasts` | the show on Apple Podcasts |
| `spotify` | the show on `open.spotify.com` |
| `podcastRss` | the actual podcast feed - not the same as this site's `/index.xml` |

## Design notes

- **Responsive, mobile first.** Two breakpoints (40em, 64em). The episode card grid uses
  `auto-fill` so it reflows without media queries.
- **Light and dark** via `prefers-color-scheme` over CSS custom properties defined once in
  `:root`.
- **No cookies before consent-by-click.** The video is a facade: a locally hosted thumbnail
  plus a play button. Clicking injects a `youtube-nocookie.com` iframe. With JavaScript
  disabled the button is an ordinary link to YouTube.
- **No external assets.** No web fonts, no CDNs, no analytics.

## Deployment

`.github/workflows/hugo.yml` builds the site and publishes it to GitHub Pages on every push
to `main`. One-time setup, in the repository on github.com:

1. **Settings → Pages → Build and deployment → Source: GitHub Actions.**
   Until this is set, the workflow fails on the "Configure Pages" step.
2. Push to `main` (or Actions → *Deploy to GitHub Pages* → *Run workflow*).
3. The finished URL appears on the workflow run and under Settings → Pages.

Without a custom domain the site is served from
`https://<user>.github.io/tech-leadership-deep-dives-website/`. To use your own domain,
enter it under Settings → Pages → Custom domain and add the DNS records GitHub shows you
(`CNAME` to `<user>.github.io` for a subdomain, or the four `A` records for an apex domain).
Tick *Enforce HTTPS* once the certificate is issued.

The `baseURL` in `hugo.toml` is **not** used by the deploy - the workflow passes the real
one from the Pages configuration, so both the `github.io` subpath and a custom domain work
without editing any file. `baseURL` only matters for local builds.

The output is a plain static bundle in `public/`, so any other static host works too; there
you would need to set `baseURL` yourself.

### Keep internal links subpath-safe

Serving from `…github.io/<repo>/` breaks any link that is written root-absolute. Two rules:

- In templates, pass `relURL` a path **without** a leading slash: `{{ "episodes/" | relURL }}`.
  With a leading slash Hugo treats the path as already final and does not add the subpath.
  (`absURL` has the same trap, and drops the subpath entirely.) For the site root use
  `{{ site.Home.RelPermalink }}`.
- In content, link to other pages with `relref` rather than a bare path:
  `[Tech Debt]({{< relref "/episodes/02-tech-debt" >}})`.

To check, build with a subpath and confirm no internal URL is missing the prefix:

```sh
hugo --gc --minify --baseURL "https://example.github.io/some-repo/"
grep -rEho '(href|src)="?/[^"[:space:]>]*' public --include='*.html' \
  | grep -v '/some-repo/' | sort -u        # should print nothing
```
