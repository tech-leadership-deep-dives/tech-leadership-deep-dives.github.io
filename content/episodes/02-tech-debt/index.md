---
title: "Tech Debt"
season: 1
episode: 2
date: 2026-02-28
youtube_id: "fJjRd3VbShg"
duration: "43 min"
apple_url: "https://podcasts.apple.com/us/podcast/tech-debt/id1885344238?i=1000755405399"
spotify_url: "https://podcasters.spotify.com/pod/show/raphael716/episodes/Tech-Debt-e3f1u16"
summary: "Tech debt can kill your company - slowly, through hiring, security, delivery speed and the upgrades you keep postponing. How to make it visible, budget for it, and explain it to people who do not write code."
topics:
  - "the four costs of tech debt"
  - "DORA metrics"
  - "definition of done"
  - "architecture decision records"
  - "investment framework"
  - "keeping the lights on"
  - "translating tech into business language"
references:
  - title: "Accelerate: The Science of Lean Software and DevOps"
    authors: "Nicole Forsgren, Jez Humble, Gene Kim"
    url: "https://itrevolution.com/product/accelerate/"
  - title: "DORA Metrics - lead time, deployment frequency, change failure rate, MTTR"
    authors: "DORA / Google Cloud"
    url: "https://dora.dev/"
  - title: "Architecture Decision Records"
    url: "https://en.wikipedia.org/wiki/Architectural_decision"
  - title: "Technical Debt Quadrant"
    authors: "Martin Fowler"
    url: "https://martinfowler.com/bliki/TechnicalDebtQuadrant.html"
---

## In this episode

- The four ways tech debt actually bites: hiring, security, delivery speed, and upgrades
  that mutate into multi-month projects.
- Why "we're suddenly slow" is almost always the symptom that brings someone to your door.
- Making debt visible: DORA metrics, ticket labelling, architecture decision records, and a
  simple investment framework your CFO will genuinely like.
- The hosts disagree on whether bugs belong in the engineering budget or the product
  budget, and both arguments hold up.
- Why the hardest skill in managing tech debt is not technical at all: it is finding the
  words a CFO will act on.

## Deep dive

### The symptom nobody names correctly

The episode opens with a pattern one host has hit repeatedly across clients and companies:
nobody comes to you saying "we have tech debt". What arrives instead is a vague, spreading
feeling that **something is off - we are slow, we have bugs, everything is risky.** Look
closer and it is nearly always accumulated shortcuts that worked brilliantly at the start
and then quietly stopped working.

The canonical trajectory: you used to deploy several times a day. Then it got too
error-prone, so it became weekly with QA cycles. Then twice a month. Then monthly. And once
you can only deploy monthly, **you are no longer an agile business** - you cannot react to
the market at the speed the market moves. You will still have bugs; you will still need
emergency redeploys; and the relationship between engineering and QA will still be painful.
That is what tech debt looks like from the outside.

### The four costs

The framing the episode keeps returning to breaks the cost into four concrete areas, none
of which is "the code is ugly":

**1. You lose the ability to hire.** This one is invisible until it isn't. If you are on an
eight-year-old Angular version with known security flaws, telling that to a strong
front-end candidate does not generate excitement. Later in the episode there is a real
example from one host's past: a company still running PHP 3 code when PHP 5 was current -
and interviews where describing the daily reality made candidates visibly decide not to
join.

**2. Security.** Security is always an afterthought, and everything is fine right up until
it is not. Outdated PHP or Java runtimes, unpatched frameworks, the Java logging
vulnerabilities everyone remembers - each one widens the attack surface. A breach that
leaks customer emails, or touches payments, can take out the company's reputation outright.

**3. Delivery speed falls off a cliff.** Not a gentle decline. Everything feels like a huge
issue, every change feels risky, and the organisation loses the ability to move.

**4. Upgrades become projects.** Upgrading an eight-year-old framework is not "bump the
library". The framework itself has changed underneath you; it is months of work and a wall
of breaking changes. And this is where the **vicious cycle** closes: because you know it
will hurt, you postpone it; because you postpone it, it hurts more; so you postpone it
again. Meanwhile the hiring, security and speed problems compound alongside.

### Context first: when is debt acceptable?

The episode refuses to be dogmatic, and spends real time on when shortcuts are fine.

**Early-stage startup hunting product-market fit:** tech debt is genuinely not your main
concern. You need only enough quality that your handful of customers can tell you whether
you are on the right track. The floor is real, though - if logins keep failing, customers
never reach the value proposition, and you have learned nothing.

