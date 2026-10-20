# **Delivery Guide - Landing Zone Accelerator to Build and Deploy Azure AI Platform​​​**
 
This delivery guide provides details and instructions to help you deploy the [**AI Landing Zone Accelerator**](https://aka.ms/ailz) for your customer.

## Description
The [AI Landing Zone Accelerator](https://aka.ms/ailz) is a Gold Standard Solution Accelerator that provides a design checklist, reference architectures and extensible implementation options (Terraform, Bicep) for production-ready enterprise scale AI Apps & Agents. It is designed to be deployed along with Azure Landing Zones (ALZ), and the best practices implemented in the LZA are derived from the [Cloud Adoption Framework (CAF)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/), [Well-Architected Framework (WAF)](https://learn.microsoft.com/en-us/azure/well-architected/ai/) and [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/). The AI Landing Zone architectural approach can be used as design guidance for greenfield implementation and as an assessment for brownfield customers already using AI Foundry.

## Objective 
- **Design** AI Landing Zones tailored to the customer requirements and their cloud platform based on the design checklist.
- **Architect** AI Landing Zones leveraging the reference architectures as baseline to align with the design.
- **Implement** AI Landing Zones using the terraform and bicep extensible implementations based on the design and architecture.

## Pre-requisites
In order to have a successful delivery, please review the pre-requisites carefully.

### Familiarity with Application Accelerators: 
These are reusable assets to help customers deploy to production faster based on recommended good practices guidance. You can leverage them as it is or customize them to meet customers' requirements.

1. [AI Landing Zone](https://aka.ms/ailz)
1. [Terraform Implementation](https://aka.ms/ailz/terraform)
1. [Bicep Implementation](https://aka.ms/ailz/bicep)
2. [Reference Architectures](https://aka.ms/ailz#reference-architectures)
3. [Design Checklist](https://aka.ms/ailz#design-framework)

## Customer Participants

Having the right customer participants in the AI Landing Zone engagement is essential to completing a successful delivery. Ensure the customer roles outlined below are available and can participate in the workshop.

|Customer Role | Description | Required or Optional|
|----|----|----|
|Infra Cloud Architect| This is the person responsible for designing the infra cloud environment | Required| 
|AI Developers| These are the people responsible for writing and developing the AI application  | Required| 
|Deployment Workload owner| The person responsible for the deployment workload, usually a Devops/Build/Site Reliability Engineer or Release Manager type role| Required|
|Other IT professionals| These are the people responsible for provisioning and managing IT resources like networking, compute, IAM, Security, ETC  | Optional| 

## Delivery Guidance

This section includes delivery guidance and supporting artifacts.  You are free to adapt each step to meet your customers needs as long as you are able to meet the objectives and deliverable standards.

### Agenda

#### Step 0: Scoping - Day 0

**Objective**: Conduct pre-scoping with team and scoping with customer

**Key Activities**: Review their existing Landing Zone or equivalent cloud environment,  identify AI workloads, models, or use cases planned for deployment and define key stakeholders, roles, and success criteria.

**Deliverables**: Scoping Presentation with details captured from the key activities above.

**Outcome**: A clear understanding and alignment on the engagement scope and outcomes.

#### Step 1: Design - Day 1

**Objective**: Define the AI Landing Zone based on customer requirements.

**Key Activities**: Design the AI Landing Zones based on design areas and the design consideration along with recommendations in each design area

**Deliverables**: AI Landing Zone Design checklist (Document or worksheet) along with presentation

**Outcome**: Alignment on high level design detail that fits enterprise and AI governance needs of the customer.

#### Step 2: Architect - Day 2

**Objective**: Define the detailed, technical architecture and blueprint to implement the AI Landing Zones.

**Key Activities**: Translate the design into technical reference architecture tailored to the requirements of the customer.

**Deliverables**: Tailored Reference Architecture

**Outcome**: Alignment on reference architecture for implementation.

#### Step 3: Implement - Day 3

**Objective**: Provide needed support for production deployment performed by customer.

**Key Activities**: Walk the customer through the implementation of AI Landing Zone using their choice of extensible implementation using either Terraform or Bicep.

**Deliverables**: Bicep or Terraform  implementation of AI Landing Zone.

**Outcome**: Implementation of AI Landing Zone in customer's Azure environment.

## Close out

Recap the engagement and discuss next steps with customer stakeholders. It is important to include all the key stakeholders in this meeting.

- Provide an overview of the design using the completed design checklist worksheet.
- Walk through the tailored reference architecture.
- Review the Terraform or Bicep implementation in Azure.
- Document recommendations including next steps
- Provide recommended resources for upskilling
- If any further VBDs are recommended, inform the CSAM.
- Collect feedback on the overall VBD delivery and delivered content.

## Resources 

### IP Assets 
* [Presentation](https://aka.ms/ailz/presentation)
* [Diagram](https://aka.ms/ailz/diagram)
* Design Checklist - [Word](https://aka.ms/ailz/documentation) or [Excel](https://aka.ms/ailz/workbook)
* [Repo](https://aka.ms/ailz)

### Level Up Training 
* [Level up slide deck - Coming Soon](https://microsoft.sharepoint.com/)
* [Level up Recoding - Coming Soon](https://microsoft.sharepoint.com/)

### Support & Feedback

- For any internal feedback on the VBD, please use this [form](http://aka.ms/vbdfeedback).
- For any public feedback on the LZA, please [create an issue](https://aka.ms/ailz) in the GitHub repository.
