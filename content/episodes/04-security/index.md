---
title: "Security"
season: 1
episode: 4
date: 2026-05-17
youtube_id: "mg6fRBnwVBE"
duration: "42 min"
apple_url: "https://podcasts.apple.com/us/podcast/security/id1885344238?i=1000768181505"
spotify_url: "https://podcasters.spotify.com/pod/show/raphael716/episodes/Security-e3jdl4o"
summary: "Security only becomes visible to the business when it fails. How to get budget before that happens - by putting a price on a CVE - and how to build security into engineering rather than bolting it on afterwards."
topics:
  - "application vs information security"
  - "shift left"
  - "supply chain attacks"
  - "CVEs and scanning tools"
  - "pricing security risk"
  - "asset inventory and tiering"
  - "security champions"
  - "OWASP Top 10"
  - "penetration testing"
  - "ISO 27001 / SOC 2"
  - "AI and attack automation"
references:
  - title: "OWASP Top 10"
    url: "https://owasp.org/Top10/"
    note: "The prime ways software gets compromised - and a ready-made training curriculum."
  - title: "CVE - Common Vulnerabilities and Exposures"
    url: "https://www.cve.org/"
  - title: "Snyk"
    url: "https://snyk.io/product/open-source-security-management/"
  - title: "GitHub Dependabot"
    url: "https://docs.github.com/en/code-security/concepts/supply-chain-security/about-supply-chain-security"
  - title: "Burp Suite"
    url: "https://portswigger.net/burp"
  - title: "ISO/IEC 27001"
    url: "https://www.iso.org/standard/27001"
  - title: "SOC 2"
    url: "https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2"
---

## In this episode

- Why "we have no security incidents" tells you nothing about whether you are secure.
- Information security vs application security - and why the USB stick in the car park is
  still one of the most effective attacks going.
- Supply chain attacks, and the uncomfortable normalisation of `curl | bash`.
- The single most useful trick in the episode: **put a euro figure on a CVE** and watch the
  budget conversation change.
- Asset inventory and a two-question tiering system that most companies cannot answer.
- Security champions and chapters as a lightweight alternative to hiring a CISO.
- Pen testing rules of thumb, certifications, and what AI does to both sides of the fight.

## Deep dive

### Two scopes, and where the leverage is

The episode separates two things that often get conflated:

**Information security** is company-wide. Who gets into the building, what happens to
laptops, whether there is a physical key or just a username and password - and what an
employee does with an email from a suddenly deceased rich uncle in Nigeria. It applies to
everyone.

**Application security** is the subset engineering owns, and where the episode spends most
of its time.

The point about relative danger is worth sitting with. The most effective attacks are often
not sophisticated malware but someone finding a **USB stick in a car park** and plugging it
into their work machine to see what is on it - the machine they would never risk at home.
And we have all been trained to click *accept* on everything: cookies, device access,
permissions. Malicious hardware can be hidden inside what looks and works exactly like a
normal USB cable. Attacks like these are found in car parks next to Google, next to Apple,
possibly next to your company.

### Security is instilled, not bolted on

The core stance: **security is not something you attach to a finished system.** It has to be
in the mindset of every individual - *is what I am about to do a safe action? Am I putting
myself or others at risk?*

For engineering, that becomes **shift left**: integrating security considerations early in
design and embedding them across the whole lifecycle - a *secure* software development
lifecycle. The starting mindset is deliberately uncomfortable: however much we would like
the world to be a benign place, there are threat actors with malicious intent trying to
exploit what you build and what you use.

The mechanism is simple and mandatory: **an annual security training for every engineer**,
repeated every year, asking simple but important questions - because the point is awareness,
and because the threats keep evolving. Information security training covers the whole
company; application security training zooms into engineering.

The anti-pattern named explicitly: engineering builds it, throws it over the fence to QA,
who throw it to the security people, who laugh and send it back to be rewritten because of a
cross-site scripting hole. Nobody wants that loop.

### Supply chain attacks

