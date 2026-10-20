# Delivery Guide: Proof of Concept for Migrating Code Repositories to GitHub
This guide provides details and instructions to help you deliver the **Proof of Concept for Migrating Code Repositories to GitHub**.
The activity leverages tools including **GitHub, Visual Studio, and GitHub CLI**. 
This engagement must accomplish the following objectives:  

**Objectives**
- Start building a Proof of Concept with your customer on their specific business needs for migrating code  repositories to GitHub based on the following options.

**Deliverable Standards**
- Delivery Guide: Proof of Concept for Migrating Code Repositories to GitHub
  - Customer Participants
  - Delivery Guidance
    - Scoping
    - Find Supporting Material
      - GitHub
      - Azure DevOps
      - GitHub CLI
      - GitHub Enterprise Importer
      - Scenarios
      - Other Resources
      - Practice Validation
    - Delivery
    - Presentation
    - Customer Close Out
  - Additional Resources \& References
    - Community Support
    - Known Issues and Updates


## Customer Participants

Having the right customer participants in the Proof of Concept is essential to completing a successful engagement. Ensure the customer roles outlined below are available and able to participate in the workshop. 

| **Customer Role** | **Description** | **Required or Optional** |
| --- | --- | --- |
| DevOps Engineers | Wants to move fast, to be enabled; Doesn't care about cost; Cares less about security, resilience, more about features | Required |
| --- | --- | --- |
| GitHub Enterprise Admins | Wants to grow and enable team; Cares about velocity and quality; Cares about budget; Struggles to get necessary budget to find the best people and invest in enablement | Required |
| Source VCS Admins  | Moving fast is not a priority; Security and stability is a priority | Required |
| Teams within the company who will perform the migration | Wants to be able to experiment; Cares about cost and following a secure path to migration| Optional |


## Delivery Guidance

This section includes delivery guidance, supporting artifacts, and scenarios.  You are free to adapt each step to meet your customers needs as long as you are able to meet the objectives and deliverable standards. We estimate Level 101 as beginner, 201 is intermediate, and 301 as advanced.

### Scoping 

