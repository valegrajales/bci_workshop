<!--- file last updated: 20250109 --->

# Solution Optimization to Build and Deploy Azure AI Platform
#### Duration - 32 hours

**Preparing for the delivery:** [Learning Path and Accreditation](./SolnOptimizationPlatform-lp.md)

### Objective

The goal of this phase is to help optimize customer environment. Assist customers with issue(s) related to Performance, Tuning and Optimization (PTO). Some of the use cases that might fall under this category would be:

- Long running AI/ML models.
- Cost of services are more than expected 
- Enhance security and compliance  
- Automate monitoring and troubleshooting  
- Foster continuous innovation
- Governance with resource organization, tagging and RBAC
- Machine Learning Operations guidance
- and many more...

<!--- Sample Template ---> 

## Deliverable Standards

* Following the delivery of this engagement, it is important to provide the customer with a close out document.  This document should detail all of the items listed in the "delivery" section below.  

> [!Important]
> Meeting these baseline requirements does not mean that the application will perform successfully in every possible scenario.
> Please ensure that you use appropriate disclaimers in any written report that you make available to a customer.

Based on the assessment of the Azure AI workload, the customer team should feel empowered to move to the next stage of their deployment.

## Customer Participants

Having the right customer participants in the deployment oversight is essential to completing a successful engagement. Ensure the customer roles outlined below are available and able to participate in the engagement.

|Customer Role | Description | Required or Optional|
|----|----|----|
|AI and App workload owner (stakeholder)|The person(s) responsible for the workload to be enhanced with AOAI (Azure OpenAI) | Required|
|Lead Developer/Architect| Responsible for delivering, reviewing, and maintaining the App/AI Code and Design and approving the outcome(s) of the oversight engagement. They will be also responsible for working with other customer IT professionals to make sure their feedback and recommendations are included in the design, and that the workload is secure, integral, and available to design specifications | Required|
|App DevOps|Responsible for maintaining app-stack code and functionality | Required|
|Infra DevOps/DevSecOps | Team responsible for deploying application to production, maintaining production platform(s) and automation code| Required|
|AppSec/ProdSec/InfraSec/Identity | Team responsible for security and identity management across all aspects of the application and Infrastructure | Required|
|Data Scientist|Team members working on machine learning experiments and models|Optional|
|Data Architect|Team member working on data structure and data platform solutions|Optional|
|Other IT professionals| These are the people responsible for provisioning and managing IT resources like databases, networking, compute, IAM ops, Security ops, etc. | Optional|

> [!NOTE]
> Not all stakeholders are always required. Their availability will help remove road blocks in a timely manner. For example, a database administrator may be required to provision access to database used in the PoC.

 
## Scoping

### Ensure the delivery aligns well with the customer requirements

#### MCEM activity alignment

Ensure you understand when a different MCEM activity might be more suitable and discuss the best solution for the customer's problem. The CSAM can assist in making any necessary adjustments to the engagement.

#### Product and scenario alignment

> [!IMPORTANT]
> This section provides a selection of pre-configured solutions and tools for consideration before the ADS session focused on developing AOAI-driven applications tailored to your customers' needs.

Confirm that the customer's use case is well-suited for Azure AI, or determine if a different, more managed solution would better meet their needs.

### VBD Flexibility and Modularity