The modern software ecosystem is Lego: we assemble libraries rather than rewrite what
already exists. That makes us fast, and it is genuinely a good thing - but it means trusting
code we did not write and pull continuously, across Go, Java, Python and above all
JavaScript.

The attack pattern, which has been in the news repeatedly: a malicious actor replaces a
library thousands of companies pull daily. If you are lucky, it mines Bitcoin - slower
builds, embarrassing, survivable. If you are not, it reads your environment variables and
your secrets and ships them to a server somewhere far away. And developers do have secrets
lying around - AWS credentials in a home directory are a prime target.

There is a sharp aside about how norms have shifted. The old rule was *never execute
something you downloaded from the internet.* The current norm is `curl … | bash` - executing
a script from a remote server with full access to your laptop, sight unseen. One changed
line in that script is all it takes. Most tooling installs this way now, and the hosts think
it deserves more discomfort than it gets.

**Defences.** The public **CVE** database tracks known vulnerabilities; serious maintainers
publish a fixed version quickly. The gap is knowing that *your* installed version is now the
vulnerable one. Tools like **Snyk** and **GitHub Dependabot** close it: they scan your
dependencies, match versions against known CVEs, tell you what to upgrade, and can open the
pull request for you. Fully automated if your test suite is good enough that you trust it to
block a broken release overnight.

The realistic caveat: **this costs money twice.** The tools cost money at scale, and fixing
the findings costs engineering time - it is often not a one-click merge but changed APIs to
adapt to and a round of testing to prove it still works.

### Putting a price on a CVE

Which leads to the conversation every CTO recognises. Your roadmap has "upgrade X and Y" on
it, and your CEO or product counterpart asks why, since it has no business value and there
are no breaches right now.

The technique - credited to a colleague, Robin, who founded a security company in London -
is to **price the impact.** For a given CVE in a given library: if this is exploited, this
is the amount of damage. Now it has a number, and the argument becomes concrete: this damage
is *invisible in our P&L, but it is there.*

How the numbers are derived, since a board will ask: from real breaches. Past incidents show
what a breach did to company valuation, stock price and lost revenue. Take incidents of
comparable type at companies of comparable size, average and adjust, and you get a defensible
estimate. It is an approximation - not a figure to quote as exact - but it is anchored in
observed outcomes: *a company of our size with a vulnerability allowing remote access under
these conditions lost this much. I recommend not carrying that in our invisible P&L.*

A related observation about who your allies are: **private equity owners care intensely
about this.** They intend to sell the company in a few years, and a breach that craters
valuation is directly against their interest - which makes PE-backed boards notably
supportive of building a strong security posture. Framed this way, the board is usually on
the CTO's side. And that is how the tooling budget gets approved.

### Know what you have

The recurring line: **a fool with a tool is still a fool.** Before buying anything, do the
unglamorous work.

**Step one: an asset inventory.** What are the artifacts actually running in production?
This is where many organisations already fail - engineers are building and shipping, and
when you ask what is really out there you get crickets, or half the picture.

**Step two: tier it.** The system can be as simple as two questions:

1. Does it contain personally identifiable information?
2. Is it exposed to the internet?

Two yeses puts it in **tier one** - if a vulnerability shows up there, fix it first. Two
noes puts it in the lowest tier. Four quadrants, no ceremony, immediately actionable.

The list is also a management tool. Write the unmaintained services on the wall, tier them,
and turn it into a visible target: *this quarter we fix 30% of the unmaintained services.*
Then take the same chart to the board - month one 0%, month three 100% of services
maintained with no known security risks. Visible progress on something that is otherwise
invisible by nature.

### Who owns security?

The accountability answer is unambiguous: **security is built in by engineering leadership,
the same way testability, quality and reliability are.** It sits with the CTO or SVP
Engineering.

But you need expertise. One host has never worked with a CISO but has worked with security
experts reporting either to them or directly to the CTO, whose job was to define what the
company wants, write down policies the organisation can be held to, and **support and train
the teams** rather than inspect their output at the end.

The size-dependent shape:

