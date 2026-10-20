# Delivery Guide: Proof of Concept to Build and Deploy Azure AI Platform

This guide will provide details and instructions to help you deliver the **Proof of Concept** activity for your customer.

## IPKit

The IPKit with artifacts to use throughout the delivery is located [here](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Apps%2FProof%20of%20Concept&newTargetListUrl=%2Fteams%2FASDIPRelease%2FAzureCloudAI&viewpath=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FForms%2FAllItems%2Easpx)

## Objectives

This engagement must accomplish the following objectives:  

- Deliver a functional small-scale version of the solution using Azure Machine Learning service and other related Azure services that can be used to determine its feasibility.
- Modernize an existing small-scale solution using Azure Machine Learning service and other related services that can be used to determine its feasibility.
- Demonstrate the architecture design is feasible.
  - This may include compete scenarios and integration with existing customer infrastructure, solutions, and applications.
- Reinforce design decisions.

## Deliverable Standards

- Outline Proof of Concept (PoC) application components and services based on architectural design.
- Develop PoC to validate a specific business scenario.
- Develop and deploy sample application workload that matches the business vision for future capabilities.
- A working PoC matching the customer needs and services as outlined during the scoping call. Some engagements may not require customer data.
- Customer acceptance and sign-off of the PoC is required for completion. Each PoC engagement should provide a roadmap to production in the close-out meeting.

## Customer Participants

Having the right customer participants in the Proof of Concept is essential to completing a successful engagement. Ensure the customer roles outlined below are available and able to participate in the workshop.

|Customer Role | Description | Required or Optional|
|----|----|----|
|Workload owner| The person responsible for the workload to be extended with Azure AI services | Required|
|Lead Developer/Architect| Responsible for delivering and reviewing PoC, Code and Design. He will be also responsible to work with other customer IT professionals to make sure their feedback and recommendations are included in the design | Required|
|Developers| Responsible for writing code and developing PoC | Required|
|DevOps/DevSecOps | Team responsible for deploying application to production| Required|
|AppSec/ProdSec/Security | Team responsible for security across all aspects of the application | Required|
|Data Analyst/Scientist/Engineer | Team responsible for the underlying data structures, platform, and services of the workload. | Required|
|Other IT professionals| These are the people responsible for provisioning and managing IT resources like databases, networking, compute, IAM, Security, etc.  | Optional|

> [!NOTE]
> Not all stakeholders are required at all times. Their availability will help remove road blocks in timely manner. For example, a DBA may be required to provision access to database used in the PoC.

## Scoping

### General Scoping Guidance

For a Proof of Concept engagement, it is required to hold a scoping call around two weeks (or more) before the delivery.

The scoping call allows you to verify if this MCEM activity aligns with the customer scenario and whether they are ready for a successful delivery.

During the scoping call please plan for and confirm the following:

- Have the agenda planned and e-mail it to the customer before the call.
- Agree on session objectives and required resources (can be sent before the scoping call).
- Have clarity and clear understanding of customer *objectives* and *goals*.
- Planning and next steps.
- Clarify any logistics (particularly in case of an on-site delivery).
- Identify which stakeholder will send any necessary meeting invites.

#### Pre-scoping - Internal

As a starting point, it is recommended you have an internal scoping call with the CSAM and account team (where applicable) in order to:

- Preview the date and time of the scheduled scoping call.
- Provide a high-level agenda for the scoping call.
- Gather as much customer information as possible like existing workload documentation and architecture diagrams (In some cases CSAM or other Microsoft person might not have all the information the CSA is looking for).

Make sure that you have ROSS dispatch for the engagement. CSAM can assist with this. They are responsible for the ROSS dispatch. There should be a corresponding MSX number.

To understand the customer's background and validate expectations, see [Pre-Scoping Call with CSAM & CSA](https://aka.ms/VBDPre-scoping). This call precedes the customer scoping call.

#### Important scoping considerations for Proof of Concept engagements

There are some specific considerations that you want to bear in mind for this delivery. It's important to clarify these during the scoping process either with the account team or the customer.

##### Defining your goal and success criteria

