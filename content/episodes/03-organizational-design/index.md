---
title: "Organizational Design in Tech Departments"
season: 1
episode: 3
date: 2026-03-31
youtube_id: "z_U8JOZwQwo"
duration: "50 min"
apple_url: "https://podcasts.apple.com/us/podcast/organizational-design-in-tech-departments/id1885344238?i=1000758541214"
spotify_url: "https://podcasters.spotify.com/pod/show/raphael716/episodes/Organizational-Design-in-Tech-Departments-e3f1u3e"
summary: "From five generalists to 180+ engineers: why frontend and backend teams break, what 'follow the flow of the work' means in practice, and how Conway's law quietly decides your architecture for you."
topics:
  - "Team Topologies"
  - "Conway's law"
  - "cross-functional teams"
  - "platform teams"
  - "enabling teams"
  - "complicated subsystem teams"
  - "Spotify model"
  - "staff and principal engineers"
  - "full-stack hiring"
  - "boring technology"
references:
  - title: "Team Topologies: Organizing Business and Technology Teams for Fast Flow"
    authors: "Matthew Skelton, Manuel Pais"
    url: "https://teamtopologies.com/"
    note: "The backbone of the episode - the four team types."
  - title: "Peopleware: Productive Projects and Teams"
    authors: "Tom DeMarco, Timothy Lister"
    url: "https://en.wikipedia.org/wiki/Peopleware:_Productive_Projects_and_Teams"
    note: "The old book whose insight still holds: it is always about people."
  - title: "Conway's Law"
    authors: "Melvin E. Conway (1967)"
    url: "https://www.melconway.com/Home/Conways_Law.html"
  - title: "Site Reliability Engineering"
    authors: "Google"
    url: "https://sre.google/books/"
  - title: "Irrational Exuberance - writing on engineering organisations"
    authors: "Will Larson"
    url: "https://lethain.com/"
    note: "Cited as a good source on making AI work inside an engineering org."
  - title: "Accelerate: The Science of Lean Software and DevOps"
    authors: "Nicole Forsgren, Jez Humble, Gene Kim"
    url: "https://itrevolution.com/product/accelerate/"
  - title: "DORA Metrics"
    url: "https://dora.dev/"
---

## In this episode

- Why there is no ideal org structure - only an ideal structure *for your current size and
  context*, which you will outgrow.
- "Follow the flow of the work" (or: follow the money) as the organising principle, and why
  frontend/backend splits collapse at around 10 people.
- Conway's law, in the original 1967 wording, and how to run it in reverse.
- All four Team Topologies team types, with real examples of each - including what a
  "platform" turns out to be when you stop assuming it means Kubernetes.
- Staff and principal engineers as domain architects who still write code, and where they
  should report.
- Two structural rules: hire full-stack minds, and keep the number of technologies small.
- What AI does to all of this - including a genuinely provocative claim about
  cross-functional teams becoming less necessary.

## Deep dive

### It is architecture - just not the technical kind

The framing the episode opens with: team structure is architecture. Not technical
architecture - **organisational architecture** - and it determines what the technical
architecture will become. Get the tech architecture perfect and the people wrong, and you
can throw both away. The reference point is *Peopleware*, written back when engineers sat
in cubicles next to IBM mainframes, whose central insight has aged perfectly: it is always
about teams and people.

The second framing point, made early and repeated: **there is no ideal organisational
setup. There are many ideal setups, each fitting a particular size and context.** People
tend to treat a reorganisation as the final answer - this is now how we are structured,
forever. It never is. The structure has to stay fluid: teams get restructured as the
organisation grows, and even a stable structure occasionally needs a specialist to move
between teams for a while. Everyone in the org has to be able to live with that.

One host is currently leading 180+ people and still growing, after previous departments in
the 30-80 range - and is explicit that the current scale is where they are learning the
most.

### Why frontend and backend teams break

The default path is understandable. Five people start out; one or two do frontend, three do
backend. As the company grows, that split hardens into a frontend team and a backend team.
It works up to maybe eight, nine, ten people.

Then it breaks, and the failure mode is precise: **the teams lose sight of the product.**
Members no longer know what they are delivering - they think in technical terms only. The
symptoms are familiar to anyone who has lived it: delivery slows, nothing is finished
end-to-end, the backend team declares done while the frontend team is still waiting, and
nobody feels ownership of a business outcome.

There is a human mechanism underneath. As the system grows more complex, people instinctively
retreat into an area where they feel competent and comfortable - **they organise into
tribes**. Left alone, they will sort themselves by technology, because that is the most
comfortable split available. That instinct is exactly what leadership has to intervene
against.

### Follow the flow of the work

The organising principle offered as the alternative is borrowed from police work: *follow
the money*. Software engineers are not employed to write beautiful code or elegantly apply
a pattern - they are there to deliver value that makes the business successful. So
structure teams along the path that value takes.