- **Hundreds of thousands of employees:** you will have a CISO.
- **Ten engineers:** you do not need one.
- **Around a hundred engineers:** the pattern they both recommend is a **security chapter**.

The chapter model works like this. Every stream-aligned team has a **security champion** -
usually not a hire but a regular engineer who is genuinely interested: knows OWASP, likes
poking at things, understands how to exploit an HTTP request from frontend to backend. The
champions meet regularly - say an hour a week - with an agenda: recent news, last week's
JavaScript supply chain attack, whether it affects any of our teams. Someone leads that
chapter: a security expert, the CTO in a smaller company, the most experienced champion, or
a VP-level security role covering the whole posture rather than just application security.

The reason it works is that it is an **influence structure rather than an authority
structure** - a soft, effective way to spread security awareness into every team without a
compliance department.

### OWASP, tools, and testing yourself

**OWASP Top 10** is the standing list of the prime ways software gets compromised, updated
regularly, with variants for different domains. Cross-site scripting and SQL injection are
still on it. As a training curriculum it is close to free lunch: widely known, off-the-shelf
courses exist, inexpensive, and it moves the whole organisation. As a checklist it is a
solid starting point for hardening.

**Red and blue teams.** Blue defends, red attacks. When you start hiring for security, hire
blue. Large companies also run their own red teams, tasked with breaching defined areas so
the gaps get fixed before someone else finds them. **Burp Suite** gets a mention as a tool in
this space.

**Penetration testing** is red teaming you buy. Two rules of thumb offered:

1. **Once a year.**
2. **Do not use the same testers repeatedly.** A firm that tests you annually settles into
   its own routine. Rotating firms - or, as one host does in practice, keeping the firm but
   rotating the individual testers - buys you new perspectives, new attack vectors, new
   findings.

**Certifications** - ISO 27001, SOC 2 - are recommended without hesitation. Some customers
require them outright (enterprise buyers, anything touching defence). Beyond that, they tell
you what to implement and document, and annual recertification guarantees a minimum posture
is maintained. They are visible at board level and feed into company valuation. And,
speaking from having done it: it sounds like an enormous amount of work and it is not,
particularly with an agency to get the first certification off the ground. The business
outcome is tangible.

### AI, on both sides

AI cuts both ways, and the hosts think the attackers get the early advantage.

**Offence.** Agents can search for CVEs and attempt to exploit production systems
automatically. Anyone can do this - which means bad actors can too, at scale. The hypothesis
stated plainly: **the number of security incidents will go up**, because it is now cheap to
field an army of capable attackers. Script kiddies existed before; this is considerably more
capable.

**Defence.** The same capability reviews your own code. AI reviewing pull requests for
security issues is already in use - a friend of one host runs exactly this. The honest
caveat: **many of the alerts are false positives**, but among them are genuinely good
findings with real security impact. Worth using, with eyes open.

And back to where they started: the tools help, but you have to understand why you are using
them and how. A fool with a tool is still a fool.

The closing joke lands on something real. If libraries are the attack surface, why not write
everything yourself with AI? Because you inherit every security flaw in the code the model
learned from - and all the maintenance burden the library maintainers were carrying for you.
Fewer libraries does not mean fewer problems. It means different problems.

## Key takeaways

1. **Price the risk.** Attaching a monetary damage estimate to a CVE is what converts a
   security backlog item into an approved budget line.
2. **Know what you have before you buy anything.** Asset inventory first, then tier it: PII?
   internet-exposed? Fix tier one first.
3. **Shift left and make it a mindset**, not a gate at the end. Annual mandatory training,
   OWASP Top 10 as the curriculum.
4. **Use security champions and a chapter** to spread ownership into every team - you
   probably do not need a CISO at 100 engineers.
5. **Pen test yearly, and rotate who does it**, so you keep getting new attack angles.
6. **Get certified** (ISO 27001, SOC 2) - it is less work than it sounds and the business
   value is concrete.
7. **Fewer dependencies, upgraded regularly.** Every library you add widens the attack
   surface.
8. **Expect more incidents as AI lowers the cost of attacking** - and use the same tooling on
   your own code.