- Set the goal on what you want to accomplish from your proof of concept project and determine what would be considered a successful execution of your project by stating the success criteria.
- We want to prove whether a concept works or not without investing a huge amount of time and resources.
- If the proof of concept project succeeds and achieves the expected results, the project team can give the green light to proceed with the next steps.
- However, should the experimentation fail, it would have failed within a fixed budget, timeline, scope, and set of resources, which would be minimal costs in the grand scheme of things.
- Therefore, the benefit of doing a proof of concept project is that it allows the project team to quickly determine whether to continue to pursue the concept, abandon it, or make alternate choices.
- Bear in mind when scoping out your project that the goal of your proof of concept is to succeed quickly (and conversely, fail quickly) so that subsequent decisions can be made in a timely manner.

##### Assembling your team

For a small one-off, simple, non-critical experimental proof of concept, a one-person team might suffice. However, for most typical proof of concept projects where the results are critical and could influence the decision of a bigger project, you should identify the mandatory team members needed and the commitment required to support your proof of concept.

The team that you are assembling must reflect the scope of your project.

For a successful PoC delivery, it is better to act in a consulting position rather than to do hands-on coding. If the customer does not have enough resources to help with the PoC and is not familiar with Azure AI services, then you may have to get hands on.

Use your judgment to best achieve your goal: Your **first** goal is to deliver a working PoC, and the **second** one is to empower the customer team to develop similar solutions in the future. If we fail to achieve either, then customer may not be able to reap the benefits of the engagement after it is over.

##### Keep the scope as small as possible

Keep in mind that you are developing a proof of concept to validate whether a concept is feasible. You must keep the goal of your project achievable within your well-scoped timeline.

When you create your high-level architecture, you must decide which essential components will be part of the proof of concept and which non-essential components should be excluded from it.

As a rule of thumb, the more Azure AI components you include in your proof of concept, the more complicated your project will become and the longer it will take to achieve your success criteria.

#### Scoping Call

During the scoping call you are going to explain:

- How the delivery will be carried out.
- What the customer can expect at each phase.
- What the customer can expect before and after the delivery.

