
# Proof of Concept for AI Apps & Agents


## Objective
- Deliver a functional, small-scale version of the solution that can be used to determine its feasibility and reinforce design decisions.
- Demonstrate that the architectural design is feasible. This may include competitive scenarios and integration with existing customer infrastructure, solutions, and applications.

<!-- IP Kit -->
<!-- TODO: replace with [!INCLUDE] --> 

## IPKit

The IPKit with artifacts to use throughout the delivery is located [here](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Apps%2FProof%20of%20Concept&newTargetListUrl=%2Fteams%2FASDIPRelease%2FAzureCloudAI&viewpath=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FForms%2FAllItems%2Easpx)

> [!NOTE]
> Scenario-based kickoff decks have been added that cover integration between Microsoft Foundry, other Azure services, and Microsoft Fabric.

## Objectives

### Core Objectives

* Understand the functional and non-functional requirements for the workload to be modernized or created.
* Assess the Microsoft Foundry solution, including the Foundry project, Foundry Models, Foundry Agents, Foundry Tools, knowledge sources, orchestration patterns, evaluation, tracing, monitoring, security controls, and integrations, to determine production readiness.
* Evaluate the Azure OpenAI workload to ensure a successful production deployment.
* Offer actionable recommendations to minimize potential downtime during integration and mitigate risks to the existing production solution.
* Identify any blockers or uncertainties that could jeopardize the existing production workload.
* Assess production readiness through evaluation of the architecture, agent design, code quality, evaluation results, tracing, monitoring, testing outcomes, cost considerations, and alignment with the Azure Well-Architected Framework and Responsible AI principles.
* Assist the customer in completing the scoped implementation for building or modernizing the workload.
* Validate AI application and agent effectiveness through testing, evaluation metrics, tracing, and predefined success criteria.
* Demonstrate secure, governed, and responsible implementation of AI applications and agents, including data protection, identity, compliance, and Responsible AI considerations.

### Optional Objectives Depending on the Use Case

The relevance of the following objectives will be determined during scoping.

* Provide clear deployment steps for the customer to implement in their DevOps tooling.
* Conduct a risk assessment of the proposed AI application or agent solution, including architecture, deployment processes, Foundry Model selection, grounding strategy, orchestration, security, governance, scalability, operational dependencies, and Responsible AI considerations.
* Offer a detailed analysis and recommendations for addressing any security or identity management issues identified in the environment.

This delivery can be booked under various SKUs depending on the desired depth of coverage. The options include:

* Introductory delivery on AI applications, covering Azure OpenAI and AI application user considerations.
* Advanced delivery focusing specifically on AI concepts.
* Advanced delivery focusing specifically on app development concepts.

## Deliverable Standards

> [!NOTE]
> Following this engagement, provide the customer with a closeout document that details all items listed in the "Delivery" section below.

* Outline Proof of Concept (PoC) application components and services based on the architectural design.
* Develop a PoC to validate a specific business scenario.
* Develop and deploy a sample application workload that matches the business vision for future capabilities.
* Deliver a working PoC that matches the customer's needs and the services outlined during the scoping call. Some engagements may not require customer data.
* Obtain customer acceptance and sign-off on the PoC to complete the engagement.
* Provide a roadmap to production during the closeout meeting.

> [!IMPORTANT]
> Meeting these baseline requirements does not mean that the application will perform successfully in every possible scenario.
> Please ensure that you use appropriate disclaimers in any written report that you make available to a customer.

Based on the workload assessment, the customer team should be prepared to move to the next stage of deployment.

## Customer Participants

Having the right customer participants is essential to a successful engagement. Ensure that the customer roles outlined below are available and able to participate.

| Customer Role | Description | Required or Optional |
| --- | --- | --- |
| AI and application workload owner (stakeholder) | Person or team responsible for the AI application or agent workload built with Microsoft Foundry, Azure OpenAI, or related Azure services. | Required |
| Lead developer/architect | Person responsible for delivering, reviewing, and maintaining the application and AI code and design, and for approving the engagement outcomes. This person also works with other customer IT professionals to incorporate their feedback and recommendations and ensure that the workload is secure, reliable, and available according to the design specifications. | Required |
| App DevOps | Team responsible for maintaining the application-stack code and functionality. | Required |
| Infrastructure DevOps/DevSecOps | Team responsible for deploying applications to production and maintaining the production platforms and automation code. | Required |
| Application, production, and infrastructure security/identity | Team responsible for security and identity management across all aspects of the application and infrastructure. | Required |
| Data scientist | Team member working on machine learning experiments and models. | Optional |
| Data architect | Team member working on data structures and data-platform solutions. | Optional |
| Other IT professionals | People responsible for provisioning and managing IT resources such as databases, networking, compute, identity and access management, and security operations. | Optional |

