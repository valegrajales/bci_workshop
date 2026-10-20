<!-- 

Some sections are optional if the content is not available like 1.1 Activity deep dive video or Other resources, readiness and references

-->

# Workshop - Foundry and Copilot Studio Agents with Microsoft Agent Factory

This delivery guide helps the instructor/CSA prepare, scope, deliver, and close the workshop consistently, ensuring participants leave with working prototypes, a reference architecture, and a clear path to production.



## Objectives and Outcomes

:point_down:
<details><summary><b>Click to expand to show more details.</b></summary>
</br>

**Objectives**
This training offers an opportunity for the audience to gain hands-on experience with the product features through guided labs.
* Gain practical experience integrating Copilot Studio with Azure AI services through step-by-step guided labs.
* Build and configure RAG-enabled copilots using Azure AI Search, vector indexes, embeddings strategy, and Azure AI Foundry models.
* Helping the audience understand the value of Copilot Studio/Azure AI Services for their organization.
* Preparing the audience for their next steps, such as executing Proof of Concepts (POCs), architecting and designing solutions, and deploying solutions in production

**Outcomes**

After attending the sessions, customers will walk away with
- Knowledge to execute Proof of Concepts (POCs) for building solutions with Azure AI Services and Copilot Studio.
- Understanding of how to architect and design solutions using Copilot Studio and Azure AI Services.
- Skills to deploy these solutions in production environments

**Customer Skilling Outcomes**

Organizations investing in Agent Factory training will achieve strategic and operational benefits:

*Technical Capability Development*
- Build internal expertise to design and deploy autonomous AI agents using Microsoft Agent Factory
- Establish competency in agentic AI architecture, orchestration, and multi-agent system coordination
- Develop skills to integrate agents with Azure AI services and copilot Studio

*Business Impact and ROI*
- Reduce reliance on external consultants for agentic AI development and deployment
- Accelerate delivery of intelligent automation solutions through in-house agent development capabilities
- Scale agentic AI initiatives across business units with trained internal resources
- Lower total cost of ownership through sustainable internal expertise and knowledge retention

*Strategic AI Advancement*
- Position organization as early adopter in the emerging field of agentic AI and autonomous systems
- Build competitive differentiation through advanced AI agent implementation capabilities
- Create foundation for innovation in autonomous workflows, intelligent automation, and AI-driven decision-making
- Develop sustainable AI talent pipeline with specialized agent development and orchestration skills



</br>


<!-- If no details, delete the <details> section and the following </br>-->

## 1 Prepare

Prior to delivering the workshop, as a CSA, ensure that the the following activities are taken care of, atleast a week before engaging with the customer.

</br>

### 1.1 Pre-Scope

Discuss with the account team your customer needs for this delivery

- :ballot_box_with_check: To understand the customer's background and validate expectations, see [Pre-Scoping Call with CSAM & CSA](https://aka.ms/VBDPre-scoping). This call precedes the customer scoping call. This call is scheduled internally with the account team and pinned CSAs.
- :ballot_box_with_check: Learn about the previous stage's status from the Account team, including the Architecture Design document, if available to understand the customer's familiarity with Azure AI services and use cases.
- :ballot_box_with_check: During the pre-scoping call, sync with CSAM and TS (Technical Specialist) to verify if a POC or any upskilling session was already delivered.

:point_down:
<details><summary><b>Click to expand to show more details.</b></summary>
</br>

#### Customer participants

Having the right customer participants in the workshop is essential to completing a successful engagement. Ensure the customer roles outlined next are available and able to participate in the session.

- Azure AI Platform Administrator  
- Data Scientist  
- AI Solution Architect  
- Application Developer  
- IT Security Specialist
- AI Engineer
- AI Developers
* IT Professionals



</details>

### 1.2 Scoping

