# Delivery Guide: Elevate your AI Apps & Agents with Hackathon​
This guide provides details and instructions to help you deliver a Hackathon engagement on AI agents built with Microsoft Foundry and Microsoft Agent Framework. 
It outlines the steps prior to, during, and after the engagement, to help you keep track of the key deliverables and action items. 

## Description
A Hackathon is an event run over a relatively short time frame, where people get the chance to collaborate in a focused way on a set of use cases, challenges, or initiatives that are deemed interesting to the participants. The goal of a Hackathon is not only to work on solutions, but also to facilitate better collaboration (often across teams and departments), team building, and innovation.

**Objectives**

An Elevate your AI Apps & Agents with Hackathon​ is intended to help customers implement AI Agents for the following example scenarios:

- Sales and Marketing Support: An AI agent helps prioritize customer leads, focus efforts effectively, and create personalized proposals, increasing productivity for sales proposal creation.

- Internal IT Ticket Management: A multi-agent system automates internal IT ticketing. Agents handle self-service, ticket creation, classification, routing, and resolution, integrating with ITSM and escalating to support teams when needed, streamlining issue resolution and reducing manual workload.

- Customer Support and Engagement: A banking avatar answers customer questions in natural language and enables digital execution of tasks like unblocking credit cards or changing limits, improving customer engagement and streamlining banking operations.

- Multi-Agent Renewal Automation: A multi-agent solution manages customer license renewals. Agents assess renewal likelihood, create renewal plans, ensure compliance, and automate customer communications, streamlining the entire renewal process.

- AI-Driven Security Automation: An AI-powered security platform automates multi-tenant operations and scales incident response. The platform filters false positives, executes responses, and preserves institutional knowledge, automating a significant portion of repetitive triage tasks.

- Medical Research and Data Analysis: Tools automate spreadsheet analysis and provide seamless access to information stored in SharePoint. These tools streamline workflows, reduce manual effort, and empower researchers to achieve more in less time.

**Deliverable Standards**

At the end of the delivery you should send an e-mail or document to the customer summarizing the work done.
Include any of the following as applicable:

- Key recommendations for the customer's next steps
- Pointers to relevant documentation and reference solutions
- Summary of the use cases explored and any relevant design guidance

## Customer Participants

The engagement is designed for up to 16 participants.
Deliveries in smaller groups are possible and should be scoped appropriately.

- Developers
- Event sponsor(s) / Leaders
- Development Leaders
- Engineering Managers
- Executive Sponsor(s)

## Delivery Guidance
This section includes delivery guidance and supporting artifacts.  
You are free to adapt each step to meet your customers needs as long as you are able to meet the objectives and deliverable standards. 

### Step 1: Scoping

Before the Hackathon event starts, you need to define the goals;
- Technical strategy
- Internal support needed
- Setting customer expectations
- Desired outcomes
- Finding help to get started
conduct a scoping call to confirm the following requirements:

- Is there any customer-specific context relevant to the Hackathon that needs to be captured or reviewed?
  - Examples:
    - Expected number of attendees (will it exceed the maximum 16 capacity?)
    - Existing hackathon process at customer (if any)
    - On-site vs. remote delivery
    - Desired duration (standard is 1-4 days)
    - Any other requirements that impact the standard hackathon agenda
- An Azure subscription and GitHub access are in place to cover all Hackathon attendees
- The chosen Azure region supports Microsoft Foundry Agent Service and has enough model quota for all participants
- Every use case link and the Version table (see Step 2) have been re-checked in the 2 weeks before delivery
Establish ownership of hackathon environment:
- Hackathons in a customer’s environment is the preference.  This would provide an easier path to production for successful workloads.
- For customers with security concerns an isolated environment can be requested with an Azure Pass.
- If Microsoft owns the environment set a timeline for when needs to be turned on and shut down to avoid additional costs.
Funding of Azure usage:
- Important to use Azure policies to manage costs. This includes;
  - Set quotas.
  - Block expensive solutions that are not needed in the hack.
  - Use RBAC wherever possible.

- Sourcing and documentation of the hackathon use case
    - If at all possible, you should discuss potential use cases ahead of the Hackathon day itself to free up more time for hands-on work and give attendees enough time to think of interesting challenges
      - Use the "Hackathon Use Cases" guide below to help the customer decide on a set of use cases that work for the time available.
    - Some customers might prefer to curate their own list of use cases on behalf of the attendees. 
      - If so, make sure to get an overview of these. You should assess if the list of use cases can be successfully completed in the time available for the hackathon event.
- Full list of attendee names and e-mails collected (if available)
- An agenda is agreed upon and circulated to all attendees (in most cases circulated by a point-of-contact on customer side)
- If delivering on-site, ensure that travel arrangements are made in accordance with the applicable guidelines and that access to on-site venue is arranged with the customer
- Confirm who the sponsors and the main points of contact will be across the event days
#### Logistical Details

Some organizations already host Hackathons on a regular basis and therefore already have a well-tested framework for running these events. Thus, the format of this module can differ between customers in terms of duration, number of attendees, and the overall process. Any such customer-specific needs that fall outside of the default structure of this module should be captured during the pre-sales / scoping process.
Assuming that there are no customer-specific modifications needed, the high-level outline of the Elevate your AI Apps & Agents with Hackathon​ is as follows;
Check on location of team - to determine daily start and finish time. Ideally organize for technical support across time zones, for when your team won’t physically be there. 
- **Duration:**  1- 4 days incl. breaks
   - Ideally delivered over consecutive days within a single week