> [!NOTE]
> Not all stakeholders are required for every engagement. Their availability helps remove roadblocks promptly. For example, a database administrator may be required to provision access to a database used in the PoC.

## Scoping

### Pre-Scoping with the Account Team

To understand the customer's background and validate expectations, see [Pre-Scoping Call with CSAM & CSA](https://aka.ms/VBDPre-scoping). This call precedes the customer scoping call.

### General Scoping Guidance

A scoping call should be scheduled at least two weeks before delivery to allow sufficient time for architecture review, prerequisite validation, environment preparation, stakeholder alignment, and use-case prioritization.

The scoping call allows you to verify whether this MCEM activity aligns with the customer scenario and whether the customer is ready for a successful delivery.

During the scoping call, plan and confirm the following:

* Prepare the agenda and email it to the customer before the call.
* Agree on session objectives and required resources (these can be sent before the scoping call).
* Ensure a clear understanding of the customer's objectives and goals.
* Outline the planning and next steps.
* Clarify any logistics, especially for on-site delivery.

### Ensure the Delivery Aligns with Customer Requirements

#### MCEM Activity Alignment

Ensure you understand when a different MCEM activity might be more suitable and discuss the best solution for the customer's problem. The CSAM can assist in making any necessary adjustments to the engagement.

#### Product and Scenario Alignment

> [!IMPORTANT]
> This section provides a selection of preconfigured solutions and tools to consider before the delivery session for applications and agents built with Microsoft Foundry and Azure OpenAI.

Confirm that the customer's use case is well suited for Microsoft Foundry and the appropriate Foundry Tools, or determine whether a different managed solution would better meet the customer's needs.

### VBD Flexibility and Modularity

