# Delivery Guide: Workshop - Agentic DevOps & GitHub Copilot Deep Dive
This guide will provides details and instructions to help you deliver the **Workshop - Agentic DevOps & GitHub Copilot Deep Dive** for your customer. This guide will focus on more advanced topics of GitHub Copilot which could differ based on target audience requirements.  There are multiple GitHub topics that you can choose from to drive the desired outcome. 


This engagement must accomplish the following objectives:  

**Objectives**
After completing this training, learners will be able to:

- Understand new advanced features that improve or impact GitHub Copilot
- Incorporate those features into their developer experience
- How to better use Agent in the SDLC workflow

After this engagement, your team will be able to:

- Know when and how to use new features
- Reduce time spent on repetitive tasks and boilerplates
- Limit context switching between different tools
- Improve the developer experience
- Integrate with different tools from you IDE

For the specific GitHub IPs, select each tab for the objectives:

## [**GitHub Copilot Agents and MCP**](#tab/GitHub-Copilot-Agents-and-MCP-Objectives)
- Understand the difference between GitHub Copilot Coding Agent vs Agent mode​
- Configure and manage GitHub Copilot agent mode and MCP Server​
- Configure and manage GitHub Copilot Coding Agent​
- Use an existing MCP server​
- Utilize best practices to maintain secure, compliant, and efficient operations​  

## [**GitHub Copilot Prompt Engineering**](#tab/GitHub-Copilot-Prompt-Engineering-Objectives)
- Master prompt engineering fundamentals and design.
- Understand AI models and prompt construction in GitHub Copilot.​
- Learn AI response generation and prompt best practices.​
- Utilize prompt enhancement concepts.​
- Recognize GitHub Copilot's role in security and compliance.​

## [**Transforming Legacy Codebases Using GitHub Copilot**](#tab/Transforming-Legacy-Codebases-Using-GitHub-Copilot-Objectives)
- AI-assisted development for legacy modernization 
- Key challenges and opportunities in transforming legacy applications 
- Strategies for improving code quality, security, and maintainability 
- Integrating AI-powered tools into modernization workflows 
- Hands-on workshop: Practical applications of AI in development 

_This module is language agnostic and does not use [GitHub Copilot App Modernization extension](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/overview).  If customer is looking to modernize .net or java applications, please refer them to [Application Modernization with GitHub Copilot VBD](../../../SP01/appmod-ghcp/overview.md)_

## [**GitHub Code Quality**](#tab/GitHub-Code-Quality-Objectives)
- Improve existing code with Standard and AI findings
- Interpret code quality ratings, severities, and rules
- Use PR-native `github-code-quality[bot]` findings
- Remediate safely: manual, Autofix, cloud agent, or dismiss findings
- Measure impact and report progress to stakeholders

***

