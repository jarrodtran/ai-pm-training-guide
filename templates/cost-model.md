# Cost Model Template

Fill-in-the-blank template for the AIPM 520 cost & latency module (M5) and the STRAT 540 unit-economics model (M1). AI breaks the software assumption that marginal cost is ~zero: every interaction burns tokens, and your bill scales with success. The discipline: **tokens × price = cost**, numbers traceable to current pricing pages, and sensitivity before launch.

**Product / feature:** [NAME]
**Date of pricing snapshot:** [DATE — MODEL PRICES CHANGE; EVERY NUMBER MUST BE TRACEABLE TO A PRICING PAGE DATED HERE]

---

## 1. Tokens per Action

Measure or estimate tokens in / tokens out for each action the system performs. Log them in production (DATA 530: model version and tokens are properties on every event) — estimates are the starting point, logs are the truth.

| Action | Tokens in | Tokens out | Notes (retrieval chunks, tool calls, caching) |
|---|---|---|---|
| [e.g. answer a support query] | [___ TOKENS] | [___ TOKENS] | [e.g. 3 chunks retrieved; system prompt ___ tokens; cacheable: yes/no] |
| [ACTION 2] | [___ TOKENS] | [___ TOKENS] | [NOTES] |
| [ACTION 3] | [___ TOKENS] | [___ TOKENS] | [NOTES] |

## 2. Price per Token

| Model tier | Model | Input price per 1M tokens | Output price per 1M tokens | Pricing source (URL + date) |
|---|---|---|---|---|
| [FRONTIER — e.g. current flagship] | [MODEL NAME] | [$___] | [$___] | [PRICING PAGE, DATE] |
| [MID — e.g. current workhorse] | [MODEL NAME] | [$___] | [$___] | [PRICING PAGE, DATE] |
| [SMALL / CHEAP — e.g. current small model] | [MODEL NAME] | [$___] | [$___] | [PRICING PAGE, DATE] |

## 3. Cost per Interaction

**Formula:** cost per interaction = (tokens in × input price) + (tokens out × output price) + retrieval/storage per interaction.

| Action | Math (show it) | Cost per interaction |
|---|---|---|
| [ACTION] | [e.g. 2,000 in × $___/1M + 400 out × $___/1M + $___ retrieval] | [$___] |
| [ACTION] | [MATH] | [$___] |

- **Cost per customer per month:** [INTERACTIONS PER CUSTOMER PER MONTH] × [COST PER INTERACTION] = **$___**
- **The two biggest cost levers in this design** (cost is a design variable, not an afterthought): (1) [LEVER — e.g. context length / prompt size], (2) [LEVER — e.g. model tier on routine calls], and what each would trade away: [TRADE-OFFS]

## 4. Monthly Bill at 3 Usage Scenarios

| Scenario | Users | Interactions / user / month | Cost / interaction | Monthly bill |
|---|---|---|---|---|
| Light (launch) | [___ USERS] | [___] | [$___] | [___ USERS × ___ × $___ = **$___**] |
| Base (plan) | [___ USERS] | [___] | [$___] | **$___** |
| Heavy (success — budget for your own success before you launch) | [___ USERS] | [___] | [$___] | **$___** |

The Duolingo lesson: AI features can work and still compress margins because compute scales with success. If the bill at the heavy scenario is uncomfortable, that is a product-strategy problem to solve now — model tiering, caching, and packaging that aligns revenue with compute — not an optimization to defer.

## 5. Model Comparison (on YOUR eval set, not the leaderboard)

Run the golden set (`eval-suite.md`) on each tier and record the result. The professional move is finding where the cheap model is good enough — using your eval set.

| Tier | Cost per interaction | Latency (p95) | Quality (golden-set pass rate) | Notes / verdict |
|---|---|---|---|---|
| [FRONTIER] | [$___] | [___ MS] | [___%] | [WHERE IT EARNS THE PREMIUM, OR WHERE IT DOESN'T] |
| [MID] | [$___] | [___ MS] | [___%] | [NOTES] |
| [SMALL / CHEAP] | [$___] | [___ MS] | [___%] | [WHERE IT IS GOOD ENOUGH, WHERE IT ISN'T] |

**Latency budget:** [___ MS P95, SET BEFORE CHOOSING THE MODEL] — latency is a product constraint, not an engineering detail.

## 6. Sensitivity

Run the sensitivity before launch, not after.

- **If usage doubles:** monthly bill goes from $___ to **$___** at the [SCENARIO] scenario — [IS THE MARGIN STRUCTURE OK, OR DOES THE PRICE NEED TO SCALE WITH USAGE?]
- **If output tokens grow 1.5×** (longer answers, more verbose model): cost per interaction goes from $___ to **$___**
- **If we switch to model Y:** we save $___ but accept [QUALITY / LATENCY TRADE-OFF, MEASURED ON THE GOLDEN SET]
- **If average conversation length grows to [N] turns:** the bill does [___] — show the curve or the number
- **If the model vendor raises prices 3×** (STRAT 540 M4): the bill does [___]; the multi-model option requires [WHAT THE EVAL SUITE WOULD HAVE TO SHOW BEFORE SWITCHING]

---

## Done when

- [ ] Tokens in/out are logged or estimated per action, with notes on caching and retrieval
- [ ] Prices are filled from a dated pricing page (traceable numbers — "opinion without math" is a C)
- [ ] Cost per interaction shows the math, not just the answer
- [ ] Monthly bill is computed at 3 scenarios, including the heavy/success scenario
- [ ] Model comparison ran the golden set on 2–3 tiers; recommendation names the trade-off
- [ ] Sensitivity covers: usage doubles, a model switch, and the vendor price hike
