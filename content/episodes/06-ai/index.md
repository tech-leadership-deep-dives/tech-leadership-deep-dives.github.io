---
title: "AI"
season: 1
episode: 6
date: 2026-07-02
youtube_id: "a8BpmzD1Xyo"
duration: "56 min"
apple_url: "https://podcasts.apple.com/us/podcast/ai/id1885344238?i=1000774930070"
spotify_url: "https://podcasters.spotify.com/pod/show/raphael716/episodes/AI-e3jdlab"
summary: "Agentic coding is here, and the interesting question is not whether it works but how you roll it out across 200 engineers - guardrails, adoption, career expectations, cost, and what smaller teams do to the product manager's job."
topics:
  - "agentic coding"
  - "levels of AI adoption"
  - "guardrails and secrets"
  - "AGENTS.md / CLAUDE.md standardisation"
  - "AI champions and chapters"
  - "AI in career frameworks"
  - "smaller teams"
  - "product manager and engineer converging"
  - "hallucinations"
  - "token cost"
  - "local models"
  - "MCP and AI-ready products"
references:
  - title: "Model Context Protocol (MCP)"
    url: "https://modelcontextprotocol.io/"
    note: "Named as one good way to open your product up to agentic customers."
  - title: "Drive: The Surprising Truth About What Motivates Us"
    authors: "Daniel H. Pink"
    url: "https://www.danpink.com/books/drive/"
    note: "Autonomy, again - the argument against putting red tape in front of experimentation."
  - title: "Claude Code"
    url: "https://claude.com/product/claude-code"
  - title: "GitHub Copilot"
    url: "https://github.com/features/copilot"
  - title: "Cursor"
    url: "https://cursor.com/"
---

## In this episode

- Where AI sits in the sequence of industry shifts - and why the hosts put it next to the
  web rather than next to blockchain.
- A four-level model of AI adoption among engineers, from "paste code into a chat window" to
  running six agents in parallel.
- The guardrails question, and the argument that agents need the same checks humans do -
  only faster.
- Rolling adoption out across a department: champions, chapters, OKRs, token usage as a
  (deliberately imperfect) metric, and putting AI competence into the career framework.
- Predictions: much smaller teams, product managers who ship prototypes, engineers who
  think like product managers.
- The unglamorous parts - hallucinations, token cost, and why the cheaper model is often
  more expensive.
- Making your *product* AI-ready, and why that turns out to be the same thing as having good
  docs and a good API.

## Deep dive

### Which kind of revolution is this?

The episode starts by placing AI in a lineage: higher-level programming languages, the mouse
and the graphical desktop, the internet, the touchscreen smartphone. Each arrived with the
promise that *now everyone can do this*, and each time the honest outcome was smaller than
the promise and larger than the sceptics allowed - not everyone could code, but far more
people could. Blockchain is named as the counter-example that did not clear the bar.

One host's position: something genuinely revolutionary is happening, it will change how we
work, but probably not in the shape the marketing suggests - *open to the revolution,
cautious about the Kool-Aid.* The other is more emphatic, and the evidence offered is
adoption rather than capability: a photographer with no technical background building her own
website with an agentic coding tool; a 13-year-old generating her own English and maths
practice material. The comparison drawn is the arrival of the internet in the 1990s - modems,
mailboxes, AOL, and the slow realisation that everything had changed.

The scoping note matters: when people say AI now, they mean **LLMs and agent systems**. AI's
1980s and 90s hype cycle - expert systems, decision trees meant to replace doctors - never
took off. This one has, with money, data centres, energy and chips behind it. It may be a
bubble; the technology is not going away either way.

### Four levels of adoption

The mental model used to think about where engineers actually are:

1. **Chat window.** Ask questions in ChatGPT, paste in some code, get a test back, paste it
   into the IDE by hand.
2. **In the IDE.** The assistant sits inside the editor with access to your files and can
   make changes itself.
3. **Agentic coding.** Tools that understand the whole codebase, use tools, spawn other
   agents, reason about the work. You develop a spec or requirements document *with* the
   tool - what should be built, in what steps, against what checklist - and then it works for
   half an hour and implements it.
4. **Parallel agents.** Ten of those running at once, on different codebases or the same one.

And beyond that, the fully automated loop, from a friend of one host: a GitHub issue arrives,
an agentic system picks it up, fixes it, opens a pull request. Reported hit rate at the start
of 2026: roughly **two out of five tickets** come back mergeable with nothing for a human to
do but review and click. In the CI/CD pipeline, unattended.

The framing both hosts settle on: **agents are junior engineers.** Very fast junior engineers
who have read every manual, lacking the creativity to design a system, needing exactly the
things a junior needs - guidance, a clear structure, stated expectations about code layout,
test coverage, domain-driven design or whatever principles you follow. The human moves from
author to **guide and reviewer**. One host compares it to pair or mob programming with the
pairs replaced by agents. The other's summary: *it is expectation management. Again.*

