# Delivery Guide: Well-Architected Assessment for Azure AI

Inspire and Design | 1 or 3 Days | Remote or Onsite | Level 200

## Introduction
This guide will provide details and instructions to help you deliver a successful technical assessment activity for your customer.
The assessment must accomplish the following objectives and delivery outcomes.

### Objectives

- Discover the organization's current state in terms of AI readiness.
- Benchmark the organization against a set of industry standards resulting in clear capability scores for core areas of AI adoption.
- Gain insights with actionable guidance for how to drive better business outcomes with AI for the organization.
- Develop a vision and roadmap for the integration of AI into the organization, focusing on workload operations, testing and evaluation, workload personas, and responsible AI.
- Provide confirmation and guidance around what next steps teams in the organization need to take to build their AI capabilities.
- Offer actionable guidance on tools, further learning, and resources which can be used to streamline the process for the customer.

### Deliverable Standards

- Ensure that every organization and their leaders have OKRs/KPIs that they care about, and align the deliverables to these objectives.
- Focus on what the customer sees as the top priority driver for AI adoption. This helps gain customer commitment and will encourage them to choose Microsoft as their partner in their AI journey.
- Deliver the deliverables for this activity as per the standards outlined in this guide, ensuring they cover all relevant AI design areas such as workload operations, testing and evaluation, workload personas, and responsible AI.
- Ensure that the deliverables include a vision and roadmap for the integration of AI into the organization, focusing on the identified AI design areas.

## Customer Participants

The assessment will be of different value to different people in the organization. 
Selecting the right participants that can influence change and outcomes is critical for a successful delivery.

You should - as much as possible - aim to include representatives from all stages of a workload's or application's lifecycle.
Review the "Scoping Call" section of this guide for more details.


| **Customer Role** | **Description** | **Required or Optional** |
|------------------ |-----------------|-------------------------|
| Lead Developer| Responsible for delivering and reviewing PoC, Code and Design | Optional |
| DevOps/DevSecOps | Team responsible for deploying application to production| Required |
| AppSec/ProdSec/Security | Team responsible for security across all aspects of the application | Required | 
| Data Scientists/ML Experts | Team responsible for developing AI and ML models and data applications | Recommended|
| Other IT professionals| These are the people responsible for provisioning and managing IT resources like databases, networking, compute, IAM, Security, etc.  | Recommended |
| Development Leader | Wants to grow and enable their team; Cares about velocity and quality; Cares about budget; Struggles to get necessary budget to find the best people and invest in enablement | Optional |
| Workload Owner | Moving fast is not a priority; Security and stability is a priority; Doesn't care about cost until it starts to impact their budget | Optional |
| Product Owner | Wants to be able to experiment; Cares about cost as it impacts the P&L; Doesn't understand the value of security, resilience, sees it as necessary but annoying | Optional |


## Delivery Guidance

This section walks you through the expected flow of the delivery and points you to any supporting resources that you may wish to use as part of the delivery. 
It includes all non-technical delivery guidance and supporting artifacts for the assessment. 
You are free to adapt each step to meet your customers' needs if you can meet the objectives and deliverable standards outlined at the start of this guide.

### Step 1: Scoping

#### Recommended: Account Team Scoping

If you do not yet know the account that you are about to conduct the assessment with, then it is highly recommended to conduct an internal (or account team facing) scoping meeting. 
The roles you might want to reach out to are the aligned App Innovation seller, Data & AI seller, Customer Success Account Manager, Account Technology strategist, or even the Services seller. 

The recommended timeframe for this call is about 3 - 4 weeks before the target delivery date.

Use your time with the account team to learn more about the key initiatives that the account team is already driving and what support offers are already in place. 
The assessment is a great discovery exercise and one of the account team members may well choose to shadow you during the engagement, which is a great way of providing additional context to conversations. 
A participating account team member can also help you during the reporting phase with next step recommendations or ensure that recommendations are followed up upon. 

#### Scoping Call

You should hold a scoping call at least 2 - 3 weeks before the target delivery date.

