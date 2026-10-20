# Delivery Guide: Proof of Concept for Zero to Agents Immersion

This guide provides details and instructions to help you deliver the **Proof of Concept for Zero to Agents Immersion** service for your customer as a 1-day Value-Based Delivery (VBD) engagement.
This engagement is designed to help development teams already using GitHub Copilot discover and explore the full potential of **GitHub Copilot Agents** and agentic workflows. Through expert-led demonstrations, interactive exploration, and practical use cases, participants will gain insights into automating development tasks with AI agents.
The delivery must accomplish the following objectives for different personas:


**Objectives**

See each persona's specific objectives below:

## [**Software Developer**](#tab/dev-persona-objectives)

- Showcase advanced GitHub Copilot Agents capabilities and agentic workflow patterns
- Demonstrate real-world automation scenarios using Copilot Agents and Model Context Protocol (MCP)
- Enable participants to understand how to leverage agents for complex development tasks and non-development use cases
- Build foundational knowledge to begin the Copilot Agents journey within the organization
- Create customer's first GitHub Copilot Agent and learn how to customize it for specific tasks in a development workspace

## [**Product / Project Manager**](#tab/pm-persona-objectives)

- Showcase GitHub Copilot's capabilities to increase PMs' productivity and efficiency
- Demonstrate how GitHub Copilot can assist in PM tasks such as planning, documentation, requirements, and tracking work items
- Understand AI models and prompt construction in GitHub Copilot.
- Learn AI response generation and prompt best practices.
- Utilize prompt enhancement concepts.
- Become familiar with VS Code and GitHub Copilot features relevant to PM workflows.

## [**GitHub Copilot Power Hour**](#tab/ph-persona-objectives)

- Start from existing GitHub Copilot knowledge and build confidence in everyday use.
- Improve prompting and context-setting techniques to get more accurate and useful responses.
- Demonstrate how Copilot helps plan, explain, and accelerate real work in a live project.
- Introduce agentic workflows and show how Copilot Agents can execute tasks end-to-end.
- Equip participants to adopt Copilot immediately and identify measurable productivity gains.

***

**Deliverable Standards**

- Deliver comprehensive demonstrations of GitHub Copilot Agents capabilities and agentic workflows
- Provide interactive exploration sessions with Q&A to address team-specific scenarios
- Share best practices and practical guidance for implementing agent-driven development
- Deliver a summary presentation covering key concepts, use cases explored, and recommended next steps
- Identify opportunities for the customer to extend agentic capabilities within their context 

>Note: These are baseline requirements that may be further specified during scoping. Always deliver against the agreed scope.



## Customer Participants
Having the right customer participants in the  workshop is essential to completing a successful engagement. 
Ensure the customer roles outlined below are available and able to participate in the workshop. 

- Developers
- Team Leads
- Development Leaders
- Project/Product Managers

## Delivery Guidance
This section includes all non-technical delivery guidance and supporting artifacts for this delivery. 

You are free to adapt each step to meet your customer's needs as long as you are able to meet the objectives and deliverable standards for next MCEM phase.

