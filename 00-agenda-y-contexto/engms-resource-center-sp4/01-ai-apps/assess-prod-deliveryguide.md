# Production Readiness Assessment

This guide provides a step-by-step delivery framework for executing the Production Readiness Assessment for AI use cases. It is designed to ensure consistency, clarity, and impact across all customer engagements.
This guide is aligned to this VBD. The automated Assessment Engine and the customer knowledge bank branching model live in this VBD. The upskilling curriculum (optional) also lives there, which can be delivered in an additional 1 day SKU of this VBD - see [Upskilling (Optional)](#upskilling-optional). See the [README](https://github.com/customer-success-microsoft/Production-Readiness-Workshop/blob/main/README.md) for the tooling overview.

## Production Readiness Assessment Agenda Overview
| Agenda Item | Who | Outcome |
|-------------|-----|---------|
| Welcome & Objectives | Cloud & AI CSA | Ensure all participants understand the session's goals and objectives, agenda, and desired outcomes for the assessment components. |
| Architecture Deep Dive | Cloud & AI CSA + Customer SMEs + other Cloud & AI CSAs on a needed basis | Identify gaps and improvement areas. This activity centers on a thorough assessment of the customer's current architecture, with the aim of identifying opportunities for improvement that will facilitate the transformation of their proof of concept (POC) into a production-ready solution. The analysis is guided by best practices, targeted use case objectives, and the alignment of key performance indicators (KPIs) to ensure successful outcomes. |

## Delivery Options

This VBD can be delivered as a one-day or a three-day dispatch. The agenda is exactly the same for both options; only the staffing differs.

| Block | Duration | Note |
|-------|----------|------|
| Scoping session | 1 hour | Held on a separate day, before the assessment day. |
| Production readiness assessment | 5 hours | |
| Post-assessment work | 2 hours | Includes creating the implementation plan. |

**Staffing**:

| Option | CSAs | Staffing |
|--------|:----:|----------|
| One day | 1 | One CSA. It is recommended to deliver with additional CSAs. |
| Three days | 3 | The primary is an AI Apps CSA or a cross-solution CSA, supported by two CSAs from Infra, Data, Copilot, or Security as needed, so that the different pillars are covered. |

The delivery guide is organized into 3 core phases, with optional upskilling between scoping and the assessment:

| Phases | Description | Assets |
|--------|-------------|--------|
| Phase 1: Scoping | **Use Case Scoping Session:** Understand the use case, technical maturity, and production goals. | [Scoping Template](https://aka.ms/FY27PathToProduction) |
| Upskilling (Optional) | **If this is requested, an additional 1 day instance of AI Production readiness assessment can be dispatched ** Upskill stakeholders and align on architecture and governance using the 6-topic curriculum, delivered either through a separate upskilling VBD dispatch or by sharing the webinars with the customer. Recommended prior to starting the assessment. | [Upskilling Assets](https://aka.ms/FY27PathToProduction) |
| Phase 2: Production Readiness Assessment | Recap use case understanding and existing technical architecture. Identify the gaps for a production-ready architecture.| [Production Readiness Assessment](https://aka.ms/P2PAgent) |
| Phase 3: Closeout | Deliver the implementation plan and confirm next steps. | [Implementation Plan](https://aka.ms/P2PAgent) |


## Overall Outcomes

- **Enhanced Use Case Understanding:** The engagement provided a deep understanding of the customer's AI use case, production goals, and technical readiness.
- **Stakeholder Upskilling (Optional):** Where upskilling was delivered through the webinars, stakeholders were upskilled on foundational AI concepts and production readiness best practices, ensuring alignment on key terminology, concepts, operations, and governance.
- **Identification of Gaps:** Architectural gaps, operational risks, and platform limitations were identified through the production readiness assessment.
- **Clear Implementation Roadmap:** A clear, actionable implementation roadmap was delivered, with assigned ownership and next steps.
- **Continued Momentum:** Ensured continuity and momentum towards production deployment with a tangible artifact to align internal teams and secure executive sponsorship.
- **Compounding Knowledge Bank:** Every engagement is captured on its own `industry/*` branch so patterns, architectures, and lessons learned accumulate across customers.


## Phase 1: Scoping

This first phase lays the foundation for the Production Readiness Assessment by engaging stakeholders to clarify objectives, understand the customer's prioritized use case, and gather key details that shape the assessment. Through focused scoping and discovery, the delivery team and customer align goals and, optionally, select relevant upskilling topics, ensuring a targeted and purposeful engagement.

### Use Case Scoping Session (Customer engagement)

**Objective**:
- The Scoping Call is a structured discovery session to align with the customer on their AI use case, production goals, and technical readiness. The Cloud & AI CSA uses this session to:
    - Understand the **business objective** and **success criteria**
    - Assess the **technical maturity** (AI Landing Zone, model usage, team skills)
    - Identify **integration needs**, **compliance constraints**, and **architecture gaps**
    - Confirm **stakeholder availability** and **platform access**
    - Identify participants for the **Production Readiness Assessment** and for **Upskilling Sessions (Optional)**
    - Capture all inputs using the official Scoping Call template - [Scoping Template](https://aka.ms/FY27PathToProduction)

**Cloud & AI CSA Responsibilities**:

| Task | Description |
|------|-------------|
| Schedule the Call | Scoping session with all relevant stakeholders (IT, Business, Domain Experts, Security, Platform). |
| Lead the Scoping Session | Use the Scoping Call template to guide the conversation. Ask all key questions (e.g., objective, success criteria, timeline, model, AI LZ, skills, volumetrics, constraints, integrations, stakeholder availability). |
| Capture Architecture Snapshot | Document the technical details of the current architecture, including data flow, model integration, and platform components. |
| Confirm Assessment Day Participants / Customer Stakeholders | Identify who will attend the assessment and their roles. |
| Identify Upskilling Participants (Optional) | If the customer wants upskilling, confirm which stakeholders should attend. Upskilling is not included as part of this dispatch - deliver it through a separate upskilling VBD dispatch or by sharing the webinars with the customer. |
| Select the Upskilling Sessions with Customer (Optional) | Upskilling is not included as part of this dispatch. If the customer wants it, identify the relevant upskilling sessions across these six topics, to be delivered through a separate upskilling VBD dispatch or through the webinars: <br> &bull; Topic 1 - AI CoE and Governance, <br> &bull; Topic 2 - AI Landing Zones, <br> &bull; Topic 3 - Agent Architectures, <br> &bull; Topic 4 - AgentOps, <br> &bull; Topic 5 - AI Security and Observability, <br> &bull; Topic 6 - Solution Optimisation. |
| Schedule a session for the Production Readiness Assessment | Conduct the production readiness assessment described here - [Production Readiness Assessment](https://aka.ms/P2PAgent) |

-----

**Cloud & AI CSA Checklist – 1.1 Scoping Call**:
- :ballot_box_with_check: Schedule scoping call with all relevant stakeholders 
- :ballot_box_with_check: Use the official Scoping Call PPT template 
- :ballot_box_with_check: Ask discovery questions from the template 
- :ballot_box_with_check: Document business goals, success criteria, and timeline 
- :ballot_box_with_check: Assess AI Landing Zone, model usage, and team skills 
- :ballot_box_with_check: Capture volumetrics, constraints, and integration needs 
- :ballot_box_with_check: Confirm stakeholder availability and platform access 
- :ballot_box_with_check: (Optional) Present the available upskilling topic sessions and shortlist the sessions of interest - upskilling is not included as part of this dispatch
- :ballot_box_with_check: Identify stakeholders for the production readiness assessment and, optionally, for upskilling sessions
- :ballot_box_with_check: Schedule a production readiness assessment session with identified stakeholders
- :ballot_box_with_check: Complete and save template

---
## Upskilling (Optional)

> **Upskilling is optional. To deliver it, an additional 1 day SKU can be dispatched for this VBD deliver the content as necessary, or share the webinars with the customer. The upskilling sessions cover the same topics that are covered in the production readiness assessment, so it is recommended to deliver the upskilling VBD or the webinars to the customer prior to starting the assessment.

**Objective**:
The upskilling sessions upskill the customer's technical and business stakeholders on foundational AI concepts and production readiness best practices. These sessions align the customer on key terminology, concepts, operations, and governance before the production readiness assessment. They:
- Establish a shared understanding of AI production principles
- Surface early blockers or misconceptions
- Align teams on roles, responsibilities, and platform readiness

All decks are authored from the specs in `specs/` and cover the Microsoft AI stack: **Foundry**, **Copilot Studio**, **M365**, **Agent 365**, with integration coverage for **Work IQ**, **Fabric IQ**, and **Foundry IQ**.

**The 6 Pillars of Production Readiness**

The following six topics represent the foundational pillars for achieving production readiness in AI initiatives. These topics guide the customer's upskilling journey and are the same topics covered in the production readiness assessment.

**Upskilling Session Topics (Optional - Chosen by Customer during Scoping Session)**:

| # | Session Name | Description | Spec | Slides |
|:-:|--------------|-------------|------|--------|
| 1 | AI CoE and Governance | Responsible AI, organizational structure, operating models, and policy frameworks for AI adoption. | [Spec](https://github.com/customer-success-microsoft/Production-Readiness-Workshop/blob/main/specs/01-ai-coe-governance.md) | [Slides](https://aka.ms/FY27PathToProduction) |
| 2 | AI Landing Zones | Platform readiness, infrastructure, networking, and identity for AI workloads. | [Spec](https://github.com/customer-success-microsoft/Production-Readiness-Workshop/blob/main/specs/02-ai-landing-zones.md) | [Slides](https://aka.ms/FY27PathToProduction) |
| 3 | Agent Architectures | Usage, agentic, platform, integration, and governance layers; multi-agent orchestration on Foundry and Copilot Studio. | [Spec](https://github.com/customer-success-microsoft/Production-Readiness-Workshop/blob/main/specs/03-agent-architectures.md) | [Slides](https://aka.ms/FY27PathToProduction) |
| 4 | AgentOps | Evaluation, release gates, CI/CD for agents, observability, and Day-2 ownership. | [Spec](https://github.com/customer-success-microsoft/Production-Readiness-Workshop/blob/main/specs/04-agentops.md) | [Slides](https://aka.ms/FY27PathToProduction) |
| 5 | AI Security and Observability | Threat models, Zero Trust, Responsible AI, identity and data protection, runtime guardrails, and continuous red teaming. | [Spec](https://github.com/customer-success-microsoft/Production-Readiness-Workshop/blob/main/specs/05-ai-security-observability.md) | [Slides](https://aka.ms/FY27PathToProduction) |
| 6 | Solution Optimisation | Cost, latency, quality, scale, and governance; the five-layer optimisation model, routing, RAG quality, and FinOps. | [Spec](https://github.com/customer-success-microsoft/Production-Readiness-Workshop/blob/main/specs/06-solution-optimisation.md) | [Slides](https://aka.ms/FY27PathToProduction) |

### Topic 1: AI CoE and Governance

- **AI Strategy Overview:** Identifying AI use cases, defining a robust AI technology strategy, and adhering to responsible AI principles, anchored by an AI Center of Excellence (AI CoE) that aligns initiatives with business objectives.
- **Business Strategy for the AI CoE:** Qualification and classification, idea generation, portfolio prioritization, development and assessment, planning, tracking, and deployment. Emphasizes upskilling top talent to become self-sustainable.
- **Cultural Aspects of the AI CoE:** Strategy, architecture, roadmap, and culture. Integrates AI responsibility and education into the fabric of the organization.
- **AI Governance & Structure:** Governance framework covering project status, issue escalation, strategy recommendations, and AI priorities aligned with business strategy and responsible AI practices.
- **Technology Strategy:** Security, management, AI platform, data platform, app platform, and infrastructure, including securing AI resources and ensuring compliance with data security standards.
- **Key Success Factors:** ROI from AI projects, increased business value, number of AI use cases, integration with existing business, AI skill and proficiency, adoption of AI ethics policies, and automation.

### Topic 2: AI Landing Zones

- **CAF & ALZ:** The Cloud Adoption Framework (CAF) provides a full-lifecycle framework for cloud adoption on Azure. Azure Landing Zones (ALZ) are opinionated reference architectures for deploying platform landing zones using CAF best practices and first-party services.
- **Tenant, Subscription & Resource Architecture:** Strategic design path and target technical state for Azure environments, including number of subscriptions, management groups, policy assignments, network connectivity, public or private access, and resource deployment.
- **Azure Policy:** Enforces standards and assesses compliance at scale for consistency, security, cost, and management. Built-in AI policies are recommended for landing zone deployment.
- **Monitoring and Alerting:** Centralized collection and monitoring, alerts and actions, baselines, and monitoring of AI resources.
- **Identity, Access, and Data Management:** Entra ID, Managed Identities, Role-Based Access Control (RBAC), Privileged Identity Management, and Conditional Access policies.
- **Secure Networking:** Encrypted virtual networks, Network Security Groups, Application Security Groups, private endpoints, DNS, firewalls, VPN/ExpressRoute, DDoS protection, and monitoring.
- **Cost Management, Security Monitoring, Design Considerations, and Operating Model:** Tagging and consumption control, Microsoft Defender for Cloud, business continuity and disaster recovery, and an AI operating model spanning governance, security, compliance, platform design, and enablement.

### Topic 3: Agent Architectures

- **Why an Agent Blueprint:** Why AI agents differ from chatbots and why enterprises need an architecture blueprint to make agent systems production-ready.
- **Layered Architecture:** The usage, agentic, platform, integration, and governance layers, and how they compose into a complete design.
- **Microsoft Platform for Agents:** Microsoft Foundry and Copilot Studio, choosing the right agent platform, hosted agents, and multi-agent orchestration patterns.
- **Grounding and Integration:** Grounding agents with enterprise data and integrating across M365, Agent 365, Work IQ, Fabric IQ, and Foundry IQ.
- **Governance for Agents:** Guardrails, identity, and controls that keep multi-agent systems safe and governable at scale.

### Topic 4: AgentOps

- **AgentOps Foundations:** The production gap, building blocks of a production agent, Microsoft Foundry as the control plane, and an AgentOps operating and maturity model.
- **Evaluate:** Evaluation strategy, red teaming, and AI safety before release.
- **Ship:** CI/CD gates for AI agents and safe release practices.
- **Operate (Day-2):** Observability, monitoring, feedback loops, and ownership for agents in production.

### Topic 5: AI Security and Observability

- **AI Threat Landscape:** The evolving threat map for AI, the top threats for AI agents, and where Microsoft Agent 365 fits.
- **Secure AI System Design:** Shared responsibility across AI service types, Zero Trust strategy and architecture for AI, and securing agentic systems from code to runtime.
- **Responsible AI:** Fairness, transparency, safety, and compliance woven into secure design.
- **Trust Observability, Identity, and Data Protection:** Runtime evidence of trustworthy behaviour, identity and access for agents, and protecting sensitive data.
- **Runtime Threat Protection and Continuous Red Teaming:** Detecting and responding to threats at runtime and keeping systems resilient through ongoing red teaming.

### Topic 6: Solution Optimisation

- **The Enterprise Agent Problem:** Why agents break the old rules and why architecture must come before tuning.
- **Anti-Patterns and the Optimisation Model:** Five critical anti-patterns in agent systems and the five-layer optimisation model.
- **Routing, Context, and RAG Quality:** Cost reduction through routing patterns, context engineering, caching, and RAG quality.
- **Orchestration and Design:** Choosing the right orchestration pattern, single-skill single-responsibility design, and performance under load.
- **Runtime Performance and FinOps:** Latency optimisation, gateway patterns, FinOps, governance, launch readiness, platform accelerators, security, and observability.

**Cloud & AI CSA Responsibilities (Optional - only if upskilling is delivered)**:

| Task | Description |
|------|-------------|
| Confirm Topics | Based on the Scoping Call, confirm which of the six upskilling topics the customer has selected. |
| Schedule Sessions | Schedule 1-hour sessions for each topic (AgentOps may need 2 hours), ideally over 2-3 days when there are multiple sessions, as agreed with the customer. |
| Deliver upskilling sessions | Deliver through a separate upskilling VBD dispatch, or share the webinars with the customer. Not included as part of this dispatch. |
| Use Official Decks | Use the standardized decks in `presentations/` to ensure consistency. Export to PPTX with `marp_to_pptx.py` when a branded deck is required. |
| Track Attendance | Maintain a record of attendees and their roles. |
| Capture Insights | Note blockers, questions, or areas of confusion raised during sessions. |
| Refine Assessment Plan | Use insights to adjust the assessment agenda, breakout groups, and focus areas. |

**Cloud & AI CSA Checklist - Upskilling (Optional)**:
- :ballot_box_with_check: Confirm selected upskilling topics from Scoping Call
- :ballot_box_with_check: Schedule the sessions, spaced over 2-3 days if there are multiple sessions
- :ballot_box_with_check: Deliver the selected upskilling sessions through a separate upskilling VBD dispatch, or share the webinars
- :ballot_box_with_check: Use official decks from `presentations/`
- :ballot_box_with_check: Track attendance and roles for each session
- :ballot_box_with_check: Capture blockers, questions, and insights
- :ballot_box_with_check: Adjust assessment agenda and breakout plan based on findings
---
## Phase 2: Production Readiness Assessment

**Assets to Leverage**: [Production Readiness Assessment Agenda](https://aka.ms/FY27PathToProduction), [Production Readiness Assessment](https://aka.ms/P2PAgent)

-------

**Objective**:
This step delivers the production readiness assessment - a structured, CSA-led evaluation of the customer's readiness to move their AI use case into production. It identifies architectural gaps, operational risks, and platform limitations that must be addressed before go-live.

In this VBD the assessment is powered by the **automated Assessment Engine** in `assessment/`. The CSA works with the customer on the solution and use case, drops the relevant documents into the pipeline, and reviews the generated report together. This is a tailored evaluation - not a one-size-fits-all checklist - and it directly informs the implementation roadmap.

#### Running the Assessment Engine

```bash
# 1. Drop customer documents into the folder (gitignored)
cp *.pdf *.docx assessment/customer-docs/

# 2. Run the pipeline (requires GITHUB_TOKEN for LLM analysis)
cd assessment
pip install -r requirements.txt
python generate.py --docs customer-docs/ --output report.html --customer "Customer Name"
```

**What the report produces:**
- Maturity scores across the 6 pillars (~90 capabilities)
- Production gaps with severity ratings
- Recommended "Path to Production" VBD activities mapped to gaps
- Stakeholder voices, current state, dependencies, and a risk register
- A phased implementation roadmap

The output is an interactive HTML report (print to PDF via Ctrl+P). An interactive web-based assessment tool is also available in `tools/assessment/`.

**Cloud & AI CSA Responsibilities**:

| Task | Description |
|------|-------------|
| Prepare Materials | Collect the customer documents and confirm access to the Assessment Engine (`GITHUB_TOKEN`, Python 3.10+, dependencies installed). |
| Run the Assessment | Execute the pipeline against the customer documents to generate the maturity report and gap analysis. |
| Facilitate the Review | Walk the customer through the generated report, using open-ended questions to explore readiness, blockers, and platform gaps - Whiteboarding Session driven by customer requirements. |
| Document Gaps and Observations | Capture all findings and refine the report notes and recommendations. |
| Generate Summary | Use the report as input to generate the implementation plan. |

**Cloud & AI CSA Checklist - Production Readiness Assessment**:
- :ballot_box_with_check: Schedule a session with all relevant stakeholders
- :ballot_box_with_check: Collect customer documents into `assessment/customer-docs/`
- :ballot_box_with_check: Install the Assessment Engine dependencies and set `GITHUB_TOKEN`
- :ballot_box_with_check: Run `python generate.py` to produce the maturity report
- :ballot_box_with_check: Facilitate the review using open-ended, scenario-based questions
- :ballot_box_with_check: Capture all gaps, blockers, and observations
- :ballot_box_with_check: Generate a summary of findings for the assessment input
- :ballot_box_with_check: Review results with internal CSAs to align on the assessment design
- :ballot_box_with_check: Commit the report (not raw customer docs) to the `customer/*` branch
- :ballot_box_with_check: Confirm next steps and follow-up with the customer with Path to Production Golden Path VBDs

#### CSA Guidance for Running the Production Readiness Assessment

**1. Introduction & Overview of the Assessment**

- Explain the goals of the production readiness assessment and how it guides the discussion.
- Review the use case options with the customer and choose the focus (e.g., Multi-Agents, RAG, etc.).

**2. Preparation**

- Gather the customer documents (architecture docs, runbooks, security posture, operational notes) into `assessment/customer-docs/`.
- Run the Assessment Engine to produce the maturity report and gap analysis.
- Thoroughly review the high-priority gaps and their corresponding best practices. The goal is a roadmap for safe and scalable adoption and alignment across cross-functional teams.
- Decide how to run the discussion: frame it as a conversation using the report for guidance, or share your screen and review the report together.

**3. Assessment with Customer**

- Walk through each pillar and gap with the customer.
- Review the status of the customer's current environment against each capability.
- Document identified gaps and use the report's resource links to address unclear recommendations.
- Deep dive into categories that require further clarification, providing context and examples of implications.
- Encourage questions and use a whiteboard to explain complex topics visually.

**4. Wrap-Up and Q&A**

- Open the floor for final questions or concerns.
- Ensure alignment on next steps and follow-up meetings (e.g., confirm the timelines).
- Thank the customer for their participation and cooperation.

---

## Phase 3. Closeout

**Assets to Leverage**: [Implementation Plan](https://aka.ms/FY27PathToProduction)

**Objective**:
The closeout phase compiles all outputs from the production readiness assessment and provides an implementation plan with recommended next activities within the Unified offer package. This plan includes the architectural decisions, identified gaps, and next steps discussed during the assessment.

This phase ensures continuity, accountability, and momentum toward production deployment. It also provides the customer with a tangible artifact to align internal teams and secure executive sponsorship. In this VBD, the finalized report and reusable improvements are committed to the customer branch and cherry-picked back to `main` (see [Customer Knowledge Bank](https://aka.ms/P2PAgent)).


**Cloud & AI CSA Responsibilities**:

| Task | Description |
|------|-------------|
| Consolidate assessment Outputs | Gather all notes, architecture diagrams, breakout session inputs, and decisions captured during the assessment. |
| Customize the Implementation Plan | Refer to the Assessment Agent output. At high level this file includes: <br> &bull; Current architecture and gap analysis with identified areas to cover to move to production-ready solution , <br> &bull; Identified risks and mitigation actions , <br> &bull; Recommended Implementation phases to follow in the context of this Unified package, <br> &bull; Roles and responsibilities for the next steps |
| Review Internally | Share the draft with the internal team that have been engaged during the assessment phases, validate technical accuracy, alignment with the requirements of the Bundle restrictions (such as number of VBDs and Time for the recommended next steps). |
| Share with Customer | Deliver the final implementation plan within 5 business days after the assessment. Schedule a call with the customer to review and ensure alignment. |
| Schedule Follow-Up (if needed) | If additional clarification or support is required, schedule a follow-up session to walk through the plan and align on execution. |


**Cloud & AI CSA Checklist – 4. Post-assessment Delivery**:
- :ballot_box_with_check: Consolidate all assessment notes, decisions, and breakout outputs
- :ballot_box_with_check: Customize the implementation plan using the Assessment Agent 
- :ballot_box_with_check: Include architecture, timeline, owners, and risks 
- :ballot_box_with_check:  Review the plan internally with internal MS account team
- :ballot_box_with_check: Share the final plan with the customer within 5 business days 
- :ballot_box_with_check: Schedule a follow-up session if needed to align with customer on plan and next steps

---

## Customer Knowledge Bank

Every customer engagement lives on its own branch so institutional knowledge compounds across engagements.

### Branching Model

```
main                          # Canonical content - never customer-specific
  |
  +-- customer/contoso        # Contoso engagement (customised decks + assessment)
  +-- customer/northwind      # Northwind engagement
  +-- customer/fabrikam       # Fabrikam engagement
  ...
```

### How to Deliver an Engagement

```bash
# 1. Create a customer branch
git checkout -b customer/your-customer-name

# 2. (Optional) Customise the webinar decks for their context
#    (edit presentations, add customer-specific examples)
#    Upskilling is not included as part of this dispatch

# 3. Run the assessment
cp /path/to/customer/docs/* assessment/customer-docs/
python assessment/generate.py --docs assessment/customer-docs/ --output assessment/report.html

# 4. Commit the implementation plan (not raw customer docs!)
git add assessment/report.html
git commit -m "Assessment: Your Customer Name"

# 5. After delivery, merge reusable improvements back to main
git checkout main
git cherry-pick <commit-with-content-improvements>
```

> :shield: **Customer data stays on branches.** Raw documents in `assessment/customer-docs/` are gitignored. Only generated reports and content improvements flow back to `main`.

---

## Reference: Repository Map

| Path | Purpose |
|------|---------|
| `specs/` | Topic specifications - the source of truth for content |
| `presentations/` | Marp slide decks + PPTX exports for the 6 upskilling topics (optional - not included as part of this dispatch) |
| `assessment/` | Automated assessment pipeline (`generate.py`, `analyze.py`, `extract.py`, `schema.py`) |
| `assessment/customer-docs/` | Drop customer files here (gitignored) |
| `tools/assessment/` | Interactive web-based assessment tool |
| `.squad/` | AI agent team configuration |
| `marp_to_pptx.py` | Marp-to-branded-PPTX converter |
| `README.md` | Repository overview |


---
## Copilot Assistance for Overall Outcomes

**Use this content below to optionally engage AI and Copilot to help you complete the outcomes as below (always verify the content generated by AI or Copilot tooling before using those for your engagement)**

| Task | Delegation to Copilot | Example Prompt | Copilot Persona | What This Copilot Does Best |
|------|----------------------|----------------|-----------------|----------------------------|
| Enhanced Use Case Understanding | ✅ Partially | "Summarize Contoso's AI use case, production goals, and technical readiness from the information available internally at Microsoft. Use this to pre-fill the scoping template." | [Researcher](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/researcher-agent-in-microsoft-365-copilot/4397186) | Synthesizes structured and unstructured data from emails, meetings, transcripts and documents to extract insights and fill templates. |
| Identification of Gaps | ✅ Partially | "Review Contoso's architecture and operational documentation. Identify gaps or risks using the Production Readiness Assessment." | [Analyst](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/analyst-agent-in-microsoft-365-copilot/4397191) | Analyzes technical documentation and checklists to surface blockers and readiness gaps. |
| Stakeholder Upskilling (Optional - not included as part of this dispatch) | ✅ Partially | "Review the uploaded presentation and Azure documentation to identify any gaps or missing topics in the upskilling sessions." | [Analyst](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/analyst-agent-in-microsoft-365-copilot/4397191) | Analyzes technical documentation and upskilling sessions to identify any gaps. |
| Clear Implementation Roadmap | ✅ Partially | "Draft an implementation roadmap for Contoso based on the assessment notes and implementation template. Include owners and milestones." | [Planner](https://support.microsoft.com/en-us/office/create-a-new-plan-with-copilot-in-planner-preview-1c986429-613a-47c3-816d-039dd91e60bf) | Translates assessment outcomes into structured plans with timelines, ownership, and dependencies. |
| Continued Momentum | ✅ Partially | "Create a post-assessment summary for Contoso that aligns internal teams and supports executive sponsorship. Include key decisions and a visual timeline." | [Visual Creator](https://support.microsoft.com/en-us/topic/how-to-create-video-with-copilot-7586329a-64e0-4ae9-9444-0da5b1c2b848) + | Visual Creator builds alignment artifacts (e.g., timelines, infographics). |