## IP Kit
IP kit can be located in [IP Release Share](https://aka.ms/GHCPAgenticDevOpsIPKit).

**Deliverable Standards**
Education session containing instructor sessions with slides, demos, and Q&A.

## Customer Participants
<details>
<summary>Click to expand</summary>

Having the right customer participants in the  workshop is essential to completing a successful engagement. 
Ensure the customer roles outlined below are available and able to participate in the workshop. 

- Developers
- Team Leads
- Development Leaders
- Project Managers
</details>

## Delivery Guidance
This section includes all non-technical delivery guidance and supporting artifacts for this delivery. 
You are free to adapt each step to meet your customers needs as long as you are able to meet the objectives and deliverable standards. 

### Step 1: Preparing for the delivery
<details>
<summary>Click to expand</summary>

- You have reviewed the training outline and objectives as described in the slide deck available on the IP Share
  - **You have reviewed the entire deck (available at [IP Release Share](https://aka.ms/GHCPAgenticDevOpsIPKit)), so that you can be knowledgeable enough to speak to the material.**

  - The slide deck contains speaker notes for each topic to help you ramp up. They are not intended to be read verbatim. 
  - Additionally, each slide has a link to the source information for further review.
  - The IPShare also contains additional resources such as enablement decks .

- You have informed the customer about the training pre-requisites. In this case, if they'd like to follow along with demos, GitHub Copilot for Business must be enabled on the supported target platforms.

- Gain access to [GitHub Copilot](https://aka.ms/copilot) for your work and personal account.


- Note: the the intent of the demos is to provide an overview of a new feature. It is not intended to be a comprehensive training. Often, these deep dives can be addressed with other VBDs or EDE office hours.
</details>

### Step 2: Scoping
<details>
<summary>Click to expand</summary>

Explain how the delivery will be carried out. What the customer can expect at each phase, before and after delivery. 
Make sure the right stakeholders from the customer's organization are present throughout the delivery. Refer to [Customer Participants](#customer-participants) section for details.

Ensure you discuss and understand the customer's requirements and that the tooling to be used is agreed. 
Ensure all the stakeholders are on the same page regarding the deliverables and outcomes.

If the customer is planning to follow along with any demos, please help them better understand the pre-requisites to set up before the day of the delivery.
You can point them to relevant documentation or recommend a proof-of-concept VBD activity, if they require help.

</details>

### Step 3: Kickoff

<details>
<summary>Click to expand</summary>

Share details of what activities you will cover and what will not be covered. For example, a customer might not want to see preview features.
If a specific topic of interest is not covered, then you should have already thought about handling it during or after scoping.
However if you can accommodate last minute request, we recommend you do so to achieve a greater level of customer satisfaction with the offering.

 </details>

### Step 4: Delivery Guidance

Select the most recent PowerPoint deck, unless the customer specifically requested an older delivery (this might occur if the customer has older IDE releases). 
If there is extra time after the core content has been completed you may pick additional feature demos or an extended Q&A to the agenda. 
Utilize the resources on the GitHub Sales SharePoint (linked below) to access the latest version of the GitHub Copilot FAQ.

#### Module 1: PowerPoint Deck Delivery

In order to keep focus and ensure that the customer gets as much as possible out of the training, please ensure the items below are completed.

-  Make sure the customer understands that all participants need a GitHub account on the supported target platform with their corporate login and GitHub Copilot enabled.
-  **Introduction** of participants and providers
-  Give a reminder that the enablement will be performed on the recent version of Copilot and Copilot Chat
-  Present and discuss the **learning objectives slide** and the **agenda**
-  Do the ice breaker to get to know the audience, encourage interactions, and learn expectations
-  For each section in the slide deck, ensure that the following items are covered:
   - A thorough, clear presentation of the content covered in the slides (don't forget the **speaker notes**)
   - While it is not mandatory for the customer to complete the Demos, we give them the opportunity to follow along if they would like. Give the audience enough time to complete the hands-ons. Have them write to the chat if they are done or have any questions
   - Questions raised by the audience, either via chat or verbally, have been either addressed directly or noted for follow-up

The [IP Release Share](https://aka.ms/GHCPAgenticDevOpsIPKit) contains the presentation deck for this delivery.

#### Module 2: Feature Demos

Ensure you cover features that are relevant to or identified for the success of the VBD activity.
The demos should augment the topics from the slide material available on the IPShare or the GitHub Sales SharePoint.

The goal of this module is to help developers understand the new features announced during the technical update briefing. Optionally, covering announcements can be demoed as well. For example, highlighting a new LLM model.

As part of your prep work for this module you should understand the feature and be able to demo it at least once in your own time before delivering.

#### Module 3: Q&A

Naturally with new features there will be questions. Ensure that time is set aside to allow for Q&A.
Additionally, monitoring the chat for questions as they arise can helpful.
Often follow-up calls will happen as customers determine how to incorporate new features into their organizations and workflows. This is a good opportunity and you should be prepared with additional VBDs or custom EDE recommendations.

- Do a retro at the end of the session to collect feedback and manage the expectations

### Step 5: Delivery


Choose one of the assets below for this delivery. If there is extra time after the core content has been completed you may pick optional topics from another assets. Alternatively you may also choose to add additional guided demos or an extended Q&A to the agenda. Ensure you cover assets that are relevant to or identified for the success of the VBD activity.

### [GitHub Copilot Agents and MCP](#tab/GitHub-Copilot-Agents-and-MCP)
GitHub Copilot Agents and MCP is an AI-powered code completion tool that helps developers write code faster.​

Note: The activities listed in the section below are for this workshop. The slide deck associated is available on the IPShare.

-  GitHub Copilot Agents and MCP 
   - Introduction
   - Learning objectives
   - Agenda
-  AI Agents
-  Agentic AI with GitHUb Copilot
-  MCP Servers
-  Hands-on Workshop
   - Creating something tangible while leveraging Agentic AI with GitHub Copilot to streamline the process
-  Conclusion
   - Wrap up
-  Cover questions from the customer

[Workshop demo repo - coding agent demo](https://github.com/ps-copilot-sandbox/copilot-mcp)

[Workshop demo repo - mcp with agent mode](https://github.com/ps-copilot-sandbox/copilot-agent-and-mcp )

[Hands-on Lab Guide - mcp with agent mode](https://github.com/ps-copilot-sandbox/copilot-agent-and-mcp )

   
### [GitHub Copilot Prompt Engineering](#tab/GitHub-Copilot-Prompt-Engineering)
GitHub Copilot prompt engineering will take the Advanced module to the next level by providing a deeper dive into prompt engineering.
Note there are no hands-on labs for this module.  The last part of the workshop is a demo of prompt engineering in practice which you can choose your own repo.

-  GitHub Copilot Prompt Engineering 
   - Introduction
   - Learning objectives
   - Agenda
-  Prompt Engineering introduction
   - Prompt Engineering overview
-  GitHub Copilot foundations
   - GitHub Copilot foundations models
-  GitHub Copilot backend
   - GitHub Copilot backend security and filters
-  Best practices
   - Best practices improving your prompts
-  Techniques
   - Prompt engineering techniques
-  GitHub Copilot
   - GitHub Copilot in practice
-  Demos
   - Demos prompts in practice and conclusion
-  Conclusion
   - Wrap up
-  Cover questions from the customer

[Workshop demo repo - Copilot Prompt Engineering](https://github.com/ps-copilot-sandbox/copilot-prompt-engineering/tree/main)

[GitHub Documentation - Prompt Engineering](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering)

### [**Transforming Legacy Codebases Using GitHub Copilot**](#tab/Transforming-Legacy-Codebases-Using-GitHub-Copilot)
GitHub Copilot AI-assisted transformation and modernization can help developers understand the cost of legacy applications, learn the framework for legacy app modernization, and leverage GitHub Copilot's capabilities and use cases that align to the different phases of the legacy app modernization framework.

_This module is language agnostic and does NOT utlized [GitHub Copilot App Modernization extension](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/overview).  If customer is looking to modernize .net or java applications, please refer them to [Application Modernization with GitHub Copilot VBD](../../../SP01/appmod-ghcp/overview.md)_

- Why modernize legacy applications?
   - Cost of legacy applications
   - Drivers of legacy application modernization
- Strategies & Frameworks for Legacy App Modernization
   - Finding the right strategy for different codebase size and complexity
- Leveraging GitHub Copilot
   - Power of GitHub Copilot
- Workshop
   - Hands-on workshop 
- Conclusion
   - Wrap up
- Cover questions from the customer

There are no demo repos for this module.  The hands-on workshop repos are listed directly in the slide deck and below:
 - Option 1: [Transform COBOL app to Node.js](https://github.com/continuous-copilot/modernize-legacy-cobol-app)
 - Option 2: [Upgrade an app’s Java version](https://learn.microsoft.com/en-us/java/upgrade/quickstart-upgrade)
 - Option 3: [Upgrade an app’s .NET version](https://learn.microsoft.com/en-us/dotnet/azure/migration/appmod/quickstart?pivots=visualstudio)
 - Option 4: Free play

### [**GitHub Code Quality**](#tab/GitHub-Code-Quality)
GitHub Code Quality helps teams identify, prioritize, and remediate code issues directly in pull requests while improving maintainability over time.

- GitHub Code Quality
   - Introduction
   - Learning objectives
   - Agenda
- Code Quality overview
   - Introduction to Code Quality fundamentals
- Enablement & Configuration
   - How to turn on Code Quality and configure related features
- Standard findings & ratings
   - Review finding views and rating definitions
- Pull request workflow
   - Code quality control right in the PR flow
- Measure & operate
   - Measure and operationalize Code Quality
- Positioning & next steps
   - Code Quality vs. Code Security, and next steps in your environment
- Conclusion
   - Wrap up
- Cover questions from the customer

[GitHub Code Quality demo repo](https://github.com/ps-resources/cosmic-pizza)

The best way to demo is to have your own GitHub Enterprise account with GitHub Code Quality enabled.  If you do not have your own Enterprise, you can create your own Enterprise environment for demos.  Please refer to [GitHub Demo Options](../../../CommonContent/gh-demo-options.md) for more information.

***

### Step 6: Customer close out

If needed send follow up materials / resources to the attendees. 
Ensure that the customer understands what the next steps are after the workshop activities. 
You need to understand the basics of VBD (such as survey procedures) and tell them what they can expect next. (in terms of communication from the CSAM or the account team)

### Community support

- [Delivery Community](https://teams.microsoft.com/l/channel/19%3A2da84a09114b46449ca0278bf8354738%40thread.tacv2/VBD%20-%20Copilot%20for%20Developers?groupId=591c20e8-6a02-4476-8881-849bf672e6cf&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47)

### Resources

#### Internal

Please review the IP Share linked above for internal resources.

   - [IP Release Share with slides, resources, and further guidance](https://aka.ms/GHCPAgenticDevOpsIPKit)

#### External

- [GitHub Copilot](https://github.com/features/copilot)
- [GitHub Copilot Documentation](https://docs.github.com/en/enterprise-cloud@latest/copilot)

<details>
<summary>GitHub Demo Options</summary>

[!include[GitHubDemo_Options_Section](../../../CommonContent/gh-demo-options.md)

</details>




