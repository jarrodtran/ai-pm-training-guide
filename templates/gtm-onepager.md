# Go-to-Market One-Pager Template

Fill-in-the-blank template for the AIPM 520 GTM module (M6) and the STRAT 540 positioning & pricing modules (M2–M3). One page. The test of positioning is not whether it is true — it is whether a customer would repeat it unprompted (the repeat-test). Pricing aligns revenue with cost and value: price follows cost **and** value.

**Product / feature:** [NAME]
**Version / date:** [VERSION — DATE]

---

## 1. Who it's for

[THE TARGET CUSTOMER — THE PERSON WHO BUYS AND THE PERSON WHO USES, IF DIFFERENT. Name the segment and the job they are hiring the product for. If you cannot name the customer, you do not have a GTM.]

## 2. One-line positioning

> [ONE LINE A CUSTOMER WOULD REPEAT. "The fastest way to resolve a refund" beats "AI-powered refund agent." If the line needs a feature list to make sense, rewrite it.]

**Why now / why this product:** [THE WINDOW AND THE ADVANTAGE — data flywheel, proprietary data/integrations, workflow lock-in, or distribution. "We use the best model" is not a moat; model capability is rented, and everyone can rent it.]

## 3. Pricing logic

- **Cost profile (from `cost-model.md`):** cost per interaction = **$___**; heavy-usage monthly bill = **$___**
- **Pricing structure:** [SUBSCRIPTION / USAGE / HYBRID / OUTCOME] — chosen because [RATIONALE: price follows cost AND value]
  - Subscription: simple and predictable, but exposes you to heavy users — cost uncapped, price isn't.
  - Usage: matches cost, taxes adoption, surprises customers ("why did my bill triple?").
  - Hybrid (base tier + usage): the common answer; pushes complexity into billing.
  - Outcome pricing ("pay per resolution"): aligns incentives perfectly and concentrates risk on your quality — if you can't resolve, you don't get paid.
- **Bill-shock mitigation:** [WHICH SEGMENT GETS SURPRISED, AND WHAT SOFTENS IT — e.g. caps with alerts, tiered pricing, base-token bundles]
- **What it would take to move to outcome pricing:** [THE QUALITY AND MEASUREMENT PREREQUISITES — e.g. a success bar we can measure in the contract, per `sow.md`]
- **How the price gets tested:** [EXPERIMENT DESIGN, PER DATA 530 — pricing is a feature: it has users, a UX (the bill), and bugs (bill shock, churn)]

## 4. Three expected objections, with answers

| # | Objection | Answer |
|---|---|---|
| 1 | [THE MOST LIKELY OBJECTION — e.g. "how do we know it's right?"] | [THE ANSWER WITH THE EVIDENCE — e.g. eval scores, golden-set pass rate, human-in-the-loop on high stakes, source links on answers] |
| 2 | [OBJECTION 2 — e.g. "what happens when it fails?"] | [THE ANSWER — detection mechanisms, escalation path, rollback trigger] |
| 3 | [OBJECTION 3 — e.g. "why not just do it with people / rules?"] | [THE ANSWER — the comparative feasibility judgment, with the client's numbers] |

---

## Done when

- [ ] One target customer is named (buyer and user if different)
- [ ] The positioning line passes the repeat-test — a customer would say it unprompted
- [ ] The moat argument names a compounding asset, not a model
- [ ] Pricing logic references the cost model and names the structure's failure mode
- [ ] Bill-shock mitigation is stated
- [ ] Three objections are written with answers that cite evidence (evals, HITL, detection)
