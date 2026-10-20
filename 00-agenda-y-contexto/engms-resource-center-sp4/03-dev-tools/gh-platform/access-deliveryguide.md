Dev engagement: delivery guide

# Delivery Guide: Go-Live Assessment for Migrating Code Repositories to GitHub

This guide will provide details and instructions to help you deliver a successful sssessment for GitHub Migrations for your customer to help them come up with a go or no go decision and understand the actions they can take to help complete a successful migration engagement. 

**Objectives**

- Evaluate your current VCS environment
- Develop a comprehensive migration plan with timelines 
- Enable and operate migration tooling effectively 
- Apply best practices for full repository migrations

**Deliverable Standards**

- Every organization and their leaders have OKRs/KPIs that **they care about**.
- DVI is a **leading** indicator. It is correlated to all customer OKRs/KPIs.
- To move the needle towards deep engagement, we need to establish a focused rhythm with the customer.
- The 46 drivers crosscut the organization.
- Focus on what the customer sees as the **top priority** driver. This helps gain buy-in. Get some wins then move on to the next.
- By the end of the assesment, the customer should now have the tools to proceed to a POC where they will gain hands-on experience in fully migrating 12 repositories. 

## Customer Participants

The DVA will be of different value to different personas. Selecting the right persona that can influence change and outcome is critical. Otherwise, the DVA will just be another "assessment".

Make sure to include all members of a cross functional team involved in the overall solution/product lifecycle if necesary. However, for simplicity make sure that at least the roles mentioned below as required are involved in each session. You'll find more details in the "Scoping Call" section of this guide.

| **Customer Role** | **Description** | **Required or Optional** |
| --- | --- | --- |
| DevOps Engineers | Wants to move fast, to be enabled; Doesn't care about cost; Cares less about security, resilience, more about features | Required |
| --- | --- | --- |
| GitHub Enterprise Admins | Wants to grow and enable team; Cares about velocity and quality; Cares about budget; Struggles to get necessary budget to find the best people and invest in enablement | Required |
| Source VCS Admins  | Moving fast is not a priority; Security and stability is a priority | Required |
| Teams within the company who will perform the migration | Wants to be able to experiment; Cares about cost and following a secure path to migration| Optional |

## Delivery Guidance

This section includes all non-technical delivery guidance and supporting artifacts for the Go-Live Assessment for Migrating Code Repositories to GitHub session. You are free to adapt each step to meet your customers' needs if you can meet the objectives and deliverable standards for the Developer Velocity Assessment. As part of the assessment, it's helpful to understand how the research below is foundational to building this assessment and how it can relate to the outcomes recommended for the assessment.


**Biggest Differentiator: Open Source**

