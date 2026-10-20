<!-- 

Some sections are optional if the content is not available like 1.1 Activity deep dive video or Other resources, readiness and references

-->

# WorkshopPLUS - Designing and implementing a data science solution on Azure delivery guide

This Course is a hands-on, instructor-led course that enables learners to design, build, train, deploy, and operationalize data science and machine learning solutions using Azure Machine Learning and Azure AI Foundry. The course aligns with DP‑100 objectives and combines Microsoft Learn content, labs, and real-world scenarios to support end-to-end ML lifecycle implementation on Azure.

## Objectives and Outcomes

**Course Objectives**

By the end of this course, learners will be able to:

-	Design an end-to-end data science and machine learning solution aligned with business and technical requirements on Microsoft Azure.

-	Explore, configure, and manage Azure Machine Learning workspaces, including data, compute, and environments.

-	Train, track, and optimize machine learning models using notebooks, jobs, pipelines, and ML flow. 

-	Implement automated machine learning and hyperparameter tuning to improve model performance. 

-	Apply Responsible AI practices to evaluate, compare, and govern machine learning models.

-	Deploy and operationalize models using managed online and batch endpoints on Azure. 

-	Build, fine-tune, and evaluate generative AI solutions using Azure AI Foundry and Microsoft Learn–aligned workflows.


**Outcomes**

 Upon successful completion of this course, learners will be able to:

-	Design and validate an end-to-end data science solution architecture using Azure Machine Learning, aligned to business objectives and technical requirements.
-	Configure, manage, and operationalize Azure Machine Learning workspaces, including data assets, compute targets, environments, and security boundaries.
-	Train, track, and optimize machine learning models using experiments, ML flow, automated machine learning, jobs, and pipelines.
-	Evaluate, compare, and govern machine learning models by applying Responsible AI practices and built-in evaluation capabilities.
-	Deploy, consume, and monitor machine learning models using managed online and batch endpoints in production-ready scenarios.
-	Build, fine-tune, evaluate, and operationalize generative AI solutions using Azure AI Foundry, including prompt flow and Retrieval Augmented Generation (RAG) patterns

:point_down:
<details><summary><b>Click to expand to show more details.</b></summary>
</br>


<!-- If no details, delete the <details> section and the following </br>-->


## 1 Prepare

Validate that participants understand the end‑to‑end data science lifecycle on Azure, including required tools, roles, and prerequisites. Confirm readiness of Azure subscriptions, Microsoft Learn access, and baseline skills in Python, machine learning concepts, and Azure Machine Learning to ensure effective participation in the engagement.


</br>

### 1.1 Pre-Scope

Discuss with the account team your customer needs for this delivery

- :ballot_box_with_check: To understand the customer's background and validate expectations, see [Pre-Scoping Call with CSAM & CSA](https://aka.ms/VBDPre-scoping). This call precedes the customer scoping call.
- :ballot_box_with_check: Connect with CSAM to learn about expectations on customer learnings and outcomes.

:point_down:
<details><summary><b>Click to expand to show more details.</b></summary>
</br>


</details>

### 1.2 Scoping