Explain how the delivery will be carried out. What they can expect at each phase, before and after delivery. Request customer that for the successful delivery who would you need. Refer to [Customer Participants](#customer-participants) section for details.

Ensure you discuss and understand the customer's requirements and tooling to be used as the source of your migration (Azure DevOps, Bitbuck or GitHub) at a high level and review any customer documentaation that will be used for PoC. Include conversation points about the general organization and coding strategy, as well as tooling currently used by developers. Ensure all the stakeholders are on the same page regarding deliverables (PoC) - **not only what PoC will be, but also what it will not be**.

Make sure that the other IT staff who can provision resources and grant access are available when needed. If the pre-requisites are not met, then it may jeopardize the delivery of the PoC.

Use scoping call to understand what topics you may have to prepare for during the engagement.

Some example questions you may ask during the scoping are:

- What do you expect from the delivery?
- What technical / business problem are you expecting the PoC to solve?
- What topic areas interest you within this PoC that are most relevant to the team?
- What are the skill levels of the developers, operation and security teams with GitHub?
- What types of performance and/or resiliency is expected from the PoC?


### Find Supporting Material

While building out a Proof of Concept might involve work specific to customer requirements, here are some resources that might be able to kick start your development.

#### GitHub 

| Level | VBD Asset Name | High Level Description | IP Kit |
|----|----|----|----|
| 300 | GitHub: GitHub Migration Offering | Guidance around migrating content from a diverse set of DevOps platforms to GitHub | [Current Version](https://aka.ms/GHIPMigration)

#### Migratrion documentation from multiple source environment

|  **Source Environment**       | **Documentation Link**                                            |
|---------------------|----------------------------------------------------------------------------|
| Bitbucket  | [About migrations from Bitbucket](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-from-bitbucket-server-to-github-enterprise-cloud/about-migrations-from-bitbucket-server-to-github-enterprise-cloud)|
|Azure DevOps | [About migrations from Azure DevOps](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-from-azure-devops-to-github-enterprise-cloud/about-migrations-from-azure-devops-to-github-enterprise-cloud)|
|GitHub Enterprise Server or other products | [about migrations betwwen GitHub Products](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-between-github-products/about-migrations-between-github-products) |


#### Scenarios

| Scenario | High Level Description | IP Kit  or other resources|
|----|----|----|
| Ent-To-End Security with Azure DevOps | This content gives you a step by step on how to implement security using GitHub Advanced Security with ADO. | [Current Version](https://docs.microsoft.com/en-us/users/githubtraining/collections/rqymc6yw8q5rey) |
| Sync GitHub issue to Azure DevOps work item | This content gives you a step by step on how to sync GitHub issue to Azure DevOps work item. | [Current Version](https://github.com/microsoftedge/action-issue-to-workitem) |
| Bitbucket Migration | Information on how to migrate a code repository from Bitbucket to GitHub| [About migrations from Bitbucket](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-from-bitbucket-server-to-github-enterprise-cloud/about-migrations-from-bitbucket-server-to-github-enterprise-cloud)|
| Azure DevOps Migration | Shows how to migrate a code repository from Azure DevOps to GitHub| [About migrations from Azure DevOps](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-from-azure-devops-to-github-enterprise-cloud/about-migrations-from-azure-devops-to-github-enterprise-cloud)|
|GitHub Enterprise Server or other products Migration | Information on how to migrate a code repository from other GitHub products to GitHub itself| [About migrations betwwen GitHub Products](https://docs.github.com/en/migrations/using-github-enterprise-importer/migrating-between-github-products/about-migrations-between-github-products) |
| Project management with Azure DevOps | This content gives you a base structure on how to use Azure Boards to manage projects with Azure DevOps. (please use PartsUnlimited template and ignore the source code) | [Current Version](https://azuredevopsdemogenerator.azurewebsites.net/) |
| Automate an existing load test with CI/CD | This content gives you a step by step on how to automate an existing load test with CI/CD (DevOps, but it can be used with GitHub). | [Current Version](https://learn.microsoft.com/en-us/azure/load-testing/quickstart-add-load-test-cicd) |
| Governance on Azure with Azure DevOps | This content provides step-by-step guidance on implementing governance practices using Azure DevOps pipelines to deploy and manage ARM templates. It includes policy enforcement, infrastructure compliance, and automated workflows. | [Current Version](https://github.com/Azure/devops-governance) |
| YAML Templates for Azure Pipelines | This resource provides ready-to-use YAML templates for various CI/CD scenarios, helping streamline pipeline creation for Azure Pipelines. It includes templates for build, release, and deployment stages. | [Current Version](https://github.com/microsoft/azure-pipelines-yaml/tree/master) |
| Terraform Labs for Azure | This content introduces Terraform basics and labs to help users manage Azure infrastructure as code. It provides hands-on exercises for provisioning, configuring, and managing Azure resources using Terraform. | [Current Version](https://github.com/Azure-Samples/terraform-fundamentals-labs/tree/main) |
| Application + Database Deployment using Azure DevOps | This demo project showcases an end-to-end CI/CD pipeline to deploy an application and its SQL database using Azure DevOps pipelines. It demonstrates integrated workflows for application code and database schema changes. |  [Current Version](https://github.com/Azure-Samples/app-sql-devops-demo-project) |
| IaC with Bicep in GitHub Actions | Demonstrates integrating Bicep-based resource deployment into GitHub Actions for infrastructure workflows. | [Current Version](https://github.com/Azure-Samples/bicep-github-actions) |
| Deployment Slots with GitHub | Shows how to manage and deploy to Azure App Service deployment slots using GitHub Actions workflows. | [Current Version](https://github.com/Azure-Samples/github-actions-deployment-slots) |


#### Other Resources 

- [GitHub Migration Planning](https://docs.github.com/en/migrations/overview/planning-your-migration-to-github)
- [Programmatically Importing Repositories](https://docs.github.com/en/migrations/overview/programmatically-importing-repositories)
- [About GitHub Enterprise Importer](https://docs.github.com/en/migrations/using-github-enterprise-importer/understanding-github-enterprise-importer/about-github-enterprise-importer)
- [DevSecOps Playbook](https://aka.ms/SolutionOps/DevSecOps-Playbook)
- [Secure DevOps by DevOps Dojo](https://microsoft.sharepoint.com/:p:/r/teams/DevOpsDojoCommunityofPractice/_layouts/15/Doc.aspx?sourcedoc=%7B86552956-01E8-487B-A25D-D268EE06BCFD%7D&file=DevOps%20Dojo%20-%20Secure%20DevOps.pptx&action=edit&mobileredirect=true&share=IQFWKVWG6AF7SKJd0mjuBrz9AYLfU8QEsOya7uxW4rbFKEg)
- [GitHub Actions for Azure](https://azure.github.io/actions)
- [DevSecOps: What, Why and How](https://www.youtube.com/watch?time_continue=1641&v=jdPlQvvloac&feature=emb_logo)
- [MS Learn Path: GitHub Advanced Security](https://docs.microsoft.com/en-us/users/githubtraining/collections/rqymc6yw8q5rey)
- [PowerBI Report with Azure Devops Analytics](https://learn.microsoft.com/en-us/azure/devops/report/powerbi/create-quick-report?view=azure-devops)

#### Practice Validation

- Migration of 12 or less repositories using GitHub Migration toolings from Bitbucket, Azure DevOps or from a different GitHub product.
- The migration team will confirm the target organization and the required integrations are configured and working. 
- The GitHub Enterprise Importer will be used to migrate the repositories from the source system to the target GitHub Enterprise Organization. 
- The migration team will monitor the migration and update the migration-inventory spreadsheet. 
- The migration team will notify the application dev teams when the migration is complete and the repositories are available for validation. 
- The migration team will validate the following: 
  - All repositories have been migrated. 
  - All branches have been migrated. 
  - All commit history has been migrated. 
  - All issues have been migrated. 
  - All pull requests have been migrated. 
  - All integrations are working.

### Delivery

This Proof of Concept (PoC) is to work with the customer to perform a dry run of the migration process. A migration plan, including schedule, source environment ifnromation and target environment information will be collected to stablish a document detailing next steps. The customer should be able to validate the results of completing this POC by checking each individual mark from the previous section (practice validation). Start the PoC design session by documenting the business needs and what a successful outcome would be like. Some topic sot cover include: 

- Define the exact criteria for a successful migration. 
- Develop a clear scoping document that articulates what is in scope and what is out of scope. Make sure all members on both teams have a copy of this scope document. Not having clearly define scoping document is one of the most common causes for unsatisfactory engagements. 
- At some point towards the end of the delivery discuss the long term support of the project (e.g bringing in Microsoft Partner Organizations, skilling up a customer internal team, ECIF funding, community resources, etc.).
- Validate that all code repositories have been migrated to GitHub from their source environment. 


### Presentation

Present the selected content to the customer. Try to keep the customer engaged during the delivery. If the customer asks questions you are unsure about the response to, record them and give an estimated timeline for follow up. Ensure that all information shared to the customer targets migration and questions brought up during scoping. 

Using the migration plan as a guide, have an interactive presentation and guide the customer to migrate 12 repositories. The customer should then validate the results of the migration and provide feedback. You should be prepared to make any necessary adjustments to the migration plan based on the feedback. 

### Customer Close Out

Thank the customer for their time. Discuss the plan to share VBD materials after the class and provide your contact information in case they need to follow up.
Explain that Microsoft may reach out to them for a course evaluation. 


## Additional Resources & References
- [Basics of code repositories in GitHub](https://docs.github.com/en/repositories)
- [Manage Repository Settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)
- [Programatically accessing Work Items Azure Boards](https://learn.microsoft.com/en-us/azure/devops/integrate/quickstarts/work-item-quickstart?view=azure-devops)
- [Rest API Azure Boards](https://learn.microsoft.com/en-us/rest/api/azure/devops/work/boards/get?view=azure-devops-rest-7.1)
- [Power BI with OData Integration](https://learn.microsoft.com/en-us/azure/devops/report/powerbi/odataquery-connect?view=azure-devops)
- [Azure Boards Github Integration](https://learn.microsoft.com/en-us/azure/devops/boards/github/?view=azure-devops)

### Community Support

- [Delivery Community](https://teams.microsoft.com/l/channel/19%3ad22589d7d37a4e8bbd025bf1697b9195%40thread.tacv2/VBD%2520-%2520Accelerate%2520Software%2520Delivery%2520Thru%2520DevSecOps?groupId=591c20e8-6a02-4476-8881-849bf672e6cf&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47)

### Known Issues and Updates

- Some source environments are not supported for migration through this VBD and through the GitHub Migration Tooling