For information about the customer scoping call, roles, and outcomes, see [Scoping Call](https://aka.ms/VBDScoping). Refer to the [IP Kit](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Platforms%2FWorkshop%20%2D%20Foundry%20and%20Copilot%20Studio%20Agents%20with%20Microsoft%20Agent%20Factory&viewid=873d8354%2D6178%2D4477%2Dba09%2D824a43c12873&ovuser=72f988bf%2D86f1%2D41af%2D91ab%2D2d7cd011db47%2Capthomas%40microsoft%2Ecom&OR=Teams%2DHL&CT=1750083286585&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNTA2MDIwNjYwOCIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D&share=cgrYqDEQ5zDdSbU5k6BCjQe%2DEgUCwyFGQbrn9wNJwGcKzy50NA) for links to scoping call artifacts.

Setting the expectations (Goals, Timing, Prerequisites Check, Outcomes, Challenges) with the customer.

- :ballot_box_with_check: Ensure the customer understands how to set up lab environment and access to the lab environment
- :ballot_box_with_check: Coordinate module selection with the customer, prioritizing those that will be most beneficial to them based on delivery timelines as this is 3 day delivery
- :ballot_box_with_check: Ensure customer is familiar with the lab setup process and has set up access to skillable environment
- :ballot_box_with_check: Finalize logistics and owner to send the meeting invite and agree on times for the delivery

Hera are some scoping questions generated by module to help guide on what questions to ask the customer to choose modules that will best fit their need:

#### 🔍 Scoping Questions by Module

🧩 Copilot Studio Overview

- Are you working with customers who need to build custom copilots or automate workflows using low‑code or pro‑code tools?
- Do you need to orchestrate conversations, actions, connectors, and RAG experiences within a secure enterprise environment?
- Is visibility into analytics, governance, ALM, and environment strategies important for your deployment scenarios?


🏭 Microsoft Foundry Overview

- Do you need a unified platform to design, evaluate, and deploy AI models and agent workflows at scale?
- Are you supporting customers who require model experimentation, grounding, safety evaluations, or PTU-based deployments?
- Is deep integration with enterprise data, vector search, and multi-model catalogs essential for your AI solutions?


🛡️ Governance for Copilot Studio & Microsoft Foundry

- Are you advising customers on roles, responsibilities, intake processes, and data governance for AI solutions?
- Do you need to ensure compliance through DLP, environment isolation, identity controls, and evaluation gates?
- Is consistent oversight of prompts, connectors, plugins, and model lifecycle upgrades critical to your projects?


🔗 Integration: Copilot Studio & Microsoft Foundry

- Are your AI solutions benefiting from combining Foundry’s model development capabilities with Copilot Studio’s orchestration and UI layer?
- Do you need to integrate models, RAG pipelines, APIs, and tools from Foundry directly into Copilot Studio agents?
- Is end‑to‑end reliability—ALM, monitoring, telemetry, safety, and lifecycle management—important across both platforms?


:point_down:
<details><summary><b>Click to expand to show more details.</b></summary>
</br>

At the time of scoping leverage the following information to discuss with the customer on which modules they would like to prioritize based on the 3-day delivery timelines.

**Note:**   You can bypass the slides you don’t need to cover
 
 - **Copilot Studio Overview:** This module provides an end-to-end overview of Copilot Studio as the platform for building and orchestrating custom agents and copilots. It covers topics, actions, connectors, RAG, and integration with M365, Dynamics, Power Platform, and Azure. Participants learn about lifecycle management, ALM, environments, permissions, and analytics. The module emphasizes guardrails, safe prompting, content policies, and structured conversations. It demonstrates how low-code and pro-code teams collaborate to deliver enterprise-grade copilots.

- **Microsoft Foundry Overview:** This module introduces Azure AI Foundry as the unified platform for developing, customizing, evaluating, and deploying AI applications and agents. It covers the model catalog, prompt and grounding workflows, evaluation pipelines, and deployment options. Participants learn about PTUs, quotas, security boundaries, and environment isolation. The module shows how Foundry integrates with Copilot Studio, AI Search, vector databases, and application backends. It also highlights MLOps/LMMOps best practices for reliability and scale.

- **Governance for Copilot Studio & Microsoft Foundry:** This module defines the governance framework for AI solutions built on Copilot Studio and Foundry. It covers roles, intake processes, data policies, DLP, environment strategy, and identity controls. Participants explore evaluation gates for safety and quality, red teaming routines, telemetry standards, and incident response. The module explains change management for prompts, actions, plugins, and model upgrades. It includes practical artifacts—checklists, RACI matrices, and review workflows—to ensure secure and compliant deployments.
  
- **Integration: Copilot Studio & Microsoft Foundry:** This module explains how Copilot Studio and Azure AI Foundry work together to deliver enterprise-grade agents. It covers how Foundry provides model development, evaluation, safety, and deployment, while Copilot Studio serves as the orchestration and UI layer. Participants learn integration patterns using APIs, connectors, plugins, RAG pipelines, and function calling. The module highlights ALM, monitoring, and responsible AI across both platforms. It demonstrates how combining both tools accelerates innovation while ensuring reliability, security, and governance.


</details>


### 1.3 Review Workshop content and Labs

At time of accreditation, you may have already done through the powerpoint slide, labs and demos. Ensure that you take time to go through the workshop and demos to ensure you have the latest changes incorporated and the sections go through periodic updates

### 1.4 Prepare deliver


Ensure that you understand the  labs requirement, adn the custumer have them set up and ready to be delivered ( It’s completely fine if we can’t complete all parts of the labs or need to skip some of them, as the labs are not dependent on each other.). 


## 2 Deliver

On the day of the workshop delivery, ensure you have the required updated materials to deliver the workshop. 


### 2.1 Delivery agenda and Recomendations 


<!-- for easy reading limit the number of line to 10 - 15. If more lines are needed, add them in a details section then put a summary before with a quick introduction. -->
<!-- Use Copilot to do the summary, an example of prompt is:  Can you summarize the following text in three to 5 bullet points. Each points should be a sentence between 15 to 20 words. -->

- :ballot_box_with_check: Leverage updated materials for labs and demos [here](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Platforms%2FWorkshop%20%2D%20Foundry%20and%20Copilot%20Studio%20Agents%20with%20Microsoft%20Agent%20Factory&viewid=873d8354%2D6178%2D4477%2Dba09%2D824a43c12873&ovuser=72f988bf%2D86f1%2D41af%2D91ab%2D2d7cd011db47%2Capthomas%40microsoft%2Ecom&OR=Teams%2DHL&CT=1750083286585&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNTA2MDIwNjYwOCIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D&share=cgrYqDEQ5zDdSbU5k6BCjQe%2DEgUCwyFGQbrn9wNJwGcKzy50NA))
- :ballot_box_with_check: Guide the customer on modules delivered that contain labs that was agreed upon at the time of scoping
- :ballot_box_with_check: Leverage the provided powerpoint slides for presenting key concepts
- :ballot_box_with_check: Leverage the labs and demos provided as part of the material to delivery the VBD
- :ballot_box_with_check: Focus on modules where the customer wants to spend more time. This needs to be determined at the time of scoping. Feel free to leverage the information below to make that determination

At the time of scoping leverage the following information to discuss with the customer on which modules they would like to prioritize based on the 1 day delivery timelines.

**Note:**   You can bypass the slides you don’t need to cover

| Module Name  | Has Labs | 
|--------------|------|
Agent Factory overview and agentic AI concepts|no|
Copilot Studio Overview|yes|
Microsoft Foundry Overview|yes|
Governance in Copilot Studio and Microsoft Foundry|yes|
Integration Copilot Studio and Microsoft Foundry|yes|

:point_down:
<details><summary><b>Click to expand to show more details.</b></summary>
</br>


Detailed Content if needed

</details>
</br>
</br>

## 3 Closeout and next steps

A closeout report is required to document the delivery and solution that was implemented. For more information, see [Actual Delivery: Report Deliverable](https://aka.ms/VBDReporting).

</br>

### 3.1 Closeout delivery

The last part of the engagement is a short session to collect feedback. Refer to the [IP Kit](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Platforms%2FWorkshopPLUS%20%2D%20Azure%20AI%20Platform%20and%20Services&viewid=873d8354%2D6178%2D4477%2Dba09%2D824a43c12873) for the closeout templates.

</br>


