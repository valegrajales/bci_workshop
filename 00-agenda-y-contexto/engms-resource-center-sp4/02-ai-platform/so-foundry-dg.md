# **Delivery Guide - Solution Optimization for Microsoft Foundry Lifecycle**

> Note - This VBD is coming soon in August 2026

This delivery guide provides details and instructions to help you deliver the **Solution Optimization for Microsoft Foundry Lifecycle** Value Based Delivery (VBD). The engagement helps customers proactively manage model and agent retirements, deprecations, and migrations with minimal disruption. Each delivery selects one of two tracks: model lifecycle or agent lifecycle.

## Description
The model lifecycle track uses the [**Foundry Models Accelerator**](https://github.com/microsoft/Foundry-Models-Accelerator), a lifecycle-oriented toolkit for teams running Microsoft Foundry Models in production. It brings together the discovery scanner, methodology playbook, evaluation framework, audit scripts, golden datasets, and rollout guidance for upgrading models approaching retirement.

The agent lifecycle track uses the [**Migrate classic agents to new agents**](https://learn.microsoft.com/azure/foundry/agents/how-to/migrate?tabs=python#migrate-classic-agents-to-new-agents) guidance and the [**V1-to-V2 Assistant Migration Tool**](https://github.com/microsoft-foundry/foundry-samples/blob/main/migration/README.md). These resources help teams move to modern APIs and SDKs and adopt the conversations-and-responses execution model. The outcome is an enterprise-ready agent aligned with the new Foundry Agent Service, with improved operability, governance, and compatibility with current and future capabilities.

## Objective 
- **Discover** Inventory model deployments and retirement timelines for the model track, or agent and application dependencies for the agent track.
- **Assess** Score model feasibility across quality, latency, cost, compatibility, capacity, and runway, or assess agent conversation and response patterns, tool compatibility, versioning, governance, and operational readiness.
- **Migrate** Apply model code and API updates, or migrate the application to the new Foundry Agent Service APIs, SDKs, and conversations-and-responses execution model.
- **Evaluate** Run model A/B evaluations on a golden dataset, or validate agent behavior, tool calls, security, observability, and performance in non-production.
- **Roll out** Define a phased production rollout, rollback gates, monitoring, owners, and post-cutover validation for the selected track.

## Pre-requisites
In order to have a successful delivery, please review the pre-requisites carefully.

### Familiarity with Solution Optimizations: 
These reusable assets help customers switch to new models or modernize classic agents and assistants using recommended practices and current Microsoft migration guidance. You can use them as provided or adapt them to the customer's requirements.

1. [Foundry Models Accelerator](https://github.com/microsoft/Foundry-Models-Accelerator)
2. [Migrate classic agents to new agents](https://learn.microsoft.com/azure/foundry/agents/how-to/migrate?tabs=python#migrate-classic-agents-to-new-agents)
3. [V1-to-V2 Assistant Migration Tool](https://github.com/microsoft-foundry/foundry-samples/blob/main/migration/README.md)

The customer must provide access to the non-production Foundry project, source repository, configuration, test cases, and required dependent services. For the model track, confirm access to deployment inventory, usage metrics, quota, and a representative golden dataset. For the agent track, confirm that the delivery team can create or use a target agent and execute validation tests without changing production.

## Customer Participants

Having the right customer participants in the Solution Optimization for Microsoft Foundry VBD engagement is essential to completing a successful delivery. Ensure the customer roles outlined below are available and can participate in the workshop.

|Customer Role | Description | Required or Optional|
|----|----|----|
| AI Engineers / AI Developers | Apply model API and parameter changes or update agent definitions, SDK integrations, conversation and response handling, and tool invocation code | Required |
| Application Developers | Update application business logic that invokes models or agents and validate end-to-end behavior | Required |
| Solution Architect / Enterprise Architect | Owns migration design, target-model or target-agent decisions, dependency decisions, governance alignment, and target-state approval | Required |
| Deployment / Workload Owner | Provides the non-production Foundry environment and supports model deployment or agent configuration, identity, networking, capacity, and quota | Required |
| DevOps / AIOps Practitioner | Updates deployment automation, monitoring, diagnostics, and operational controls | Required |
| Data Scientist / Prompt Engineer | Curates the model golden dataset and interprets A/B evaluation results, or supports agent response-quality validation | Optional (Required if a golden dataset must be built) |
| Application Tester / Product Owner | Defines acceptance criteria, business-value scoring, and validation priorities | Optional |

## Delivery Scenarios

Select **one** scenario for each engagement. Do not combine both scenarios within the same three-day delivery.

### Scenario 1: Model Lifecycle Migration

Choose this scenario when a deployed Microsoft Foundry model is approaching retirement or deprecation and the customer needs to migrate an application to a replacement model.

- **Scope**: One retiring-to-target model pair in a non-production environment.
- **Primary guidance**: Foundry Models Accelerator.
- **Key focus**: Deployment discovery, retirement runway, model feasibility, API and parameter changes, A/B evaluation, and production rollout planning.
- **Expected result**: The application is validated against the target model in non-production, with a customer-executable production migration and rollback plan.

### Scenario 2: Agent Lifecycle Migration

Choose this scenario when the customer needs to migrate a classic Foundry agent or OpenAI Assistant to the new Foundry Agent Service.

- **Scope**: One classic agent or assistant workload in a non-production environment.
- **Primary guidance**: Migrate classic agents to new agents guidance and the V1-to-V2 Assistant Migration Tool.
- **Key focus**: Agent dependencies, conversations-and-responses patterns, SDK and API changes, tool compatibility, security, observability, validation, and production rollout planning.
- **Expected result**: The application is validated against the new Foundry Agent Service in non-production, with a customer-executable production migration and rollback plan.

## Delivery Guidance

You may adapt each step to meet the customer's needs while meeting the objectives and deliverable standards. Both scenarios follow **Discover -> Assess -> Migrate -> Evaluate -> Roll out**. The production cutover is delivered as a plan for the customer to execute after the engagement.

### Scenario 1: Model Lifecycle Migration Agenda

#### Step 0: Scoping - Day 0

**Objective**: Conduct pre-scoping with the delivery team and scoping with the customer; select the single target model pair and confirm non-production scope.

**Key Activities**: Review the customer's existing Microsoft Foundry Models footprint at a high level; identify the retiring model and candidate replacement model; confirm the engagement targets **one** model pair in a **non-production** environment; agree stakeholders, roles, and success criteria; verify access to the subscription, resource group, non-production Foundry project, code repository, and prerequisites needed to run the discovery scanner.

**Deliverables**: Scoping presentation capturing the selected model pair, non-production environment, stakeholders, success criteria, and prerequisite checklist.

**Outcome**: Clear alignment on one retiring-to-target model pair, non-production scope, stakeholders, and success criteria.

#### Step 1: Discover - Day 1 (AM)

**Objective**: Build a complete inventory of model deployments and enrich it with retirement dates and recent usage.

**Key Activities**: Run the Foundry Models Accelerator **discovery scanner** across the in-scope subscription or tenant; enrich each deployment with retirement timelines and recent usage metrics; confirm the in-scope retiring model and its non-production deployments; document remaining runway to retirement.

**Deliverables**: Model deployment inventory with retirement dates, usage, and runway, with the in-scope deployment highlighted.

**Outcome**: A shared, data-backed view of the retiring model's footprint and the urgency of the upgrade.

#### Step 2: Assess - Day 1 (PM)

**Objective**: Confirm the candidate target model and score migration feasibility.

**Key Activities**: Identify the **target model**. Use the methodology playbook to score the candidate across **quality, latency, cost, compatibility, capacity, and runway**; verify capacity and quota for the target model in the non-production region; identify API and parameter differences between source and target; record a go/no-go decision.

**Deliverables**: Feasibility scorecard for the target model and go/no-go decision.

**Outcome**: An agreed target model and feasibility baseline for migration.

#### Step 3: Migrate - Day 2

**Objective**: Update the application code and configuration to call the target model in the non-production environment.

**Key Activities**: Run the **audit scripts** to surface parameters and API calls that need updating, such as deprecated parameters, response-format changes, token limits, and API versions; apply the required changes; deploy or repoint the application to the target model in the non-production Foundry project; run smoke tests. Review the findings manually because the accelerator may not capture every application-specific change.

**Deliverables**: Updated application code and configuration, migration log, and smoke-test results.

**Outcome**: The application runs against the target model in the non-production environment.

#### Step 4: Evaluate - Day 3 (AM)

**Objective**: Validate the candidate model with A/B evaluation on a golden dataset.

**Key Activities**: Assemble or curate a representative golden dataset; run **A/B evaluations** of source and target using the evaluation framework locally, through the CLI, or through the web UI; compare quality, latency, and cost; review regressions and tune prompts where needed.

**Deliverables**: Evaluation report comparing source and target across quality, latency, and cost; the golden dataset.

**Outcome**: Evidence that the target model meets the agreed non-production acceptance criteria, with any remaining gaps documented.

#### Step 5: Plan Production Roll-out - Day 3 (PM)

**Objective**: Produce a production rollout plan using the accelerator's rollout guidance. Because this VBD is non-production only, the customer performs the production cutover after the engagement.

**Key Activities**: Define the phased traffic plan, rollback gates and criteria, monitoring, and post-cutover evaluation cadence; document production capacity and quota requirements; identify owners and a target timeline.

**Deliverables**: Production rollout and rollback plan, including phased traffic, gates, and monitoring, plus a handoff document.

**Outcome**: The customer is equipped to execute the production model migration safely.

### Scenario 2: Agent Lifecycle Migration Agenda

> [!NOTE]
> The three-day agenda is a maximum delivery timebox covering discovery, assessment, migration, validation, and rollout planning. A simple migration may take one day, a moderate migration may take two days, and complex migrations may require three or more days depending on application complexity, tool compatibility, testing needs, and customer readiness.

#### Step 0: Scoping - Day 0

**Objective**: Select one classic agent or assistant workload and confirm the target non-production environment and migration boundaries.

**Key Activities**: Review the customer's agent footprint; select one classic Foundry agent or OpenAI Assistant; confirm the source and target non-production environments; agree on stakeholders, success criteria, acceptance tests, access, and prerequisites.

**Deliverables**: Scoping presentation capturing the selected agent workload, environments, stakeholders, success criteria, and prerequisites.

**Outcome**: Clear alignment on one agent workload, a non-production migration, and measurable success criteria.

#### Step 1: Discover - Day 1 (AM)

**Objective**: Build an inventory of the source agent and the dependencies that affect its migration.

**Key Activities**: Use the migration guidance and tool to inventory the in-scope agent, application integration, tools, files, data stores, security, monitoring, and test assets. Identify dependencies and historical conversation state that may require separate handling.

**Deliverables**: Agent dependency inventory and current-state architecture.

**Outcome**: A shared view of the source implementation and the dependencies that control migration complexity.

#### Step 2: Assess - Day 1 (PM)

**Objective**: Define the target Foundry Agent Service pattern and assess migration readiness.

**Key Activities**: Assess the changes required for agent definitions, conversations, responses, tools, files, data stores, security, observability, and deployment. Identify unsupported or changed capabilities, manual remediation, and the approach for conversation state, which is not migrated by the tool.

**Deliverables**: Migration readiness assessment, source-to-target mapping, identified gaps, and go/no-go decision.

**Outcome**: An agreed target architecture and migration plan for the in-scope agent.

#### Step 3: Migrate - Day 2

**Objective**: Migrate the in-scope agent and application integration in the non-production environment.

**Key Activities**: Use the migration tool where applicable; migrate the agent definition and associated resources; update the application to use the new Foundry Agent Service patterns; address unsupported capabilities and application-specific changes; deploy the migrated workload to non-production.

**Deliverables**: Migrated agent, updated application and configuration, migration log, and non-production deployment.

**Outcome**: The application runs against the new Foundry Agent Service in the non-production environment.

#### Step 4: Evaluate - Day 3 (AM)

**Objective**: Validate migrated agent behavior and operational readiness against the agreed success criteria.

**Key Activities**: Validate agent creation, conversations, responses, context retention, tools, files, security, monitoring, and application behavior. Compare source and target behavior where practical and address significant regressions.

**Deliverables**: Validation report with test evidence, known gaps, and remediation recommendations.

**Outcome**: The migrated agent meets the agreed non-production acceptance criteria, or remaining gaps are documented with owners.

#### Step 5: Plan Production Roll-out - Day 3 (PM)

**Objective**: Produce a customer-executable production rollout and rollback plan. Because this VBD is non-production only, the customer performs the production cutover after the engagement.

**Key Activities**: Define deployment stages, traffic transition, rollback gates, monitoring, post-cutover validation, support coverage, owners, and timeline. Include the approach for starting new conversations and retaining access to historical state after migration.

**Deliverables**: Production rollout and rollback plan, operational checklist, and handoff document.

**Outcome**: The customer is equipped to migrate the agent to production with clear controls, ownership, and recovery steps.

## Close out

Recap the engagement and discuss next steps with customer stakeholders. It is important to include all key stakeholders in this meeting.

- For the model lifecycle track, walk through the model deployment inventory, retirement runway, feasibility scorecard, target-model decision, migration changes, and A/B evaluation results.
- For the agent lifecycle track, walk through the agent dependency inventory, target architecture, migration readiness assessment, source-to-target mapping, migrated agent demonstration, and validation results.
- Review known gaps, remediation recommendations, and owners for the selected track.
- Walk through the production rollout and rollback plan, and confirm owners and timeline.
- Document recommendations including next steps.
- Provide recommended resources for upskilling.
- If any further VBDs are recommended, inform the CSAM.
- Collect feedback on the overall VBD delivery and delivered content.

## Resources 

### IP Assets
* [VBD IP Kit](https://aka.ms/vbd-so-foundry/ipkit)
* [Foundry Models Accelerator](https://github.com/microsoft/Foundry-Models-Accelerator)
* [Migrate classic agents to new agents](https://learn.microsoft.com/azure/foundry/agents/how-to/migrate?tabs=python#migrate-classic-agents-to-new-agents)
* [V1-to-V2 Assistant Migration Tool](https://github.com/microsoft-foundry/foundry-samples/blob/main/migration/README.md)

### Level Up Training 
* Level up slide deck - Coming Soon
* Level up Recording - Coming Soon

### Support & Feedback

- For any internal feedback on the VBD, please use this [form](http://aka.ms/vbdfeedback).
