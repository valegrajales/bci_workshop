# Learning Path - Solution Optimization for Microsoft Foundry Lifecycle

> Note - This VBD is coming soon in August 2026

## Foundry Model Lifecycle

The **Solution Optimization for Microsoft Foundry** engagement provides a structured, lifecycle-oriented approach for proactively managing Microsoft Foundry model changes and retirements — discovering model deployments, assessing a target model, migrating application code, evaluating the candidate, and planning a safe production roll-out. This enables you to demonstrate a smooth, low-disruption migration from a retiring model to a target model in a non-production environment.

Follow the steps below to build your knowledge and practical skills:

### 1. Introduction

**Goal:**  Understand the purpose and scope of the Solution Optimization for Microsoft Foundry.

*   Explore the solution materials: [VBD IP Kit](https://aka.ms/vbd-so-foundry/ipkit)

*   Access the accelerator: [Foundry Models Accelerator Repo](https://github.com/microsoft/Foundry-Models-Accelerator)

*   Review the Delivery Guide: [Delivery Guide](so-foundry-dg.md)

**Activity:** Summarize in a few sentences the main objective of the Accelerator and its five-stage lifecycle (Discover → Assess → Migrate → Evaluate → Roll out).

### 2. Key Concepts and Architecture

**Goal:** Learn the foundational lifecycle and the accelerator's building blocks.

*    Review the five lifecycle objectives — **Discover, Assess, Migrate, Evaluate, Roll out** — in the Delivery Guide
*    Understand the accelerator's components: discovery scanner, methodology playbook, evaluation framework, audit scripts, golden datasets, and rollout guidance
*    [Foundry Models Accelerator Repo](https://github.com/microsoft/Foundry-Models-Accelerator)

**Activity:** Draw or annotate a diagram of the model upgrade path and all the components or artifacts needed to deliver it.

### 3. Professional Soft Skills and Capabilities

**Goal:** Recognize essential soft skills for successful delivery and customer engagement.

*    Review these resources:
     *    [Data & AI Architectural Design](https://aka.ms/DataAI/ArchitecturalDesign)
     *    [Data & AI Business Value](https://aka.ms/DataAI/BusinessValue)
     *    [Data & AI Situation Fluency](https://aka.ms/DataAI/SituationFluency)
     *    [Data & AI Trusted Advisership](https://aka.ms/DataAI/TrustedAdvisership)
     *    [Data & AI Digital Signals](https://aka.ms/DataAI/DigitalSignals)
       
**Activity:** Select one soft skill and describe a scenario where it would be important in a Foundry model-migration engagement.

### 4. Explore the Solution Optimization Repository

**Goal:** Get familiar with the official codebase and documentation.

*   Access the main repository: <https://github.com/microsoft/Foundry-Models-Accelerator>
*   Review the discovery scanner, methodology playbook, evaluation framework, audit scripts, and golden datasets
*   Read deployment guides and README files

**Activity:** Locate the discovery scanner, methodology playbook, evaluation framework, audit scripts, golden datasets, and rollout guidance.

### 5. Hands-On Deployment

**Goal:** Practice running the accelerator end-to-end against one retiring → target model pair in your own demo environment.

*   **Discover:** run the discovery scanner to inventory model deployments and enrich them with retirement dates and recent usage
*   **Assess:** score the target model across quality, latency, cost, compatibility, capacity, and runway using the methodology playbook, and record a go/no-go decision
*   **Migrate:** run the audit scripts, apply the API/parameter changes, repoint the app to the target model in the non-prod Foundry project, and run smoke tests
*   **Evaluate:** run A/B evaluations (source vs. target) on a golden dataset — locally, via the CLI, or through the web UI

**Activity:** Run and test the accelerator end-to-end against one retiring → target model pair in your own demo environment.

### 6. Deep Dive: Customization and Best Practices

**Goal:** Learn how to adapt the accelerator to different scenarios and requirements.

*   Leverage the accelerators as-is or customize them to meet customer requirements
*   Scope the engagement to one retiring → target model pair in a non-production environment; deliver the production cutover as a *plan* the customer executes after the engagement
*   Note that the repo is evolving — some changes may not be captured by the audit scripts alone, so review manually where needed

**Activity:** Adapt one lifecycle step (e.g., the methodology playbook scoring or the migration audit) to reflect a specific customer scenario. Explain your choices.

### 7. Validation and Troubleshooting

**Goal:** Develop skills in validating deployments and resolving common issues.

*   Validate: run smoke tests after repointing the application to the target model
*   Evaluate: compare quality, latency, and cost via A/B evaluation on the golden dataset; review regressions and tune prompts where needed
*   Roll out safely: define rollback gates and criteria, monitoring, and a post-cutover evaluation cadence

**Activity:** Document a validation or troubleshooting step (e.g., a smoke test or an A/B evaluation result) you performed after migrating to the target model.

### 8. Additional Resources

**Goal:** Access further materials for deeper learning and reference.

*    [Foundry Models Accelerator (Repo)](https://github.com/microsoft/Foundry-Models-Accelerator)
*    [Azure OpenAI in Microsoft Foundry Models working with models - Microsoft Foundry | Microsoft Learn](https://learn.microsoft.com/en-gb/azure/foundry/openai/how-to/working-with-models?tabs=powershell)
*    [Upgrade or switch models with Ask AI - Microsoft Foundry | Microsoft Learn](https://learn.microsoft.com/en-gb/azure/foundry/observability/how-to/optimization-model-upgrade)
*    [Foundry Models lifecycle and support policy - Microsoft Foundry | Microsoft Learn](https://learn.microsoft.com/en-gb/azure/foundry/openai/concepts/model-retirements)
*    [Model retirement schedule - Microsoft Foundry | Microsoft Learn](https://learn.microsoft.com/en-gb/azure/foundry/openai/concepts/model-retirement-schedule)
*    [How to Evaluate & Upgrade Model Versions in the Azure OpenAI Service](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/how-to-evaluate--upgrade-model-versions-in-the-azure-openai-service/4218880)
*   [Delivery Guide](so-foundry-dg.md)

**Activity:** Bookmark these resources for future reference.

## Foundry Agent Lifecycle

The **Solution Optimization for Microsoft Foundry Agent Lifecycle** engagement provides a structured approach for migrating one classic Foundry agent or OpenAI Assistant to the new Foundry Agent Service in a non-production environment. The lifecycle covers discovery, assessment, migration, validation, and production rollout planning.

Follow the steps below to build your knowledge and practical skills.

### 1. Introduction

**Goal:** Understand the purpose and scope of the agent lifecycle migration scenario.

- Review the [Agent Lifecycle Migration Delivery Guide](so-foundry-dg-agents%20copy.md).
- Review [Migrate classic agents to new agents](https://learn.microsoft.com/azure/foundry/agents/how-to/migrate?tabs=python#migrate-classic-agents-to-new-agents).
- Explore the [V1-to-V2 Assistant Migration Tool](https://github.com/microsoft-foundry/foundry-samples/blob/main/migration/README.md).

**Activity:** Summarize the migration scenario, its non-production scope, and the five lifecycle stages: Discover, Assess, Migrate, Evaluate, and Roll out.

### 2. Key Concepts and Architecture

**Goal:** Understand the main differences between classic agents or assistants and the new Foundry Agent Service.

- Learn how classic threads, messages, and runs relate to conversations, conversation items, and responses.
- Understand versioned agent definitions and the conversations-and-responses execution model.
- Review tool compatibility and identify capabilities that may require an alternative or redesign.
- Understand that historical conversation state is not migrated by the migration tool and requires separate planning.

**Activity:** Create a high-level source-to-target mapping for one classic agent or assistant workload.

### 3. Professional Soft Skills and Capabilities

**Goal:** Develop the customer engagement skills required to scope and guide an agent migration.

- [Data & AI Architectural Design](https://aka.ms/DataAI/ArchitecturalDesign)
- [Data & AI Business Value](https://aka.ms/DataAI/BusinessValue)
- [Data & AI Situation Fluency](https://aka.ms/DataAI/SituationFluency)
- [Data & AI Trusted Advisership](https://aka.ms/DataAI/TrustedAdvisership)
- [Data & AI Digital Signals](https://aka.ms/DataAI/DigitalSignals)

**Activity:** Describe how you would align stakeholders on scope, success criteria, migration risk, and production ownership.

### 4. Explore the Migration Guidance and Tool

**Goal:** Become familiar with the official migration guidance and supporting tool.

- Review the supported migration path from classic agents and OpenAI Assistants.
- Understand what the migration tool can migrate and what requires manual application changes.
- Review how agent definitions, tools, files, and data stores affect migration readiness.
- Identify prerequisites for accessing the source and target Foundry environments.

**Activity:** Review one sample agent and list the dependencies that must be assessed before migration.

### 5. Hands-On Migration

**Goal:** Practice the lifecycle against one agent or assistant workload in a non-production environment.

- **Discover:** Inventory the agent, application integration, tools, files, data stores, security, monitoring, and test assets.
- **Assess:** Identify target patterns, compatibility gaps, manual remediation, and the approach for historical state.
- **Migrate:** Use the migration tool where applicable, update the application, and deploy the migrated workload to non-production.
- **Evaluate:** Validate conversations, responses, context retention, tools, security, monitoring, and application behavior.

**Activity:** Migrate and validate one sample classic agent or OpenAI Assistant in a non-production Foundry environment.

### 6. Customization and Best Practices

**Goal:** Learn how to adapt the migration approach to customer requirements.

- Scope the engagement to one agent or assistant workload.
- Review tool compatibility before committing to the migration approach.
- Plan manual remediation for unsupported capabilities and application-specific integrations.
- Treat the three-day agenda as a maximum timebox; actual duration depends on complexity, testing needs, and customer readiness.
- Deliver production cutover as a customer-executable rollout and rollback plan.

**Activity:** Adapt the migration plan for a sample workload that uses tools, files, or external integrations.

### 7. Validation and Troubleshooting

**Goal:** Develop skills in validating migrated agents and resolving common migration issues.

- Confirm that the migrated agent can be created and invoked successfully.
- Validate conversations, responses, context retention, and tool behavior.
- Test identity, authorization, files, data access, monitoring, and error handling.
- Compare source and target behavior and document significant regressions.
- Plan for new conversations after migration while retaining appropriate access to historical state.

**Activity:** Document one validation result, migration gap, and recommended remediation.

### 8. Additional Resources

**Goal:** Access further materials for delivery and continued learning.

- [Agent Lifecycle Migration Delivery Guide](so-foundry-dg.md)
- [Migrate classic agents to new agents](https://learn.microsoft.com/azure/foundry/agents/how-to/migrate?tabs=python#migrate-classic-agents-to-new-agents)
- [V1-to-V2 Assistant Migration Tool](https://github.com/microsoft-foundry/foundry-samples/blob/main/migration/README.md)
- [Foundry Agent Service documentation](https://learn.microsoft.com/azure/foundry/agents/)
- [Delivery Community](https://teams.microsoft.com/l/channel/19%3Adc692f3bec324088bbe5b9d07565c0f2%40thread.tacv2/VBD%20-%20Innovate%20Apps%20with%20AI?groupId=591c20e8-6a02-4476-8881-849bf672e6cf&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47)

**Activity:** Bookmark these resources for future reference.

### 9. Accreditation

An assessment is available to reinforce key concepts. It consists of 25 questions, with 60 minutes to respond. The minimum passing score is 80%.

| Accreditation | Link |
| --- | --- |
| Solution Optimization for Microsoft Foundry [Accreditation](https://learningplayer.microsoft.com/activity/successfactors/s9319856/launch) |
