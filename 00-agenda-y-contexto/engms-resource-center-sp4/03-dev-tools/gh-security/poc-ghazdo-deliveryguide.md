# Delivery Guide: Proof of Concept - GitHub Advanced Security for Azure DevOps
This guide provides details and instructions to help you deliver the **Proof of Concept - GitHub Advanced Security for Azure DevOps** for your customer. This engagement must accomplish the following objectives:  

## IPKit

> The IPKit with artifacts to use throughout this delivery is located [here](https://microsoft.sharepoint.com/:f:/r/teams/ASDIPRelease/AzureCloudAI/SP2%20VBD/DevTools/GitHub/Proof%20of%20Concept%20-%20GitHub%20Advanced%20Security%20for%20ADO?csf=1&web=1&e=q5Z6Va).

**Objectives**

- Build a Proof of Concept (PoC) around one or more of the customer's Azure DevOps Repos (Azure DevOps Services) that they would like to enable GitHub Advanced Security to demonstrate value
- Help the customer understand the value of GitHub Advanced Security on Azure DevOps and DevSecOps practices, including the new standalone product offerings (GitHub Secret Protection and GitHub Code Security)
- Increase the customer's knowledge and experience through the PoC, so that you can have more informed and effective discussions around enabling GitHub Advanced Security for Azure DevOps at scale across the entire organization
- Enable GHAS on Azure DevOps repositories
- Demonstrate security features: Secret Scanning, Dependency Scanning, Code Scanning.
- Educate teams on DevSecOps practices.
- Demonstrate integration capabilities with Microsoft Defender for Cloud for enhanced security posture visibility

**Prerequisites**
- Azure DevOps Services with Azure Repos Git and Pipelines.
- Permissions:
  -- Project Collection Administrator or Advanced Security: manage settings = Allow.
  -- Edit Build Pipeline permissions.
- Billing: charged per active committer for enabled repos.

**Feature Overview**

Standalone:
- Secret Protection: push protection, secret scanning alerts.
- Code Security: dependency alerts, CodeQL scanning.

Bundled:
- All features combined under one license.

**Deliverable Standards**

- Delivery of Education Sessions (DevSecOps, Secret Scanning, Dependency Scanning, Code Scanning)
- Forecast time needed to complete proof of concept for identified Azure DevOps Repos
- Deploy Proof of Concept (PoC) implementation of GitHub Advanced Security for Azure DevOps on agreed repositories
- Demonstrate new standalone product capabilities and pricing models 

## Customer Participants

`Note: Provide details on the customer participants that are needed for a successful delivery `

Having the right customer participants in the Proof of Concept is essential to completing a successful engagement. Ensure the customer roles outlined below are available and able to participate in the workshop.

|Customer Role | Description | Required or Optional|
|----|----|----|
|DevOps/DevSecOps | Team responsible for deploying application to production and pipeline setup | Required
|Software Developers | People with experience in coding or advanced makers | Required
|Security Team | Team responsible for security across all aspects of the application and alert triage | Required
|Developers Team | Team responsible for remediation and adoption | Required
|Other IT professionals| These are the people responsible for provisioning and managing IT resources like databases, networking, compute, IAM, Security, etc.  | Optional|

## Delivery Guidance

This section includes delivery guidance and supporting artifacts.  You are free to adapt each step to meet your customers needs as long as you are able to meet the objectives and deliverable standards. We estimate Level 101 as beginner, 201 is intermediate, and 301 as advanced

### Step 1: Scoping

Explain how the delivery will be carried out. What they can expect at each phase, before and after delivery. Request the customer roles that will be needed for a successful delivery. Refer to [Customer Participants](#customer-participants) section for details.

Understand the requirements and resources required to deliver the PoC. Ensure they are clearly documented and communicated to the customer. Ensure all the stakeholders are on the same page regarding deliverables (PoC) - **not only what PoC will be but also what it will not be**.

Key Requirements Include:
- Customer must have enabled GitHub Advanced Security on their organization prior to engagement OR be ready to purchase one of the new standalone products (GitHub Secret Protection $19/active committer/month or GitHub Code Security $30/active committer/month)
- Customer must use Azure DevOps Services (Azure Repos Git and Azure Pipelines)
- Customer develops primarily in the [languages that CodeQL covers](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) - now supporting 13+ languages including C/C++, C#, Go, Java, JavaScript/TypeScript, Python, Ruby, Kotlin, Swift, Rust, and GitHub Actions
- Customer understands the new pricing model: there is no "free trial" license with GHAS for ADO. Customers will be charged for active committers using either the bundled GitHub Advanced Security or the new standalone products (Secret Protection and/or Code Security)

Make sure that the other IT staff who can provision resources and grant access are available when needed. If the pre-requisites are not met, then it may jeopardize the delivery of the PoC.

Initial access must include:

- Member of Project Collection Administrator group
- Delegated the “Advanced Security: read alerts, manage and dismiss alerts, manage settings” permission
- Permissions to Edit Build Pipeline will also be required to configure security scans

Use scoping call to understand what topics you may have to prepare for during the engagement.

Some example questions you may ask during the scoping are:

- What do you expect from the delivery?
- What is your current application security state?
- What technical / business problem are you expecting the PoC to solve? / What is your desired Application security desired future state?
- What topic areas within the PoC are most relevant to the team?
- What are some of your larger business objectives that GitHub Advanced Security for Azure DevOps would support?
- Are you interested in the new standalone products (Secret Protection vs Code Security) or the full bundled Advanced Security solution?
- How do you currently manage security scanning and vulnerability management across your development lifecycle?
- What integration do you have with Microsoft Defender for Cloud, and are you interested in unified security posture visibility?
- What are the skill levels of the developers, operations and security teams?

### Step 2: Find Supporting Material

While building out a Proof of Concept might involve work specific to customer requirements, here are some updated resources that might be able to kick start your development.

| Level | Resource | High Level Description |
|----|----|----|
| 300 | [GitHub Advanced Security for Azure DevOps](https://azure.microsoft.com/en-us/products/devops/github-advanced-security) | Official product page with latest features and capabilities |
| 200 | [GitHub Secret Protection and Code Security Blog](https://devblogs.microsoft.com/devops/github-secret-protection-and-github-code-security-for-azure-devops/) | Latest announcement about standalone products (June 2025) |
| 300 | [CodeQL Language Support](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) | Current supported languages and frameworks for code scanning |

#### Other Resources

- [Azure DevOps Pricing Calculator](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/) - Use this to estimate costs for Secret Protection ($19/month) and Code Security ($30/month) per active committer
- [Microsoft Defender for Cloud Integration](https://www.microsoft.com/en-us/security/business/cloud-security/microsoft-defender-cloud) - Learn about unified security posture management
- [Azure DevOps Documentation](https://learn.microsoft.com/en-us/azure/devops/) - Latest Azure DevOps documentation and features

### Step 3: Delivery

**Day 1: Education and Discovery**

Open the Day 1 session with the customer by delivering education on GitHub Advanced Security for Azure DevOps, including the new standalone product offerings:

- **GitHub Secret Protection** ($19 per active committer per month): Includes push protection, secret scanning alerts, and security overview
- **GitHub Code Security** ($30 per active committer per month): Includes dependency alerts, CodeQL scanning, security findings for third-party tools, and security overview  
- **Bundled GitHub Advanced Security**: Traditional offering that includes all features

A demo of GitHub Advanced Security for Azure DevOps should be included with the education portion of the session. This allows all participants to see the latest features in action and align on the technical goals for the POC. Highlight the integration with Microsoft Defender for Cloud for unified security posture visibility.

**Key Topics to Cover:**
- Latest CodeQL language support (13+ languages including new support for Rust, Swift, Kotlin, and GitHub Actions)
- Enhanced secret scanning with 200+ token types and 100+ service provider integrations
- Integration capabilities with Microsoft Defender for Cloud
- New flexible pricing options with standalone products

Next, start the Discovery portion of the PoC session by documenting the business needs and what a successful outcome would be like. 

This Proof of Concept (PoC) should focus on identifying 3-4 repos to configure and then working with the customer to implment based on 2-3 defined goals and measures of success for the engagement. 

Some common goals/measures of success include:

- We would like to speed up our release process by reducing time spent fixing vulnerabilities. To achieve this, we need to not only scan pushes to the default branch but also pushes and pull requests on all long lived branches (release/qa/dev) so we increase our chances of finding vulnerabilities early in the development cycle, where it is easier and faster for a developer to fix the issues reported

- We would like to have confidence that security testing has been run before merge, so we need developers to accept security as part of the merge process. We do not want our scanning tool to be a blocker on merging pull requests which will result in developers bypassing the tool, so we need a tool that can be configured to run quickly and will be adopted by our developers.

- We would like reduce organizational workload and enable our developers to directly triage and fix vulnerabilities, so we need a tool that puts developer experience first. They should be able to use the tool easily and not find it a burden to review and understands scan results, which should lead to more vulnerabilities being fixed without the need for specialist support.

- We would like to increase productivity with a tool that decreases the amount of time we spend looking at false positives and increases focus on true vulnerabilities. This leads to less wasted time looking through endless reports.

Next, align 2-3  metrics with the goals set by the customer:

Some example metrics include:

- How many false positives versus true positives were found during a GitHub Code Scanning scan?

- How many vulnerabilities were remediated out of the total that GHAzDO reported? (numbers, percentages)

- How many secrets were found during a Secret Scan?

Finally, wrap up by working with the customer to identify 3-4 repos for the POC and ensure the appropriate security features are enabled on these repos based on their chosen product tier (Secret Protection, Code Security, or full Advanced Security). This will help prepare for enablement of the selected security capabilities and review of all scan results as part of Day 2-3 of the PoC. 

Some items to consider when choosing repos:

- Recommend identifying critical business applications where the customer is already able to build the code in existing AzDO Pipelines
- Repositories with large amounts of code in are good as they have a higher chance of containing vulnerabilities.
- New applications using modern web frameworks are less likely to contain significant vulnerabilities.

**Day 2-3: Proof of Concept Execution**

Following these Day 1 discussions, work with the customer in Days 2-3 to fully configure and implement the identified repos for GitHub Advanced Security, remaining mindful of the agreed exit criteria, and avoiding scope creep.

Overall goals for each POC repository identified in Day 1:

- Enable GHAS (Standalone or Bundled).
- Configure the selected security products (Secret Protection and/or Code Security) based on customer requirements and budget
- Enable push protection for secret scanning to prevent secrets from being committed
- Setup an Azure Pipeline to run dependency and code scanning (if Code Security is enabled)
- Ensure findings are properly being reported in the Azure DevOps UI and Security Overview
- Demonstrate integration with Microsoft Defender for Cloud for unified security posture (if applicable)
- Develop a remediation plan for any scanning results found
- Show how to manage alerts and security findings at scale across multiple repositories
- Configure pipelines for scanning.
- Validate alerts and remediation workflows.

**Updated POC Activities:**
- Configure repository-level security settings based on chosen product tier
- Demonstrate the new security overview dashboard capabilities
- Walk through alert management and remediation workflows
- Show integration points with existing DevOps toolchain
- Demonstrate cost management and active committer tracking



***Pipeline Configuration (YAML Examples)***

**Code Scanning with CodeQL**
```yaml

trigger:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: CodeQLInitialize@1
    inputs:
      languages: 'csharp, javascript'
      buildMode: 'manual' # or 'none'
  - task: CodeQLAnalyze@1

````

**Supported languages:** cpp, csharp, go, java, javascript, python, ruby, swift.
**Build modes:**
- none – no build required (interpreted languages).
- manual – define build steps for compiled languages.


**Secret Scanning**
```yaml
steps:
  - task: AdvancedSecurity-SecretScan@1
    inputs:
      failOnSecretsFound: true
````
Includes push protection and historical scan.

**Dependency Scanning**
```yaml
steps:
  - task: AdvancedSecurity-DependencyScan@1
    inputs:
      failOnVulnerabilitiesFound: false
````

Optional: Custom CodeQL Queries
- Add qlpack.yml and reference custom queries:
```yaml
steps:
  - task: CodeQLInitialize@1
    inputs:
      queries: 'path/to/custom/query.ql'
```
Supports query packs and GitHub-hosted packs with token authentication


**Integration with Microsoft Defender for Cloud**

Sync GHAS alerts with Defender dashboards for unified security posture.

Benefits:
- Centralized view of vulnerabilities.
- Correlation with broader cloud security signals.


Steps:
- Enable integration in Azure DevOps Advanced Security settings.
- Verify alerts appear in Defender for Cloud Security Posture dashboard.

***Day 3: Presentation and Customer close out***

At the end of the 3 days, present the completed PoC and the related findings and conclusions to the customer. Ideally, the customer team would have been engaged during the delivery, and you can encourage the team to be involved in the presentation. If the customer asks questions you are unsure about the response to, write them down and give an estimated timeline for follow up. Be sure to highlight where the PoC deviated from the original plan, and why, as this may be valuable information that the customer can use to refine their plans for enabling GitHub Advanced Security for Azure DevOps at scale across the entire organization.

Thank the customer for their time, and identify the next follow-up actions, which could be one or more of the following:

- A regular check-in to provide continuous guidance as they scale their adoption
- Discussion about migrating from bundled to standalone products (if applicable) or planning for organization-wide rollout
- Guidance on cost optimization strategies with the new pricing models  
- Integration planning with Microsoft Defender for Cloud for enhanced security posture management
- Provide ongoing support resources and contact information for follow-up questions

## Additional Resources & References

### Official Documentation and Resources
- [GitHub Advanced Security for Azure DevOps Product Page](https://azure.microsoft.com/en-us/products/devops/github-advanced-security)
- [GitHub Secret Protection and Code Security Announcement](https://devblogs.microsoft.com/devops/github-secret-protection-and-github-code-security-for-azure-devops/) (June 2025)
- [Azure DevOps Pricing Calculator](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/)
- [CodeQL Language Support Documentation](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/)
- [Azure DevOps Security Documentation](https://learn.microsoft.com/en-us/azure/devops/organizations/security/)

### Integration and Advanced Features  
- [Microsoft Defender for Cloud](https://www.microsoft.com/en-us/security/business/cloud-security/microsoft-defender-cloud)
- [Azure DevOps Blog - Latest Updates](https://devblogs.microsoft.com/devops/)
- [GitHub Security Features Overview](https://docs.github.com/en/code-security)

### Community and Support
- [Azure DevOps Documentation](https://learn.microsoft.com/en-us/azure/devops/)
- [Developer Community for Azure DevOps](https://developercommunity.visualstudio.com/AzureDevOps)
- [Microsoft Tech Community - Azure DevOps](https://techcommunity.microsoft.com/)


## Known issues and updates

### Recent Updates (2025)
- **June 2025**: Launch of standalone GitHub Secret Protection  and GitHub Code Security products
- **Ongoing**: Enhanced CodeQL language support including Rust, Swift, Kotlin, and GitHub Actions workflows
- **2025**: Improved integration with Microsoft Defender for Cloud for unified security posture management
- **Latest**: Secret scanning now supports 200+ token types with 100+ service provider partnerships

### Migration Information
- Existing customers can continue using bundled GitHub Advanced Security
- To migrate to standalone products, contact Azure DevOps support via Azure Portal
- File support ticket under "GitHub Advanced Security for Azure DevOps" service with problem type "Billing migration from bundled to standalone products"

### Current Limitations
- GitHub Advanced Security features are only available for Azure DevOps Services (not Azure DevOps Server)
- Active committer billing applies to all users who commit to enabled repositories within the billing period
- Push protection and some advanced features require specific repository permissions 

### Community support

- [Azure DevOps Blog](https://devblogs.microsoft.com/devops/)
- [Developer Community for Azure DevOps](https://developercommunity.visualstudio.com/AzureDevOps)
- [Microsoft Tech Community - Security](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/ct-p/MicrosoftSecurityandCompliance)
- [Azure DevOps Documentation](https://learn.microsoft.com/en-us/azure/devops/)
- [GitHub Advanced Security Documentation](https://docs.github.com/en/code-security/getting-started)