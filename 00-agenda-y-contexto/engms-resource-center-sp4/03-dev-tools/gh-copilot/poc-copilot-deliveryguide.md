# Delivery Guide: PROOF OF CONCEPT for GitHub Copilot
This guide provides details and instructions to help you deliver the **Proof of Concept VBD** for your customer. This engagement must accomplish the following objectives:  

**Objectives**
- Completed proof of concept deployment in line with the expectation set during scoping.
- Help the customer evaluate GitHub Copilot (Business or Enterprise) in their own environment and with a set of developers chosen by the customer.
- Deliver survey data showing the differences between independent and assisted software development. 
- Build the customer's experience and knowledge of Copilot to build the confidence to deploy in production.

**Deliverable Standards**
- Ensure the customer has all technical pre-requisties in place to successfully enable Copilot on Day 1 of the delivery for the team(s) testing the product
  - Refer to the proof of concept guide in the IP Share for more details
- Give time between delivery dates for the teams testing out Copilot to experience the product fully
- Forecast time needed to complete proof of concept and run necessary surveys
- Have proof of concept survey and interview results ready in time for the close out meeting

## Customer Participants
`Note: Provide details on the customer participants that are needed for a successful delivery `

Having the right customer participants in the Proof of Concept is essential to completing a successful engagement. Ensure the customer roles outlined below are available and able to participate.

|Customer Role | Description | Required or Optional|
|----|----|----|
|Customer Relationship Holder| The person(s) responsible for the deliver on the customer site | Required (at least kick off and close out)
|Developers| The developers testing GitHub Copilot during the testing phase. As well as using Copilot for at least one week, they will also be asked to complete a survey ahead of and after the pilot. | Required
|GitHub Organizational Admin| The owner of the GitHub organization where GitHub Copilot will be enabled | Required
|Azure Subscirption Admin| To ensure billing accrues against ACR you should make sure any Copilot consumption is charged against an Azure Subscription | Highly Recommended
|Architects| To review the impact of GitHub Copilot on the creating of key architectural assets and related code. A few architects (if organized separately) may want to participate in active testing | As Required
|Other IT professionals| These are the people responsible for provisioning and managing IT and Azure resources. You may need access to them to configure deployment to developer IDEs.| As Required|

## Delivery Guidance
This section includes delivery guidance and supporting artifacts.  
You are free to adapt each step to meet your customers needs as long as you are able to meet the objectives and deliverable standards. 

