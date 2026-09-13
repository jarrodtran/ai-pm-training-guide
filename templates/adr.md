# Architecture Decision Record (ADR) Template

Fill-in-the-blank template for Module 1 of the FDE-PM Field Manual (`fde-pm-field-manual.md`). One page per consequential decision, numbered, in the repo, never edited after acceptance — superseded instead. The rule that makes an ADR useful: **the Consequences section is the PM's section.** Costs, trade-offs, and what you are giving up are what make the record honest, and they are exactly what is missing from most engineering documents.

**ADR-[NNN] — [DECISION IN ONE LINE, AS A STATEMENT, NOT A TOPIC]**

- **Status:** [Proposed / Accepted / Superseded by ADR-NNN] · **Date:** [YYYY-MM-DD]
- **Deciders:** [NAMES AND ROLES — including the client-side security or architecture owner where relevant]
- **Supersedes / Superseded by:** [ADR IDS OR —]

## Context

[THE FORCES AT PLAY: the client requirement, the constraint, the failure we are avoiding, the deadline, the thing that changed. Include the numbers — latency budget, volume, residency requirement, cost ceiling. Anyone reading this in two years should understand why the decision was necessary without asking a human.]

## Decision

[THE CHOICE, IN THE ACTIVE VOICE, SPECIFIC ENOUGH TO BE TESTED AGAINST. "We will…" — not "we prefer…". If the decision has a scope limit, state it.]

## Consequences

**Positive**

- [WHAT THIS BUYS US — with the requirement it satisfies]

**Negative / costs accepted**

- [LATENCY, COST, COMPLEXITY, LOCK-IN, ONGOING MAINTENANCE, TRAINING BURDEN, CLIENT-SIDE DEPENDENCY]
- [THE THING WE ARE GIVING UP — and where it might hurt]

**Follow-on work created**

- [WHAT MUST NOW BE BUILT, DOCUMENTED, TESTED, OR CONTRACTED BECAUSE OF THIS DECISION]

## Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| [OPTION A] | [THE DISQUALIFYING REASON — cost, risk, residency, latency, maintainability] |
| [OPTION B] | [REASON] |
| [OPTION C — including "do nothing" where relevant] | [REASON] |

## Reversibility

[ONE-WAY DOOR OR TWO-WAY DOOR? If it is one-way, say what would make it worth revisiting anyway and what that would cost. If two-way, say who may change it and how.]

## Review date

[QUARTERLY, OR ON A NAMED TRIGGER — e.g. "on any change to the client's group model" or "if p95 exceeds 4 s in production"]

---

## Worked example (delete when filling in)

> **ADR-014 — Retrieval uses per-user ACL filtering at query time.** *Status: Accepted (2026-09-12). Deciders: PM, FDE lead, client security architect.*
> **Context:** the assistant answers questions over documents with mixed sensitivity. Retrieval currently indexes all documents; any user can receive content from any document. The client's security review identified this as the blocker to production.
> **Decision:** retrieval applies the requesting user's entitlements from the client IdP (group membership synced hourly). The index stores ACL tags per chunk; filtering happens **before** ranking. Cache keys include the entitlement set.
> **Consequences:** *Positive* — prevents cross-team disclosure, unblocking the security review. *Costs* — retrieval latency +~80 ms; entitlement sync lag up to 1 hour must be documented to users; index size grows ~15% with ACL metadata. *Follow-on* — entitlement-sync monitoring and an on-demand check path for role changes.
> **Alternatives rejected:** post-filter after ranking (leaks through rank position, wastes prompt tokens); separate index per team (40+ indexes, unmaintainable); document-level ACLs only (too coarse for shared spaces).
> **Reversibility:** one-way door — migrating away means re-indexing and re-testing the whole corpus.
> **Review:** quarterly, or on any change to the client's group model.

## Done when

- [ ] The decision is stated as a decision (not a topic) and is falsifiable
- [ ] Consequences name at least two real costs, not just benefits
- [ ] At least two alternatives are recorded with disqualifying reasons
- [ ] Reversibility is classified (one-way vs. two-way) with the cost of reversal
- [ ] A review date or trigger exists
- [ ] The client-side owner for any dependent decision is named
