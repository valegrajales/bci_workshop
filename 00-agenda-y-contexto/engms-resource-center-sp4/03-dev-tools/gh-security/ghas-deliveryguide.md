Dev engagement: delivery guide

# Delivery Guide: Workshop - GitHub Advanced Security for GitHub Enterprise - Getting Started

# Introduction

This guide will provide details and instructions to help you deliver a successful GitHub Advanced Security workshop for your customer. 

## IPKit

> The IPKit with artifacts to use throughout this delivery is located [here](https://microsoft.sharepoint.com/:f:/r/teams/ASDIPRelease/AzureCloudAI/SP2%20VBD/DevTools/GitHub/Workshop%20-%20GitHub%20Advanced%20Security%20for%20GitHub%20Enterprise%20-%20Getting%20Started?csf=1&web=1&e=iLQl9s).

**Objectives**

- Provide training and guidance to a customer to raise awareness and understanding of GitHub Advanced Security
- Assist a customer accelerate adoption of Advanced Security in GitHub while avoiding common pitfalls 
- Work with a customer to learn and apply best practices for deploying GitHub Advanced Security through guided modules and hands on labs

**Deliverable Standards**

- Education sessions for GitHub Advanced Security for GitHub Enterprise workshop containing instructor sessions with slides, demos, and hands on labs
- Demonstrate GitHub Advanced Security features, policies, and configuration at Enterprise, Organization, and Repository level

## Customer Participants

| **Customer Role** | **Description** | **Required or Optional** |
| --- | --- | --- |
| DevOps/DevSecOps Team | Team responsible for deploying application to production | Required |
| Software Developers | People with experience in coding or advanced makers | Required |
| Security Team | Team responsible for security across all aspects of the application | Required |

## Delivery Guidance

This section includes all non-technical delivery guidance and supporting artifacts for the GitHub Advanced Security for GitHub Enterprise session. You are free to adapt each step to meet your customers' needs if you can meet the objectives and deliverable standards for the GitHub Advanced Security for GitHub Enterprise Workshop.

Before starting the engagement the following prerequisites will need to be satisfied:

- The customer's organization has GitHub Advanced Security.
- The customer's organization has identified attendees for each of the training sessions.
- The customer's participants have public GitHub handles (non EMU) for accessing the lab environment.
- The customer's code base is hosted in GitHub.


### Step 1: Scoping Call

During the call the delivery resource explains the delivery flow and objectives of each section. Explain how the delivery will be carried out and what can be expected at each phase. 

The scoping call provides an opportunity to ask questions such as:

- What do you expect from the workshop?
- Who needs to be in the room for the engagement on each day?
- What topic areas are most relevant to the team during the pilot implementation and security review?
- What are the skill levels of the developers, DevOps, and security teams?

As part of the call, make sure the customer understands what will be covered (i.e. "in scope"), what will not be covered (i.e. "out of scope"), and, most importantly, agree to the terms and scope of the engagement. This agreement serves as both a guard against "scope creep," and as a structure for the rest of the engagement.

Identify who should participate in each section of the workshop. Many organizations have a diverse set of development teams. Given the limited time available, the most practical approach will often be to focus on one of the customer's flagship products or projects.

Depending on the customer's organizational structure, people who can represent all aspects of the product lifecycle should participate in the assessment. 

Roles might include:
- Engineering Managers
- DevSecOps Team Members
- Application Security Teams
- Influential senior developers and leaders
- Software Development Engineers 
- Product Security Teams
   

#### Recommended: Account Team Scoping

If you have not worked with the account team or the teams you will be working with, it is highly recommended to also have a scoping call with the account team. 
The roles you might want to reach out to are the aligned Technical Specialist, Customer Success Account Manager, Account Technology strategist, or Solutions Engineer. 
Use your time with the account team to learn more about the key initiatives that the account team is already driving and what support offers the customer has already got in place. 

### Step 2: Engagement Overview

This engagement is a three part workshop designed to help customers implement GitHub Advanced Security for GitHub Enterprise. The engagement can be scheduled as several 1-day engagements with one module each or as a block of modules delivered over three days. The content is provided separately with all modules having some common content (see below for details if delivering all three in the same delivery)

The engagement contains the following modules: It is suggested to deliver the modules in the order listed below, but not required and can change based on customer needs.

1. GHAS Code Security
2. GHAS Secret Protection
3. GHAS Supply Chain Security

### Common Content
Each module contains common content to ensure that all attendees have a good understanding of GitHub Advanced Security for GitHub Enterprise. This common content is outlined below:
This content should not be delivered multiple times if delivering all three modules as part of one engagement. Once you have determined the delivery schedule you can adjust the content accordingly and hide the following slides in the modules delivered after the first module.

1. GHAS Code Security
      Section: The state of security today (Slides 8-25)
      Section: Third party integrations (Slide Title - SIEM Integrations, Jira Integration, Audit log, Webhooks, APIs)
2. GHAS Secret Protection
      Section: The state of security today (Slides 8-25)
      Section: Third party integrations (Slide Title - SIEM Integrations, Jira Integration, Audit log, Webhooks, APIs)
3. GHAS Supply Chain Security
      Section: The state of security today (Slides 8-25)
      Section: Third party integrations (Slide Title - SIEM Integrations, Jira Integration, Audit log, Webhooks, APIs)

**NOTE:** You might see some common slides across these modules, for example, under the Security Overview section, but those are tailored to each specific module. Therefore, you should **NOT** skip any slides except those explicitly mentioned here.

**Reminder**
Before starting the engagement the following prerequisites will need to be satisfied:

- Attendees identified for each of the training sessions
- Create a sandbox environment and GitHub Organization per participant for the lab exercises
- Participants must have enabled GitHub Advanced Security on selected repositories

### Module 1: GHAS Code Security
--------------------------------
The GitHub Code Security offering is one 4-hour (3 hours if common content is removed) training session that provides developers with foundational skills on the GitHub Advanced Security features included with a GitHub Code Security license: Code Scanning and CodeQL.

### Target Audience

- Application security teams
- DevSecOps teams
- Security champions
- Influential senior developers and leaders (optional)

### Engagement schedule

This module consists of one session of 4 hours. Maximum session size is typically 16 people. If common content is removed due to multiple modules being delivered in one engagement the session time will be reduced to approximately 3 hours.

### Syllabus

- Introduction (5 minutes)
- State of security today (10 minutes)
- Policies and Configurations (45 minutes)
- Code Security (1 hour 40 minutes)
- Security Overview (40 minutes)
- 3rd Party Integrations (30 minutes)
- Recap and Next Steps (10 minutes)

### Prework Required
1. Understand the offering 
- Review the delivery guide, slide deck, and any supporting enablement materials. 
- Setup a sandbox organization from the prepared templates and familiarize yourself with the repository content, structure and the demos. **NOTE:** If the sandbox environment isn't accessible or you can't set one up, please use a GitHub Enterprise Cloud trial account by following the instructions provided at the end.
  - This can be done using this issue ops automation, which spins up a GitHub organization per GitHub handle and automatically deletes the orgs after 14 days. 
- Practice the demos and the lab exercises in the sandbox environment.   
- If any content is unfamiliar, contact a peer and gather any supporting guidance. 
 
2. Pre-engagement 
- Read through the slide deck and prepare to deliver the content. 
- Personalize the slide deck with your headshot and contact information. 
- Gather public GitHub handles for each training participant (Note: these cannot be tied to an Enterprise Managed Users or GitHub Enterprise Server instance, since those handles are privately managed). 
- Create a GitHub organization per participant that they will use during the lab exercises. 
  - This can be done using this issue ops automation, which spins up a GitHub organization per GitHub handle and automatically deletes the orgs after 14 days. 
- Ensure the organizations have copies of the repository templates mentioned in the lab exercises. 
- Ensure each participant has the organization owner role in their organization. 

### Delivery Execution
1. During engagement 
- Complete pre-session tasks. (These are listed in the session slide deck.) 
- Record the session(s) and ensure it’s saved in an appropriate location (if applicable). 
- Deliver the content and demonstrate the exercises as directed in the presentation deck. 
- Answer any participant questions as necessary. 
- Take away questions that you could not answer during the session to follow-up on. 
- Ensure that participants know their sandbox environment will be automatically deleted shortly after the training session. 
- Complete post-training tasks. (These are listed in the session slide deck.) 

### Wrap Up
1. Wrap up the engagement 
- Close the loop on any open items/questions from the session. 
- Gather customer feedback. Send attendees a feedback survey, and ask the customer if they feel the session delivered on expectations. 
- Send feedback about the engagement to all internal stakeholders. 
- Review the Action logs in the issue ops automation to ensure that the temporary participant organizations have been properly deleted without errors. 
- Report any time and effort spent on engagement in ESXP. 

### Learning outcomes/business outcomes

After completing this module participants will be able to:

- Enable CodeQL analysis within GitHub Actions to perform static analysis for commonly used languages 
- Configure GitHub Actions to trigger CodeQL analysis on both a schedule and in response to a pull request 
- Understand, triage, and remediate reported vulnerabilities with the Code Scanning user interface 
- Configure CodeQL to improve the quality of results 
- Integrate common third party tools into Code Scanning via GitHub Actions 
- Conduct static analysis scans with the CodeQL CLI locally, in GitHub Actions, and in third-party CI/CD tools 
- Scan monorepos with CodeQL 

### Frequently Asked Questions
**Q:** The customer is on GitHub Enterprise Server. Can they do the training in their environment? 

**A:** *The training materials are built and meant to be delivered on GitHub Enterprise Cloud. If the customer has GitHub Enterprise Server, the content might not map to their environment and therefore the provisioning solution as well as the content would need to be customized.*
 
**Q:** The customer cannot commit their engineers for 4 hours in one day. What should I do? 
**A:** *Recognizing 4 hours of engineers’ time is a lot these days, you can suggest breaking down the 4 hours to be delivered over 2 days and working with the customer on scheduling it.*
 
**Q:** I’ve learned that the customer has GitHub Secret Protection and GitHub Supply Chain Security trainings lined up as well. How should I approach the delivery of this training? 

**A:** *You would want to adapt the training accordingly. If you are the delivery engineer that is going to be delivering the other (two) trainings make sure to review the common content section in this guide, and remove/hide the repetitive slides on the other two trainings.*
 
**Q:** A lot of people did not complete the lab exercises during the delivery, what do I do? 

**A:** *Keeping time and sticking to the schedule is important. There will be cases where some trainees do not complete their exercises in time. Assure them that they can follow through and complete the exercises after the session by following the walkthrough/instructions at their own pace after the session. Remind the participants that they will have access to their sandbox environment for about a week after the training if you are using the sandbox environment.*

### Module 2: GHAS Secret protection
------------------------------------
The GitHub Secret Protection offering is a 4-hour (3 hours if common content is removed) training session that's designed to equip developers with practical skills for using GitHub Advanced Security with a focus on GitHub Secret Protection.

### Target Audience

- Application security teams
- DevSecOps teams
- Security champions
- Influential senior developers and leaders (optional)

### Engagement schedule

This module consists of one session of 4 hours. Maximum session size is typically 16 people. If common content is removed due to multiple modules being delivered in one engagement the session time will be reduced to approximately 3 hours.

### Syllabus

- Introduction (5 minutes)
- State of security today (10 minutes)
- Policies and Configurations (45 minutes)
- Secret Protection (1 hour 40 minutes)
- Security Overview (40 minutes)
- 3rd Party Integrations (30 minutes)
- Recap and Next Steps (10 minutes)

### Prework Required
1. Understand the offering 
- Review the delivery guide, slide deck, any supporting enablement materials and product introduction resources in this guide. 
- Setup a sandbox organization from the prepared templates and familiarize yourself with the repository content, structure and the demos. **NOTE:** If the sandbox environment isn't accessible or you can't set one up, please use a GitHub Enterprise Cloud trial account by following the instructions provided at the end.
  - This can be done using this issue ops automation, which spins up a GitHub organization per GitHub handle and automatically deletes the orgs after 14 days. 
- Practice the demos and the lab exercises in the sandbox environment.   
- If any content is unfamiliar, contact a peer and gather any supporting guidance. 
 
2. Pre-engagement 
- Read through the slide deck and prepare to deliver the content. 
- Personalize the slide deck with your headshot and contact information. 
- Gather public GitHub handles for each training participant (Note: these can’t be tied to an Enterprise Managed Users or GitHub Enterprise Server instance, since those handles are privately managed). 
- Create a GitHub organization per participant that they’ll use during the lab exercises. 
  - This can be done using this issue ops automation, which spins up a GitHub organization per GitHub handle and automatically deletes the orgs after 14 days. 
- Ensure the organizations have copies of the repository templates mentioned in the lab exercises. 
- Ensure each participant has the organization owner role in their organization. 

### Delivery Execution
1. During engagement 
- Complete pre-session tasks. (These are listed in the session slide deck.) 
- Record the session(s) and ensure it’s saved in an appropriate location (if applicable). 
- Deliver the content and demonstrate the exercises as directed in the presentation deck. 
- Answer any participant questions as necessary. 
- Take away questions that you could not answer during the session to follow-up on. 
- Ensure that participants know their sandbox environment will be automatically deleted shortly after the training session. 
- Complete post-training tasks. (These are listed in the session slide deck.) 

### Wrap Up
1. Wrap up the engagement 
- Close the loop on any open items/questions from the session. 
- Review the Action logs in the issue ops automation to ensure that the temporary participant organizations have been properly deleted without errors. 
- Gather customer feedback. Send attendees a feedback survey, and ask the customer if they feel the session delivered on expectations. 
- Send feedback about the engagement to all internal stakeholders. 
- Report any time and effort spent on engagement in ESXP. 

### Learning outcomes/business outcomes

After completing this module participants will be able to:

- Set up and manage custom security configurations for secret scanning across repositories 
- Create and deploy custom secret scanning patterns  
- Enable and utilize push protection to block secret exposure at the source 
- Remediate secret scanning alerts efficiently 

### Frequently Asked Questions
**Q:** The customer is on GitHub Enterprise Server. Can they do the training in their environment?

**A:** *The training materials are built and meant to be delivered on GitHub Enterprise Cloud. If the customer has GitHub Enterprise Server, the content might not map to their environment; therefore, the provisioning solution as well as the content would need to be customized.*
 
**Q:** The customer can't commit their engineers to 4 hours in one day. What should I do?

**A:** *Recognizing 4 hours of engineers’ time is a lot these days, so you can suggest breaking down the 4 hours to be delivered over 2 days and working with the customer on scheduling it. Naturally the training can be broken down into:  
Part 1: State of Security today, Policies and Configurations, Secret Protection - the detection and prevention part up to Push Protection. 
Part 2: The rest of Secret Protection, Security Overview, Third party integrations. 
You might still have to adjust the plan during the delivery as per the progress the attendees make with the lab exercises.*
 
**Q:** I’ve learned that the customer has both the GitHub Code Security training and GitHub Supply chain security training lined up. How should I approach the delivery of this training?

**A:** *If you are the delivery engineer that is going to be delivering the other (two) trainings make sure to review the common content section in this guide, and remove/hide the repetitive slides on the other two trainings.*
 
**Q:** A lot of people don’t complete the lab exercises during the delivery; what do I do?

**A:** *Keeping time and sticking to the schedule is important. There will be cases where some trainees don’t complete their exercises in time. Assure them that they can follow through and complete the exercises after the session by following the walkthrough/instructions at their own pace after the session. RRemind the participants that they will have access to their sandbox environment for about a week after the training if you are using the sandbox environment.*

 
### Module 3: GHAS Supply Chain Security
----------------------------------------
GitHub Advanced Security for GitHub Enterprise allows you to have a "developer-first" approach to Application Security, recognizing that developers have a critical role to play in securing applications. This module will enable developers to both understand and effectively use the features of GitHub Advanced Security.

### Target Audience

- Application security teams
- DevSecOps teams
- Security champions
- Influential senior developers and leaders (optional)

### Engagement Schedule

This module consists of one session of 4 hours. Maximum session size is typically 16 people. If common content is removed due to multiple modules being delivered in one engagement the session time will be reduced to approximately 3 hours.

### Syllabus

- Introduction (5 minutes)
- State of security today (10 minutes)
- Policies and Configurations (45 minutes)
- Supply Chain Security (1 hour 40 minutes)
- Security Overview (40 minutes)
- 3rd Party Integrations (30 minutes)
- Recap and Next Steps (10 minutes)

### Prework Required
  
1. Understand the offering 
- Review the delivery guide, slide deck, and any supporting enablement materials. 
- Setup a sandbox organization from the prepared templates and familiarize yourself with the repository content, structure and the demos. **NOTE:** If the sandbox environment isn't accessible or you can't set one up, please use a GitHub Enterprise Cloud trial account by following the instructions provided at the end. 
  - This can be done using this issue ops automation, which spins up a GitHub organization per GitHub handle and automatically deletes the orgs after 14 days. 
- Practice the demos and the lab exercises in the sandbox environment.   
- If any content is unfamiliar, contact a peer and gather any supporting guidance.
  
2. Pre-engagement 
- Read through the slide deck and prepare to deliver the content. 
- Personalize the slide deck with your headshot and contact information. 
- Gather public GitHub handles for each training participant (Note: these can’t be tied to an Enterprise Managed Users or GitHub Enterprise Server instance, since those handles are privately managed). 
- Create a GitHub organization per participant that they’ll use during the lab exercises. 
  - This can be done by using this issue ops automation, which spins up a GitHub organization per GitHub handle and automatically deletes the orgs after 14 days. 
- Ensure the organizations have copies of the repository templates mentioned in the lab exercises. 
- Ensure each participant has the organization owner role in their organization.  

### Learning outcomes/business outcomes

After completing this module participants will be able to:

- Visualize and analyze software dependencies using GitHub's Dependency Graph and Insights 
- Configure Dependabot for automated vulnerability detection and remediation 
- Draft and manage Security Policies and Advisories effectively 
- Create and utilize Software Bill of Materials (SBOM) to maintain accurate software inventory 

### Frequently Asked Questions
**Q:** The customer is on GitHub Enterprise Server. Can they do the training in their environment?

**A:** *The training materials are built and meant to be delivered on GitHub Enterprise Cloud. If the custom has GitHub Enterprise Server, the content might not map to their environment and therefore the provisioning solution as well as the content would need to be customized.*  
 
**Q:** The customer can’t commit their engineers to 4 hours in one day. What should I do? 

**A:** *Recognizing 4 hours of engineers’ time is a lot these days, you can suggest breaking down the 4 hours to be delivered over 2 days and working with the customer on scheduling it.*
 
**Q:** I’ve learned that the customer has GitHub Code Security and GitHub Secret Protection trainings lined up, too. How should I approach the delivery of this training?

**A:** *You would want to adapt the training accordingly. If you are the delivery engineer that is going to be delivering the other (two) trainings make sure to review the common content section in this guide, and remove/hide the repetitive slides on the other two trainings.*

**Q:** A lot of people didn’t complete the lab exercises during the delivery, what do I do?

**A:** *Keeping time and sticking to the schedule is important. There will be cases where some trainees don’t complete their exercises in time. Assure them that they can follow through and complete the exercises after the session by following the walkthrough/instructions at their own pace. Remind the participants that they will have access to their sandbox environment for about a week after the training if you are using the sandbox environment.*

### Close Out

If necessary an executive close out meeting can be scheduled at the end of the engagement. This is more likely to be relevant in circumstances where you have delivered several modules and/or enabled GitHub Advanced Security for GitHub Enterprise on various repositories in the organization. 

This meeting is intended to recap the core findings and actions completed. It's an opportunity to review key strengths and optimization opportunities. 

If you have delivered the Security Review you may want to document your most common findings in a slide deck to present on this occassion. 

It is important to include executive sponsors and IT decision makers in this meeting so they gain awareness of improvement recommendations and how Microsoft can help, which they can use to make resourcing and investment decisions on what steps will be taken to execute on the recommendations.

If needed, the CSAM can help with scheduling this close out meeting. The recommended duration is 30 minutes. 


## Resources, Readiness and References

- View the [IPKit](https://microsoft.sharepoint.com/:f:/r/teams/ASDIPRelease/AzureCloudAI/SP2%20VBD/DevTools/GitHub/Workshop%20-%20GitHub%20Advanced%20Security%20for%20GitHub%20Enterprise%20-%20Getting%20Started?csf=1&web=1&e=iLQl9s) for the full bill of materials within this VBD IP
- Review the [lab setup instructions](https://github.com/ghas-lab-automation/ghas-lab-builder) and ensure that the sandbox environment (GitHub Organization per participant) is created at least a day prior to the delivery
- Review the [lab exercises/modules](https://github.com/ghas-lab-templates/exercises/tree/main), and familiarize yourself with the GHAS exercises 

### Public Documentation

- Customer facing website for GitHub Advanced Security: [GitHub Advanced Security for GitHub Enterprise docs](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)
- [MS Learn Path: GitHub Advanced Security](https://learn.microsoft.com/en-us/users/githubtraining/collections/rqymc6yw8q5rey)
-	[Adopting GHAS at scale](https://docs.github.com/en/enterprise-cloud@latest/code-security/adopting-github-advanced-security-at-scale/)
-	[Achieving DevSecOps with GitHub Advanced Security](https://youtu.be/hln5v7odguE)
- [GitHub CLI documentation](https://cli.github.com/)

### Community support

- [Advanced Security Foundations VBD channel](https://teams.microsoft.com/l/channel/19%3A941409945e8a4362a16e8dd81e64149d%40thread.tacv2/VBD%20-%20GitHub%20Advanced%20Security%20Foundations?groupId=591c20e8-6a02-4476-8881-849bf672e6cf&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47) for tips, best practices, and peer sharing

### GitHub Enterprise Cloud Trial

[!include[GitHubDemo_Options_Section](../../../CommonContent/gh-demo-options.md)]