VBD Engagements are offerings characterized by their flexible timing and modular content. For more information, see [VBD Flexibility and Modularity](https://aka.ms/VBDFlexibility).

### Scoping Call with the customer

It is recommended to schedule the scoping call at least two weeks before the delivery.

**Pre- Scoping**
To understand the customer's background and validate expectations, see [Pre-Scoping Call with CSAM & CSA](https://aka.ms/VBDPre-scoping). This call precedes the customer scoping call.

This phase is crucial to ensure expectations are set, prerequisites are met, stakeholders are identified, outputs are clear, and all parties have time to research and prepare.

* Ensure the CSAM is included and kept up to date on all communications with the customer.
* Confirm that you have a dispatch for the engagement.
* The CSAM can assist with this and is responsible for dispatching you.
* Clarify who will send the meeting invites and establish the working "rhythm".
* Understand the nuances related to the account you are working on, including any political, sales, account renewals, difficult points, or other considerations.

Next, complete the customer scoping for this engagement. The CSAM should assist in booking a scoping call with the customer-side Business Sponsor and any relevant stakeholders.

During the scoping call, plan to:

* Agree on session objectives and required resources.
  * It may be convenient to exchange these via Teams or email ahead of the call.
* Ensure a clear understanding of customer objectives and goals.
* Prepare the agenda and email it to the customer before the call.
* Outline the planning and next steps.
* Clarify any logistics, especially for on-site delivery.

#### Scoping Questions by Outcome Area

Use the questions below as a reference while you scope the engagement on Solution Optimization

**Cost Optimization**
- What are your current cost drivers for AI/ML workloads on Azure?
- Do you have visibility into token usage and model execution costs?
- Are there long-running models or endpoints that could benefit from optimization?
- How do you currently attribute costs across teams, apps, or business units?

**Monitoring**
- What tools are you using today for monitoring ML models and infrastructure?
- Do you require real-time alerts for model drift, latency, or failures?
- How do you track model performance post-deployment?
- Are you using Azure Monitor or Application Insights with AzureML?

**Performance Improvements & Resiliency**
- Are there known performance bottlenecks in your current ML workflows?
- Do you use autoscaling or caching for model endpoints?
- What is your current strategy for failover and high availability?
- How do you measure and tune throughput and response time?

**Governance (Resource Org, Tagging, RBAC)**
- How are your Azure resources currently organized (e.g., by project, team, region)?
- Do you enforce tagging policies for traceability and cost management?
- What RBAC roles are in place for ML engineers, data scientists, and app developers?
- Are there governance policies for model approval and promotion?

**Security (Network, Policy, Identity, Data)**
- Are your ML environments network-isolated (e.g., VNet integration)?
- What policies are enforced for data access and model deployment?
- How is identity managed across ML and app teams (e.g., managed identities, AAD)?
- Are you encrypting data at rest and in transit?

**MLOps**
- Do you have CI/CD pipelines for model training and deployment?
- Are infrastructure and environments defined as code (e.g., Bicep, Terraform)?
- How do ML and app teams collaborate during development and release?
- What tools are used for versioning models, datasets, and experiments?

**Model Training Specific Questions**
- What is the client's expected runtime for pipeline, notebook, ML model etc.  
- What is the current baseline for the slow running object?
- Details on the dataset that is being ingested, or modeled.
    - what type of data is in the dataset.
    - can the ingestion be incremental, or transformed.
    - where is the data being sourced from.
- Details on what type of ML models the client is trying to build \ deploy
    - What packages is the client using.
    - Can the Data Frames be converted.
- What is the Success Criteria that meets the client's expectations with each use case.
    - Are client's expectations in line with the Services Capabilities or SLA. 

Use the scoping call to confirm:

* What are the customer's goals for the workload?
* What workload(s) and teams are involved in the engagement?
* How much experience does the customer have in building AI apps?
* What considerations or preparations have they already made for their upcoming production deployment?
* What is the planned outcome after the review with the customer teams?
You should also:
* Review the delivery assets with the customer based on the workload that needs the solution assessment.
* Address potential blockers or uncertainties that could jeopardize the workload's deployment or any other integrated/connected workloads.
  * Is the integration of Azure OpenAI the most efficient solution for solving the customer's problem at a production scale?
    * If not, inform the CSAM and account team so they can make necessary adjustments in the future.

At the end of the scoping call, recommend a high-level agenda for the engagement duration.

Scoping call outcomes:

* Assess the skill levels of the data scientists, developers, operations, and security teams.
* Ensure the existing application workload has been identified and agreed upon by all relevant stakeholders.
* Understand the infrastructure and identify any security requirements, boundaries, or control systems.
  * Clearly identify and understand the underlying infrastructure type, such as compute and data platforms.
* Agree on expectations and outcomes with the customer.
* Establish who will attend the session.
* Confirm logistics and send meeting invites.


</BR>

- It would be a good idea to recommend a high level agenda on how you plan to handle this engagement. For example, what type of services, training, delivery etc., would you be planning as a part of the delivery. Also, roughly a ball park range of the duration of engagement will be useful for the customer to plan on their side.

- Verify Access to customer environment
   - Check if the customer has access to an Azure Subscription that they can test any demos or labs 

</BR>

At the end of scoping, set clear expectations on what is in scope and what is out of scope with the customer. Use the table below as a guide

| **Success Criteria**  |
|---------         |
|Success Criteria will be determined on the scoping call, some examples below: <br> &bull; What specific KPIs or metrics define success for this engagement?,  <br> &bull; Are there baseline benchmarks for cost, latency, or model accuracy? <br> &bull;  What timeline and milestones are expected for implementation? <br> &bull; Who are the key stakeholders responsible for sign-off?|

## Delivery Guidance

This section includes all non-technical delivery guidance and supporting artifacts for the Proof of Concept you can deliver.  You are free to adapt each step to meet your customers needs as long as you are able to meet the objectives and deliverable standards.
Any optional requirements have been marked out.

## Overview

In this engagement, we oversee the solution optimization of Azure Machine Learning and Model related deployments across the pillars mentioned earlier such as Cost, Monitoring etc,  ensuring it aligns with the solution assessment and adheres to Well-Architected pillars. Our goal is to optimize without any blockers that could jeopardize the production workload. A Microsoft Cloud Solution Architect (CSA) will ensure the solution meets the desired outcomes while following best practices and patterns.

To support the customer in this scenario, various engagement options are available. The Supporting Material section below provides resources to explore.

You are encouraged to add, develop, customize, and leverage other documentation, training, and content from different scenarios to ensure successful delivery.

#### Deliver the selected scenario
  In order to assist the customer with this scenario, various engagement options are mentioned below.  You are not limited to the below engagements.  You are more than welcome to add, develop, customize, leverage other documentation, training, content from other scenarios that can help you deliver this successfully. 

- Understand key decisions, features, and functionality built into the solution
- Highlight gaps in Solution based on Best Practices for prioritized solution scenarios
- Build improvement roadmap for enhancing business value
- Assist with implementation of scoped optimization recommendations for current solution

Below are various **deliveries, documents and other assets** that you can leverage.  Note you are NOT limited to or bound by below deliveries.  You have the freedom to use the below deliveries, come up with your own custom deliveries, mix and match, etc. to reach a solution that is favorable to customer.

**Internal-Only guidance**

| Delivery Type | Delivery Name | Customer Level | Target Audience | Delivery Method|Use Case | Outcome
| --- | --- | --- | --- | --- | ---| ---|
| Guidance (Internal-only)* | [AOAI Model Migration Guidance](https://aka.ms/aoai-model-migration-guidance) | Intermediate | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architects | Discussion / Guidance| This guidance document offers internal field teams a systematic approach for migrating to newer Azure OpenAI models based on model retirements and deprecation considerations | To maintain continuity, optimize performance, and minimize business disruptions when current model versions are deprecated or retired

> [!NOTE]
>Guidance marked (Internal-only)* is for internal consumption only and should not be shared with customers

**External guidance by Outcome area**
**Outcome Area - MLOps/Data Flows**

| Outcome Area | Delivery Type | Delivery Name | Customer Level | Target Audience | Delivery Method|Use Case | Outcome
| --- | --- | --- | --- | --- | --- | ---| ---|
MLOps| Training  | [MLOps model management with Azure Machine Learning ](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2) | Advanced | ELT Developers, Data Engineers, DevOps Engineers  | Discussion, Hands On | Use machine learning operations (MLOps) to manage the lifecycle of your models  | Improving Quality and consistency of MLOps solutions
MLOps/Dataflows| Training  | [Optimizing Mapping Data Flows Overview ](https://learn.microsoft.com/en-us/azure/data-factory/concepts-data-flow-performance) | Advanced | ELT Developers, Data Engineers  | Discussion, Hands On | Use case gathered from scoping call  | Mapping Flow is Optimized

**Outcome Area - Cost**

| Outcome Area | Delivery Type | Delivery Name | Customer Level | Target Audience | Delivery Method|Use Case | Outcome
| --- | --- | --- | --- | --- | --- | ---| ---|
Cost | Training | [Manage and Optimize Machine Learning Cost](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-optimize-cost)| Advanced | Data Scientists, Data Engineers, Azure Admin | Discussion, Hands On | Use case gathered from scoping call | Azure ML Cost Optimized
Cost | Reference/Training  | [Cloud Cost Optimization ](https://azure.microsoft.com/en-us/solutions/cost-optimization/#training) | Intermediate/Advanced | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architects | Discussion/Hands-on | Cloud cost optimization training and tools   | Get an understanding of cloud cost optimization and the available tools to achieve cost optimization


**Outcome Area - Monitoring**
Monitoring| Guidance | [Monitoring Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/monitor-azure-machine-learning?view=azureml-api-2 ) | Intermediate | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architects | Discussion / Guidance| Monitoring Guidance for Azure Machine learning resources | Understand monitoring options available for resources with Azure Machine Learning service
Monitoring| Guidance | [Azure Monitor Baseline Alerts (AMBA) for AI workloads](https://azure.github.io/azure-monitor-baseline-alerts/patterns/artificial-intelligence/) | Intermediate | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architects | Discussion / Guidance| Azure Monitor Baseline Alerts (AMBA) enhances your Azure experience by offering essential metrics and guidelines for optimal performance. It provides expert recommendations, near real-time notifications, automation policies, guided documentation, and enhanced resiliency for a proactive and informed Azure monitoring approach. | Understanding essential metrics and guidelines to ensure Azure services that are a part of Generative AI Deployments are performing optimally.


**Outcome Area - Performance Improvement and Resiliency**
Performance Improvement and Resiliency| Guidance | [Reliability and Resiliency Azure Machine Learning](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-machine-learning#reliability ) | Intermediate | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architects | Discussion / Guidance| Reliability and Resilieny best practices for Azure Machine learning resources | Understand options available to configure resilency for resources with Azure Machine Learning service
Monitoring| Guidance | [Azure Proactive Resiliency Library v2(APRL) for AI workloads](https://azure.github.io/Azure-Proactive-Resiliency-Library-v2/azure-specialized-workloads/ai/) | Intermediate | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architects | Discussion / Guidance| APRL curated catalog of resiliency recommendations for workloads running in Azure, many of which include supporting Azure Resource Graph (ARG) queries to identify non-compliant resources | Understanding different recommendations for resiliency for resources deployed as a part of Generative AI Deployments


**Outcome Area - General Azure Environment Optimization**

| Outcome Area | Delivery Type | Delivery Name | Customer Level | Target Audience | Delivery Method|Use Case | Outcome
| --- | --- | --- | --- | --- | --- | ---| ---|
Optimization | Reference  | [Optimizing Azure Environment ](https://azure.microsoft.com/en-us/blog/how-to-optimize-your-azure-environment) | Intermediate/Advanced | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architects | Discussion/Hands-on |Optimizing Azure Environment using Azure Advisor, Azure Architecture Center  | Get an understanding the different areas Azure Environment can be optimized

**Outcome Area - Security and Governance**

| Outcome Area | Delivery Type | Delivery Name | Customer Level | Target Audience | Delivery Method|Use Case | Outcome
| --- | --- | --- | --- | --- | --- | ---| ---|
AML Security| Reference/Training  | [Securing AML workspace](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-secure-workspace-vnet?view=azureml-api-2&tabs=required%2Cpe%2Ccli) | Intermediate | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architect | Presentation/Hands-on |How to secure AML workspace and resources | Enables customers to secure AML workspace and resources.
AML Security and Governance| Reference/Training  | [Enterprise security and governance for Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-enterprise-security?view=azureml-api-) | Intermediate | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architect | Presentation/Hands-on |Security and governance features that are available for Azure Machine Learning| Enables customers to secure AML workspace and resources and create a secure configuration that complies with an organization's policies.


**Outcome Area - Model Management**

| Outcome Area | Delivery Type | Delivery Name | Customer Level | Target Audience | Delivery Method|Use Case | Outcome
| --- | --- | --- | --- | --- | --- | ---| ---|
Model Management| Reference/Training  | [Azure OpenAI Model Evaluation](https://aka.ms/DATAAI-IP/AOAIModelEval) | Intermediate | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architect | Presentation/Hands-on | Azure OpenAI model evaluation framework designed to aid customer in evaluating multiple models concurrently on same prompt, and selecting the right AI-assisted/NLP metrices to evaluate the model responses | Enables customers to build Azure OpenAI model evaluation framework to test the application for model migration.
Model Management| Repo | [Transition Embedding models](https://github.com/Azure/transition_embeddings_model) | Intermediate | AI Architects, Developers | Hands-on | Repository that leverages Azure AI Inference SDK and Azure AI Search to migrate indices from one embeddings model to another | When an embeddings model goes out of support the index has to be recreated. This repo automatically creates a new index using the new embeddings model.


**Outcome Area - Other**

| Outcome Area | Delivery Type | Delivery Name | Customer Level | Target Audience | Delivery Method|Use Case | Outcome
| --- | --- | --- | --- | --- | --- | ---| ---|
Other | Reference/Training  | [Azure AI Search - Service Statistics](https://learn.microsoft.com/en-us/rest/api/searchservice/get-service-statistics?view=rest-searchservice-2024-07-01) | Intermediate/Advanced | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architects | Discussion/Hands-on | Monitoring and Analyzing Azure AI Search Service Statistics for Object Count, Storage Utilization, and Tier-Based   | Gain a comprehensive understanding of service usage, storage consumption, and object limitations based on tier constraints. Utilize this data to optimize resource allocation and improve overall system performance.



---
</BR>

**Note:** Guidance marked (Internal-only)* is for internal consumption only and should not be shared with customers


> [!NOTE]
> You are NOT limited to or bound by above examples.
> You have the freedom to use the above examples, come up with your own custom deliveries, or mix and match to reach a solution that is favorable to the customer.
> You can use assets from any of the above deliveries in your dispatch based on scoping with the customer.

