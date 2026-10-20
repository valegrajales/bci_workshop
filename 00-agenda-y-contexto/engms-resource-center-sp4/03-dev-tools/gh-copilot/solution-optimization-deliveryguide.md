# Delivery Guide: Solution Optimization for GitHub Copilot

## Introduction

This guide is designed to help you deliver a *Solution Optimization for GitHub Copilot* engagement.

GitHub Copilot is an AI coding assistant that helps you write code faster and with less effort, allowing you to focus more energy on problem solving and collaboration. GitHub Copilot has been proven to increase developer productivity and accelerate the pace of software development.

Some of the key reasons via enterprises invest in the adoption of GitHub Copilot are:

- Increase Efficiency: With the help of GitHub Copilot, developers can write code more quickly and efficiently.
- Improve Codebase Quality: GitHub Copilot can suggest code snippets and offer guidance on best practices.
- Reduce Workload: GitHub Copilot can automate repetitive tasks, freeing up developers to work on more important tasks.
- Easier Onboarding: When new developers join a team, it can be sometimes challenging for them to get up to speed on the codebase.

Adopting GitHub Copilot can help companies improve their development processes, increase productivity, and reduce failures.

This engagement guides engineering teams through evaluating and optimizing **GitHub Copilot's impact on developer productivity and organizational goals**. It covers methodologies, metrics, and best practices for integrating and assessing Copilot.

> [!TIP]
> This VBD delivery guide, as well as the topic of Developer Productivity in general, covers a lot of material and possible scenarios.  Be mindful of this when scoping and preparing for this engagement.  The material and guidance in this delivery guide is provided to support your delivery of this VBD and to be used as a reference.  Carefully select topics that will provide the most value to the particular customer scenario.

The remaining sections in this guide will help you prepare for this engagement, set clear expectations with your customer, and deliver high-quality results.  

## Objectives

Using the resources in this guide, along with one or more of the delivery modules, successful delivery of this engagement will include:

- Understand how GitHub measures developer productivity via ESSP.
- Develop skills in using surveys and telemetry data to evaluate productivity.
- Learn how to measure GitHub Copilot's impact from adoption to sustained efficiency.
- Learn to plan and implement system-level improvements with GitHub Copilot.

## IPKit