### Guardrails without red tape

Two real problems land on a department head at once.

**The spectrum problem.** In any engineering organisation you have enthusiasts using agentic
tooling every day at home, and sceptics who do not trust it - often for defensible reasons,
sometimes based on an experience six months ago with tooling that has since improved beyond
recognition. Managing both ends at the same time is genuinely hard.

**The safety problem.** Let AI tooling loose on your codebases and there is a real chance
credentials and secrets end up on somebody else's server. And the guardrails you design today
may be obsolete in two weeks, because the technology is moving that fast.

The position argued for is careful and worth stating in full. **An agent can do roughly what
an engineer can do, so the controls you need are the controls you already needed for humans**
- the difference is speed. If the rule is "write unit tests", it applies to agents too. The
awkward part is what this exposes: we have long allowed humans to merge and deploy on the
strength of some manual testing, without integration or system tests - and no amount of
manual testing before release really tests what you need tested. Now that agents move faster,
we suddenly insist all those tests exist first. The host names the tension honestly as a
chicken-and-egg problem they have not solved, and leans toward: **build the checks when you
find something not working, rather than making them a barrier to using agentic coding at
all.**

The barrier argument is the strongest thread in the episode. Requiring every instruction file
and standard to exist before anyone may touch the tooling is red tape - and engineers who want
to innovate will simply go home and do it on their pet projects. **You want the innovation
happening inside your company, where both sides benefit.** This is the *autonomy* leg of
Pink's autonomy/mastery/purpose, applied directly: decentralised experimentation, with
leadership guiding rather than gating.

The counterweight, and both hosts agree on it: an individual team cannot see across the
department. You can. So when standardisation clearly helps, drive it. The concrete example:
if several teams use the same framework, they share conventions on structure, secrets handling
and testing. **Write that down once, put it in an `AGENTS.md` or `CLAUDE.md`, replicate it
across projects, improve it jointly.** The same instructions serve the agents and the humans -
and if you never documented any of it, this is a good excuse to finally do so.

### Rolling it out across a department

The concrete programme described, from a company one host works with:

- **An OKR for AI adoption**, on the theory that better software and higher productivity
  follow.
- **GitHub Copilot as the sanctioned tool**, chosen specifically so that secrets do not flow
  to models outside their control, with GDPR compliance and measurable token usage.
- **Token usage as an adoption metric** - offered with an immediate, honest caveat that it is
  *a bad metric*: rising usage is weakly good, flat usage suggests something is off, and it is
  trivially gameable. (Somewhere out there, a company put up a token-usage leaderboard and
  switched it off quickly when people started burning money to top it.)
- **An AI champion in each team and an AI chapter** across them - the identical pattern to
  the security chapter from [the Security episode]({{< relref "/episodes/04-security" >}}), for the same
  reason: it is a concern that cuts across every team.
- **At least three presentations** from teams already using it, so that the sceptics see
  peers demonstrating real results rather than a leader insisting.

Then the sharpest exchange in the episode. The OKR was called *"becoming AI ready"*, and the
other host objects to the name: **naming it "AI ready" creates a hurdle.** It implies you are
not allowed until every goal is checked off. You are AI-ready *today*, with what you have. The
things you want to build do not create readiness - they increase your professionalism in
handling it, and let you sleep better. The point is accepted on the spot: write the objective
so it pulls in a direction, rather than erecting another gate.

**Getting the sceptics on board** has three parts: lead by example; let peers demonstrate;
and - the structural move - **put AI competence in the career framework.** The reasoning is
by analogy with testing. Writing tests has no value in itself; stable software does, and tests
are how you get it. AI will not make you a good engineer; producing good software productively
is the goal, and AI is now part of how that is done. So a senior engineer is expected to have
demonstrable AI competence, and that shows up in performance reviews. Someone can still choose
to work without it - but it becomes a conversation, not an unexamined preference.

### Predictions

Both hosts flag that they are bad at predicting the future and that the video will be worth
rewatching in a year. With that caveat:

**Teams get much smaller.** A product area currently staffed by a product manager and five or
six engineers might be a product manager and one or two engineers. Framed negatively: fewer
people needed. Framed positively: far more things get built. (The other host pushes back on
"one engineer" for a practical reason - if that person is ill, nobody is supervising the
agents.)

**The product manager becomes more important, and changes shape.** With fewer engineers per
product area, you need either more product managers or engineers with much better product and
customer understanding. Senior and staff engineers are already expected to be customer-minded;
in future, a senior engineer should be *able* to cover the product manager role. Meanwhile
product managers ship: the example cited is a company where getting approval for a feature
means bringing a **working prototype**, not Figma screens - built by the product manager with
an agentic coding tool, not scalable, but clickable. Engineering then takes over to make it
real.

