# Pattern Ledger Template

Fill-in-the-blank template for Module 5 of the FDE-PM Field Manual (`../fde-pm-field-manual.md`). The ledger is the instrument that makes productization possible: it captures, during engagements, the requests and bespoke work that recur — so the "should this become product?" question is answered with evidence instead of memory. Reviewed monthly; every abstraction RFC and every documented "no" starts as a row here.

**Team / portfolio:** [NAME] · **Ledger owner:** [PM NAME] · **Last reviewed:** [DATE] · **Review cadence:** monthly + at each engagement close

---

## 1. Ledger

| ID | Pattern (plain language) | Instances (clients, builds) | Bespoke cost per instance (eng-days) | Core overlap % | Who asks for it | Signal test (F/C/W/D) | Status | Decision date | Owner |
|---|---|---|---|---|---|---|---|---|---|
| P-[NNN] | [e.g. policy answer + citation over client corpus] | [3 clients, 4 builds] | [~25] | [~70%] | [ops leads] | [✓✓✓✓] | [watching / RFC / shipped / declined] | [YYYY-MM-DD] | [NAME] |
| P-[NNN] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

**Signal test columns (all four must hold for a product candidate):**

- **F — Frequency:** recurs across ≥ 3 clients, or ≥ 3 times at one client
- **C — Cost:** bespoke delivery costs a meaningful number of engineering-days each instance
- **W — Willingness:** ≥ 2 clients would pay for a configured version
- **D — Differentiation:** close enough to our core to defend, not commodity glue anybody can buy

## 2. Status vocabulary (use these exact words)

| Status | Meaning | Next action |
|---|---|---|
| **Watching** | Seen once or twice; not yet a pattern | Re-check monthly; note the next occurrence |
| **RFC in progress** | Signal test passed; abstraction being written | [Owner] drafts the productization memo by [date] |
| **On core roadmap** | Accepted and slotted | Sized against platform capacity; committed date |
| **Shipped to core** | Built; golden path and exemplar updated | Migrate existing bespoke implementations |
| **Bespoke frozen** | Existing instances support-only; no new ones | Track instance count down to zero |
| **Declined** | Not worth productizing | Recorded permanently with reasoning — do not re-litigate |

## 3. Distance from core (portfolio view)

Score every live engagement monthly on a 1–5 scale: 1 = pure configuration of existing capabilities; 5 = new bespoke system. Then watch the distribution.

| Engagement | Score (1–5) | Main driver of the score | What would move it down one point |
|---|---|---|---|
| [CLIENT] | [ ] | [ ] | [ ] |
| [CLIENT] | [ ] | [ ] | [ ] |

**Interpretation:** a portfolio drifting toward 5 means the platform is not keeping up with sales promises; drifting toward 1 means the team is not learning anything new from the market. Neither extreme is healthy.

## 4. Health metrics (report quarterly, with guardrails)

| Metric | Definition | This quarter | Guardrail |
|---|---|---|---|
| Reuse rate | Share of engagement engineering work delivered from core capabilities | [__]% | Client satisfaction and quality scores must not fall |
| Time to first deploy | Days from engagement start to a working system in the client's environment | [__] days | Do not count "demo in our sandbox" |
| Bespoke instance count | Live bespoke implementations of each pattern | [__] | Must be trending down after a core ship |
| Support load per client | Support hours per client per month | [__] | Watch the tail, not the average |
| Harvest output | Abstraction RFCs written and declined-with-reason entries per quarter | [__] | Zero for two quarters means the ritual is not happening |

---

## Done when

- [ ] Every recurring request from the last two quarters has a row (reconstructed from memory is acceptable for the first pass, then maintained live)
- [ ] Each row has an owner and a decision date
- [ ] Signal-test columns are filled with evidence, not impressions
- [ ] Declines are recorded permanently with reasoning
- [ ] Distance-from-core scores exist for every live engagement
- [ ] The ledger has been reviewed in a harvest session within the last month
