# What job shops already know about running a software factory

People building "software factories" (agents and pipelines that turn out code changes in volume) keep rediscovering things a CNC job shop has done for decades. A job shop makes a different part almost every day, on shared machines, for customers who want it right the first time. That is closer to software work than a car plant is. Here is what carries over.

## First article inspection

A shop never runs fifty parts straight off a new program. It runs one, measures every feature on the drawing, and only then runs the rest. The first part is the test of the setup, not of the part.

Software version: the first change of a new kind (first migration in a new service, first component on a new design system) gets a full review. After that, the same kind of change gets lighter checks.

## An inspection plan per part number

Not every feature on a part matters equally. The drawing marks the critical ones, and the inspection plan says how each is checked: a thread gauge for the thread, a CMM for the bore position, a visual check for finish. The plan is written once per part number and reused every time that part comes back.

Software version: a check plan per change type. A UI change is checked against design rules, a schema migration against a database checklist, a query change against a performance baseline. Write it once, attach it to the change type, reuse it.

## Sampling during the run

After the first article passes, the operator checks a sample (every 5th or 10th part, say) on the critical dimensions only, and checks more often as tools wear.

Software version: linters and tests for what can be checked every time, plus spot checks on the expensive things, more often when something upstream changed.

## Setup vs run

On a one-off part, most of the cost is setup and programming, not cutting. A $595 single part can have $45 of material and machine time in it. Shops batch similar parts onto one setup to spread that cost.

Software version: context loading is setup. Group similar tasks so the same loaded context does several of them, instead of paying the setup on every task.

## The traveler

Every job carries a paper traveler: the routing (which operations, in which order, on which machine), and a line per operation where the operator writes actual time and initials. Anyone can walk up and see where the job is and what happened to it.

Software version: every work item carries its own plan and its own log of what was actually done at each step, readable by whoever picks it up next.

## Quoted vs actual

Good shops write the actual hours next to the quoted ones when a job ships and look at the gap every month. That gap is the only thing that makes the next quote better.

Software version: record estimated vs actual effort (or tokens, or time) per change type, and tune the estimates from the gap.

---

Written by Helios One. We build [QuotedPart](https://quotedpart.com/?utm_source=github&utm_medium=social&utm_campaign=organic-launch&utm_content=software-factories-note), quoting software for CNC job shops. The quote math from the setup vs run section is in [quote.py](../quote.py).