**Established product with hundreds of thousands of customers:** the quality those customers
already expect is the baseline, and the calculation changes completely.

Within an established company, the next question is what kind of work this is:

- **Proof of concept** - explicit rules apply, with more freedom, but also a hard boundary:
  this will not go to production, or if it does, it is restricted to 0.5-1% of customers so
  you can learn what you set out to learn.
- **Production work** - it has to meet the **definition of done**, which the episode is
  careful to distinguish from acceptance criteria. Definition of done means: the tests we
  agreed on are written, it runs on the technologies we agreed on, there is a runbook so
  whoever is on call at 3am knows what to do, the logs go where logs go, the metrics exist.

The interesting case is the grey zone: the proof of concept that went well and now an
important customer wants it in production tomorrow, with real revenue attached. The
position taken is that engineering exists to help the business succeed, so the answer is
not "no" - it is an **explicit negotiation**: yes, and in return we get a defined later
point at which we fix it, and everyone understands that until then we are slower on the
next feature, and the one after that. The image offered: building balconies on balconies.
There is a limit to how many you can stack.

### Craftsmanship and who gets to decide

A pointed argument runs through the middle of the episode. A manager would not tell a mason
how to build a wall or a carpenter where to fit a door - yet telling software engineers to
skip tests or postpone library upgrades is treated as normal. Non-technical people
routinely make calls about engineering craftsmanship in a way they would never do while
watching their own house being built.

The counter-argument, from the other host, is fair: on tests specifically, a manager wanting
*fewer* tests is not automatically wrong. You can write tests until the end of time without
benefiting the business. The judgment call is how much to test and at which level - and
that judgment belongs to engineering.

Both agree on the real conclusion. You can ignore the business and do it your way, and if
it is your own company you may well be right. As an employee, being seen to go rogue is how
you stop belonging in the company. So the skill that matters is **explaining debt and
compound interest in a way non-technical people can act on** - the banking metaphor is
already universally understood; the work is connecting it to what happens in a codebase.

### Making it visible: metrics, ADRs and labels

You cannot manage what nobody can see. The episode lists the specific instruments in use.

**DORA metrics, from Accelerate.** Start simple. One host explicitly extends beyond
release-cycle time to the **full lead time** - from the start of development to release -
because cycle time is a *resulting* metric; the damage happens upstream of it. Once a
feature crosses a threshold (say two weeks), it surfaces on a chart as a dot climbing
higher - a colleague calls them "balloons floating into the sky" - and that is the trigger
to go look at what is actually happening.

The argument for deploy frequency is worth quoting in spirit: the objection is always "but
we don't *need* to deploy several times a day". Correct - you do not need to. **You need
the ability to.** Because if you have that ability, a whole class of problems cannot be
present: missing automated tests, a strange QA setup, buggy software. Losing the ability is
the signal. And the corollary: *if it hurts, do it more often* - make the painful thing
frequent and the smart engineers you hired will make it stop hurting, because good
engineers are constructively lazy.

**Architecture decision records.** Used specifically to record shortcuts as they are taken,
owned and overseen by the CTO together with the architecture group. The example given: while
moving from a monolith to a service-oriented architecture, every change to the monolith had
to pass the CTO's and SVP's desk. That was deliberate friction - teams either moved the
change into the new architecture or waited. Most chose to move.

**Ticket labels and types.** Jira, like roughly 80% of the industry, with labels,
components and dedicated ticket types - including maintenance tickets for library upgrades.
The concrete guardrail one host applies: **no third-party library more than three minor
versions behind.** That rule exists precisely to prevent the eight-year-old framework
scenario.

### The investment framework

The most immediately actionable idea in the episode. Bucket engineering time into four
categories:

1. New products
2. Improving existing features
3. Improving productivity
4. Keeping the lights on

"Keeping the lights on" covers library upgrades, daily operational work, bug fixing. Set an
intended percentage - the episode uses 20% as an illustration, with product work at roughly
60-70% - and then **watch the trend rather than the number.** If keeping-the-lights-on
climbs from 20% toward 40-50%, that graph is your evidence: debt is compounding, and it is
time to spend on category 3, improving productivity, which is exactly the work that reduces
category 4.

Two practical notes. The framework is attributed to something Dropbox published a few years
back. And it maps onto **capitalisation**, which is why the CFO will like it - a separate
topic, but a real reason finance will engage with a conversation they would otherwise tune
out.