A feature is not done when the frontend looks right but the backend has not started, or
when the data science piece is missing. So the people needed to deliver a slice of value
**end to end** belong in the same team. That is what a cross-functional team is for. The
host is candid that this creates its own problems - it does not make them disappear, it
trades them for better ones.

Timing matters. You can start this at five people, but it is not obvious yet - you have
generalists because you cannot afford specialists. It becomes genuinely effective at 10-20
people, when you stop being one team and become three, four, five, six. And the warning
attached: **do not do business-unit-style structuring too early.** At 10-20 people that is
premature optimisation. Your real problem is finding product-market fit, and you should
assume that much of what you are building now will not survive five years, because you will
pivot more often than you would like. Build to prove the value exists; build the system
meant to last once it is proven.

### Conway's law, forwards and in reverse

The episode takes the trouble to quote Melvin Conway properly, from the 1967 paper:

> Organizations which design systems are constrained to produce designs which are copies of
> the communication structures of these organizations.

The shorthand version: give two teams a compiler to write, and you get a two-pass compiler.
Give it to three teams, and there is a good chance you get a three-pass compiler.

Applied to the earlier discussion, it explains itself: **frontend and backend teams produce
a frontend monolith and a backend monolith.** Teams organised around business domains
produce their own small kingdoms - separate services, probably some event-driven
integration between them. The structure you choose is the architecture you will get,
whether or not you intended it.

Hence the **reverse Conway manoeuvre**: choose the team structure that matches the
architecture you want, and let the teams reshape the existing system toward their new
organisational shape. Use the law deliberately rather than being surprised by it.

### The four team types, with real examples

**Stream-aligned teams.** The default. Aligned to a flow of work - a slice of the product,
end to end.

**Platform teams.** Here the episode makes its most useful correction. Reading Team
Topologies, the instinct is that "platform" means infrastructure and Kubernetes. In
practice, working with 20+ teams, what emerged was closer to an **operating system for the
company**: the services every other team needs in order to function at all. The concrete
example is user and profile access - under GDPR, one person can have several profiles
depending on which B2B customer they arrive through, and every team needs that service to
work. That *is* the platform. The Kubernetes-and-infrastructure platform team existed too,
but redefining "platform" around what teams actually depend on was the insight. Three years
on, those platform teams are being converted into stream-aligned teams by handing them
product feature responsibility - the structure keeps moving.

**Complicated subsystem teams.** The type almost nobody uses, per the hosts. A team holding
deep specialist knowledge of something inside the product that requires rare skills, or
that you deliberately keep narrow. Examples given: the data science team training your
models; video specialists on a product built around processing a 3D camera signal to find
body joints; and a real one from a past company - **an algorithm only two engineers had
access to**, because it was the differentiating capability no competitor could match.

**Enabling teams.** A team of experts that helps other teams cross a transition. The worked
example: five stream-aligned teams on HTML/CSS/jQuery that need to move to React. An
enabling team of React experts joins them, teaches them, consults with them through the
transition. Very handy specifically for technology changes.

The real-world hybrid: their **SRE team is simultaneously a platform team and an enabling
team.** Part of it runs the Kubernetes platform and the administration around it. The SREs
themselves *embed into stream-aligned teams* - helping with operational features and
observability, and because they are engineers, also picking up feature tickets. Deployment
is nominally temporary but elastic: an SRE joining a team for a year feels permanent to
some. Greenfield projects get them for longer, both to bootstrap and to ensure the agreed
processes and technologies are actually followed, then they phase out. Long-running work
like dismantling a monolith - which takes years, not weeks - keeps one or more SREs along
for the whole ride.

### The Spotify model

Handled briefly and with the standard caveat: everyone quotes it, nobody uses it, and
reportedly not even Spotify uses it as described online.

The real problem it addressed is genuine, though. Once you have five stream-aligned silos,
what stops team one using React, team two Vue, team three something else - and all the
Spring Boot services being deployed five different ways? Spotify's answer was a matrix
organisation with **chapters**: the frontend engineers across all teams meet regularly and
agree coding styles and technology choices, so that what emerges from the silos stays
broadly consistent. An old idea, correctly applied to a real problem.

### Staff and principal engineers

The concept enters through a story about a CTO who deployed staff engineers as **free
radicals** - largely choosing their own assignments, gravitating to the most important
teams, and partly leading technology transitions such as breaking large services into
microservices.

The version in use in one host's company is similar in intent, different in mechanics. They
run **principal engineers** who behave like domain architects - and the title choice is
deliberate: *architect* is avoided, because **they want these people to still write code.**
If not up to their neck in it, at least up to the waist. An architect who does not code does
not know what they are architecting, and the actual job is helping others make good
architecture decisions: sane, not prematurely optimised, and not a dead end for next year's
extension of the feature.

Two structural notes:

- **This is a scale-dependent role.** At five people you do not need it - you can listen to
  all five. At 50, 80, 150+, an SVP has no chance of knowing what is really happening
  everywhere. Trusted people who understand where the organisation is going become
  structural necessities.
- **Reporting line matters.** Very senior engineers who built the systems and have been
  there for years feel wrong slotted into a team, reporting to a team lead who reports to a
  head of engineering who reports to the CTO. The classic solution is to have them report
  directly to the CTO - above the field, which everyone tends to accept - with regular
  one-on-ones that also give the CTO an unusually clear view of what is going on.

Behind that sits a broader claim about engineering leadership: it needs either a split brain
- strong at technology *and* at organisation - or two people carrying those halves and
working as one leadership unit, both engineers. In the current setup described,
organisational responsibility for the 180+ people sits with the SVP, while technical
responsibility runs on a **dotted line to the CTO** for that same group, who work together
as a technical body.

### Two rules that make structures work

**Hire full-stack minds.** Proposing a full-stack hire to a frontend/backend-split team is
mind-blowing to them, and their objection is reasonable: specialisation is real, and someone
who spent their career in C++ *is* a C++ expert. But the thing being hired for is not
uniform competence - it is **a specialist in one area who is willing to contribute
elsewhere.** Someone who writes good C++ can contribute React code. They will not be the
best CSS juggler in a large frontend architecture, but they can contribute - and that makes
assigning stories across teams dramatically more fluid. One host set up an entire business
unit staffed only with full-stack people, and reports it made both their life and the
teams' lives easier, because they can work across the whole product the unit owns.

**Keep the number of technologies small.** Imagine five teams contributing to one business
domain in C++, Flutter, Java, TypeScript and Rust. No team can help another, nobody can read
anyone else's code, and hiring has to be adapted per stack - the cost multiplies. Google is
the counter-example: on the backend, essentially C++, Java and Go across an enormous
engineering population, which means anyone can open anyone's repository and contribute.

The refinement, offered by the other host and accepted: **as few as possible, and as many as
necessary.** A native app on iOS and Android forces certain choices; firmware for your own
circuit board forces others. And prefer **boring technology** - battle-tested, widely known,
already taught at university, so you can actually hire for it. Switching your Angular
experts to React because React is the new thing is expensive and, in most cases, unwise.

### What AI changes

The episode's most interesting stretch, and one both hosts flag as deserving its own episode
(it got one - Season 1 closes with it).

The framing claim: **AI is as disruptive to this industry as the arrival of the web.**

The distinction it forces is between a **coder** - someone who knows a technology inside out,
years of C++ in their hands - and a **software engineer**, someone who understands how to
build a system: how to run it, maintain it, upgrade it over five to ten years, grow teams
around it, reason about its performance. The illustrative test offered: knowing what
exponential backoff is and why an API needs it.

The consequence for org design is genuinely provocative. If a strong backend engineer who
does not know React can now solve easy-to-mediocre frontend tasks with AI assistance, then
that engineer has effectively become full-stack - and **the argument that every team must be
cross-functional weakens.** From 180 people of experience: hiring specialists is painful and
necessary, and anything that widens what a good engineer can pick up is worth a lot.

The hosts explicitly do *not* go to "AI makes engineers obsolete". The direction taken is the
opposite: **software engineering - understanding how to build systems - becomes more
important**, while the specific technology skill matters slightly less.

It cuts both ways across disciplines, too. A product manager with a tool like Lovable can
prototype without an engineer. An engineer with access to a proper design system can build
UI, run A/B tests, read the metrics, and make calls that used to need a product manager. The
recommendation is to experiment with this deliberately in both directions - and to see
enabling other departments as an engineering duty: if a product manager wants to tune the
frontend with an AI tool, engineering's job is to make that safely deployable.

The structural conclusion closes the loop back to the start of the episode: **a
frontend/backend structure, or any structure not focused on business domains, helps you even
less in the age of AI.** Keeping the stack simple and the organisation focused on business
outcomes matters more now, not less.

## Key takeaways

1. **Organisational design is architecture.** Conway's law means your team structure will
   be reproduced in your systems whether you plan for it or not - so plan for it.
2. **There is no permanent structure.** Fluidity is the requirement; expect to reshape as
   you grow, and make sure people expect it too.
3. **Follow the flow of the work, not the technology.** Frontend/backend splits break around
   10 people and cost you product focus and end-to-end ownership.
4. **Redefine "platform" around what your teams actually depend on**, which may well be a
   user service rather than a Kubernetes cluster.
5. **Complicated subsystem and enabling teams are underused** - both solve real problems that
   stream-aligned teams handle badly.
6. **Principal and staff engineers should still code**, and usually need a reporting line
   that reflects their scope rather than a team slot.
7. **Hire specialists with an open mind, and keep the technology count low** - as few as
   possible, as many as necessary, and prefer boring.