Ask the customer to nominate the stakeholders required for a successful delivery. Refer to the [Customer Participants](#customer-participants) section for details.

Review architectural design diagram(s) or document(s) that will be used as blueprint to develop the PoC.

It's important to reuse materials shared in the pre-scoping phase with the account team to build on existing work where available.

Understand the requirements and resources required to deliver the PoC. Ensure they are clearly documented and communicated to the customer.

Also ensure all the stakeholders are on the same page regarding deliverables (PoC) - **not only what a PoC includes, but also what is out of scope**.

> [!NOTE]
> If the customer does not have an architecture design, then review with the CSAM and decide whether an Architecture Design Session should be conducted first to increase the chance of a successful delivery.
>
> If a full ADS cannot be run, you will have to work with the customer to design and architect the AI solution and that may significantly increase the time required to deliver this VBD.
>
> The CSAM can help adjust the engagement to the right time frame as required.

Identify all non-functional requirements like network access, database access etc.

Additional scoping questions as it relates to Azure Machine Learning are below:
- What is the primary business objective you aim to achieve with this PoC using Azure Machine Learning?
- Which type of use case is most relevant for showcasing AzureML’s capabilities in your organization?
  - Predictive Analytics, Optimization tasks, Classification or any other topic?
- What is the current level of familiarity with Azure Machine Learning among your technical teams?
- What metrics will you use to evaluate the success of the PoC?
  - Accuracy and performance of models, reduction in time to insight, Improvement in Operational Efficiency
- How do you plan to scale the solution if the PoC is successful?
- What is the primary goal of MLOps in machine learning workflows?
  - Automate Data pre-processing, to ensure reproducilbility and scalability of ML Models, to improve acccuracy etc
- What are some areas of monitoring you would like to focus on within the scope of Azure Machine Learning service deployment
  - Model monitoring, cost monitoring, data drift detection etc


Ask the customer to complete the below pre-requisites before the VBD engagement starts:

- Azure subscription available, and participants have appropriate access to test any demos or labs.
- Developer environment for each participant (install Visual Studio Code, Microsoft Dev Box, GitHub Copilot, others.).
- Any other tools or environments as appropriate for the scope of the PoC.

If the pre-requisites are not met, it may jeopardize the delivery of the PoC on time.

Ask open scoping questions to fully understand what the customer wants to achieve. Document their responses for your delivery preparation. A set of sample scoping questions has been given in the section below.

Finally clarify who would be sending the meeting invites - CSAM, TSP, CSA, customer or someone else, once the engagement has been confirmed after the scoping call with the customer.

If it's an on-site delivery, don't forget to discuss any related logistics to the trip.

For information about the customer scoping call, roles, and outcomes, see [Scoping Call](https://aka.ms/VBDScoping).

##### Scoping Questions

This is important as it may help you discover that a different VBD offering is more appropriate for their proof of concept.

You may also use this document as a reference for your scoping questions: [Scoping Questions](scoping-questions.md).

> [!TIP]
> To ensure that your proof of concept project can be scoped and completed in a timely manner, keep the workloads and scenarios as small as possible.
>
> Choose a timeline that aligns well with the planned scope, such as two or four weeks.
>
> If you find that your proof of concept is estimated to run for a long period of time, consider reducing its scope to focus on the highest priority goals.

## Delivery Guidance

This section includes all non-technical delivery guidance and supporting artifacts for the Proof of Concept engagement. You are free to adapt each step to meet your customer's needs as long as you are able to meet the objectives and deliverable standards for the Proof of Concept.

### VBD Flexibility and Modularity

Keep in mind that an engagement can effectively accommodate duration flexibility and content modularity. For more information, see [VBD Flexibility and Modularity](https://aka.ms/VBDFlexibility).

#### Prepare for the delivery

Prepare for the Proof of Concept delivery with the information collected during scoping.

- Draft/update a solution architecture design diagram.
- Draft a PoC scoping document that articulates what is in scope and what is out of scope.
- Select and test code samples and accelerator resources which best fit customer scenario.

#### Find Supporting Material

While building out a Proof of Concept might involve work specific to customer requirements, here are some resources that might be able to kick start your development.

Below are various **deliverables, documents, and other assets** that you can utilize. Please note that you are not limited to or bound by these deliverables. You have the freedom to use the provided deliverables, create your own custom deliverables, mix and match, etc., to reach a solution that is favorable to the customer.

| Delivery Type | Delivery Name | Customer Level | Target Audience | Delivery Method | Use Case | Outcome
| --- | --- | --- | --- | --- | ---| ---|
| Solution Accelerator  | [MLOps V2 Solution accelerator](https://github.com/Azure/mlops-v2)| Advanced| Data scientists, Data Science Managers, MLOps Engineers, Infrastructure Engineers | Demo| Implement MLops with GitHub, Azure Devops with Azure Machine Learning  | Customer will have an understanding on how MLops can be implemented with Azure Machine Learning
| Delivery Guide | [Azure ML PoC VBD Supporting Material](https://aka.ms/DATAAI-IP/DetailedPoC) | Intermediate | Data Scientist, Data and Domain Experts, Business stakeholders  | Presentation, Hands-on Development | Delivery guide supporting material on data and domain understanding as well as Azure ML PoC delivery support, including delivery planning, timelines, ML Ops considerations, and helpful links. | This delivery guide material supports stronger understanding of Azure ML PoC delivery from domain and data understanding perspective. Better alignment on customer success criteria, outcomes, and project plans / timelines. | 
| Git Repo | [largescale-deep-learning](https://github.com/Azure/azureml-examples/tree/main/best-practices/largescale-deep-learning/Training) | Intermediate | Data Scientist, Data and Domain Experts, Business stakeholders  | Presentation, Hands-on Development | Delivery guide supporting material training Deep Learning models. | This repo outlines best practices to allow you to train large models very efficiently with high throughput in AzureML, leveraging full utilization of GPU to keep the cost low. |



#### Kickoff

The delivery starts with a kickoff. Schedule a session with the customer in order to kick off the engagement and make sure customer stakeholders are aligned on the PoC options and structure.

1. Review and validate PoC scope and outcomes with stakeholders. Make sure all members on both teams have a copy of this scope document.
2. Review and finalize solution architecture design.
3. Draft a PoC high-level plan and review the timeline with customer stakeholders.
4. Validate environments pre-requisites and teams availability for PoC execution.

While 'perfect' is the enemy of 'good', avoid the temptation to start the PoC execution prematurely without the necessary deliverables and if the environment/tools prerequisites are not met.

Use your judgment to validate consistency and quality level of the above deliverables. If you find any gap, then schedule additional sessions with customer to address them.

For more information, refer to the [IPKit](#ipkit) for the kickoff templates.

#### Proof of Concept Execution

During PoC execution you may work offline or contact the customer team developers ad-hoc, it is recommended you have regular team sync calls/meetings.

This helps define the right rhythm to align on PoC implementation status as you:

- Utilize the architecture design diagram as a reference for the development of the PoC.
- Break down high-level tasks into low-level tasks.
- Introduce the customer to the relevant Azure AI services included in the PoC.
- Utilize the developers in the customer team and assign tasks to them either directly or with the assistance of their team lead.
- Mentor and encourage developers in the customer's organization. Remember, a successful engagement will empower their developers.
- Monitor the scope, schedule, and cost, and provide education on the reasons for choosing one option over another.
- Towards the end of the delivery, discuss the long-term support of the project, such as involving Microsoft Partner Organizations, upskilling the customer's internal team, ECIF funding, and community resources.

#### Presentation

Once your Proof of Concept (PoC) is complete, evaluate whether you have met the success criteria defined during the scoping phase and consolidate the findings at the end of the planning phase.

Schedule a presentation session to demonstrate the PoC and share conclusions with the customer. Ideally, the customer team would have been engaged throughout the delivery, and you can encourage their involvement in the presentation:

- Determine who will kick off the presentation.
- Schedule the meeting in the morning, if possible.
- Prepare the demos and slides.
- Conduct a dry run to refine the presentation.
- If the customer asks questions you are unsure about, record them and provide an estimated timeline for follow-up.

##### If your Proof of Concept (PoC) was unsuccessful

- You have to pick a way forward:

  - Retry the proof of concept by redefining the goal, timeline, budget, scope, and architecture.
  - Conduct a post-mortem review on the failure to see if there is any insights or lessons learned during the proof of concept.

If time permits consider to include the engagement closeout activities as part of the presentation session. If not possible, then schedule a separate session.

#### Reporting

A closeout report is required to document the delivery and solution that was implemented. For more information, see [Actual Delivery: Report Deliverable](https://aka.ms/VBDReporting).

#### Closeout

At the end of the engagement, schedule a closeout meeting to wrap up the engagement. This meeting is the final activity performed as part of the engagement. The findings are presented to the customer, and recommendations are delivered. It is also an opportunity to propose any follow-up engagements identified during this delivery. Topics related to the closeout meeting include:

- Results of the PoC, mapped to the original requirements.
- Recommendations resulting from the implementation.
- Gathering customer feedback and satisfaction.
- Discussion on how to proceed and operationalize the PoC.
  - If possible, provide a high-level estimate of costs in terms of both human and technical resources, along with a timeline.
  - Ensure the CSAM and wider account team are aware of the next steps to align the right support.
- Determining customer satisfaction.
- Discussing the plan to share VBD materials after the engagement and providing your contact information for follow-up.
- Explaining that Microsoft may reach out with an invite to evaluate the engagement.

Send the customer an email summarizing all activities performed, including details of the final state of the PoC. Share any relevant resources and copy the account team to ensure the next steps are implemented promptly.

Refer to the [IPKit](#ipkit) for the closeout templates.

### Share feedback with the account team

Engage in follow-up conversations to discover new opportunities. Discuss with the delivery lead or CSA any next steps and recommendations to accelerate deployment or optimization. For more information, see [Post Delivery Activities](https://aka.ms/VBDPost-Delivery).

## Additional Resources & References

### [Learning Resources](#tab/Learning-Resources)

- [AI Learning hub](https://learn.microsoft.com/ai/)
- [OpenAI Readiness - Foundational](https://learningpath.microsoft.com/8228): Introduces Azure OpenAI concepts, use cases and provides resources to demos that you can use to showcase capabilities to customers.
- [OpenAI Readiness - Intermediate](https://learningpath.microsoft.com/8232): Immerse further with technical training resources and more in-depth understanding of technical concepts.
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners): Course with lessons and labs covering the fundamentals of building AI Agents.
- [CSU AI LevelUp Series](https://microsoft.sharepoint.com/teams/LevelUpSkilling/SitePages/LevelUp-AI.aspx)

### [GenAIOps Considerations](#tab/GenAIOps-Considerations)

- [GenAIOps with PromptFlow](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-end-to-end-azure-devops-with-prompt-flow?view=azureml-api-2)
- [Maturity assessment for GenAIOps](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/concept-llmops-maturity?view=azureml-api-2)
- [Evaluation of generative AI applications](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/evaluation-approach-gen-ai)
- [Monitoring and traceability for deployed Azure OpenAI Models](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/monitor-openai)
- [Incorporate A/B testing for testing intelligent apps](https://azure.microsoft.com/en-us/blog/achieve-generative-ai-operational-excellence-with-the-llmops-maturity-model/)

### [GenAI Patterns and Frameworks](#tab/GenAI-Patterns-and-Frameworks)

- [RAG in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
- [RAG - Designing and developing a RAG solution](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide)
- [RAG - Evaluator](https://github.com/Azure-Samples/ai-rag-chat-evaluator)
- [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/prompt-flow)
- [Agents - How to use function calling with Azure OpenAI service](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling)
- [Agents - Azure OpenAI Assistants API](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/assistants)
- [Agents - Develop AI agents with Semantic Kernel](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-azure-open-ai-semantic-kernel-sdk/)
- [Semantic Kernel - Introduction](https://learn.microsoft.com/en-us/semantic-kernel/overview/)
- [Azure AI Agent Service - Documentation](https://learn.microsoft.com/en-us/azure/ai-services/agents/overview)
- [AutoGen - Official Documentation](https://microsoft.github.io/autogen/stable/index.html)

### [Public Documentation and Resources](#tab/Public-Documentation-and-Resources)

- [Azure OpenAI in a Day](https://microsoft.sharepoint.com/teams/CSUDataAICommunityIPLibrary/Shared%20Documents/Forms/AllItems.aspx?id=%2Fteams%2FCSUDataAICommunityIPLibrary%2FShared%20Documents%2FAzure%2DAI%2DBuilding%2DIntelligent%2DSolutions%2FAzure%2DOpenAI%2Din%2Da%2DDay%2FPPTs%2FLatest%20Decks&viewid=ab71ea0d%2Dce8e%2D4932%2Da091%2D5173f4ecc8ab)
- [Develop AI apps using Azure AI services](https://learn.microsoft.com/en-us/azure/developer/ai/azure-ai-for-developers?tabs=dotnet)
- [Azure Well-Architected Framework on Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-openai)

### [Supporting Concepts](#tab/Supporting-Concepts)

- [Grounding LLMs - RAG](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/grounding-llms/ba-p/3843857#:~:text=What%20is%20Grounding%3F,relevance%20of%20the%20generated%20output.)
- [RAG - Retrieval and document chunking strategies](https://aka.ms/ragrelevance)
- [Semantic Kernel - What it is and Why it matters](https://techcommunity.microsoft.com/t5/azure-developer-community-blog/semantic-kernel-what-it-is-and-why-it-matters/ba-p/3877022)
- [Azure AI Agent Service - Introduction](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357)
- [AutoGen - Introduction](https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications/)
- [RAG Hack Series](https://github.com/microsoft/RAG_Hack?tab=readme-ov-file#raghack-lets-build-rag-applications-together)

### [Community Support](#tab/Community-Support)

- [Semantic Kernel Teams Support](https://teams.microsoft.com/l/team/19%3aW5nYJLrRvQatcJ04yDmCkzm-t7B6c7VTxS57yNtvSzU1%40thread.tacv2/conversations?groupId=a87ae912-78ce-4eb9-862a-e7edf1b2aaa6&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47)
- [Semantic Kernel Discord Community](https://aka.ms/SKDiscord)
- [Submit EA engagement](https://microsoft.sharepoint.com/teams/AIEngagements/)
- [Teams Channel - VBD - AI Apps and Agents](https://teams.microsoft.com/l/channel/19%3Adc692f3bec324088bbe5b9d07565c0f2%40thread.tacv2/VBD%20-%20AI%20Apps%20and%20Agents?groupId=591c20e8-6a02-4476-8881-849bf672e6cf&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47)