VBD engagements are characterized by flexible timing and modular content. For more information, see [VBD Flexibility and Modularity](https://aka.ms/VBDFlexibility).

### Customer Scoping Call

It is recommended to schedule the scoping call at least two weeks before the delivery.

This phase is crucial to ensure expectations are set, prerequisites are met, stakeholders are identified, outputs are clear, and all parties have time to research and prepare.

* Ensure the CSAM is included and kept up to date on all communications with the customer.
* Confirm that you have a dispatch for the engagement.
* The CSAM can assist with this and is responsible for dispatching you.
* Clarify who will send the meeting invites and establish the working "rhythm".
* Understand relevant account considerations, including organizational sensitivities, sales context, renewals, known challenges, and other dependencies.

Next, complete the customer scoping for this engagement. The CSAM should assist in scheduling a scoping call with the customer's business sponsor and relevant stakeholders.

During the scoping call, plan to:

* Agree on session objectives and required resources.
  * It may be convenient to exchange these via Teams or email ahead of the call.
* Ensure a clear understanding of the customer's objectives and goals.
* Agree on the next steps.

Use the scoping call to confirm:

* What are the customer's goals for the workload?
* What workload(s) and teams are involved in the engagement?
* How much experience does the customer have in building AI applications?
* What considerations or preparations have they already made for their upcoming production deployment?
* What outcome does the customer expect after the review?

You should also:

* Review the delivery assets with the customer based on the workload being assessed.
* Address potential blockers or uncertainties that could jeopardize the workload's deployment or any other integrated or connected workloads.
* Determine whether a Foundry project, Foundry Models, Foundry Agent Service, Foundry Tools, or Azure OpenAI provides the most appropriate production-scale solution to the customer's problem.
* If not, inform the CSAM and account team so they can make the necessary adjustments.

At the end of the scoping call, recommend a high-level agenda for the engagement duration.

Scoping call outcomes:

* Assess the skill levels of the developers, operations, and security teams.
* Ensure the existing application workload has been identified and agreed upon by all relevant stakeholders.
* Understand the infrastructure and identify any security requirements, boundaries, or control systems.
* Clearly identify and understand the underlying infrastructure type, such as compute and data platforms.
* Agree on expectations and outcomes with the customer.
* Establish who will attend the session.
* Confirm logistics and send meeting invites.

## Delivery Guidance

This section includes nontechnical delivery guidance and supporting artifacts for the Proof of Concept. You may adapt each activity to meet the customer's needs, provided that you meet the objectives and deliverable standards.
Optional requirements are identified where applicable.

### Overview

In this engagement, the customer develops and validates an AI workload built with Microsoft Foundry and Azure services. The solution should align with the assessment and the pillars of the Azure Well-Architected Framework. A Microsoft Cloud Solution Architect (CSA) helps the customer achieve the desired outcomes while following recommended practices and patterns and identifying blockers that could affect production.

To support the customer in this scenario, various engagement options are available. The [Supporting Material](#find-supporting-material) section below provides resources to explore.

You are encouraged to add, develop, customize, and leverage other documentation, training, and content from different scenarios to ensure successful delivery.

This engagement offers three delivery SKUs:

* Introductory delivery on AI applications, covering Azure OpenAI and AI application user considerations.
* Advanced delivery focused on AI concepts.
* Advanced delivery focused on application development concepts.

## Delivery Effort

### Delivery Duration
The **Proof of Concept for AI Apps & Agents** scenario is available as a **1-day, 3-day, or 5-day delivery**. The appropriate duration depends on the selected modules, complexity of the business scenario, implementation scope, and depth of coverage agreed with the customer during the scoping call. The flexible and modular format can support an introductory delivery covering Azure OpenAI and AI application user considerations or a more advanced delivery focused on AI concepts, agents, and application development.

### Select a Delivery Scenario
A Proof of Concept (PoC) is a functional, small-scale implementation of an architectural design used to demonstrate its feasibility and reinforce design decisions. It may include integration with the customer's existing infrastructure, solutions, applications, data platforms, and operational processes, but it may not include every architectural aspect required for a production deployment.

Agree with the customer on one or more AI Apps & Agents focus areas:

| Scenario | Objectives |
| --- | --- |
| AI Application Proof of Concept | Build or modernize a functional AI-enabled application using Azure OpenAI, Foundry Models, and relevant Foundry capabilities. Validate the application architecture, model integration, code quality, user experience, deployment approach, and integration with the customer's existing applications and infrastructure. |
| AI Agent Proof of Concept | Design and implement an agent-based solution using Foundry Agent Service. Validate the Foundry project, selected Foundry Models, prompt or hosted agents, Foundry Toolbox, knowledge sources, orchestration patterns, operational dependencies, security controls, and integration points. |
| Retrieval-Augmented Generation | Demonstrate an AI-powered assistant or chatbot that retrieves and generates contextually relevant answers from enterprise knowledge sources. Validate the grounding strategy, retrieval behavior, response quality, security, observability, and evaluation criteria. |
| Intelligent Document Processing | Demonstrate document analysis, extraction, and processing workflows using Foundry Tools such as Azure AI Document Intelligence. Validate the selected document types, extraction requirements, integration workflow, accuracy expectations, and expected business outcome. |
| AI Workload Production Readiness | Assess the proposed AI application or agent for production readiness, including architecture, agent design, deployment processes, Foundry Model selection, grounding, orchestration, code quality, evaluation results, tracing, monitoring, testing, security, governance, scalability, cost considerations, Responsible AI, and alignment with the Azure Well-Architected Framework. |

## Kickoff

### Introduction to Delivery
The CSA can select and adapt the available delivery assets based on the scope agreed with the customer. The kickoff should confirm the PoC objectives, success criteria, roles, agenda, working rhythm, prerequisites, and expected outputs.

### Design a New Architecture
As a core part of this engagement:

- Present and discuss the scenario-based kickoff material selected for the AI application or agent use case.
- Review the functional and non-functional requirements for the workload being created or modernized.
- Define the proposed architecture, including the Foundry project, Foundry Models, prompt or hosted agents, Foundry Toolbox, Foundry Tools, knowledge sources, orchestration, application components, deployment approach, integrations, evaluation, tracing, monitoring, identity, security, governance, and Responsible AI considerations.
- Discuss architectural decisions, assumptions, dependencies, risks, and trade-offs with the customer.

### Review an Existing Architecture
As a core part of this engagement:

- Review the existing AI application or agent architecture and its integration with the customer's infrastructure, applications, and data platforms.
- Assess Foundry Model selection, grounding strategy, agent and tool design, orchestration, evaluation, tracing, monitoring, security, identity, governance, scalability, cost, and operational dependencies.
- Highlight decisions, risks, blockers, and trade-offs, and agree on the decisions and PoC boundaries with the customer.

## Deliver the Proof of Concept

### Validate Prerequisites
During this phase, the CSA will:

- Confirm the selected AI application or agent scenario, PoC outcome, success criteria, and in-scope components.
- Validate access to the application code, Foundry project, Azure environment, Foundry Models, data or knowledge sources, Foundry Tools, integrations, and deployment resources required for the PoC.
- Review the workload requirements and validate the architecture and implementation checklist.
- Confirm the security, identity, data protection, compliance, governance, and Responsible AI requirements.
- Identify any blockers that could affect the implementation or the existing production workload.

### Select a Delivery Asset

The following links give the lead technical CSA access to catalogs of GitHub repositories. These repositories provide starting points for creating and deploying a functional Proof of Concept (PoC) in the customer's environment. Each catalog includes applications with information about deployment, use cases, technologies, and implementation steps. Review the catalogs and select one or more applications based on the solution requirements.

- [AI Apps Repository Catalog](https://github.com/microsoft/App-Templates/tree/main/ai-templates). This is maintained by Corp CSU Tech Strategy teams.
- [AI Apps Template Gallery](http://aka.ms/aiapps). This is maintained by DevDiv Dev Relations/Cloud Advocacy teams.
- [Gold Standard Accelerators](https://mcaps.accelerators.ms/). This is maintained by Data & AI GBB teams.

The following assets provide differentiated options for AI application and agent PoCs. Select the asset that best matches the customer's required delivery format, architecture, data platform, and document-processing needs:

| Delivery Type | Delivery Name | Customer Level | Target Audience | Delivery Method | Use Case | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| Proof of Concept | [AI Multi-Agent Architecture](https://github.com/MSUSAzureAccelerators/Azure-Cognitive-Search-Azure-OpenAI-Accelerator) | Advanced | AI Engineers, Application Developers, Data Engineers, Cloud Architects, Business Stakeholders | Workshop, Hands-on Development | Delivers a time-boxed multi-agent PoC that combines retrieval-augmented generation (RAG), enterprise search, and multichannel experiences. | Customer will understand how to design and implement a secure multi-agent application grounded in enterprise data. |
| Solution Accelerator | [Enterprise RAG Solution Accelerator (GPT-RAG)](https://github.com/Azure/GPT-RAG) | Advanced | AI Engineers, Application Developers, Cloud Architects, Security Architects | Presentation, Hands-on Development | Implements an enterprise agentic RAG architecture with Microsoft Foundry, agent orchestration, enterprise data grounding, tool integration, security, and observability. | Customer will understand how to deploy a secure, scalable, and observable agentic RAG solution that provides grounded answers from enterprise data. |
| Solution Accelerator | [Azure Chat](https://github.com/microsoft/azurechat) | Intermediate | AI Engineers, Application Developers, Cloud Architects, Business Stakeholders | Demo, Hands-on Development | Implements a private Azure-hosted chat experience for organizational data and files when a full enterprise RAG architecture is not required. | Customer will gain a private chat application that uses organizational content while supporting enterprise identity and networking patterns. |
| Code Sample | [Cosmos DB for MongoDB Copilot](https://github.com/AzureCosmosDB/cosmosdb-mongo-copilot) | Intermediate | AI Engineers, Application Developers, Data Engineers, Cloud Architects | Hands-on Development | Demonstrates a generative AI application using Azure Cosmos DB for MongoDB vector search, Azure OpenAI, Semantic Kernel, conversational history, and semantic caching. | Customer will understand how to implement conversational RAG with MongoDB-compatible vector search and contextual conversation management. |
| Solution Accelerator | [ContentFlow](https://github.com/Azure/contentflow) | Advanced | AI Engineers, Application Developers, Data Engineers, Cloud Architects | Demo, Hands-on Development | Implements configurable document and content-processing pipelines using Azure AI Document Intelligence, embeddings, parallel and conditional processing, and Microsoft Agent Framework orchestration. | Customer will understand how to automate document ingestion, extraction, enrichment, and downstream AI processing using a scalable content pipeline. |


### Find Supporting Material

The following assets can be used as part of the delivery.


> [!NOTE]
> You are not limited to the examples below.
> You may use these examples, create a custom delivery, or combine assets to produce a solution that meets the customer's needs.
> You may use assets from any of these deliveries in the engagement based on the scope agreed with the customer.

Use the resources in the following sequence: begin with Microsoft Learn content, review the certification guidance, complete the hands-on lab, explore the GitHub repository, and then review the reference architecture.

- **Microsoft Learn documentation:** [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/foundry/)
- **Microsoft Learn certification guidance:** [Microsoft Certified: Azure AI Apps and Agents Developer Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/?practice-assessment-type=certification)
- **Hands-on training lab:** [AI-103T00-A Develop AI apps and agents on Azure (Cloud Slice Provided) - MS - Skillable TMS](https://mslearningcampus.com/Course/50542)
- **GitHub repository:** [microsoft/agent-framework: A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET.](https://github.com/microsoft/agent-framework)
- **Azure reference architecture:** [Azure OpenAI Landing Zone reference architecture](https://techcommunity.microsoft.com/blog/azurearchitectureblog/azure-openai-landing-zone-reference-architecture/3882102)

### Prepare for Delivery
During this phase, the CSA will:

- Help the customer prepare the development and target environments.
- Select an appropriate starting point from the AI Apps Repository Catalog, AI Apps Template Gallery, Gold Standard Accelerators, or other approved delivery assets.
- Define the implementation steps for the selected AI application, agent, RAG, or document-processing use case.
- Prepare a checklist covering the Foundry project, Foundry Models, prompt or hosted agents, Foundry Tools, knowledge sources, orchestration, application integrations, deployment, evaluation, tracing, monitoring, testing, security, identity, and governance.
- Agree on the evaluation metrics, tracing approach, test scenarios, and predefined success criteria that will be used to validate the PoC.

### Implement the PoC
During this phase, the CSA will:

- Assist the customer in building or modernizing the scoped AI workload and integrating it with the required applications, infrastructure, tools, and knowledge sources.
- Implement the selected Foundry Model, agent, grounding, orchestration, or document-processing capabilities.
- Support the customer in validating the implementation through functional testing, evaluation metrics, tracing, and the agreed success criteria.
- Track implementation progress, architectural decisions, risks, issues, and remediation actions.
- Where included in scope, provide clear deployment steps that the customer can incorporate into their DevOps tooling.

### Recommendations
Because this is a PoC, discuss the following with the customer:

- Production-readiness gaps related to architecture, agent design, code quality, deployment, observability, evaluation, testing, security, identity, governance, scalability, operational dependencies, cost, and Responsible AI.
- Risks or blockers that could affect the existing production workload or connected workloads.
- Recommendations for improving Foundry Model selection, grounding strategy, orchestration, integrations, evaluation quality, traceability, and operational readiness.
- Actions required to align the solution with the Azure Well-Architected Framework and Responsible AI principles.
- The limitations of the PoC and the additional validation required before production deployment.

## Closeout

In the closeout meeting, provide the customer with a summary of the engagement, including:

- The implemented PoC and the extent to which it met the agreed objectives and success criteria.
- Architecture and design decisions, assumptions, dependencies, and trade-offs.
- Testing outcomes, evaluation results, tracing findings, and identified limitations.
- Production-readiness findings covering observability, security, identity, governance, scalability, cost, operational readiness, and Responsible AI.
- Risks, blockers, remediation recommendations, and issues requiring follow-up.
- Recommended next steps to help the customer move to the next stage of deployment.

The last part of the engagement is a short session to collect feedback. Refer to the [IPKit](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Apps%2FProof%20of%20Concept&newTargetListUrl=%2Fteams%2FASDIPRelease%2FAzureCloudAI&viewpath=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FForms%2FAllItems%2Easpx&share=cgqBkXabxwwVT6f0q%5FxhQIVmEgUCochjJGOv1Iw24cB%5FBkf20A) for the closeout templates.

## Share Feedback with the Account Team
The CSA will collate the relevant information gathered during the delivery, including architectural decisions, implementation outcomes, evaluation results, risks, blockers, mitigations, recommendations, and customer feedback. The CSA will share this information with the account team.

Engage in follow-up conversations to identify additional opportunities and agree on the actions required to accelerate deployment, improve production readiness, or optimize the AI application or agent solution. See [Post-Delivery Activities](https://aka.ms/VBDPost-Delivery).

## Additional Learning Resources

- [AI Agents for Beginners: 18 Lessons to Get Started Building AI Agents](https://github.com/microsoft/ai-agents-for-beginners)
- [Azure AI Search Documentation](https://learn.microsoft.com/en-us/azure/search/)
- [RAG and Generative AI in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview?tabs=videos)
- [AI Learning Hub](https://learn.microsoft.com/en-us/ai/?tabs=business-technical-leader)
- [Foundry Models Sold Directly by Azure](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai)
- [Semantic Kernel: What It Is and Why It Matters](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/semantic-kernel-what-it-is-and-why-it-matters/3877022)
- [AutoGen: Enabling Next-Generation Large Language Model Applications](https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications/)

### Community Support

- [VBD - AI Apps and Agents Teams Channel](https://teams.microsoft.com/l/channel/19%3Adc692f3bec324088bbe5b9d07565c0f2%40thread.tacv2/VBD%20-%20AI%20Apps%20and%20Agents?groupId=591c20e8-6a02-4476-8881-849bf672e6cf&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47)