For information about the customer scoping call, roles, and outcomes, see [Scoping Call](https://aka.ms/VBDScoping). Refer to the [IP Kit](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Platforms%2FWorkshopPLUS%20%2D%20Azure%20Machine%20Learning&viewid=873d8354%2D6178%2D4477%2Dba09%2D824a43c12873) for links to scoping call artifacts.

Setting the expectations (Goals, Timing, Prerequisites Check, Outcomes, Challenges) with the customer.

- :ballot_box_with_check: Understand whether the customer has worked in Azure Machine Learning Service before and whether they have models deployed in production already.
- :ballot_box_with_check: Validate that required Azure services, including Azure Machine Learning and Azure AI Foundry (where applicable), are enabled and permitted within the customer tenant.
- :ballot_box_with_check: Confirm that the scoping call includes the Business Sponsor or Engagement Owner, Data Science Lead, Machine Learning Engineer or practicing Data Scientist, Azure/Cloud Architect, and IT or Platform Administrator from the customer side, along with the CSA and Delivery Instructor/Partner (if applicable), to validate business objectives, participant readiness, environment access, and delivery alignment prior to course execution
- :ballot_box_with_check: Scope includes instructor‑led delivery aligned to DP‑100 objectives, combining presentations, demonstrations, and hands‑on labs using Azure Machine Learning and Azure AI Foundry.
- :ballot_box_with_check: Hands‑on lab execution is in scope and will be delivered using Microsoft Learn‑aligned labs or an Authorized Lab Hoster (ALH) environment.
- :ballot_box_with_check: Scope includes exposure to Responsible AI practices, model governance, and evaluation using native Azure Machine Learning capabilities.
- :ballot_box_with_check: Generative AI topics using Azure AI Foundry (model catalog, prompt flow, RAG, fine‑tuning, evaluation) are included as part of the advanced modules.
- :ballot_box_with_check: Environment provisioning, Azure subscription enablement, and cost management approvals are customer responsibilities unless explicitly stated otherwise.
- :ballot_box_with_check: Understand whether they are interested in Advanced concepts such as Responsible AI, MLOPs, monitoring, integration of Azure ML with other services, etc. 


### 1.3 Prepare Classroom

- :ballot_box_with_check: Verify you have checked the accreditation guide.[Here](https://eng.ms/docs/microsoft-customer-partner-solutions-mcaps/customer-experience-and-support/asd-management/og-management/ppe-resource-center-repos/azure-engagement-resource-center/wiki/wwl_guides/accreditation_wwl_courses)
- :ballot_box_with_check: Review Courseware Content here : [**Learning Download Center (LDC)**](https://learningdownloadcenter.microsoft.com)
- :ballot_box_with_check: Each IPKit contains the following assets that will help you to prepare your delivery:
    *   Trainer prep guide
    *   Change log
    *   Delivery IP (Presentations and supporting documents)
    *   Access Skillable Labs in https://aka.ms/lod, check [Instructions Here](https://eng.ms/docs/microsoft-customer-partner-solutions-mcaps/customer-experience-and-support/asd-management/og-management/ppe-resource-center-repos/azure-engagement-resource-center/wiki/createlodclass)
- :ballot_box_with_check: Learn how to create a Delivery prep access classroom [Here](https://eng.ms/docs/microsoft-customer-partner-solutions-mcaps/customer-experience-and-support/asd-management/og-management/ppe-resource-center-repos/azure-engagement-resource-center/wiki/upskilling_faq)
- :ballot_box_with_check:  If you dont see the Admin menu, or the Create Class option, or have issues with Labs. Login to Skillable [Support Center](https://www.skillable.com/customer-support/) and file a support case.
- :ballot_box_with_check:  If have a change proposal for the lab instructions or you want to fix an issue please use the Labs Instructions github and submit issues or Pull Requests [Here](https://github.com/orgs/MicrosoftLearning/repositories)



## 2 Deliver Learn Course

This course is delivered as an instructor‑led, hands‑on engagement aligned with DP‑100 objectives, combining presentations, demonstrations, and Microsoft Learn–based labs. Delivery guides participants through the end‑to‑end machine learning lifecycle using Azure Machine Learning and Azure AI Foundry, with emphasis on practical execution, Responsible AI, and production readiness. Labs and case scenarios reinforce real‑world application and measurable outcomes.


### 2.1 Delivery agenda and Recommendations 


<!-- for easy reading limit the number of line to 10 - 15. If more lines are needed, add them in a details section then put a summary before with a quick introduction. -->
<!-- Use Copilot to do the summary, an example of prompt is:  Can you summarize the following text in three to 5 bullet points. Each points should be a sentence between 15 to 20 words. -->

- :ballot_box_with_check: The course is delivered over four days, progressing from machine learning fundamentals to advanced deployment and generative AI scenarios.
- :ballot_box_with_check: Each day combines instructor‑led explanations with hands‑on labs to reinforce end‑to‑end machine learning lifecycle concepts on Azure.
- :ballot_box_with_check: Significant emphasis is placed on practical execution using Azure Machine Learning, including experimentation, optimization, and responsible AI practices.
- :ballot_box_with_check: Recommendations emphasize prior lab completion by instructors, sufficient lab time allocation, and cost governance throughout the delivery.


**Note:**   You can bypass the slides you don’t need to cover

| Module Name  | Description | Has Labs | 
|--------------|-------------|------|
Module 1|Introduction to Machine Learning|yes|
Module 2| Optimizing Data for Better Insights|yes|
Module 3| Azure Machine Learning service|yes|
Module 4| Azure Machine Learning Service - Advanced Concepts|yes|


### 2.2 Deliver Diplomas

To request diplomas please follow the instructions [here](https://eng.ms/docs/microsoft-customer-partner-solutions-mcaps/customer-experience-and-support/asd-management/og-management/ppe-resource-center-repos/azure-engagement-resource-center/wiki/upskilling_faq)


:point_down:
<details><summary><b>Click to expand to show more details.</b></summary>
</br>


Detailed Content if needed

</details>
</br>

## 3 Closeout and next steps

A closeout report is required to document the delivery and solution that was implemented. For more information, see [Actual Delivery: Report Deliverable](https://aka.ms/VBDReporting).

</br>

### 3.1 Closeout delivery

The last part of the engagement is a short session to collect feedback. Refer to the IP Kit for the closeout templates.

You can find the closeout PowerPoint template [on SharePoint.]()

</br>

#### 3.2 Next Best Actions

[!INCLUDE[Closeout Next Best Actions](.. .. .. ../../../ CommonContent/closeout_next_best_actions.md)]

</br>

[!INCLUDE[Closeout Recommended Steps](.. .. .. ../../../ CommonContent/closeout_recommended_steps.md)]

</br>


####  CLoseout Resources

[!INCLUDE[Closeout Resources](.. .. .. ../../../ CommonContent/closeout_resources.md)]


## Other resources, readiness and references

Add content

## Known issues and updates

Add content


