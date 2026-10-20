# Solution Optimization for FinOps for GitHub Copilot

*A FinOps-aligned scope for AI credits, budgets, and reporting.*

This Value-Based Delivery (VBD) helps customers govern GitHub Copilot AI credit consumption, distinguish included credits from additional metered spend, and establish budget guardrails, cost attribution, and an operating cadence. It applies the FinOps Foundation's **FinOps for AI** technology category as a focused scope, not as a complete FinOps programme or a licence-management engagement.

Delivery progresses through three phases. Educate establishes shared vocabulary; Plan turns customer evidence into a co-authored governance blueprint; Implement applies the approved recommendations across the agreed organizations.

| Phase | Duration | Purpose and output |
| --- | --- | --- |
| Day 1 - Educate | 2 hours, including a 15-minute break | Understand AI credits, reporting, budget controls, scope boundaries, and minimum viable Start actions. |
| Day 2 - Plan | 2 hours 15 minutes, including a 10-minute break | Co-author the GitHub Copilot AI Credit Governance Blueprint, including a budget configuration matrix and implementation backlog. Educate is a prerequisite. |
| Day 3 -Implement | Multi-day engagement; duration agreed during scoping | Plan and apply approved governance practices, validate controls, and hand over operations. |

## Objectives and Outcomes

**Objectives**

- Establish a shared understanding of the FinOps capabilities relevant to Copilot AI credits, budgets, and reporting.
- Separate fair access to the included credit pool from governance of additional metered spend.
- Assess enterprise structure, attribution, consumption, controls, stakeholder accountability, and continuity risks.
- Design layered budgets, reporting, communication, exception handling, and evidence-based usage guidance.
- Prioritize and implement approved improvements without treating cost reduction as the only measure of success.

**Outcomes**

- A completed discovery questionnaire and an evidence-based current-state assessment, with known gaps recorded.
- A customer-owned governance blueprint with named decision makers, approvals, and support responsibilities.
- A scope-by-scope budget configuration matrix covering amounts, owners, alert recipients, inclusion decisions, and enforcement rationale.
- Universal, cost center, and individual user-level budget (ULB) profiles, with a provisional baselining path where necessary.
- A reporting data contract, attribution approach, stable value scorecard, and threshold-response runbook.
- A prioritized Start/Adopt/Advance backlog with owners, prerequisites, acceptance measures, and review dates.
- For an Implement engagement, a record of approved changes, validation results, and operational handover.

### In Scope / Out of Scope

**In scope**

- GitHub Copilot included AI credits and additional metered spend, with visibility into other eligible workloads consuming the shared pool.
- Data Ingestion, Allocation, Reporting & Analytics, Anomaly Management, Budgeting, Risk/Policy & Governance, FinOps Education & Enablement, and FinOps Practice Operations.
- Concept-level education on Planning & Estimating, Forecasting, KPI & Benchmarking, Unit Economics, Usage Optimization, and Invoicing & Chargeback; customer-specific planning within the agreed credit-governance scope.
- Copilot-scoped capability readiness, budget design, identity and cost center mapping, showback, and an operating model.
- Implementation of agreed controls and reporting improvements from the approved backlog.

**Out of scope**

- Non-GitHub Copilot AI spending, such as Azure OpenAI, other model vendors, or other GitHub SKUs.
- Architecting & Workload Placement, Rate Optimization, Sustainability, and training, inference, or GPU-efficiency optimization.
- Licensing & SaaS seat management, procurement, contract lifecycle, renewal negotiation, and application-portfolio rationalization.
- A full FinOps maturity assessment or implementation of a broader FinOps practice. The Plan assessment is limited to this Copilot scope.
- Technique-level prompt and model optimization training; this delivery names the levers and routes deeper enablement separately.
- FOCUS adoption, virtual-currency mapping, finance-system integrations, and custom automation unless separately scoped and approved as follow-on implementation work.
- ITAM, SAM, TBM, and Procurement alignment beyond identifying dependencies and routing actions to their owners.