The call is a meeting between the customer, the CSAM, you (the delivering engineer), and anyone else from the MSFT account team. (as needed)
During the call you should explain the structure of the delivery and ensure the customer understands whether all of their requests are "in scope" for the delivery.

The following activities are examples of what is out-of-scope during the delivery:
- Remediation during the assessment delivery
- Classroom-style education

As part of the call, identify who should participate in the assessment activity.
Depending on the customer's organizational structure, people who can represent all aspects of the Azure AI workload lifecycle should participate in the assessment. Familiarize yourself with the assessment categories and questions before the scoping call, so that you can ensure the correct roles for each category are identified.

The scoping call also provides an opportunity to ask customer questions such as:

- What are the expectations from the assessment?
- Where are you on your AI journey?
- What is the level of knowledge about AI on the team participating in the assessment?
- Are there specific topics that you would like to discuss more deeply?
- Have you completed a similar assessment before?

> [!NOTE]
>
> Ask the customer to share any relevant artifacts in advance of the delivery. This could be architecture diagrams of PoCs or reports of previous assessments that you may want to reference.

The recommended duration for this assessment is three days. The delivery is eligible for t-shirt sizing which allows the customer to book additional assessment days.
If during scoping you realize that more or less time than allocated will be required - for example because the customer has a uniquely complex use case - you should inform the CSAM as soon as possible, as they can help adjust the engagement duration by booking additional days.

Other topics to include in the call are:

- Engagement logistics and scheduling
- Expected deliverables (core assessment output) 
- Physical security requirements for on-site visit (if applicable)

Please refer to the template resources provided here [IPShare](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Apps%2FWAF%20AI%20Assessment&viewid=873d8354%2D6178%2D4477%2Dba09%2D824a43c12873&newTargetListUrl=%2Fteams%2FASDIPRelease%2FAzureCloudAI&viewpath=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FForms%2FAllItems%2Easpx&share=cgpx5wIUBKmmT4HNlWmSd3bOEgUCFvsNRo4ndnmVufTRsMOx8g)

#### Delivery Structure

**Day 1**