The IPKit with artifacts to use throughout this delivery is located [aka.ms/GHCopilotSolOptVBD](https://aka.ms/GHCopilotSolOptVBD)

## Participants

The target audience includes the following personas:

| Customer Role           | Description                                                                                                          | Required or Optional |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------- |
|Software Development Stakeholder| The person who aligns the business goals and outcomes with the use of software development tools within an organization  | Required| 
|Engineering Manager| The person responsible for managing development teams that utilize GitHub and GitHub Copilot Manager type role| Optional|
| Business sponsor        | The person who funds and supports GitHub and GitHub Copilot as a platform.                        | Required             |
| GitHub admin         | The person who administers and implements the DevOps infrastructure and services that support GitHub and GitHub Copilot.                        | Required             |
| Other IT professionals  | The people who perform various tasks related to DevOps and Software Development. | Optional             |

The target audience should also include roles with skills and accountability for the entire operations.

> [!TIP]
> Not all stakeholders are required all the time, but their availability will help remove road blockers in timely manner.

## Prerequisites

The participants need to have completed the prerequisites listed below before attending this engagement.

- At least one customer participant has an account with sufficient permissions in GitHub to access and manage the GitHub Copilot and related services.

## Delivery Guidance

This section includes all non-technical delivery guidance and supporting artifacts. You are free to adapt each step to meet your customers needs as long as you are able to meet the objectives and deliverable standards for the delivery.

### Discovery and preparing for the delivery

***Preparing for this engagement*** before the initial meeting with a customer will help ensure a successful and productive delivery. Work with the account team to gather context. Look for public information or news articles that may give clues to the customer's motivations or direction. Also, take the time review MSX, Customer360, Support Center, and other internal tools to gain insights into the customer's recent experience with Azure.

Here are some key areas to prepare for if possible:

- **Understand the Customer's Business:** Research and understand the customer's industry, market, and specific business goals and challenges. This knowledge will help tailor your recommendations to their unique needs.

- **Familiarize Yourself with the GitHub Copilot:** Review the customer's GitHub and GitHub Copilot usage, components. Familiarity with their usage is crucial for providing relevant guidance.

- **GitHub Copilot Knowledge:** Ensure you have a deep understanding of GitHub Copilot service, its features, pricing, and capabilities. Be prepared to discuss its role in developer productivity.

- **Stay Updated**: Coordinate with the GitHub Copilot Account team to stay informed about any new or upcoming features. This ensures you are aligned and aware of the latest developments. 

- **Identify Pain Points:** Prior to the meeting, identify potential areas of concern related to the GitHub Copilot.

- **Know the Customer's Goals:** Understand what the customer hopes to achieve in terms of improved developer productivity. 

- **Gather Questions and Prerequisites:** Prepare a list of questions to ask the customer during scoping to gain deeper insights into their needs, constraints, and expectations.  Have the pre-requisites ready to discuss with them.

#### Pre-scoping Email

Pre-Scoping Email (sent approximately 5 days before Scoping Call)

The pre-scoping email is sent by the dispatched delivery resource to:

- Primary point of contact(s) at the customer
- Customer Success Account Manager (CSAM)
- Relevant Microsoft and GitHub account team stakeholders, as applicable

The designated customer point of contact is expected to manage logistics, requirements, and interactions with customer stakeholders. This role is usually filled by a program manager, project manager, or team lead.

The objective of this email is:

- Communicate the scheduled date and time of the scoping call
- Outline a high-level agenda for the upcoming scoping call
- Make the customer contact aware of the customer stakeholders/roles that should be included
- Make requests for any information the customer should provide, or pre-requisites to be completed, prior to the call.  

> [!NOTE]
> Your email should be clear and detailed.  This will help the customer plan appropriately and understand what is needed to prepare for an efficient and productive scoping call.  

#### Scoping Call

Reference here for a detailed overview of how to hold a [Scoping Call](https://aka.ms/VBDScoping). Use the PowerPoint deck [here](#ipkit) for the Scoping.

Use your prepared questions to help you gain insights during the Scoping Call.  The customer should be doing most of the talking, but you may need to provide prompts or ask follow-ups to ensure you are getting the information you need and the course of the discussion stays relevant to the engagement.  You should plan for a 1-hour meeting.  A sample agenda is provided below:

1. **Welcome and Introduction** *(5 minutes)*
  - Introduce yourself and give a quick overview of your background that's relevant to this engagement
  - Customer introductions, their role, and their organization.
2. **Objectives and Expectations** *(10 minutes)*
 - Discuss the primary goals and expectations
  - Clarify what the customer hopes to achieve in terms of developer productivity and GitHub Copilot usage.
  - Explain that while GitHub has in-product dashboards, there are several open-source tools available to help with customized reporting needs. Encourage the customer to review the guidelines for these tools to understand their features, deployment costs, and prerequisites.
  - Inform the customer that while a Microsoft CSA can assist with the setup, maintaining and updating the solution will be their responsibility.
  - Check the pre-requisites section of each relevant GitHub repo to select the appropriate tool for deployment. Inform the customer about any potential costs associated with the chosen tools and deployment options.
3. **Current Challenges and Pain Points** *(10 minutes)*
  - Invite the customer to share any current challenges or pain points related to developer productivity measurement.
  - Discuss GitHub Copilot adoption at scale, and explore available workshops or value-based delivery (VBD) sessions, such as Prompt Engineering workshops, office hours, or Hackathons, to boost adoption and address any pain points.
4. **GitHub Copilot Overview** *(15 minutes)*
  - Ask the customer to provide a brief overview of their GitHub and Copilot usage.
5. **Scope and Deliverables** *(10 minutes)*
  - Discuss the scope of the engagement, including deliverables and modules
  - Preliminary timeline
  - Review Prerequisites
6. **Close** *(10 minutes)*
  - Review key points
  - Address any unresolved issues or uncertainties.
  - Ensure consensus
  - Agree on actions or next steps

## Actual VBD Delivery

### Kickoff

The delivery starts with a kickoff. For more information, see [Actual Delivery: Kick-off meeting](https://aka.ms/VBDKickoff). Refer to the [IPKit](#ipkit) for the kickoff templates.

## Technical Delivery Guidance

Measuring the adoption and impact of GitHub Copilot is crucial for understanding its value and effectiveness. This guidance will help you set up and deliver a comprehensive dashboard to track key metrics and insights.

**Delivery Tips**
- **Security at the Top**: Ensure all data, metrics, and dashboards are securely handled and comply with relevant data protection regulations.
- **Be Objective**: Focus on the customer’s expectations and needs, providing relevant and actionable insights.
- **Knowledgeable Preparation**: Be well prepared to discuss customer-specific, organization-specific, or application-specific details, aligning recommendations with best practices.
- **Seek Guidance**: Consult with colleagues or subject matter experts within Microsoft/GitHub if needed.
- **Transparency**: If uncertain about any aspect, be transparent about your limitations and offer to gather additional information.
- **Manage Expectations**: Inform the customer about the complexity, uncertainty, or potential risks associated with any solution or guidance provided.

### Step 1: Discuss Developer Productivity Fundamentals

Begin with a broad overview to ensure participants understand the basic concepts and terminology related to Dev Productivity and happiness.

- **Dev Productivity**: Provide an overview of the software development cycle, emphasizing that overall productivity is achieved when the entire process is optimized. Highlight that measuring developer productivity requires data from multiple tools, not just GitHub Copilot. Discuss how optimizing each step or process within the software development cycle leads to overall efficiency gains.
- **ESSP Framework**: Introduce the holistic approach developed by Microsoft and GitHub for measuring developer productivity. Explain that it goes beyond traditional activity-related metrics to include additional criteria like developer well-being and community.
  - **Developer happiness**
  - **Quality**
  - **Velocity**
- **Understand Customer’s Org KPIs and System-Level Indicators**: Ensure you understand the customer's key performance indicators and system-level indicators relevant to their organization. This helps tailor recommendations and measure success effectively.
- **GitHub Copilot Adoption Stage**: Assess the customer's current GitHub Copilot adoption stage. Guide them through current challenges and provide educational materials to help them progress to the next stages.

Use the Brainstorming Guide in the delivery guidance to learn more about how you can drive an in-depth exploration of Developer Productivity with the customer.
Based on the outcomes of the scoping call, adjust how much time you want to spend on brainstorming as compared to delivering the structured content.

### Step 2: GitHub Copilot Usage Metric Dashboard Review

Guide the customer through in-product GitHub Copilot adoption metrics and charts. Discuss the various adoption stages and relevant key measures for each stage.

#### Familiarize with GitHub Copilot Adoption Stages

- **Understand Customer’s Current Adoption Stage**: Identify where the customer is in their adoption journey and what organizational metrics are most relevant to them.
- **Highlight Leading/Lagging Indicators**: For each adoption stage, emphasize the key indicators that will help track progress and impact.

#### Visualization Tools
The Copilot usage metrics dashboard, code generation dashboard, and GitHub Copilot Metrics API are generally available (GA). Availability and access are controlled by enterprise policy settings.

The AI era of software development isn’t about are teams using AI, but rather how well are they using it?

The GitHub Copilot usage metrics dashboard, code generation dashboard, and API for GitHub Enterprise customers using Copilot, helps you answer that question with data.

#### Copilot usage metric dashboard
The Copilot usage metrics dashboard gives enterprise administrators and billing managers direct visibility into Copilot usage and adoption under the Insights tab. The dashboard provides an aggregated enterprise view, while the NDJSON download or API offer user-level granularity for deeper analysis.

#### Copilot code generation dashboard
The code generation dashboard shows how Copilot is generating code across your enterprise. By comparing user-initiated and agent-initiated activity across models, languages, and modes, you can see how teams are adopting AI-assisted and agent-driven development.

You’ll find metrics including:
Daily and weekly active users across GitHub Copilot IDE modes, including agent mode.
Agent adoption across your user base.
User-initiated code changes vs Agent-initiated code changes.
Lines of code added and deleted across all IDE modes.
Language and model usage patterns across IDEs.



These metrics help you understand:

Overall usage and adoption: Review indicators like weekly usage provide a broad view of Copilot adoption across your enterprise.
Specific model, feature, and language usage: See which AI models and programming languages are most utilized by your teams, highlighting areas for even greater value.
Agent adoption percentage: Track how many developers are using Copilot for advanced tasks like refactoring, debugging, and complex problem solving. High agent adoption signals a shift toward truly transformative coding.
Together, these are foundational metrics showing who’s adopting Copilot, how consistently, and what that usage looks like across your enterprise.

#### How to enable Copilot usage metrics in your enterprise
Copilot usage metrics availability is controlled by enterprise policy settings.

Enterprise admins can enable them as follows:

1. Navigate to your AI Controls tab on github.com.
2. Select Copilot in the left sidebar.
3. Scroll down to the “Metrics” section where you’ll see Copilot usage metrics.
4. Change the Copilot usage metrics policy setting to Enabled. This will enable the Copilot usage metrics dashboard and API for your enterprise, allowing enterprise administrators and billing managers to view usage and adoption data.

Otherwise, if the customer opts for an alternative solution, review the prerequisites section of each solution to choose the appropriate tool for deployment. Inform the customer about any potential costs associated with the chosen tools and deployment options.
- **Preferred Visualization Tools**: Use the visualization tools preferred by the customer, as listed in the reference section.
- **Interactive Dashboards**: Follow GitHub repository instructions to build interactive and insightful dashboards.

#### Metrics Tracking

- **Representative Metrics**: Track metrics that typically improve with Copilot, noting that the degree of impact may vary.
- **Neutral-to-Positive Improvement**: Focus on observing neutral-to-positive trends rather than hitting specific benchmarks.
- **Addressing Regressions**: If a metric regresses, identify and address the root cause.

#### Data Sources & Metrics Retention

- **GitHub Copilot API**: Use the API to access metrics for the prior 28 days.
- **Data Retention Options**: Discuss with the customer their preferences for data retention to enable long-term analysis.

**General Tips:**  

- **Focus on Continuous Improvement**: Aim for gradual improvements in each measure over time rather than setting fixed targets.
- **Align with Development Cadence**: Match the frequency of your measurements with your development cycles, such as sprint cycles.
- **Data Collation**: Consider integrating your data points into existing BI or reporting tools for easier analysis and trend review. Alternatively, use a spreadsheet to track measures over time.
- **Onboarding Impact**: As new developers start using Copilot, some metrics may initially decline as they build their skills and confidence. Analyze metrics by onboarding groups to better understand these trends.
- **Early Indicators**: During the evaluation and adoption stages, monitor some DevOps metrics for early signs of system impact. However, prioritize happiness and engagement measures during these stages. System-level metrics are more likely to improve once developers are proficient with Copilot.
- **Identify Opportunities**: Use metrics to spot opportunities for improvement and address gaps through educational sessions like workshops, webinars, or office hours.
- **Glossary**: Measuring the impact of GitHub Copilot.

---

### Step 3: Engagement Closeout

The last part of the engagement is a short session to collect feedback. Reference here for a detailed overview of how to hold a [Closeout meeting](https://aka.ms/VBDCloseOutMeeting). Refer to the [IPKit](#ipkit) for the closeout templates.

In the Closeout section, provide an overview and review the completed deliverables.

- Thank the customer for their time and participation.
- Briefly summarize the actions that took place during the engagement and their outcomes.
- Review any recommendations for their future consideration and action.
- Discuss next steps with customer stakeholders.
- Spend some time at the end of the engagement to hear the customer's feedback and take notes.

After the meeting:

- Summarize feedback on the overall VBD delivery and delivered content, and share feedback and/or open an issue for any problems encountered.
- Finalize and follow up actions or additions to your recommendations. Send the documents to the customer.

## IPShare

You can access the slide deck for this engagement on its [IP Share](https://aka.ms/GHCopilotSolOptVBD). 

## Additional Resources
- [Viewing the Copilot usage metrics dashboard](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/view-usage-and-adoption)
- [Viewing the code generation dashboard](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/view-code-generation)
- [Mock Dashboard: Copilot Metrics Viewer](https://copilot-metrics-viewer-gthcc5cmd9ebf2ff.westeurope-01.azurewebsites.net/)
- [Open Source Copilot Metrics Viewer](https://github.com/github-copilot-resources/copilot-metrics-viewer)
- [CSV Export Action](https://github.com/marketplace/actions/github-copilot-metrics-api-export) - Lightweight action for producing a flattened csv of results from the Metrics API endpoint
- [Metrics & Seat Management Report Generation Action](https://github.com/marketplace/actions/copilot-usage-action) - Generates data visualizations. Connects to Metrics API, Billing API, and User Managements Seats API. Allows for report automation with email, slack, teams, discord, etc.
- [Copilot Usage Report](https://github.com/marketplace/actions/copilot-usage-report) - Other Marketplace Reports
- [Copilot Metrics Retention](https://github.com/marketplace/actions/copilot-metrics-retention) - Other Marketplace Reports
- [Copilot User Management](https://github.com/marketplace/actions/copilot-user-management) - Other Marketplace Reports
- [Audit Log Events](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise#copilot) - Other Potential Data Source Enhancements
- [Webhook Events and Payloads](https://docs.github.com/en/enterprise-cloud@latest/webhooks/webhook-events-and-payloads) - Other Potential Data Source Enhancements

[!include[GitHubDemo_Options_Section](../../../CommonContent/gh-demo-options.md)