### Step 1: Scoping
Using the information in the scoping deck, and the datasheet, eplain how the delivery will be carried out and what they can expect at each phase, before and after delivery. 
Request the customer roles that will be needed for a successful delivery. Refer to [Customer Participants](#customer-participants) section for details.

Review the [technical pre-requsites](https://docs.github.com/en/copilot/getting-started-with-github-copilot#prerequisites) for GitHub Copilot with the customer and confirm that they meet the requirements.
Review any business pre-requisites (such as budget approvals or necessary permissions) with the customer to confirm that all necessary approvals on their end are in place.

In case you receive questions about security, liability, or copy right, you can point them to the [public customer terms](https://github.com/customer-terms) that their privacy and compliance teams can review ahead of the delivery.
If the customer is not ready to move forward, it may make sense to position the Workshop for GitHub Copilot for Developers delivery ahead of this delivery to help the customer build additional knowledge about the offering.

Identify all the other non-functional requirements. These may include areas such as [necessary network access](https://docs.github.com/en/copilot/overview-of-github-copilot/enabling-and-setting-up-github-copilot-for-business#configuring-network-settings) (Is the team testing GH Copilot a group of developers who can connect out to the internet?) or IDE extension roll out strategies. (Is there a process in place to deploy the necessary Copilot extension to developer workstations?)

Use scoping call to understand what topics you may have to prepare for during the engagement.
Some example questions you may ask during the scoping are:

- What do you expect from the delivery?
- What technical / business problem are you expecting the PoC to solve?
- What are the skill levels of the developers, operation, and security teams?

Finally, ask the customer to review the relevant [documentation](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-settings-on-githubcom) around configuring and rolling out GitHub Copilot in preparation for the engagement. 
There will be time during the delivery to clarify any questions about the approach. 

### Step 2: Find Supporting Material

### [Documentation](#tab/Documentation)

Review the public [GitHub Copilot documentation](https://docs.github.com/en/copilot/quickstart) for the latest product updates.
The [Microsoft Learn Module on GitHub Copilot](https://learn.microsoft.com/en-us/training/paths/copilot/) is a good resource for your personal ramp up.
Work through the [Product Quickstart](https://docs.github.com/en/copilot/quickstart) ahead of the session.

Review GitHub's [research](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) around productivity increases with GitHub Copilot as context for the delivery.

Also consider reviewing internal resources around GitHub Copilot:

- [Set your account up with access to GitHub Copilot for demo purposes](https://aka.ms/copilot)
- [Review existing customer usage in OctoDash](https://aka.ms/octoDash)
  
### [Demo and Presentation Material](#tab/Demo-and-Presentation-Material)

The [GitHub Sales SharePoint](https://microsoft.sharepoint.com/teams/GithubSales) has resources for pitching and demoing the GitHub Copilot offering. 

- [Review GitHub and Copilot demo scripts](https://microsoft.sharepoint.com/teams/GithubSales/SitePages/SalesTools.aspx)
- [Review GitHub Copilot demos for Visual Studio Code](https://www.youtube.com/playlist?list=PLj6YeMhvp2S5_hvBl2SE-7YCHYlLQ0bPt)
- [Review GitHub Copilot demos for Visual Studio IDE](https://www.youtube.com/playlist?list=PLReL099Y5nRckZDdcQ21UigO9pKa14yxC)
- [Review Copilot pitch and demo content](https://microsoft.sharepoint.com/sites/GitHubHelp)
- [Review GitHub Copilot Sandbox org with demos](https://github.com/ps-copilot-sandbox)
- [Review the GitHub Copilot "Getting Started" resources](https://github.com/features/copilot/getting-started)
- [Review GitHub Copilot usage guidance by the Cloud Advocacy team](https://repos.opensource.microsoft.com/orgs/MicrosoftCopilot?section=videos)
- [Review the latest Copilot Adoption updates](https://microsoft.sharepoint.com/teams/DevRelTeam/Shared%20Documents/Forms/AllItems.aspx?id=%2Fteams%2FDevRelTeam%2FShared%20Documents%2FDeveloper%20Cloud%2FCopilot%20Adoption%20Updates)

### [Checklists, Guides and Decks](#tab/Checklists-Guides-and-Decks)

You may utilize the process decks included with this offering for scoping, kick-off, and close out.
You can find them on the [IP Share](https://aka.ms/GHPOCCopilotDev)

The following shared resources are also available on the IP Share:
- checklists
- deployment planning documentation
- survey templates
- interview guidance

---

### Step 3: Delivery
Working with the customer you should identify one or more teams that can test GitHub Copilot during the course of a week or another time frame set by the customer. 
**You should agree upon the exact time frame during your scoping meeting.** 

While the Proof of Concept delivery is for a fixed set of days they can be booked together or further apart. 
Leaving a gap of a few days based on the customer preferences can be preferable here as it allows developers to gather more experience using GitHub Copilot. 

Depending on the size of the customer organization, you may also choose to split the tasks outlined over a number of days or deliver them all in one day. 
Work with the CSAM so that the delivery schedule can work in line with everyone's expectations and needs.

#### Whiteboarding
Start your delivery with a Kick Off session with all main stakeholders. 
Use a whiteboard to map out the deployment process of the GitHub Copilot extension and detail the license assignment process based on the customer's input.
Document the process used as part of your close out content. Review with the customer if this process could scale for an eventual production deployment. 
The [IP Share](https://aka.ms/GHPOCCopilotDev) contains some additional documentation on this task that you can review as a guide. 

#### Documentation Review
Ensure that the customer understands the relevant [documentation](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-settings-on-githubcom) around GitHub Copilot configuration before proceeding. 
If there are any open questions, then now is the time to answer them. The customer should have reviewed the documentation ahead of the engagement. (as requested during scoping)

#### Design the evaluation process
Because this engagement is scheduled around enabling the customer to trial GitHub Copilot with a limited set of stakeholders you will need to spend time designing the exact evaluation process with the customer together.
If survey evaluation is not possible, or not preferred by the customer, you can also collect data via interviews. 

**Survey**
Using a tool like Microsoft Forms (or a different platform if the customer prefers it) create a survey [aligned to the research published by GitHub](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) at the time of release of GitHub Copilot.
A detailed guide is available on the [IP Share](https://aka.ms/GHPOCCopilotDev).

Select questions based on the customer's organizational needs. You should aim to keep the survey anonymous unless if the customer has a strong reason not to do this. 
Only ask a few questions to keep participation rates high. 

It is strongly recommended that you collect survey results ahead of when the team(s) testing the tool starts working with GitHub Copilot (Business or Enterprise) and then again after working with it for at least a week.
- Based on the outcome you may choose to present both or just one survey in your close out presentation. 
- Based on the organizational needs you may want to adjust your line of questioning to more easily delivery the proof the customer is looking for.

**Interviews**
You can conduct interviews and collect more qualitative data instead of survey results.
A guide for this option is available on the [IP Share](https://aka.ms/GHPOCCopilotDev).

#### Deploy GitHub Copilot to your testers
Help the customer's IT team make the necessary changes to 
- roll out the GitHub Copilot extension to developer machines
  - and/or allow developers to install the extension themselves
- enable appropriate GitHub Copilot Business or GitHub Copilot Enterprise licensing 

The [quickstart and Copilot documentation](https://docs.github.com/en/copilot/quickstart) will help guide you on the necessary steps.

#### Education

The team(s) that you work with may need some help understanding the benefits of Copilot following the activation and enablement of their license.
Use the demo scripts on [GH Sales](https://microsoft.sharepoint.com/teams/GithubSales/SitePages/ProductInformation.aspx#github-copilot) to build one or two engaging demos that are aligned to the Copilot features that they are interested in.

### Step 4: Customer close out
The customer close out day should take place at the end of the testing period that the customer has set.
On the day you should re-run your evaluation process either by conducting fresh interviews or by re-running the same survey that you ran at the start of the delivery.
Gather the evidence and finalize your close out deck. A template is provided on the [IP Share](https://aka.ms/GHPOCCopilotDev).

In addition to collecting evidence from the developers who worked with GitHub Copilot throughout the testing period, you should consider interviewing the team implementing the administration changes about their experience and document it in the close out deck.
In the second half of the day, present the close out deck to the key customer stakeholders identified during scoping.

Thank the customer for their time, and identify the next follow-up actions, which could be one or more of the following:

- A production deployment of GitHub Copilot to the whole organization
- A detailed review of the roll out approach to avoid technical issues
- Further proof of concepts to gradually increase the coverage of GitHub Copilot in the organization over time. 

## Additional Resources & References

Always review the [GH Sales SharePoint](https://microsoft.sharepoint.com/teams/GithubSales) for newly created presentation materials and pitch decs.
This is also where you can find product FAQs and demo guides.

Leverage the [Copilot Trust Center](https://github.com/trust-center) to answer questions around security, privacy, and compliance with Copilot.
Lean on other members of the account team where a specific privacy/security/compliance question needs to be answered by either the product team or the corporate Sales leadership.

[!include[GitHubDemo_Options_Section](../../../CommonContent/gh-demo-options.md)

### Ramp Up Resources

- [IP Release Share with PoC guide and delivery templates](https://microsoft.sharepoint.com/:f:/r/teams/ASDIPRelease/IP%20Release/Modern%20Apps/GitHub/Proof%20of%20Concept%20-%20GitHub%20Copilot%20for%20Developers?csf=1&web=1&e=s1UndY)
- [Technical documentation](https://docs.github.com/en/copilot)
- [Microsoft Learn Module on GitHub Copilot](https://learn.microsoft.com/en-us/training/paths/copilot/)
- [Product Quickstart](https://docs.github.com/en/copilot/quickstart)

- [Case Study: Adding support for Jetbrains IDE at scale](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/customer-success-meesho-s-genai-approach-with-github-enterprise/ba-p/4033097)

## Known issues and updates
- N/A 

### Community support
- [Teams Channel](https://teams.microsoft.com/l/channel/19%3A2da84a09114b46449ca0278bf8354738%40thread.tacv2/VBD%20-%20Copilot%20for%20Developers?groupId=591c20e8-6a02-4476-8881-849bf672e6cf&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47)