- Welcome / Kick-off session
- [Assessment](https://learn.microsoft.com/en-us/assessments/ea306cce-c7fa-4a2b-89a6-bfefba6a9cf4/) taken via the Microsoft Assessments platform
- Recap and high level results discussion

**Day 2**

- Report preparation
- Clarification of any of the evidence given by the customer team

**Day 3** 

- Close Out
- Report delivery

If needed, you can extend the assessment interview into the second day.
The remainder of the day will be spent processing the output of the questionnaire, generating recommendations, and putting together the reporting deliverables.

On the third day, you will be presenting the outcomes of the assessment along with some targeted recommendations. Ensure that you have enough time for the report generation as all deliverables need to be ready before the engagement concludes.

Please refer to the [Tooling Guide](./WAA-Tools%20Overview%20Guide.md)

##### Delivery Excellence

The assessment is conducted using the [Microsoft Assessments](https://learn.microsoft.com/en-us/assessments/) platform.

Interviews are a critical part of the engagement, where the main goal is to get as much information and insights from the customer as possible. 
It’s important to have the correct customer stakeholders in the room.

This ensures that accurate responses are given and that rich and meaningful responses are collected for the Microsoft Assessments survey. 
The spirit of these customer interviews is to have open conversations about each of the practice areas instead of trying to ask a bunch of questions to get binary answers that might miss a lot of other important details. 
Try to identify strengths, challenges, and opportunities. For the report generation, it's good to capture both positives and negatives (gaps) so that the final report has an encouraging feel to it.

**Capture notes for all questions**

For high-quality report results, it's important to capture notes for every question in the assessment, using the Notes field in the UI. The notes will be used by the reporting tool, to generate initial contents using AI, so the accuracy is critical.

- Write the notes from the customer's perspective. For example, "**We're** very early in our AI journey so there is only a short term roadmap."
- You don't have to capture everything that the customer says but all the important mentions should be captured.
- The notes don't have to be concise and summarized, it's better to write the notes in natural language. 1-3 lines of notes is perfectly fine.
- Even if the customer doesn't have any comments for the score, take the opportunity to write notes. For example, "This is not relevant to us", "we don't use this product", "we are not at this point yet in our AI journey."
- Instead of using acronyms, write the full words whenever possible. For example:
  - instead of WAF, write Well-Architected Framework
  - instead of CAF, write Cloud Adoption Framework
- Whenever the customer mentions names of persons, it's better to refer to the role of the person if it's important.
  - Customer: "Diana has been researching our approach to ethical AI
  - CSA: "Who is Diana?"
  - Customer: "Diana is our head of HR"
  - *Notes: "The head of HR has been researching our approach to ethical AI"*
- Be precise when product or company names are mentioned. For example, instead of writing "Copilot" in the notes, use the specific product name "GitHub Copilot", "Copilot for Security", "Microsoft Copilot" or similar.


**Do not just read the assessment questions line by line.** 

- Ask questions in your words. 
- Extend the questions with examples from your own experience.
- Provide context and background information why this question matters and what its impact is.
- Prompt the customer with open-ended follow-up questions where appropriate.
- Ask the customer to share their experience openly.
- Encourage the customer to use the whiteboard to visualize their explanation where possible.

**Allow for openness and discussion while keeping an eye on the time.**

Keep an eye out for what questions the team finds easy to answer and which ones they struggle with. This may give you a good indication of where there is disagreement within the organization.
Where necessary scope a question to a specific project or product area to make it easier for the customer to answer.
Ensure to timebox the topics and use a “parking lot” for challenging discussions. This will allow you to conduct the assessment in the time available.
Make notes of the questions and topics that seem to be important to the customer team. This will help with determining the most important items when suggesting next steps.

**Reporting**

*Prerequisites: You need access to an Azure OpenAI model to generate the report contents. Prefer GA gpt-5 or cost-optimized gpt-5-mini. If using gpt-5 (base), ensure limited-access registration is approved via https://aka.ms/oai/gpt5access; otherwise use gpt-5-mini or gpt-5-nano for fastest start without registration. Avoid preview models (e.g., gpt-5.1-chat, gpt-5.2-chat) for customer-facing reports; they are suitable for pilots only. For reporting setup guidance, see the [Tooling Guide](./WAA-Tools%20Overview%20Guide.md)

When the session is complete, ensure all answers are captured in the assessment on the Microsoft Assessments platform. Download the CSV output from the platform and use the results to fill in the customer summary deck (WAFAIAssessment_SummarySlides.pptx), available on the [IP Share](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Apps%2FWAF%20AI%20Assessment&viewid=873d8354%2D6178%2D4477%2Dba09%2D824a43c12873&newTargetListUrl=%2Fteams%2FASDIPRelease%2FAzureCloudAI&viewpath=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FForms%2FAllItems%2Easpx&share=cgpx5wIUBKmmT4HNlWmSd3bOEgUCFvsNRo4ndnmVufTRsMOx8g)

A helpful summary deck that you can use for this report summary is available on the [IP Share](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Apps%2FWAF%20AI%20Assessment&viewid=873d8354%2D6178%2D4477%2Dba09%2D824a43c12873&newTargetListUrl=%2Fteams%2FASDIPRelease%2FAzureCloudAI&viewpath=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FForms%2FAllItems%2Easpx&share=cgpx5wIUBKmmT4HNlWmSd3bOEgUCFvsNRo4ndnmVufTRsMOx8g) for this delivery.

With the report generated, review the output, and add additional context from customer conversations.
- As the initial content in the report is generated with an LLM using a baseline data set, and the customer score and comments, it's important to carefully review the content. There can be mistakes in the generated content.
  - If the customer has mentioned team names, organization units etc. make sure they are handled correctly in the text.
  - Some product names are confusing to the report generator. Make sure they have been interpreted correctly.
  - Ensure that the writing style stays the same in the document.
- Suggest follow-up VBD deliveries that can help implement the three top recommendations.
- Finalize your report, and share the initial findings with the account team if possible. (CSAM, other account team stakeholders, you)
  - Allowing the account team a few moments to preview the content and add any additional comments will be useful to present a unified position.

**Update MSX**

> [!IMPORTANT] 
> Use MSX to track the top recommendations and post-delivery follow-ups. MSX is an internal-facing collaboration tool for CSAM, CSA and account team.

Work with the CSAM to update the Opportunity within MSX, and create milestones to capture the ACR impact of all P0-P1 committed recommendations:

- Group them by expected completion timeline, for example small recommendations 1-2 months, medium 3-4 months, large 5-6 months.
- Ideally, no more than 3 milestones would be created.
- Any recommendations that could take more than 6 months, should be captured as a new opportunity.
- Note: The recorded ACR impact could be $0 or a negative amount

##### Close Out with the customer

The executive close out meeting is intended to recap the core findings from the assessment, focusing on key strengths and optimization opportunities. 
A helpful summary deck that you can use for this meeting is available on the [IP Share](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Apps%2FWAF%20AI%20Assessment&viewid=873d8354%2D6178%2D4477%2Dba09%2D824a43c12873&newTargetListUrl=%2Fteams%2FASDIPRelease%2FAzureCloudAI&viewpath=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FForms%2FAllItems%2Easpx&share=cgpx5wIUBKmmT4HNlWmSd3bOEgUCFvsNRo4ndnmVufTRsMOx8g) for this delivery.

It is important to include executive sponsors and IT decision makers in this meeting so they gain awareness of improvement recommendations and how Microsoft can help, which they can use to make resourcing and investment decisions on what steps will be taken to execute on the recommendations.

**Deliverables**

At the end of the engagement, Microsoft will provide a set of reporting deliverables for the customer to use as references to execute on the improvement recommendations and for internal reporting purposes.
You will generate the reporting deliverables using the instructions in the Delivery Excellence section about **Reporting**.

## Resources, Readiness and References

- Leverage the [learning path](./WAA-lp.md) for the Assessment resources contained in this VBD IP
- Please submit your feedback for this delivery via [aka.ms/logVBDFeedback](https://aka.ms/logVBDFeedback).
- Check out the resources on the [IPShare](https://microsoft.sharepoint.com/teams/ASDIPRelease/AzureCloudAI/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FSP2%20VBD%2FAI%20Apps%2FWAF%20AI%20Assessment&viewid=873d8354%2D6178%2D4477%2Dba09%2D824a43c12873&newTargetListUrl=%2Fteams%2FASDIPRelease%2FAzureCloudAI&viewpath=%2Fteams%2FASDIPRelease%2FAzureCloudAI%2FForms%2FAllItems%2Easpx&share=cgpx5wIUBKmmT4HNlWmSd3bOEgUCFvsNRo4ndnmVufTRsMOx8g) for this delivery.

### Community support

- [Delivery Community](https://teams.microsoft.com/l/channel/19%3Adc692f3bec324088bbe5b9d07565c0f2%40thread.tacv2/VBD%20-%20Innovate%20Apps%20with%20AI?groupId=591c20e8-6a02-4476-8881-849bf672e6cf)

## Known issues and updates

None identified yet.

## Frequently Asked Questions

**The assessment platform's frequently asked questions site describes all assessments as 'completely free and open'. How should I respond to a customer who is questioning the fact that the assessment is a paid delivery?**
The platform indeed states that all assessments are free and open; and that's because they are available publicly for anyone on the internet. The additional value comes from the time spent with a Microsoft professional taking the assessment, reviewing each question in detail, and receiving high value actionable outcomes. 

Customers also receive tailored reporting and an action plan aligned with their priorities as identified in the delivery.

As a side note: Under the VBD process deliveries can be Microsoft-funded following a manager approval. 

**How does the scoring for the questions in the assessment work?**
Each question usually has a score between 0 and 100. In general, most questions divide their points evenly. The best answer will score 100 points and the worst answer will score 0 points. For multiple choice answers each option usually contributes an equal share of points to the overall score. 
The overall score is an average of the individual question scores. 