Among the key drivers of Developer Velocity for top-performing organizations, open-source adoption is the biggest differentiator. According to [research](https://azure.microsoft.com/mediahandler/files/resourcefiles/developer-velocity-how-software-excellence-fuels-business-performance/Developer-Velocity-How-software-excellence-fuels-business-performance-v4.pdf), Organizations that are best-in-class on open-source capabilities score 30 percent higher on innovation and 20 percent higher on developer satisfaction.


### Step 1: Scoping Call

During the call the delivery resource explains the delivery flow and measures of the assessment.

The focus of this engagement is on enabling the customer to complete their migration to GitHub Enterprise Cloud. The customer will be responsible for the actual migration of their repositories, but the provider will be responsible for enabling the customer to complete the migration. The provider will also be responsible for providing guidance on the migration process and best practices. 

The scoping call provides an opportunity to ask questions such as:

- What do you expect from the assessment?
- Who needs to be in the room for the engagement?
- Are we schedulig this session to be remote or onsite?
- When should advisory sessions, planning sessions, enablement sessions happen?
- Does the customer meet the technical prerequisites? 

As part of the call, identify who should participate in the Developer Velocity Assessment. Many organizations have a diverse set of development teams. Given the limited time available, the most practical approach will often be to focus on one of the customer's flagship products or projects. Depending on the customer's organizational structure, people who can represent all aspects of the product lifecycle should participate in the assessment. The following lists serve as a suggetsion of what roles should be required and optional for the sessions. 

Required roles include:
- DevOps Engineers 
- GitHub Enterprise Admins 
- Source VCS Admins 

Optional roles might include:
- Teams within the company who will perform the migration 
- Workload Owners or Solution Architects
- Product or Project Managers
- Members of the customer's security team
- Software Development Engineers and Testers
- UX Designers or Specialists
- etc.

Based on the organizational structure, calendar availability and size of the team, it might be useful to schedule more than one session in order to ensure you can maximize the amount of information captured. 

#### Recommended: Account Team Scoping

If you have not worked with the account or the teams, you will be interviewing previously it is highly recommended to also have a scoping call with the account team. 
The roles you might want to reach out to are the aligned App Innovation seller, Customer Success Account Manager, Account Technology strategist, or even the Services seller. 
Use your time with the account team to learn more about the key initiatives that the account team is already driving and what support offers the customer has already got in place. 

The assessment is a great discovery exercise and one of the account team members may well choose to shadow you during the engagement, which is a great way of providing additional context to conversations. A participating account team member can also help guide discussions or take notes as you move through the assessment.

### Step 2: Engagement Overview

After Scoping & Setup, the next phase is to proceed with four individual days that can be broken down in several sessions each. These sessions are: kickoff call, advisory, planning and enablement. Look at the details below to further your understanding about what each day will consist of. 

Before this training, the customer needs to have in place: 

- GitHub Enterprise Cloud Account 

- GitHub Enterprise configured for developer use 

- Identification of teams within the company who will perform the migration 

#### Day 1: Kickoff call

The kickoff call is an introduction and overview of the engagement.The customers are either presented with a pre-migration questionnaire or are interviewed regarding the source environment and the overall scope of the migration. This will help with setting up expectations and collecting information about the main objectives of each individual session. 

Agree on meeting values: transparency, honesty and free speech. Everyone's input should be valued. 

From this point forward you should aim to adress the customer following the below practices: 

- For each question you ask the customer make sure you **listen** to the customer discussion, particularly if there is disagreement between different members of the group. Take notes to capture what you are observing. 

- Once the group agrees on an answer **ask** probing questions and ensure participation.

- Before moving onto the next question, **capture** all your learnings. This helps you surface these learnings in the report later.

-As you move through the assessment **consult** real-time around how Microsoft helps customers accelerate and note down relevant offerings the customer may want to take advantage of. Capture any relevant Microsoft offerings and prioritize areas of focus with the customer as needed.

- Where time permits, check in with the account team and share any findings and potential oportunites to support the customer further. This can help you in identifying Unified Support opportunities for Enhanced Solution Add-ons, proactive delivery options, and identify existing and upcoming opportunities with the customer.

As you undergo this assesment with the customer, ask yourself and the customer the following questions:

- "In which area can the customer improve?"
- "What opportunities are most accessible in a 12 month timeframe?"
- "How else can we support the customer in this migration?" 
- "How can Microsoft help accelerate developer velocity?" 
- "What are the options available to us given the current state of the customer?"

#### Day 2: Advisory

The second day of the engagement is designed to give you and the customer the oportunity to do a deep dive into the customer's current state and desired future state based on the following migration options
- Develop a comprehensive migration plan for code repositories with timelines on one of ithe following
    - ADO to GitHub Enterprise
    - Bitbucket to GitHub Enterprise
    - GitHub to GitHub 

**Deliverables**

Facilitate two 4-hour sessions, preferably booked on two separate days. You will take notes of all the answsers collected during these sessions and use them for furthering the support in day 3 and 4. 

**Questions to be answered by the customer during advisory sessions**

|  **Question**       | **Notes to consider**                                            |
|---------------------|----------------------------------------------------------------------------|
| Q: What is the current source environment?  | For standard migrations only GEI migration paths are supported.  |
| Q: What is the target environment?  | The target environment for standard migrations is GitHub Enterprise Cloud but it is important to know if GHEC instance is configured for Enterprise Managed Users or Data Residency. |
| Q: How many repositories are there?  | The number of repositories will help determine the overall length of the migration. While not a hard limit, standard migrations tend to involve 3000 repositories.  |
| Q: What is the size of the largest repository?  | There is a 20GB limit on repository size. |
| Q: Are there any empty or archived repositories?  | Empty or archived repositories can be excluded from the migration.  |
| Q: Is LFS in use? | While LFS can be used with GitHub Enterprise Cloud, it is not supported by the migration tooling. |
| Q: What external integrations are in use?  | The customer will need to recreate any external integrations in GitHub Enterprise Cloud. |
| Q: What organization(s) are being migrated to?  | The customer may have a singular organization they wish to migrate to or multiple |
| Q: Depending on the source environment, the GitHub Enterprise Importer may have specific requirements and limitations, these should be reviewed with the customer to determine if any third party tooling or scripts will be required to handle any gaps in the migration tooling. Use the following direct links to the relevant information:  | [About migrations from Bitbucket](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-from-bitbucket-server-to-github-enterprise-cloud/about-migrations-from-bitbucket-server-to-github-enterprise-cloud), [about migrations from Azure DevOps](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-from-azure-devops-to-github-enterprise-cloud/about-migrations-from-azure-devops-to-github-enterprise-cloud) and [about migrations betwwen GitHub Products](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-between-github-products/about-migrations-between-github-products) |

The combined answers to these questions along with any other relevant information captured during scoping should be enshrined in a markdown document in the collaboration repository. This document is intended to be a living document that can be updated as more information is gathered, and is the formal Migration Requirements document. An example of this document can be found [here](https://github.com/ps-resources/es-offerings-assets/blob/antgrutta/migrations-revamp/gh-github-migrations/examples/migration-requirements.md).

#### Day 3: Planning

**Deliverables**

Facilitate two 4-hour sessions, preferably booked on two separate days. You will take notes of all the answsers collected during these sessions and use them for furthering the support in day 4. The customer team identified for the migration enablement should be present for this session.

The planning session is intended to define and document the end-to-end migration steps. This includes the migration tooling to be used, the migration order, the migration schedule, and the validation steps.

**Pre-migration Tasks**

|  **Task**       | **Notes to consider**                                            |
|---------------------|----------------------------------------------------------------------------|
| Identify repositories that will or will not migrate.  | Provide criteria for determining if a source repository is eligible for migration.   |
| Document how large files will be handled.  | Document the steps the customer should take prepping repositories with large files. |
| Document how repositories will be scheduled for migration.  | Document how the customer is grouping repositories for migration and the proposed order. Note any deadlines or proposed timelines from the customer. This may be updated based on feedback during the proof-of-concept activity.  |
| User access and permissions.  | Document how user access and permissions will be handled in the target versus the old.  |
| Document how external integrations will be handled.  | Document how the customer will recreate any external integrations in GitHub Enterprise Cloud and validation steps. |

**Migration Tasks**

|  **Task**       | **Notes to consider**                                            |
|---------------------|----------------------------------------------------------------------------|
| Document the migration tool to be used.   | GitHub Enterprise Importer is the only supported tool for standard migrations, however it comes in different versions based on the source environment. Provide the documentation link to the specific GEI version chosen.  |
| Document other migration related tooling  | Document any other tooling that will be used in the migration process. These are usually custom scripts or third part tools to cover gaps in the migration tooling. For example, a script to handle LFS files, add custom repository properties, etc. |

**Post-migration Tasks**

|  **Task**       | **Notes to consider**                                            |
|---------------------|----------------------------------------------------------------------------|
| Document the validation steps.  | Document the steps the customer will take to validate the migration.  |

This information should be captured in a markdown document in the collaboration repository. This document is intended to be a living document that can be updated as more information is gathered, and is the formal Migration Plan document. 

#### Day 4: Enablement

**Deliverables**

Facilitate four 4-hour sessions, preferably booked on four separate days. You will take notes of all the answsers collected during these sessions and use them for a succesful completion of the assesment. The customer team identified for the migration enablement should be present for this session.

The enablement session is intended to ensure that the customer has the migration tooling installed and configured. This is a hands-on session where the customer will install the migration tooling and configure it to connect to their source environment. 

During the enablement session, the customer should perform all tasks necessary to install and configure the migration tooling on their system. While this tooling can be installed on a desktop and or laptop, our recommendation is that this tooling be installed on a server to mitigate any potential network issues. 

**Step 1** 

Installing the GitHub CLI: A prerequisite of installing the migration tooling is the installation of the [GitHub CLI](https://cli.github.com/), the installation instructions can be found [here](https://github.com/cli/cli#installation).

**Step 2**

Installing the GitHub Enterprise Importer: Using the below table, the customer should be directed to the appropriate documentation for their source environment. Assist the customer in installing the required extension and configuring it per the documentation.

|  **Source Environment**       | **Documentation Link**                                            |
|---------------------|----------------------------------------------------------------------------|
| Bitbucket  | [About migrations from Bitbucket](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-from-bitbucket-server-to-github-enterprise-cloud/about-migrations-from-bitbucket-server-to-github-enterprise-cloud)|
|Azure DevOps | [About migrations from Azure DevOps](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-from-azure-devops-to-github-enterprise-cloud/about-migrations-from-azure-devops-to-github-enterprise-cloud)|
|GitHub Enterprise Server or other products | [about migrations betwwen GitHub Products](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-between-github-products/about-migrations-between-github-products) |

**Step 3** 

Migrate a single repository: The customer should be walked through the process of migrating a single repository. This will allow them to become familiar with the tooling and the process, directions are included as part of the installation documentation.
**Step 4**

Test all other migration related tooling: If there are any other tools that will be used in the migration process, the customer should be walked through the installation and configuration of these tools. This is also a good time to test the tools to ensure they are working as expected.

**Close Out**

You will deliver Migration Requirements document, the Migration Plan documentand, a fully migrated repository and executive summary deck stating any follow up recomendations including but not limited to a proof of concept session during a close out meeting.
This meeting is intended to recap the core deliverables from the assessment focusing on key taks to be completed moving forward and answer any questions in regards to what has been done. It is important to include executive sponsors and IT decision makers in this meeting so they gain awareness of improvement recommendations and how Microsoft can help, which they can use to make resourcing and investment decisions on what steps will be taken to execute on the recommendations.

If needed the CSAM can help with scheduling this close out meeting on the last day. The recommended duration is 30 minutes of your last session with the team. 

**Understanding the assessment results**
Based on the objectives of this assement, you can consider this enagment successful if the following criteria is met:

1. You managed to develop a comprehensive migration plan with timelines and specific criteria for migration.
2. The customer was successfully enabled to use migration tools and is now well versed on how to operate migration tooling effectively 
3. Customer is able to apply best practices for full repository migrations
4. One repository was fully migrated
5. Migration validation was performed
6. Migration Requirements document was completed
7. Migration Plan document was completed
8. All pre-migration, migration and post-migration tasks have been compelted without any errors
9. All stakeholders have access to collaborate in the repository containing the migration documents mentioned above
10. The cusotmer is awre of their responsibility for migrating the reimaining repositories

## Resources, Readiness and References

- Leverage the [learning path](./access-lp.md) for the Assessment resources within this VBD

### Public Documentation

- Customer facing website for Developer Velocity: [https://azure.com/developervelocity](https://azure.com/developervelocity)
- [Developer Velocity: How software excellence fuels business performance](https://azure.microsoft.com/en-us/resources/developer-velocity-how-software-excellence-fuels-business-performance/)
- Assessment platform [Frequently Asked Questions site](https://learn.microsoft.com/assessments/support/)

### Supporting videos and concepts
- [video recordings](https://github.com/ps-resources/es-offerings-assets/discussions/229)
- [GitHub Enterprise Importer](https://docs.github.com/en/enterprise-cloud@latest/migrations/using-github-enterprise-importer)
- [The SPACE of Developer Productivity](https://www.youtube.com/watch?v=t7SXM7njKXw&ab_channel=MicrosoftResearch)
- [Developer Velocity - YouTube](https://www.youtube.com/playlist?list=PLLasX02E8BPAvZ1ZH9fuF__VB2qDe3xGN)
- [VBD Bootcamp for this delivery](https://microsofteur-my.sharepoint.com/:v:/g/personal/dasto_microsoft_com/EcH4iIyyEfBLtALXXUTkiPMB6oHha9i89N0KrmFp0eFS5Q)
- [VBD Bootcamp slides](https://microsoft-my.sharepoint.com/:p:/p/apthomas/ETjGXLgSaVxEjXVolTOMKqIBrfBckcl2Cv7E7AZUjkmeCg)

### Community support

- [Developer Acceleration Program Teams Channel](https://teams.microsoft.com/l/channel/19%3A68e6e017cd9346b2918fccdd9e53c637%40thread.tacv2/Developer%2520Acceleration?groupId=d9e33d34-3af7-4998-8355-ba6bd1c89bf1&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47) for tips, best practices, and peer sharing

## Known issues and updates

- We lack MIP, VBD or other offerings that focus on Organizational Enablement.
- The DVA doesn't replace offerings such as the DevOps Capability Assessment. There are times when the DevOps Capability Assessment is required to discover deep information where a DVA is inconclusive.
- There is a telemetry dashboard for the Microsoft Assessment platform that shows metrics about the assessments taken on the platform: [https://aka.ms/AssessmentsDashboard](https://aka.ms/AssessmentsDashboard)
- The version of the DVA that was hosted outside of the Microsoft Assessment platform used to capture customer-specific details and average assessment scores by industry. The assessment platform team is actively working on enabling the capture of these details for all assessments on aka.ms/assessments. If you require averages from previous assessments as part of your reporting, you can review to the table of averages in this document. Please note that all averages are computed purely based on completed assessments during the time when the first version of the DVA was live.
- A user taking an assessment on aka.ms/assessments is asked to log in. If an assessment is completed by a customer account, they are able to retake the assessment with the same account and show progress over time. This is a new feature that wasn't available when the first version of the DVA was live.

## Frequently Asked Questions

**I'm a GitHub Hubber. What internal resources are available to support my delivery of this offering?**
Refer to the provided [video recordings](https://github.com/ps-resources/es-offerings-assets/discussions/229) for our es-offerings-assets GitHub repository. Ensure you are proficient with the [GitHub Enterprise Importer](https://docs.github.com/en/enterprise-cloud@latest/migrations/using-github-enterprise-importer) content as that is the basis of this offering.  

**How do we ensure that the migration tooling installation and configuration goes smoothly?**
Before the enablement session begins, we strongly recommend the customer to have an environment that has network connectivity to their source VCS and github.com. They should also have access to their source repositories and write access to their target organisation in GitHub.

**How do we ensure migration enablement is successful?**
The key is to ensure that all the required stakeholders are present for the training and enablement sessions. The customer may request to start these sessions without all attendees due to resourcing constraints, however we strongly recommend holding off the engagement until everyone is present. It is critical that everyone is on the same page for the migration to be successful.