- **Agenda:**
   - Introduction (~30min)
     - Facilitators
     - Team overview
     - Use cases
     - (any customer-specific messaging)
   - Overview of Microsoft Foundry, Foundry Agent Service and Microsoft Agent Framework / Q&A (~30min)
   - Hacking (~8 hours daily) incl. lunch break
   - Team presentations (~45min) on the last day
   - Roundtable discussion / Q&A / WrapUp (~30min - 1 hour) on the last day
- **Remote/onsite:** As agreed with customer

Please review the datasheet for more metadata about the offering.

### Step 2: Delivery

Scope in and deliver one of the following built in use cases or a use case that customer brings. 

|Use Cases|Links|
|-----|-----|
|Use Case 1|[Getting started with AI Agents](./ai-hackathon-usecases/ai-agents/Readme.md) 
|Use Case 2|[Explore the Microsoft Foundry playground](https://learn.microsoft.com/en-us/azure/foundry/concepts/concept-playgrounds)
|Use Case 3|[Quickstart: Create an agent with Microsoft Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/prompt-agent?tabs=python)
|Use Case 4|[Use Azure Logic Apps as tools with Microsoft Foundry Agent Service](./ai-hackathon-usecases/use-azure-logic-apps-as-openai-functions/Readme.md)
|Use Case 5|[Implement Semantic Caching with Azure API Management](./ai-hackathon-usecases/semantic-caching-with-azure-api-management/Readme.md) 
|Use Case 6|[Organization-wide provisioning and monitoring of OpenAI Provisioned Throughput Unit (PTU) deployments with API Management](./ai-hackathon-usecases/ptu/Readme.md)
|Use Case 7|[VoiceRAG: An Application Pattern for RAG + Voice Using Azure AI Search and the GPT-4o Realtime API for Audio](https://github.com/Azure-Samples/aisearch-openai-rag-audio)
|Use Case 8|[Build agents with Microsoft Agent Framework on Microsoft Foundry](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-azure/) 
|Use Case 9|[Multi-agent workflows with Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/journey/workflows)


During the Hackathon itself, ensure that these tasks are completed:

- All presentations / agenda items are presented and completed as per the plan agreed upon with the customer
- All teams / attendees have chosen / been assigned to a use case
- All attendees have access to the tooling they need for the Hackathon (customer responsibility)
- The provider is available (on-site or remote) throughout the Hackathon for any support needed by the Hackathon attendees
- All teams / attendees have presented their results to the broader group
    - This can be skipped in case the number of attendees is so large that it does not fit into the allotted time. For example, if there are 30 teams and each get 5 minutes to present then that will consume at least 2.5 hours.
    - Make sure this is discussed with the customer up front.
- Potential challenges and how to address them

    - Technical Issues: Participants may encounter technical issues with the tools and technologies being used. To address this, ensure that there is adequate technical support available throughout the Hackathon. Provide participants with access to documentation and resources, and consider having a dedicated support team on standby. Common issues include model quota limits and region availability; check both during scoping.
    - Time Management: With a limited timeframe, participants may struggle to complete their projects. Encourage teams to set realistic goals and prioritize tasks. Provide a clear agenda and schedule to help participants manage their time effectively.
    - Team Collaboration: Effective collaboration can be challenging, especially for teams that are not used to working together. Encourage open communication and regular check-ins. Provide collaboration tools and platforms to facilitate teamwork.
    - Scope Creep: Participants may try to tackle too many features or use cases, leading to scope creep. Remind teams to stay focused on their core objectives and to avoid adding unnecessary features. Encourage them to create a clear project plan and stick to it.


### Step 3: Close Out and Follow Up


When closing out the delivery, please remember to:

- Ensure all questions that were not addressed during the Hackathon directly are followed up on
- Like with any other Unified delivery your main customer contact may receive an automated survey for this engagement. Ensure that their contact details are correct before closing your dispatch. 
- Ensure all of your time has been recorded in ESXP 
- Discuss with the Account Team about creating a customer story for the delivery of the engagement
    - This might be of interest in case the Hackathon is delivered as a standalone engagement and e.g. there were a large number of attendees

### Step 4: Customer close out

## Prerequisites
In order to run most labs successfully, the customer needs to - at a minimum - ensure that:

- All participants have access to an Azure Subscription
- All participants have Owner or Contributor permissions on the Azure resource groups they need to work with as part of the lab, and the Azure AI User role (or equivalent) on the Microsoft Foundry project 
- A Microsoft Foundry project is created in a supported region, with the required models deployed and enough quota for all participants
- There is sufficient Azure credit/budget (50 USD or more recommended) per participant available to allow for experimentation and to spin up some more expensive data service
- All participants either have or can create a GitHub user to access and work with GitHub repos containing the labs
- All participants have access to a compatible IDE (for example: Visual Studio Code) and a Git client (for example: Git for Windows) or a Microsoft Dev Box or Codespace with similar development tools
- All participants have Python [Add version] or .NET [Add version] installed, plus the Microsoft Foundry SDK and Microsoft Agent Framework packages

## Demos, Additional Resources & References
To enhance your Hackathon experience, here is a list of projects, additional resources, and references that can be valuable for your Hackathon

- [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/foundry/) 
- [Microsoft Agent Framework documentation](https://learn.microsoft.com/en-us/agent-framework/) 
- [Migrate from classic Assistants to Microsoft Foundry Agent Service](https://learn.microsoft.com/azure/foundry/how-to/navigate-from-classic)
