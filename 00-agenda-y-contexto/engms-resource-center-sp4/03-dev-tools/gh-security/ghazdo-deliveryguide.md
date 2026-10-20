Dev engagement: delivery guide

# Delivery Guide: Workshop - GitHub Advanced Security for Azure DevOps - Getting Started

# Introduction

This guide will provide details and instructions to help you deliver a successful GitHub Advanced Security for Azure DevOps VBD IP for your customer. 

## IPKit

> The IPKit with artifacts to use throughout this delivery is located [here](https://microsoft.sharepoint.com/:f:/r/teams/ASDIPRelease/AzureCloudAI/SP2%20VBD/DevTools/GitHub/Workshop%20-%20GitHub%20Advanced%20Security%20for%20ADO?csf=1&web=1&e=hs2URf).


**Objectives**

- Provide training and guidance to a customer to raise awareness and understanding of GitHub Advanced Security
- Assist a customer accelerate adoption of Advanced Security while avoiding common pitfalls 
- Work with a customer to learn and apply best practices for deploying GitHub Advanced Security through guided modules and hands on labs

**Deliverable Standards**

- Education sessions for GitHub Advanced Security for Azure DevOps workshop containing instructor sessions with slides, demos, and hands on labs
- Conduct Pilot Implmentation of GitHub Advanced Security for Azure DevOps on 1-5 customer repositories

## Customer Participants

| **Customer Role** | **Description** | **Required or Optional** |
| --- | --- | --- |
| DevOps/DevSecOps | Team responsible for deploying application to production | Required |
| Software Developers | People with experience in coding or advanced makers | Required |
| Security Team | Team responsible for security across all aspects of the application | Required |

## Delivery Guidance

This section includes all non-technical delivery guidance and supporting artifacts for the GitHub Advanced Security for Azure DevOps session. You are free to adapt each step to meet your customers' needs if you can meet the objectives and deliverable standards for the GitHub Advanced Security for Azure DevOps Workshop.

Before starting the engagement the following prerequisites will need to be satisfied:

- Attendees identified for each of the training sessions
- Identification of a pilot team with 1-5 repositories hosted in Azure Repos (Azure DevOps Services)
- GitHub Advanced Security for Azure DevOps has been enabled for selected repositories

## Demo Environment Access
- Demo environment can be accessed via https://github.com/msft-common-demos/bootstrap
- Delivery agent will require access to GitHub Golden Ticket repository, access instructions are available at https://aka.ms/golden-ticket 
- There are two flavors of demo available (choose one based on customer technology stack):
    - **GHAzDOs**: A demonstration of GitHub Advanced Security for Azure DevOps (GHAzDO) using WebGoat, a deliberately insecure application. This demo showcases key security features including secret scanning with push protection, dependency vulnerability detection, CodeQL-powered code analysis, PR gating, and integration with third-party security tools—all seamlessly integrated into the Azure DevOps workflow.
    - **GHAzDO .NET**: A demonstration of GitHub Advanced Security for Azure DevOps (GHAzDO) using WebGoatCore for .NET 7, a deliberately insecure application. This demo showcases comprehensive security scanning features including secret scanning with push protection, dependency vulnerability analysis, CodeQL-powered code scanning, PR gating, and third-party tool integration—all seamlessly working within the Azure DevOps environment for .NET applications.
### Step 1: Scoping Call

During the call the delivery resource explains the delivery flow and objectives of each section. Explain how the delivery will be carried out and what can be expected at each phase. 

The scoping call provides an opportunity to ask questions such as:

- What do you expect from the workshop?
- Who needs to be in the room for the engagement on each day?
- What topic areas are most releveant to the team during the pilot implementation and security review?
- What are the skill levels of the developers, DevOps, and security teams?

As part of the call, identify who should participate in each section of the workshop. Many organizations have a diverse set of development teams. Given the limited time available, the most practical approach will often be to focus on one of the customer's flagship products or projects.
Depending on the customer's organizational structure, people who can represent all aspects of the product lifecycle should participate in the assessment. 

Roles might include:
- Engineering Managers
- DevSecOps Team Members
- Platform Team Members
- Software Development Engineers 
- Product Security Teams
- Team Leads
- etc.

Selection of 1-5 repositories used for the Pilot Team Implementation and Security Results Review sections should also be discussed. Delivery Resource should ensure:
- Customer must have enabled GitHub Advanced Security on selected repositories prior to delivery.
- Code base must be in Azure Repos (Azure DevOps Services) prior to delivery.
    > *Note: Azure DevOps Server is not supported*
   
- The attendees must either:
  1. Have administrative privilege of the selected repositories; or
  2. Have Project Collection administrators enable GitHub Advanced Security for Azure DevOps on the selected repositories prior to delivery.

Templates:
- [Engagement Kickoff Template](https://microsoft.sharepoint.com/:p:/t/ASDIPRelease/EQBThJb-3yVKnt-aosbdPMsBtq3zQR_jAGKmHjFGvETm8Q?e=h1bvgS)

#### Recommended: Account Team Scoping

If you have not worked with the account or the teams you will be working with previously it is highly recommended to also have a scoping call with the account team. 
The roles you might want to reach out to are the aligned App Innovation seller, Customer Success Account Manager, Account Technology strategist, or even the Services seller. 
Use your time with the account team to learn more about the key initiatives that the account team is already driving and what support offers the customer has already got in place. 

### Step 2: Engagement Overview

This engagement supports "Getting Started" with GitHub Advanced Security for Azure DevOps. It helps accelerate customer adoptions in the critical first few weeks of deployment by providing training, advice, and best practices for key stakeholders. 

The engagement contains the following modules:

1. GHAS for Azure DevOps Rollout and Deployment Training
1. GHAS for Azure DevOps Security Team Training
1. GHAS for Azure DevOps Developer Training
1. GHAS for Azure DevOps Pilot Team Implementation
1. GHAS for Azure DevOps Security Results Review

**Reminder**
Before starting the engagement the following prerequisites will need to be satisfied:

- Attendees identified for each of the training sessions
- Identification of a pilot team with 1-5 repositories hosted in Azure Repos (Azure DevOps Services)
- Customer must have enabled GitHub Advanced Security on selected repositories

**Day 1: GHAS on AzDO Rollout & Deployment Training**

A successful GitHub Advanced Security for Azure DevOps rollout at scale requires careful planning and involves both technical and organizational change management. This training provides support during the planning phases by providing best practices, recommended rollout strategies and identifying common pitfalls and issues.

### Target Audience

- Platform Team
- Product Security teams
- DevSecOps teams

### Key features and benefits

- Understand best practices for rolling out GitHub Advanced Security for Azure DevOps.
- Learn about the technical features that help support a phased or gradual rollout of Advanced Security across your organization.
- Explore the techniques used to achieve high compliance and high remediation rates for identified vulnerabilities, including documentation and proactive enablement via PRs.
- Demonstration of how to enable GitHub Advanced Security for Azure DevOps.

### Engagement schedule

This module will consist of one session of 2 hours face-to-face time. Maximum session size is typically 16 people.

### Syllabus

- Introduction
- Enabling GitHub Advanced Security for Azure DevOps
- Planning a rollout
  - How to avoid forseeable problems
  - Get clean vs. keep clean
  - Code Scanning:
    - CI/CD integration, leveraging automation and CodeQL query selection
  - Secret Scanning:
    - Push protection, notifications and campaigns
  - Dependency Scanning:
    - Build logs, alerts, pipeline detections
- How to enable Code Scanning at scale
  - CI/CD integration strategies for CodeQL
  - Automating enablement of CodeQL
- Supporting developers
  - Internal documentation
  - Internal communication and support
  - Education
- How to enable Secret Scanning at scale
- Common pitfalls & how to be successful

### Learning outcomes/business outcomes

After completing this module participants will be able to:

- Enable the organization to maintain a sustained and controlled rollout of GitHub Advanced Security for Azure DevOps.

**Day 2: GHAS on AzDO Security Team Training**

This training session supports those who are responsible for reviewing, monitoring and driving remediation of security results across an enterprise. 

### Target Audience

- Product Security teams
- DevSecOps teams

### Key features and benefits

- We will review the basics of GHAS and its component features (Code Scanning, Secret Scanning and Dependency Scanning), and how access can be granted to those results.
- Discussion of monitoring and reviewing alerts

### Engagement schedule

This module will consist of one session of 2 hours face-to-face time. Maximum session size is typically 16 people.

### Syllabus

- Review of Advanced Security features
- Granting access to configure Advanced Security and view results
  - Permissions required to view results on repositories
  - Custom roles
    - Using custom roles to enable Security team members to view results across repos
- Reviewing alerts
    - Code Scanning Alerts
    - Secret Scanning Alerts 
    - Dependency Scanning Alerts
- Monitoring and responding to Advanced Security alerts
 
### Learning outcomes/business outcomes

After completing this module participants will be able to:

- Understand how to enable access to view the key components of GitHub Advanced Security for Azure DevOps
- Understand the options available for reporting, monitoring and responding to Advanced Security alerts.

**Day 3: GHAS on AzDO Developer Training**

GitHub Advanced Security for Azure DevOps allows you to have a "developer-first" approach to Application Security, recognizing that developers have a critical role to play in securing applications. This module will enable developers to both understand and effectively use the features of Advanced Security.

### Target Audience

- Developers
- Product Security teams
- DevSecOps teams

### Key features and benefits

- Understand the features available in GitHub Advanced Security for Azure DevOps
- Hands-on experience enabling GitHub Advanced Security for Azure DevOps features
- Reduce developer friction by increasing awareness of GitHub Advanced Security for Azure DevOps features.

### Engagement Schedule

This module will consist of one session of 2 hours face-to-face time. Maximum session size is typically 20 people.

### Syllabus

- What is GitHub Advanced Security for Azure DevOps 
  - Features of GHAS for Azure DevOps 
  - The benefits of using GHAS for Azure DevOps 
- Dependency Scanning (Lab)
  - Using Dependency Scanning
  - Enabling Dependency Alerts 
- Secret Scanning (Lab)
  - Using Secret Scanning
  - Push Protection
- Code Scanning (Lab)
  - Using Code Scanning
- CodeQL
  - What is CodeQL
  - How to Interact with CodeQL
  - Setting Up CodeQL Azure Pipelines
- GHAS for Azure DevOps in the Developer flow

### Learning outcomes/business outcomes

After completing this module participants will be able to:

- Understand the key components of GitHub Advanced Security
- Enable Secret Scanning and understand how to triage and remediate results
- Enable Dependency Scanning and understand how to triage and remediate results
- Enable CodeQL analysis within Azure Pipeines to perform static analysis for commonly used languages.
- Interact effectively with the Advanced Security user interface to understand, triage and remediate reported vulnerabilities.

**Day 4: Pilot team implementation**

In this module we will work with a pilot or lighthouse team to help them enable GitHub Advanced Security for one or more key repositories.

###  Target Audience

- Developers
- Product Security teams
- DevSecOps teams

###  Key features and benefits

- Guided session to help teams enable GitHub Advanced Security features on one or more repositories.
- Collaborate on customizing the configuration for the selected repositories to improve engagement and remediation rates.
- Provide a blueprint for the team, and the wider organization, to enable GitHub Advanced Security for Azure DevOps at scale.
- Accelerate the adoption of Advanced Security within an organization.

###  Engagement schedule

This module consists of three sessions, described further below:

- Discovery ([See Scoping](#step-1-scoping-call)) - review proposed repositories, understand and align on pre-requisites (30 minutes).
- Delivery - screen sharing session where we walk through enablement (2-4 hours)
- Follow-up (**See Day 5: Security Results Review)**- screen sharing session where we review enablement and address any issues (2-4 hours)

Maximum session size is typically 10 people.

### Delivery

The Delivery session may either be 2 hours or 4 hours long. Regardless of the duration, a Microsoft CSA will walk the customer through the process of enabling GitHub Advanced Security for Azure DevOps on the selected repositories. However, with 4 hours, the customer is assured enough time to cover all of the listed features, talking points, and include time to troubleshoot errors.

- Demonstrate the process of enabling GitHub Advanced Security and its various features:
  - Code scanning
  - Secret scanning
  - Dependency Scanning
- Answer questions about GitHub Advanced Security for Azure DevOps.
- Support troubleshooting common build failures.


### Learning outcomes/business outcomes

After completing this module participants will have:

- GitHub Advanced Security for Azure DevOps enabled on one or more repositories.
- Developers are able to take responsibility for enabling GitHub Advanced Security for Azure DevOps in their own repositories.
- A blueprint for enabling GitHub Advanced Security for Azure DevOps on further repositories in your organization.

###  Pre-requisites

- Must have enabled GitHub Advanced Security on selected repositories prior to delivery.
- Code base must be in Azure Repos (Azure DevOps Services) prior to delivery.
- The attendees must either:
  1. Have administrative privilege of the selected repositories; or
  2. Have Project Collection administrators enable GitHub Advanced Security for Azure DevOps on the selected repositories prior to delivery.

**Day 5: Security results review**

This module is delivered to single team of developers to walk them through the process of reviewing the results produced by Advanced Security. Product security and DevSecOps team members might take part with the goal of disseminating best practices in triaging and fixing security issues as well as in Advance Security configuration.

###  Target Audience

- Developers
- Product Security teams
- DevSecOps teams

###  Key features and benefits

- Review the results produced by Advanced Security with an expert on the call.
- Receive a guided tour on how to effectively use the Advanced Security interface to understand and triage results taking advantage of the offered documentation.
- Receive customized guidance on remediation.
- Receive customized guidance on configuration changes to improve the results produced by Advanced Security.

###  Engagement schedule

This module will consist of one session of 2 hours face-to-face time, and some pre and post-session support. Maximum session size is typically 16 people.

###  Syllabus

- Overview of the Advanced Security interface functionalities
- Analysis of the results obtained on 1-5 customer repositories focusing on:
  - Quantity of results - likely explanations for the absence/abundance of results
  - Approaches to fixing highest severity issues
  - Configuration options

###  Learning outcomes/business outcomes

After completing this workshop participants will be able to:

- Use the GitHub Advanced Security interface to understand the reported security vulnerabilities on the selected repositories.
- Triage and remediate the existing vulnerabilities in their repository
- Address new vulnerabilities as they are reported in the pull request workflow.
- Identify build and configuration improvements for the given repositories to reduce false positives and false negatives

###  Prerequisites

- 1-5 repositories must be selected where Advanced Security is already enabled.
  - If the repositories are not already enabled, the "Pilot Team Implementation" offering can be provided to support enabling GHAS.
- The attendees must have access to the relevant security results on the selected repositories

    | Azure DevOps group  | Default permissions |
    | ----------- | ----------- |
    | Contributors | Advanced Security: read alerts |
    | Project administrator | Advanced Security: read alerts, manage and dismiss alerts |
    | Project collection administrator | Advanced Security: read alerts, manage and dismiss alerts, manage settings |

**Deliverables**

A set of reporting deliverables are provided to the customer to use as references and to execute improvement recommendations for internal reporting purposes.
The templates linked below, or a custom reporting format can be used. 
Pick whichever approach works better for the customer's, your, or the account team's needs.

Templates:
- [Security Results Review Closeout Template](https://microsoft.sharepoint.com/:p:/t/ASDIPRelease/EV6UTvN_l-JAsRCUcIAXedwBgX1AnIvmgtfi-lKizVaf4w?e=dbhbXh)

**Close Out**

You will deliver both the Security Results Review deck as part of the executive close out meeting.
This meeting is intended to recap the core findings from the review focusing on key strengths and optimization opportunities. It is important to include executive sponsors and IT decision makers in this meeting so they gain awareness of improvement recommendations and how Microsoft can help, which they can use to make resourcing and investment decisions on what steps will be taken to execute on the recommendations.

If needed the CSAM can help with scheduling this close out meeting. The recommended duration is 30 minutes. 
During this meeting, present results, recommendations, and possible improvements to their build and configurations for the repositories used for implementation.


## Resources, Readiness and References

- View the [delivery resources](https://microsoft.sharepoint.com/teams/ASDIPRelease/IP%20Release/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FIP%20Release%2FModern%20Apps%2FGitHub%2FWorkshop%20%2D%20GitHub%20Advanced%20Security%20for%20ADO&viewid=971b6985%2D5ac6%2D47e5%2Da6dc%2D5c0664b149a9) for the full bill of materials within this VBD IP

### Public Documentation

- Customer facing website for GitHub Advanced Security for Azure DevOps: [GitHub Advanced Security for Azure DevOps Microsoft Learn Docs](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops&tabs=yaml)
- [MS Learn Path: GitHub Advanced Security](https://learn.microsoft.com/en-us/users/githubtraining/collections/rqymc6yw8q5rey)
- [Secret Scanning for GitHub Advanced Security](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-secret-scanning?view=azure-devops)
- [Dependency Scanning for GitHub Advanced Security](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-dependency-scanning?view=azure-devops)
- [Code Scanning for GitHub Advanced Security](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-code-scanning?view=azure-devops)

### Community support

- [Advanced Security Foundations VBD channel](https://teams.microsoft.com/l/channel/19%3A941409945e8a4362a16e8dd81e64149d%40thread.tacv2/VBD%20-%20GitHub%20Advanced%20Security%20Foundations?groupId=591c20e8-6a02-4476-8881-849bf672e6cf&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47) for tips, best practices, and peer sharing

## Known issues and updates

-

## Frequently Asked Questions