**The two roles converge**, which one host frames as an acceleration of **T-shaped skills**:
deep in one area, shallow-but-real in adjacent ones, with AI filling the gaps. An engineer who
understands design and product; a product manager who understands delivery. Neither host finds
that threatening - they welcome it. And it extends beyond engineering: UX research, design,
experience design, product discovery are all in scope, not just the code.

**The engineer's day changes.** A senior engineer running five or six agents in parallel is
effectively leading a team: writing the specs, guiding, reviewing, correcting. Mentoring and
coaching were always part of the senior role; the mentees are now agents. The immediate
objection is raised and left open - **that is the opposite of focus**, and parallelising your
attention across five problems is genuinely dangerous.

**On layoffs**, both hosts are unambiguous and aligned: the big-tech layoffs are mostly a
symptom of **over-hiring in previous years**, with AI as a convenient explanation. Most
companies are not drowning in surplus engineers; they are short of them. The likelier outcome
is hiring somewhat less, or - if you are ambitious and funded - hiring more, because you
finally have capacity for the backlog of ideas every company carries. The engineers hired will
be the ones who have embraced agentic work.

### The risks

**Hallucinations.** Stated bluntly: these are probabilistic machines that extend sentences,
and they can be confidently, completely wrong - about architecture, about facts, about maths.
The personal example is the 13-year-old's generated study material containing errors. The
professional worry is compounding: **architectural mistakes that compound across iterations
produce unusable software.** One host describes deliberately testing ChatGPT on a legal
question they already knew the answer to, and getting it wrong - with the uncomfortable
follow-on question of how many past answers they simply accepted. Always take a second look,
ask for references, and remember that "I would not google a medical problem" applies here too.
This is exactly why the human stays in the loop - as guide and final check.

**Cost.** It gets expensive, and it needs managing. Roughly, **a word is about a token**, so
the arithmetic is doable once you know your per-token price. Where it becomes unpredictable is
agents calling sub-agents and tools - scraping websites through an agent is startlingly
expensive. One team went as far as adopting a terse "caveman" prompting style to cut word
count.

The genuinely counter-intuitive finding: **choosing the cheaper model can cost more.** A less
capable model needs more reasoning tokens to reach an answer a stronger model reaches quickly.
In the experiments described, the expensive model was cheaper overall - shorter thinking, fewer
tokens, faster resolution.

**Vendor and model risk.** Nobody knows how the providers will change their pricing or
business models. Which leads to the most concrete prediction in the episode: **models move
local.** Open-source models already run acceptably on a home machine or a modest GPU, and
research on reducing precision and memory footprint keeps cutting the requirements. Two or
three years out, the expectation is models running on your laptop and your phone as part of
the operating system, rather than in a data centre - with the trade-off that a local model has
a knowledge cutoff you have to manage.

### Beyond engineering: three more surfaces

The episode closes by widening the frame past coding.

**AI inside management.** Giving the CFO access to data lakes so a quarterly deck can be
generated from a template and the underlying data rather than assembled by hand. For
engineering, that means opening your repositories and data up so the company's agents can
reach them.

**The "mini CTO".** Agentic tooling supporting the leadership job itself: automating weekly
reviews, checking Jira hygiene, verifying that recurring meetings are actually scheduled - the
large repetitive surface of running a department. The other host visibly takes this away as a
to-do, noting that with 20 teams and 200+ people, manually checking a dozen tools does not
scale, and a self-built dashboard now costs a fraction of what commissioning one used to.

**AI-ready products.** Other companies' agents will want to use *your* systems. MCP is one
good way to expose your data; a solid API is another. And here is the neat observation the
episode ends on: if you already have a good API, a CLI over it, and good documentation, then
**an agent can read your docs and use your product today** - you are already AI-ready. If it
cannot, that is not really an AI problem: it means your human customers also struggle to
understand your API. AI does not create the problem; it **makes an existing problem more
visible**, and rewards the companies that did the boring things well. A flywheel for good
documentation.

## Key takeaways

1. **Treat agents like junior engineers**: state expectations, give them structure, review
   their output. Everything you know about setting expectations still applies.
2. **The guardrails agents need are the ones humans always needed** - the difference is
   speed. Build them when you find gaps rather than gating adoption behind them.
3. **Do not put red tape in front of experimentation.** If engineers cannot innovate at work,
   they will innovate at home and you get none of it.
4. **Standardise the instructions**, not the enthusiasm: one shared `AGENTS.md` /
   `CLAUDE.md` per stack, improved jointly, serving humans and agents alike.
5. **Use champions and a chapter to drive adoption**, lead by example, and put AI competence
   in the career framework so it becomes a normal expectation.
6. **Watch the cost, and question the cheap model** - more reasoning tokens can cost more than
   a stronger model that answers quickly.
7. **Hallucinations compound.** Architectural errors that go unreviewed produce unusable
   software a few iterations later.
8. **Making your product AI-ready is mostly just having a good API and good docs** - and if
   agents cannot use it, your customers probably struggle too.