## IP Kit

> [!TIP]
> The working IP kit is the [GitHub Copilot Cost Governance source repository][source-repository]. Use its README and workshop specifications for delivery preparation. Confirm access and the approved material version before sharing customer-facing artifacts.

| Artifact | Use |
| --- | --- |
| [VBD overview and phase definitions][source-readme] | Confirm purpose, scope, delivery phases, and foundational references. |
| [Educate agenda and capability coverage map][educate-agenda] | Prepare the 120-minute learning session and explain scope boundaries. |
| [Budget setup discovery questionnaire][questionnaire] | Issue after Educate; collect customer evidence before Plan. |
| [Plan agenda][plan-agenda] | Run the 135-minute working session and map activities to blueprint sections. |
| [Plan facilitator playbook][plan-playbook] | Apply readiness checks, timeboxes, contingency guidance, and follow-up actions. |
| [AI Credit Governance Blueprint template][blueprint] | Co-author the Plan deliverable live and maintain the implementation record. |

## 1 Prepare

Prepare the delivery team, confirm customer needs, and establish access to the evidence and decision makers needed for each phase. Keep Educate and Plan as separate events, with time between them for discovery homework and facilitator preparation.

### 1.1 Pre-Scope

Discuss customer needs with the account team before the customer scoping call. Refer to [Pre-Scoping Call with CSAM & CSA](https://aka.ms/VBDPre-scoping).

- :ballot_box_with_check: Align with the CSAM, CSA, Technical Specialist, and relevant GitHub account stakeholders on business drivers and expected outcomes.
- :ballot_box_with_check: Review previous delivery stages, Technical Blocker Mitigation findings, and any POC or Copilot adoption work already completed.
- :ballot_box_with_check: Confirm whether the request is education, governance planning, approved implementation, or a combination.
- :ballot_box_with_check: Identify current pain points: unpredictable metered spend, pool exhaustion, attribution gaps, blocked workflows, unclear ownership, or ineffective reporting.
- :ballot_box_with_check: Route licence rightsizing, procurement, developer-productivity assessment, and non-Copilot AI governance to the appropriate engagement.

### 1.2 Review Customer Information

Gather available enterprise and billing context without requiring customers to answer the detailed discovery questionnaire before they have attended Educate.

- :ballot_box_with_check: Confirm GitHub Enterprise Cloud and the customer's Copilot Business or Copilot Enterprise plan, enterprise structure, and participating organizations.
- :ballot_box_with_check: Identify enterprise owners, billing managers, finance or budget holders, engineering sponsors, and operational cost owners.
- :ballot_box_with_check: Review existing cost centers, cross-product chargeback arrangements, enterprise teams, identity mappings, and delegation requirements.
- :ballot_box_with_check: Establish access to billing settings and the AI usage report; capture current budgets, hard stops, and available history.
- :ballot_box_with_check: Identify high-consumption users, automated workflows, other shared-pool workloads, and business-continuity-sensitive use cases.

### 1.3 Scoping

Use [Scoping Call](https://aka.ms/VBDScoping) guidance to agree goals, timing, prerequisites, challenges, and deliverables. Refer to the [IP Kit](#ip-kit) for workshop materials.

- :ballot_box_with_check: Agree the participating enterprise and organizations, phase boundaries, success measures, and customer approval process.
- :ballot_box_with_check: Schedule Educate, a homework return date, Plan, and any separately scoped multi-day Implement work.
- :ballot_box_with_check: Confirm attendance and authority to recommend or approve budget amounts and changes.
- :ballot_box_with_check: Agree evidence-sharing arrangements and how unavailable data, access, or approvals will be tracked.
- :ballot_box_with_check: Establish that Plan produces recommendations; production configuration occurs only in the approved Implement scope.

<details>
<summary><b>Participants and readiness gates</b></summary>

| Customer role | Required contribution |
| --- | --- |
| Engineering or platform sponsor | Business outcomes, continuity-sensitive workflows, and decision criteria. |
| Enterprise owner or billing manager | Current controls, configuration access, budget recommendations, and change authority. |
| Finance representative or budget holder | Approved metered-spend envelope, showback or chargeback requirements, and approval decisions. |
| Cost owners and FinOps practitioners | Attribution, alerts, operating cadence, and exception handling. |
| Enterprise admin or identity/IdP owner | Enterprise structure, team membership, cost center assignment, and identity mapping. |
| Support and developer representatives | Communication, self-service visibility, blocked-user support, and practical usage guidance. |

**Before Educate:** send the reading prework from the Educate slide specification: Managing AI credits, Budgets for usage-based billing, and FinOps for AI. Ask attendees to identify who holds enterprise owner or billing manager access and whether cost centers already serve other products. Review speaker notes, personalize provider details, and rehearse demonstrations in a suitable non-production environment.

**Before confirming Plan:** verify that these attendees completed Educate; the questionnaire has been returned and reviewed; an enterprise owner or billing manager, or an agreed proxy, will attend; finance representation or a written approved envelope is available; and blueprint sections 2 and 3 are pre-populated or their evidence gaps are understood.

If homework is missing, mostly blank, or based on guesses, book a separate **60-90 minute discovery fill-in session** before Plan. Work questionnaire sections A, D, C, then B, and assign unresolved questions to owners with due dates. Do not absorb this work into the 135-minute Plan session.

Unavailable historical usage is not a blocker: agree the provisional baselining path. If the room cannot approve amounts, explicitly frame the configuration matrix as a recommendation awaiting approval rather than an approved decision.

</details>

## 2 Deliver Solution Optimization

Use Educate to establish understanding, Plan to make and document decisions, and Implement to apply approved changes. The blueprint remains the single Plan deliverable; every module contributes to it.

### 2.1 Kickoff

Begin with [Actual Delivery: Kick-off meeting](https://aka.ms/VBDKickoff) guidance.

- :ballot_box_with_check: Confirm customer priorities, delivery scope, phase timings, participant roles, and success measures.
- :ballot_box_with_check: Restate the boundary: Copilot AI credits, budgets, and reporting, not a complete FinOps programme.
- :ballot_box_with_check: Explain that included-pool access and metered-spend governance require different controls.
- :ballot_box_with_check: Confirm that production changes require the customer's agreed approvals and implementation scope.
- :ballot_box_with_check: Introduce the questionnaire handoff, live blueprint, decision log, and customer ownership of follow-up actions.

<details>
<summary><b>Educate run-of-show: 120 minutes</b></summary>

Use the [Educate agenda][educate-agenda] and [slide content with speaker notes][educate-slides]. Retain the scheduled break before the most demanding budget module.

| Time | Module | Delivery focus |
| --- | --- | --- |
| 0-5 min | Opening | Set expectations and surface participant priorities. |
| 5-12 min | Why Copilot needs a FinOps lens | Explain pooled consumption, variable demand, and why credit governance differs from licensing. |
| 12-21 min | FinOps fundamentals | Introduce principles, personas, scopes, Inform/Optimize/Operate, and the four capability domains. |
| 21-33 min | Copilot scope and capability map | Distinguish deep coverage, awareness topics, and excluded capabilities with their destinations. |
| 33-44 min | How AI credits work | Explain included credits, subsequent metered spend, model and context consumption, and shared-pool workloads. |
| 44-55 min | Inform: visibility and attribution | Demonstrate reporting access, identity enrichment, attribution, and the separation from feature-adoption metrics. |
| 55-70 min | Break | Post the return time and protect the budget-strategy timebox. |
| 70-84 min | Budget strategy | Explain ULB precedence, concurrent controls, alerting, and continuity-aware enforcement. |
| 84-92 min | Optimize | Name model, context, retry, and automated-session levers; route technique-level enablement separately. |
| 92-102 min | Value and ROI | Establish defensible measures and baselines without claiming causation or proven ROI. |
| 102-112 min | Operate | Define roles, review cadence, alerts, and response ownership. |
| 112-120 min | Wrap-up and action plan | Identify minimum viable Start actions and issue the discovery homework. |

At the close, send the [questionnaire][questionnaire] the same day, name one customer owner to collate answers, and agree a return date that leaves preparation time before Plan. Explain that honest unknowns are preferable to guesses.

</details>

### 2.2 Assess / Review

Prepare blueprint **section 2, Readiness and evidence**, and **section 3, Consumption baseline**, from available billing settings, identity mappings, usage reports, and returned homework. Plan validates evidence rather than extracting raw data live.

- :ballot_box_with_check: Review questionnaire A for goals, D for structure, C for consumption, and B for accountability; resolve accountability in the target-governance module.
- :ballot_box_with_check: Establish pool size, consumption profiles and percentiles, exhaustion timing, current controls, unmapped users, and continuity-sensitive workflows.
- :ballot_box_with_check: Validate identity-to-business-unit mapping and existing cost center constraints before proposing attribution or chargeback.
- :ballot_box_with_check: Assess Copilot-scoped readiness by capability rather than assigning one global FinOps maturity score.
- :ballot_box_with_check: Record evidence gaps and the top continuity, financial, and attribution risks with named owners and due dates.

<details>
<summary><b>Evidence and reporting considerations</b></summary>

- The Billing and licensing AI usage dashboard provides interactive visibility and UI downloads covering up to **31 days**. The Educate specification identifies the Billing API as a separate access path for AI credit usage reports covering up to the past **24 months**. Confirm current availability and customer permissions before relying on either path.
- Usage data is not real time and can take up to **two days** to surface. Record this latency in the reporting operating model.
- Preserve per-user, per-model, and per-day usage, including `quantity`, `gross_amount`, `discount_amount`, and `net_amount`. Enrich billing data with identity, organizational, cost center, and workload context.
- Keep billing and credit consumption distinct from Copilot feature-adoption metrics; they answer different questions.
- Do not attribute all shared-pool depletion to interactive Copilot users. Eligible GitHub AI workloads, including Code Quality and cloud agents, can also consume the pool.
- A user's usage is attributed to one cost center. Direct assignment takes priority; otherwise, the oldest applicable enterprise team by creation date determines attribution.
- Where existing cost centers already serve chargeback for other products or SKUs, do not design a second AI-credit-only set. Reuse a suitable existing structure or use ULBs and track mapping improvements.
- If no consumption baseline exists, explicitly mark it unavailable and select a deliberately permissive provisional universal ULB with alert-only metered budgets for **one or two billing cycles**, followed by an owned review.

</details>

### 2.3 Prep and Plan configuration

Run Plan as a **135-minute facilitated decision meeting**, not a repeat of Educate. Keep the questionnaire and [blueprint][blueprint] open on screen, type decisions as participants make them, and use the [facilitator playbook][plan-playbook] to protect timeboxes.

- :ballot_box_with_check: Confirm business outcomes, decision criteria, and out-of-scope routing before discussing configuration.
- :ballot_box_with_check: Assign named owners, budget-change authority, temporary ULB override approvals, communication, and blocked-user support.
- :ballot_box_with_check: Complete every applicable budget matrix row with amount, owner, recipients, enforcement choice, and rationale.
- :ballot_box_with_check: Define attribution, a stable scorecard, threshold responses, and daily/weekly/monthly/quarterly operating responsibilities.
- :ballot_box_with_check: Sequence the Start/Adopt/Advance backlog, close open decisions with owners and dates, and book the first weekly review.

<details>
<summary><b>Plan run-of-show and budget-design guardrails</b></summary>

| Time | Module | Blueprint sections and required output |
| --- | --- | --- |
| 0-10 min | Opening and outcome alignment | 1: scope and decision criteria; 13: routing; open 8: decision log. |
| 10-40 min | Discovery and current state | 2: readiness; 3: baseline; confirm 1 against homework and evidence. |
| 40-60 min | Target governance and communication | 4: named responsibilities and approvals; 5: communication, support, and exceptions. |
| 60-70 min | Break | Protect the break before budget design. |
| 70-100 min | Layered budget and usage-guidance design | 6: configuration matrix; 7: ULB profiles; 8: decisions and assumptions. |
| 100-120 min | Reporting, value, and operations | 9: reporting data contract; 10: scorecard baseline; 11: threshold-response runbook. |
| 120-135 min | Recommendation and commitments | 12: Start/Adopt/Advance backlog; 13: routing; close 8 with owners and dates. |

**Budget-design guardrails**

1. Treat applicable user, cost center, organization, and enterprise controls as concurrent guardrails, not a top-down allocation tree.
2. ULB precedence is **individual, then cost center, then universal**. The applicable ULB is a per-user hard cap across included and metered consumption; another budget cannot extend it.
3. Distinguish a cost center ULB, which caps each member, from a cost center metered budget, which caps the group's additional charges. An optional cost center included-usage control limits consumption of the shared pool.
4. Metered cost center, organization, and enterprise budgets block usage only when **Stop usage when budget limit is reached** is enabled. Among applicable ULB and enforced limits, the control with the lowest remaining headroom blocks first.
5. Size the enterprise metered budget to the approved envelope, enable **75%, 90%, and 100% alerts**, name recipients, and keep the **enterprise hard stop disabled** to protect continuity.
6. Evaluate lower-scope hard stops against developer and automated-workflow interruption risk. Keep metered budgets alert-only during provisional baselining.
7. Record the enterprise-wide cost center include/exclude toggle explicitly. By default, cost center metered usage also counts against the enterprise budget; exclusion delegates spending authority to cost center budgets and applicable ULBs. Do not describe the toggle as a separate choice for each cost center.
8. Size ULBs from observed profiles, including legitimate power users and metered work. Document time-bound individual overrides, approval authority, expiry, and review.
9. Communicate thresholds and enforcement before rollout. Define how blocked users identify the responsible scope and request help; code completion and next edit suggestions remain available at a ULB cap.
10. Name usage levers such as auto model selection, task-to-model matching, context and retry reduction, and `--max-ai-credits` for automated CLI/SDK sessions, without turning this session into optimization-technique training.

**Protect the deliverable:** the configuration matrix in section 6 must finish. When running late, reduce assessment depth or scorecard detail rather than sacrificing it. Unresolved decisions become `TBD` plus an owner and due date in section 8; recommendations awaiting approval must be labelled as such, not presented as approved settings.

**Reporting and value:** define showback before chargeback where attribution is unproven. Choose at least one business and one technical outcome, observe them alongside credit usage and adoption, and lock definitions, population, and measurement method for one year. Separate licence cost from credit cost and avoid claiming that Copilot caused every observed change.

**Operating cadence:** daily alert and anomaly review; weekly rollout reporting; monthly budgets and pool-exhaustion review; quarterly rightsizing and policy review. For 75%, 90%, and 100%, document the notified owner, action, approval authority, and conditions for optimizing, restricting, increasing a budget, or accepting interruption risk.

</details>

### 2.4 Configure

Use the approved blueprint to scope and execute the multi-day Implement phase. The source defines its purpose but does not prescribe a fixed duration or detailed run-of-show; agree both with the customer before production work.

- :ballot_box_with_check: Confirm approvals, configuration access, dependencies, change windows, and recovery steps for each implementation item.
- :ballot_box_with_check: Apply approved budget amounts, alert recipients, ULB profiles, included-usage controls, and the enterprise cost center inclusion setting.
- :ballot_box_with_check: Preserve the enterprise alert-only guardrail and implement lower-scope enforcement only where its risk and rationale are approved.
- :ballot_box_with_check: Establish the agreed reporting and identity-enrichment process, publish usage guidance, and activate support and exception handling.
- :ballot_box_with_check: Validate the applied configuration and operational responses, record evidence, and hand over ownership and outstanding actions.

<details>
<summary><b>Implementation sequence and acceptance checks</b></summary>

| Stage | Implementation focus | Acceptance evidence |
| --- | --- | --- |
| Start | Alert-only enterprise budget, named owners, showback evidence, advance communication, and evidence-based or provisional universal ULB. | Settings match approved matrix rows; recipients and responsibilities are confirmed; reporting and support paths work; baseline review is scheduled. |
| Adopt | Suitable cost center or organization controls, profile-based ULBs, chargeback where attribution is proven, and stable usage guidance and cadence. | Assignments and ULB precedence are checked; approved exceptions and expiry are recorded; attribution reconciles with billing; enforcement risks are acknowledged. |
| Advance | Separately approved API automation and forecasting based on observed trends. | Data access and history are verified; latency and reporting definitions are documented; automation and forecasts meet the agreed backlog acceptance measures. |

Validate configuration against the approved matrix, including amounts, scopes, ULB precedence, alert recipients, hard-stop settings, and the enterprise-wide inclusion toggle. Use safe demonstrations or tabletop walkthroughs for threshold and blocked-user responses; do not exhaust a production budget merely to prove enforcement.

For each implemented item, capture before/after settings, approval, validation results, operational owner, and recovery steps. Distinguish implemented controls from recommendations, provisional settings, and work awaiting approval. If validation fails, record the failure, notify the responsible owner, and resolve it or retain it as an explicit open action.

</details>

## 3 Closeout and next steps

A closeout report is required to document the delivery, recommendations, and any implemented changes. Follow [Actual Delivery: Report Deliverable](https://aka.ms/VBDReporting).

### 3.1 Closeout delivery

Hold a short feedback and handover session. Use the agreed closeout template and the [IP Kit](#ip-kit) artifacts to review outcomes.

- Send the completed blueprint within **one working day** of Plan and send section 8 decision-log actions directly to their named owners.
- Summarize the phases delivered, evidence reviewed, approved recommendations, actual changes, validation results, and unresolved risks.
- Escalate unresolved budget amounts or approvals to the enterprise owner; do not imply an unsized or unapproved recommendation is an implemented guardrail.
- Confirm ownership of reporting, alerts, exceptions, support, and the first weekly review.
- For provisional baselining, confirm the one-to-two-cycle collection window, review date, and owner before tightening controls.
- Route section 13 items to their owning teams and collect customer feedback on readiness, value, and next steps.

### 3.2 Next Best Actions

- **After Educate:** return the discovery questionnaire and complete the Plan readiness check.
- **After Plan:** approve the configuration matrix and prioritize the Start implementation backlog.
- **After Start:** review observed consumption and attribution before moving to profile-based controls or chargeback in Adopt.
- **After Adopt:** consider separately scoped automation, forecasting, and optimization enablement in Advance.
- Route broader licence, procurement, developer-productivity, and FinOps requests to their owning teams or follow-on engagements.

[!INCLUDE[Closeout Next Best Actions](../../../CommonContent/closeout_next_best_actions.md)]

[!INCLUDE[Closeout Recommended Steps](../../../CommonContent/closeout_recommended_steps.md)]

#### Closeout Resources

[!INCLUDE[Closeout Resources](../../../CommonContent/closeout_resources.md)]

Engage in follow-up conversations with the delivery lead or CSA to confirm opportunities and recommendations. Follow [Post Delivery Activities](https://aka.ms/VBDPost-Delivery), finalize the agreed implementation roadmap, and send the delivery documents to the customer.

## Other resources, readiness and references

- [GitHub Well-Architected: Managing AI credits](https://learn.github.com/well-architected/governance/recommendations/managing-ai-credits)
- [FinOps Foundation: FinOps for AI](https://www.finops.org/framework/technology-categories/ai/)
- [FinOps Foundation: FinOps for SaaS](https://www.finops.org/framework/technology-categories/saas/)
- [Microsoft FinOps Framework overview](https://learn.microsoft.com/en-us/cloud-computing/finops/framework/finops-framework)
- [GitHub Docs: Budgets for usage-based billing](https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/billing/budgets-for-usage-based-billing)
- [GitHub Docs: AI usage report](https://docs.github.com/billing/reference/billing-reports#ai-usage-report)
- [GitHub Docs: Optimizing your budget configuration](https://docs.github.com/en/copilot/tutorials/budgets/optimizing-your-budget-configuration)
- [GitHub Docs: Control costs at scale](https://docs.github.com/en/billing/tutorials/control-costs-at-scale)
- [GitHub Docs: Auto model selection](https://docs.github.com/copilot/concepts/models/auto-model-selection)
- [GitHub Docs: Models and pricing](https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing)
- [GitHub Support: Understanding Copilot budgeting](https://support.github.com/product-guides/github-copilot/get-started/understanding-copilot-budgeting)

FinOps capability names and scope framing are adapted from the FinOps Foundation Framework, licensed [CC BY 4.0](https://www.finops.org/introduction/how-to-use/).

## Known issues and updates

- Billing features, model pricing, reporting access, and enforcement behaviour can change. Verify current GitHub documentation and tenant availability before delivery; do not hard-code prices or allowances into customer recommendations.
- The Educate specification distinguishes 31-day UI downloads from up-to-24-month Billing API history. The Plan playbook and blueprint readiness checklist emphasize the 31-day CSV path; make the chosen access path explicit rather than treating all reporting history as limited to 31 days.
- Missing discovery homework requires the separate fill-in session, not an expanded Plan timebox. Evidence gaps remain owned actions, not guessed answers.
- Existing cross-product cost centers and one-cost-center attribution constrain design. Validate assignments before introducing chargeback or enforcing profile-based limits.
- No fixed Implement agenda is supplied in the workshop specifications. Agree implementation scope, duration, approvals, and acceptance criteria explicitly.
- Record source-material corrections and recurring questionnaire gaps in the [source repository][source-repository] so future deliveries use consistent guidance.

[source-repository]: https://github.com/customer-success-microsoft/vbd-github-copilot-cost-goverance
[source-readme]: https://github.com/customer-success-microsoft/vbd-github-copilot-cost-goverance/blob/main/README.md
[educate-agenda]: https://github.com/customer-success-microsoft/vbd-github-copilot-cost-goverance/blob/main/specs/github-copilot-cost-governance-educate-agenda.md
[educate-slides]: https://github.com/customer-success-microsoft/vbd-github-copilot-cost-goverance/blob/main/specs/github-copilot-cost-governance-educate-slides.md
[educate-styled]: https://github.com/customer-success-microsoft/vbd-github-copilot-cost-goverance/blob/main/specs/github-copilot-cost-governance-educate-slides-styled.md
[questionnaire]: https://github.com/customer-success-microsoft/vbd-github-copilot-cost-goverance/blob/main/templates/copilot-budget-discovery-questionnaire.md
[plan-agenda]: https://github.com/customer-success-microsoft/vbd-github-copilot-cost-goverance/blob/main/specs/github-copilot-cost-governance-plan-agenda.md
[plan-playbook]: https://github.com/customer-success-microsoft/vbd-github-copilot-cost-goverance/blob/main/specs/github-copilot-cost-governance-plan-facilitator-playbook.md
[blueprint]: https://github.com/customer-success-microsoft/vbd-github-copilot-cost-goverance/blob/main/templates/copilot-ai-credit-governance-blueprint.md