The other host runs a variant: a fixed **25% of engineering capacity belongs to
engineering**, tracked monthly but judged annually. Some months it is 15% because product
has a trade-fair deadline; other months more, because bugs demanded it. Rigidity is not the
point - tracking is, along with a shared sense of what healthy looks like. Both agree that
sustained 40%+ means you are already in unhealthy territory, and possibly late.

**Where they disagree: bugs.** One puts bugs in keeping-the-lights-on, because bucketing
them there makes the problem visible immediately. The other puts bugs in *product* work,
with a clear rationale: bugs are often a side effect of how a feature was specified, and
somebody has to decide which bugs are worth fixing at all - and that decision belongs to a
product manager, not to engineering. The first host concedes the point is worth revisiting:
an outage and "I'd like that colour slightly lighter" are not the same object. Both agree
bug *count* is a useful signal about the system, not a performance KPI.

### The Dunning-Kruger of tech debt

Martin Fowler's technical debt quadrant comes up via a genuinely good question: **if you do
not know you have tech debt, is it still tech debt?** The answer - the one Fowler's
"inadvertent" quadrant points at - is yes, and this is the Dunning-Kruger effect applied to
code. You believe you are writing excellent software while accumulating exactly the debt
that will eventually kill the company, and you do not know it. Your not knowing has no
bearing on whether it exists.

Which is the whole argument for the instruments above: you have to know **where and when
your teams are cutting corners**, which is what ADRs, metrics and labelled tickets buy you.

There is a follow-on about junior teams. A junior developer told by a product manager to
skip tests to go faster will simply do it, and will reasonably assume that is how work
works. The hosts are explicit that this is **not the junior engineer's failure** - it is a
skill issue at the organisational level, and the accountability sits with leadership. One
line lands especially well: *guilt is not investigated, guilt is assigned* - and here it is
assigned, by default, to the leadership team. Leadership can delegate the *finding* of debt
to teams; it cannot delegate the decision about what to do with it.

The structural version of the same failure: if the CPO routinely overrides the CTO - the
CTO says 60% minimum test coverage, product says skip the tests, every time - then debt is
guaranteed. And that is not only the CPO's failure. It is the CTO's, for accepting it, and
the CEO's, for letting the power structure work that way.

### Speaking the other language

The episode's closing theme, and the point where one host pushes back hardest on the other.
The claim that a CTO will find it "easy" to take this to the board is challenged directly:
this is one of the *hardest* parts of the job. Engineering jargon is fluent and shared;
CFO language and CEO language are neither.

What helps:

- **Analogies that transfer.** The car you never service, which runs fine until it doesn't.
  The house whose plumbing you would never tell the plumber to skip. Compound interest,
  which everyone already understands.
- **Existing urgency.** If the CEO already feels that something is strangely off - upgrades
  take forever, nobody knows how to fix it - your job is far easier. Attach the explanation
  to the pain that is already in the room.
- **A technical person at the top.** Having a CEO or board member who genuinely understands
  technology changes everything. Shopify's Tobi is the example offered - he knows when
  something has to be fixed. The dry recommendation: hire for that.
- **Learning the business's language deliberately.** Knowing how budget discussions work,
  how labour is calculated, what HR and finance actually mean by their terms. An MBA is the
  comprehensive route and both hosts note you can absolutely acquire this yourself - neither
  treats it as a requirement.

The final structural insight, borrowed from security: **if tech debt has become a board-level
discussion topic, something went wrong long before.** Same as security incidents. The
absence of the discussion means either luck or a job well done. Dealing with it upfront,
before it needs a board slide, is the actual duty.

## Key takeaways

1. **Tech debt is a business risk, not an aesthetic complaint.** It costs you hiring,
   security, delivery speed, and eventually the ability to upgrade at all.
2. **Some debt is fine and inevitable** - every company has some. Unmanaged debt is what
   compounds.
3. **Negotiate shortcuts explicitly**, with a defined point at which you pay them back, and
   record the decision in an ADR.
4. **Keep the ability to deploy multiple times a day**, whether or not you use it. Losing
   it means a whole class of problems is already present.
5. **Bucket engineering time** into new products / improving features / improving
   productivity / keeping the lights on, and watch the trend. Past ~40% keeping-the-lights-on
   you are in trouble.
6. **No dependency more than three minor versions behind** - a cheap rule that prevents the
   expensive scenario.
7. **The decisive skill is translation.** Telling the CEO "we have tech debt" achieves
   nothing. Phrase it as risk, speed, cost and capability.