This delivery can change rapidly as the product evolves, so please make sure to check the [GitHub Copilot - Zero to Agents Immersion VBD Assets](https://github.com/customer-success-microsoft/z2a-immersion-vbd-assets) for the most up-to-date assets and documentation.


### Step 1: Preparing for the delivery
Use the scoping deck, prerequisites checklist, and datasheet to explain how the delivery will be carried out and what the customer can expect at each phase. Request the customer roles needed for a successful engagement (see [Customer Participants](#customer-participants)). 

- Each attendee must have a valid GitHub Copilot Business or Enterprise license and access to the necessary tools and platforms for the workshop activities.
- Review the technical prerequisites and confirm readiness for GitHub [Organization](https://docs.github.com/en/copilot/how-tos/set-up/set-up-for-organization) or [Enterprise](https://docs.github.com/en/copilot/how-tos/set-up/set-up-for-enterprise)
- Assess business prerequisites (budget, permissions, approvals)
- Identify non-functional requirements (network, IDE extension rollout)
- Address questions on security, privacy, and compliance using [public customer terms](https://github.com/customer-terms)
- If the customer wants hands-on practice or prefers a more interactive learning experience, recommend a [**GitHub Copilot workshop**](./intro.md) to build foundational knowledge before this immersion
- Use the scoping call to identify educational topics and blockers to adoption
- Agree on expectations, outcomes, session participants, and logistics

***Learn the Delivery***

The **Proof of Concept GitHub Copilot - Zero to Agents Immersion** engagement is designed to help development teams (including non-developers) already using GitHub Copilot discover and explore the full potential of GitHub Copilot Agents and agentic workflows. Through expert-led demonstrations, interactive exploration, and practical use cases, participants will gain foundational knowledge and actionable insights to begin their journey toward automating complex development and non-development tasks with AI agents.

This immersion showcases advanced capabilities available in **GitHub Copilot Enterprise**, including agent mode, Model Context Protocol (MCP), and custom agent development.

On average this engagement takes **1 day of effort** delivered as a focused, intensive immersion experience.


### Step 2: Scoping

Explain how the delivery will be carried out. What the customer can expect at each phase, before and after delivery. 
Make sure the right stakeholders from the customer's organization are present throughout the delivery. Refer to [Customer Participants](#customer-participants) section for details.

Ensure you discuss and understand the customer's requirements and that the tooling to be used is agreed. 
Ensure all the stakeholders are on the same page regarding the deliverables and outcomes.

If you are delivering the lab component or if the customer is planning to follow along with any demos, please help them better understand the pre-requisites to set up before the day of the delivery.
You can point them to relevant documentation or recommend a proof-of-concept VBD activity, if they require help.

***

### Step 3: Kickoff

Share details of what workshop activities you will cover and what will not be covered. 
If a specific topic of interest is not covered, then you should have already thought about handling it during or after scoping.
However if you can accommodate last minute request, we recommend you do so to achieve a greater level of customer satisfaction with the offering.

### Step 4: Delivery
The stages are onboarding, adoption, optimization, and sustain.  This delivery guide focuses on the onboarding and adoption phases. Each customer is in a slightly different place in their journey, so you will need to adapt the delivery to meet their needs and the Q&A that arises during the session.

#### Attendance and Setup
- Ensure all participants have access to the meeting platform (Teams, Zoom, etc.)
- Confirm that all participants have the necessary permissions and access to GitHub Copilot Enterprise features
- Microsoft architect will work with the customer to agree on the number of participants for this engagement 

#### Module 1: Zero to Agents workshop delivery

Ensure you cover modules that are relevant to or identified for the success of the VBD activity.


`The slide deck will have a format of  language-vMMYYYY (e.g. en-v032026*) where the date represents the last update of the deck. Please make sure to use the most recent version of the deck for your delivery. The slide deck is available in the [IP Release Share](https://aka.ms/Z2AAdoptionIPKit)`.

## [**Software Developer**](#tab/dev-persona-agenda)

- **Copilot Foundations**
  - Overview
  - Copilot works behind the scenes
  - Shortcuts for context awareness - prompts / commands / variables
- **Demo 1**
  - Live coding demos showcasing Copilot features and prompting techniques
- **Advanced Prompting Techniques**
  - Setting better context for GitHub Copilot
  - Pillars of effective GitHub Copilot Context
  - Instructions and prompt files
  - Probabilistic nature of LLMs
- **Copilot Agents Overview**
  - What are Copilot Agents
  - Benefits of using Copilot Agents
  - Key Concepts
  - Model Context Protocol (MCP)
- **Demo 2 (VSCode) OR Demo 3 (Copilot CLI)**
  - Live coding demos showcasing Copilot Agents and MCP
  - Execution-Scope Control
  - Testing and Code Architecture Definition
  - Spec/Requirement Development
  - Full Agent Mode
- **FAQ**
  - Community
  - FAQ Resources
- **Cover questions from the customer**

[Demo 1 & 2 script](https://github.com/customer-success-microsoft/z2a-immersion-vbd-assets/blob/main/demo-script/z2a-demo-script.md)
[Demo 3 script (Copilot CLI)](https://github.com/customer-success-microsoft/z2a-immersion-vbd-assets/tree/main/demo-script/z2a-demo-copilot-cli)

## [**Product / Project Manager**](#tab/pm-persona-agenda)
- **Copilot Foundations**
  - Overview
  - GitHub.com Copilot Cloud Agent
- **Demos 1**
  - Live GitHub.com demos showcasing Copilot features and prompting techniques
- **Advanced Prompting Techniques**
  - Setting better context for GitHub Copilot
  - Pillars of effective GitHub Copilot Context
  - Instructions and prompt files
  - Probabilistic nature of LLMs
- **Copilot Agents Overview**
  - What are Copilot Agents
  - Benefits of using Copilot Agents
  - Key Concepts
  - Model Context Protocol (MCP) - External Gateway
- **Visual Studio Code Overview**
  - Introduction to VS Code
  - Benefits of using VS Code for PMs
  - Overview of VS Code Copilot features for PMs
- **Demo 2**
  - Live demos showcasing VS Code Copilot Agents and MCP
  - Spec/Requirement Development
  - Full Agent Mode
- **FAQ**
  - Community
  - FAQ Resources
- **Cover questions from the customer**

[Demo 1 & 2 script](https://github.com/customer-success-microsoft/z2a-immersion-vbd-assets/blob/main/demo-script/z2a-demo-script-pm.md)


## [**GitHub Copilot Power Hour**](#tab/ph-persona-agenda)

**Power Hour Delivery Guidance**
- Power Hour should be delivered for customers who have GitHub Copilot licenses but low active usage, with the goal of helping users experience GitHub Copilot hands-on in their own IDEs and realize immediate value in real-world workflows.
- To maintain quality and engagement, Power Hour sessions should target no more than a 1:30 instructor-to-participant ratio, ensuring attendees receive sufficient hands-on guidance and support throughout the workshop.
- Power Hour engagements should also be limited to no more than three sessions per customer to encourage long-term adoption momentum and self-sufficiency rather than recurring dependency.
- While the live session itself is one hour, the broader value comes from accelerating activation, increasing usage confidence, and helping customers realize ROI on their existing GitHub Copilot investment.


- **Power Hour Prerequisites**
  - Participants have a GitHub Copilot license, are signed into GitHub in their IDE, have VS Code or JetBrains installed, and have a sample or real project ready.
- **Set the frame**
  - Why this hour matters
- **Live Installation**
  - Everyone installs together (VS Code + JetBrains)
- **First Prompts**
  - Inline completions
  - Comment-to-code
- **Copilot Chat**
  - Where daily adoption accelerates
- **Agent Mode Preview**
  - When to move from chat to delegated task execution
- **Your Own Project**
  - Run prompts on real code
- **Close + Metrics**
  - Lock momentum and measure value
- **Metrics to track after session**
  - Active Copilot users
  - Prompt/chat usage frequency
  - Task completion time
  - Self-reported time saved
- **Power Hour Success Outcomes**
  - Each participant runs at least one prompt in a real project
  - Uses Copilot Chat on real code
  - Identifies one daily use case
  - Agrees on a 2-4-week follow-up metric



***



In order to keep focus and ensure that the customer gets as much as possible out of the training, please ensure the items below are completed.

-  Make sure the customer understands that all participants need a **GitHub account** on the supported target platform with their corporate login and **GitHub Copilot enabled**.
-  **Introduction** of participants and providers
-  Give a reminder that the enablement will be performed on the current version of Copilot and Copilot Chat, we cannot support older versions, and that features covered in the training may not be available if they are not on the latest version.
-  Present and discuss the **learning objectives slide** and the **agenda**
-  Do the ice breaker for training day to get to know the audience, encourage interactions, and learn expectations (optional)
-  For each section in the slide deck, ensure that the following items are covered:
   - A thorough, clear presentation of the content covered in the slides (don't forget the **speaker notes**)
   - While it is not mandatory for the customer to complete the Demos, we give them the opportunity to follow along if they would like. 
   - Demo the hands-on yourself to make sure nobody was lost and could not follow along
   - Questions raised by the audience, either via chat or verbally, have been either addressed directly or noted for follow-up
-  Do a retro at the end of each day to collect feedback and manage the expectations
-  Once the session is done, do a final Q&A to collect any questions not addressed during the training

The [IP Release Share](https://aka.ms/Z2AAdoptionIPKit) contains the presentation deck for this delivery.

#### Module 2: Zero to Agents Follow Along Lab

The follow along lab provides an opportunity for participants to apply the concepts and techniques covered in the workshop. Participants will work through hands-on exercises to reinforce their understanding and gain practical experience with GitHub Copilot and Copilot Agents.

To follow along please provide customers with the link below.
<!-- TODO: need to add instructions for PM  -->
- [GitHub Copilot - Zero to Agents Immersion Follow Along Lab](https://aka.ms/Z2AImmersionLab)

**This section should take approximately 1.5 hours, depending on the customer and how many exercises they choose to complete. Be sure to encourage participants to complete as many exercises as possible to get the most out of the lab. This section can also include a secondary Q&A section as needed.**

### Step 4: Customer close out
Thank the customer for their time and identify next follow-up actions.

Recap the engagement and discuss next steps with customer stakeholders, including:

- Overview of GitHub Copilot and its value for the organization
- Review of engagement outcomes, learnings, and value delivered
  - Rollout and governance approach
  - User and administrator experience
  - Tasks completed and support provided
  - Share 'Next Steps' slide to help the customer understand how to continue their GitHub Copilot journey
- Share productivity statistics and value realization evidence ([Report](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/))

## Additional Resources & References

Lean on other members of the account team where a specific privacy/security/compliance question needs to be answered by either the product team or the corporate Sales leadership.

### Ramp Up Resources

<!-- TODO: update the ppt and demo material -->
- Demo and Presentation Material in this delivery guide
- [Technical documentation](https://docs.github.com/en/copilot)
- [Product Quickstart](https://docs.github.com/en/copilot/quickstart)

## Known issues and updates
- N/A 

### Community support
- [Teams Channel](https://teams.microsoft.com/l/channel/19%3A2da84a09114b46449ca0278bf8354738%40thread.tacv2/VBD%20-%20Copilot%20for%20Developers?groupId=591c20e8-6a02-4476-8881-849bf672e6cf&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47)

<details>
<summary>Demo options and resources (click to expand)</summary>

[!include[GitHubDemo_Options_Section](../../../CommonContent/gh-demo-options.md)

</details>



