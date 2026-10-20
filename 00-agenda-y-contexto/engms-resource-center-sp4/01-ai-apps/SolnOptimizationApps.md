<!--- file last updated: 6/23/2025 by yonahshafner--->

<!-- [!INCLUDE [Style Block](../CommonContent/MD_StyleBlock.md)] -->

# Solution Optimization for AI Apps & Agents



<!--If you have feedback for any Data & AI VBD, let us know [here](https://aka.ms/csudai/feedback). -->

## Objective

The goal of this phase is to optimize the customer environment by addressing issues related to Performance, Tuning, and Optimization (PTO). This includes a comprehensive approach that aligns with our AI optimization pillars: Governance, Performance Improvements & Resiliency, Security, and Monitoring. Some of the use cases that might fall under this category are:

- [Cost](#cost-optimization): Reviewing and optimizing resource allocation to manage and reduce operational expenses associated with AI workloads.
- [Monitoring](#monitoring): Setting up Azure Monitor Baseline Alerts (AMBA) for AI workloads, using the Azure AI benchmarking tool to validate throughput and performance statistics. 
- [Performance Improvements & Resiliency](#performance-improvements--resiliency): Establishing a CI/CD cycle for AI models to ensure continuous integration and delivery.
- [Governance](#governance): Implementing Prompt Engineering, fine-tuning, load balancing, and securing the deployed AI solution.
- [Security](#security): Enhancing the solution for the next version, such as evolving generative AI assistants or chatbots to Agentic Apps.


## Understanding Customer Objective and Maturity
It is essential for the CSA to collaborate closely with the customer to determine which engagements will best address their needs and objectives. Together, you should discuss and align priorities, ensuring that the scope of work is tailored to the customer's unique environment and goals. 
Here are some questions to guide that conversation.

- What are the performance issues in the solution and how long are they happening?
- Are the issues replicable?
- Is data logging enabled? What logs are we collecting from the services?
- Does the customer have any benchmark numbers?
- What has changed in the environment?
- What troubleshooting steps have been performed?
- What is the business impact?

To optimize the customer's solution, it is crucial to understand their maturity in Azure and AI. Use this table to help guide the conversation:


*Customer Maturity*
| Readiness Dimension | Early Stage | Mid-Maturity| Advanced |
| --- | --- | --- | --- |
| AI Maturity | PoCs, prompt-based prototypes | Deployed GenAI apps, experimenting with tuning | Multi-agent orchestration, integrated LLMs in prod |
| Use Case Type | Single chatbot, basic QnA | LLM-powered assistants, retrieval-augmented generation (RAG) | Agent based apps, AI copilots, multi-turn logic |
| Infra Posture | No Landing Zone, limited monitoring or tagging | Basic Landing Zone, partial monitoring (e.g., log analytics enabled) | AI-ready Landing Zone with policy, cost tracking, and observability |

## Scoping the Delivery
Based on your conversation with the customer, suggest a high-level agenda for managing this engagement. This should include the types of services, training, and delivery you plan to provide. Additionally, giving an approximate duration for the engagement will help the customer plan accordingly. Ensure clear communication regarding what is within the scope and what is not with the customer.

| **Success Criteria**  |
|---------         |
|Assess customer performance issues and provide guidance and remediation that help resolve the performance issues |



## Deliver the Selected Scenario
To collaborate effectively with the customer and develop a comprehensive scope of engagements, consider the following steps:

- Understand key decisions, features, and functionality built into the solution
- Highlight gaps in Solution based on Best Practices for prioritized solution scenarios
- Build improvement roadmap for enhancing business value
- Assist with implementation of scoped optimization recommendations for current solution


Below are various **deliveries, documents and other assets** that you can leverage.  Note you are NOT limited to or bound by below deliveries.  You have the freedom to use the below deliveries, come up with your own custom deliveries, mix and match, etc. to reach a solution that is favorable to customer.

**Internal-Only guidance**

| Delivery Type | Delivery Name | Customer Level | Target Audience | Delivery Method|Use Case | Outcome
| --- | --- | --- | --- | --- | ---| ---|
| Guidance (Internal-only)* | [AOAI Model Migration Guidance](https://aka.ms/aoai-model-migration-guidance) | Intermediate | Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers and Security Architects | Discussion / Guidance| This guidance document offers internal field teams a systematic approach for migrating to newer Azure OpenAI models based on model retirements and deprecation considerations | To maintain continuity, optimize performance, and minimize business disruptions when current model versions are deprecated or retired

> [!NOTE]
>Guidance marked (Internal-only)* is for internal consumption only and should not be shared with customers

Refer to the Customer Maturity Chart in the "Understanding Customer Objective and Maturity" section to choose the right delivery method and IP for the customer. 

**For Early-Stage customers,**
Focus on Governance and Monitoring pillars
- Tagging, RBAC, policy setup
- Azure Monitor Baseline Alerts (AMBA)
- Basic observability and cost visibility

**For Mid-Maturity customers,**
Expand to Performance Improvements, Resiliency and Cost Optimization pillars:
- Throughput tuning, caching, autoscaling
- Benchmarking tools, APRL checks
- Token efficiency and FinOps strategies

**For Advanced customers,**
Introduce Model DevOps, advanced Security, and deeper Governance:
- CI/CD for models, blue/green deploys, AKS/ACA lifecycle
- PTU-M migration and cost control
- Secure API access, multi-agent observability, agent failure handling

**For all customers,**
Introduce [resiliency](#performance-improvements--resiliency) to the customer as a best practice, especially for production environments. Below are various deliveries, documents, and assets available for use. Feel free to use these options, create custom ones, or combine different elements to meet the customer’s needs.

## Solution Optimization Pillars and Engagement Recommendations
### Cost Optimization
Optimize the cost of generative AI applications on Azure AI Service by proactively controlling costs, improving token efficiency, and ensuring accurate cost attribution for app and agent workloads.

**[Optimizing Cost of Generative Applications on Azure AI Service ](https://microsoft.sharepoint.com/:f:/r/teams/ASDIPRelease/IP%20Release/Data%20and%20AI/Azure%20OpenAI/Optimizing%20Generative%20AI%20Application%20on%20AOAI?csf=1&web=1&e=N0EXWV)** 

- Level: Intermediate
- Target Audience: Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers, and Security Architects
- Delivery Method: Discussion / Article
- Outcome: This engagement focuses on how to optimize the cost of Azure AI applications for both new and existing customers. It includes strategies for reducing token usage, implementing cost-effective AI solutions, and ensuring accurate cost attribution for various workloads. The engagement also covers best practices for monitoring and managing costs, as well as tools and techniques for achieving cost efficiency

To explore advanced optimizations with the customer like token compression, especially for managing vector costs in AI search use [Tech Community Azure AI Search Compression](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/azure-ai-search-cut-vector-costs-up-to-92-5-with-new-compression-techniques/4404866)  and [Strategies for Optimizing High-Volume Token Usage with Azure AI](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/strategies-for-optimizing-high-volume-token-usage-with-azure-openai/4007751)

**[Financial Operations (FinOps) on Azure](https://learn.microsoft.com/cloud-computing/finops/)** 

As AI workloads—particularly those involving large language models (LLMs)—become more prevalent, managing their financial impact is critical. FinOps (short for “Financial Operations”) is a collaborative discipline that brings together engineering, finance, and business teams to manage cloud spend with accountability and efficiency.

AI introduces unique cost challenges, including:
- High GPU infrastructure costs and limited availability.
- Unpredictable usage patterns driven by experimentation.
- Involvement of non-traditional stakeholders (e.g., marketing, product, leadership) in AI consumption.

For even more information on FinOps training look at [FinOps Training](https://learn.microsoft.com/training/modules/get-started-with-finops/)

### Monitoring

Monitoring enables real-time insights and issue detection across infrastructure, apps, agents, and models. This Pillar aims to ensure optimal performance and resilience of AI workloads through comprehensive monitoring solutions.

**[Azure Monitor Baseline Alerts (AMBA) for AI workloads](https://azure.github.io/azure-monitor-baseline-alerts/patterns/artificial-intelligence/)** 

- Level: Intermediate
- Target Audience: Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers, and Security Architects
- Delivery Method: Discussion / Guidance
- Outcome: AMBA enhances the Azure experience by offering essential metrics and guidelines for optimal performance. It provides expert recommendations, near real-time notifications, automation policies, guided documentation, and enhanced resiliency for a proactive and informed Azure monitoring approach.

**[Application-Level Monitoring](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/azure-openai-gateway-monitoring)**

For API or token-based authentication, you can:
- Monitor token usage (like access tokens, JWTs) to detect anomalies
- Enforce security controls such as expiry, rotation, rate limits
Azure API Management (APIM), especially when enhanced with AI capabilities or gateway policies, can help:
- Observe and manage token behaviors in real-time
- Implement intelligent throttling, anomaly detection, or access control
- Automate responses or alerts if token misuse is detected



### Performance Improvements & Resiliency

Improves response time, throughput, and system availability using caching, autoscaling, and failover strategies. The goal of this Pillar is to enhance the performance and resiliency of AI workloads, ensuring optimal system functionality and availability. 

**[Azure AI Service Provision Throughput](https://microsoft.seismic.com/app?ContentId=a7cb4996-b424-4bc8-a583-0f9662d01d3a#/doccenter/9d48f049-f6f7-4d11-8e91-958ef85c3dcc/doc/%252Fdd3ef767e6-7f21-4190-afcf-7c5bd5a17be8%252Fdd6832f537-b841-4e44-84d1-5163bc51ad8c%252FdfNWMzZThiNDQtYjYxZS0wNGI2LWJkY2UtYzYzODZjNGMwYTE3%252CPT0%253D%252CU2FsZXMgUmVzb3VyY2U%253D%252Flfd61d09a7-b603-4089-a15b-84eeed24fd75//?mode=view&searchId=e3df6cef-ed4f-4d88-95fc-67c8d0f480b1)** 

- Level: Intermediate/Advanced
- Target Audience: Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers, and Security Architects
- Delivery Method: Discussion
- Outcome: This engagement focuses on educating new and existing customers on Provisioned Throughput Units (PTUs) with AI. It covers the benefits and process of adopting PTUs with models in AOSI, providing a comprehensive understanding of PTUs and the optimization process.


**[Azure Proactive Resiliency Library v2 (APRL) for AI workloads](https://azure.github.io/Azure-Proactive-Resiliency-Library-v2/azure-specialized-workloads/ai/)** 


- Level: Intermediate
- Target Audience: Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers, and Security Architects
- Delivery Method: Discussion / Guidance
- Outcome: APRL provides a curated catalog of resiliency recommendations for workloads running in Azure. It includes supporting Azure Resource Graph (ARG) queries to identify non-compliant resources, ensuring that AI deployments are resilient and compliant.

**[Solution Optimization for AI Apps & Agents ](https://esxp.microsoft.com/#/omexplanding/services/15448/geo/FRA/details/3)** 

- Level: Intermediate
- Target Audience: Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers, and Security Architects
- Delivery Method: Discussion / Guidance
- Outcome: This engagement focuses on optimizing AI applications and agents by improving response time, throughput, and system availability. It includes strategies for caching, autoscaling, and failover, ensuring that AI solutions are efficient and resilient.

**[PTU-M Migration Guidance for AI Workloads ](https://aka.ms/DATAAI-IP/AOAI-PTUMMigration)**

- Level: Intermediate 
- Target Audience: Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers, and Security Architects
- Delivery Method: Discussion / Guidance
- Outcome: PTU-M Migration Guidance provides tools and processes needed to migrate PayGo to PTU-M, PTU-C to PTU-M, and performance considerations. It ensures that AI deployments are optimized for performance, providing a comprehensive understanding of PTUs and the optimization process.

**[Azure AI Benchmarking Tool for AI Workloads  ](https://aka.ms/ImprovedAOAIBenchmarkingTool)** 

- Level: Intermediate 
- Target Audience: Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers, and Security Architects 
- Delivery Method: Discussion / Hands-on 
- Outcome: The Azure AI benchmarking tool provides a simple way to run test traffic on deployments, validate the throughput for traffic workloads, and gather essential performance statistics like average and 95th percentile latencies, along with deployment utilization metrics. This ensures that AI deployments are optimized for performance and can handle the expected load efficiently.

### Governance

Encompassing Resource Organization, Tagging, and Role-Based Access Control (RBAC), is essential for structured resource management, traceability, and regulated access, ensuring compliance and accountability. The goal of this Pillar is to provide a comprehensive approach to managing AI resources, ensuring compliance and accountability through structured resource management.

A large amount of governance including Policy and RBAC is implemented pre-deployment. This guidance can be found by following the [AI Landing Zone Checklist](https://github.com/Azure/review-checklists/tree/main) for a more technical approach and the [Technical Assessment for Generative AI in Azure](https://learn.microsoft.com/assessments/443670b4-11d1-4dd7-8128-b2bdb7a2bf2f/) for a more strategic approach. Both of these assessments and more are found in the [GO-LIVE assessment VBD](https://aka.ms/golivefy26) in the customers AI path to production. 


**[AI Scalability and Governance Implementation](https://microsoft.sharepoint.com/:w:/r/sites/AIScalabilityGovernanceCatalogExtension/_layouts/15/Doc.aspx?sourcedoc=%7B2BB79715-5C36-401A-9766-B53AC7DFDB88%7D&file=AI%20Scalability%20and%20Governance%20Implementation%20Guide%20V2.0.docx&action=default&mobileredirect=true&DefaultItemOpen=1&wdLOR=cB3DDBFC8-95B4-4D75-8490-2133B90B1C20)** 

This guide includes post-deployment best practices for AI workloads.
- Level: Intermediate/Advanced 
- Cost governance via Azure Budgets and CLI-based alerts
- CI/CD pipelines for infrastructure and ML code
- Blue/green and canary deployments for model updates
- Dev/test environments using IaC for safe experimentation

**AI Gateway With API Management for AI Workloads**

- Level: Intermediate/Advanced 
- Target Audience: Project Manager, Application Architects, Data Scientists, API Developers, Infrastructure Architects, Application testers, and Security Architects 
- Delivery Method: Discussion/Hands-on 
- Outcome: Implement an AI Gateway using API Management (APIM) for secure keyless access to large language models (LLMs), prompt caching to enhance response time, manage AI costs with token limits, track tokens, and block harmful content, including prompts that align with attack patterns or specific blocklists. This ensures that AI deployments are secure, efficient, and compliant with governance policies.

Leverage [AI Gateway Accelerator](https://github.com/Azure/apim-landing-zone-accelerator/blob/wip/apim-lza/scenarios/workload-genai/README.md) implementing the gateway with Azure API Management provisioned in a secure baseline and AI policies configured to handle the below scenarios
- [Load balancing (round-robin)](https://github.com/Azure/apim-landing-zone-accelerator/blob/wip/apim-lza/scenarios/workload-genai/policies/fragments/load-balancing/README.md) - Load balance traffic across PAYG endpoints using simple and weighted round-robin algorithm.
- [Managing spikes with PAYG](https://github.com/Azure/apim-landing-zone-accelerator/blob/wip/apim-lza/scenarios/workload-genai/policies/fragments/manage-spikes-with-payg/README.md) - Manage spikes in traffic by routing traffic to PAYG endpoints when a PTU is out of capacity.
- [Adaptive rate limiting](https://github.com/Azure/apim-landing-zone-accelerator/blob/wip/apim-lza/scenarios/workload-genai/policies/fragments/rate-limiting/README.md) - Dynamically adjust rate-limits applied to different workloads
- [Tracking token usage](https://github.com/Azure/apim-landing-zone-accelerator/blob/wip/apim-lza/scenarios/workload-genai/policies/fragments/usage-tracking/README.md) - Record the token consumption for usage tracking and attribution
- [Multi-tenancy](https://github.com/Azure/apim-landing-zone-accelerator/blob/wip/apim-lza/scenarios/workload-genai/policies/multi-tenancy/README.md) - Implementing multi-tenancy using Products and Product Policies

For customers looking for individual walkthrough of API Management AI policies, leverage the [AI Gateway labs](https://azure-samples.github.io/AI-Gateway/)

Here are some helpful links for customers looking to learn more and walk through labs on these topics:
- Realtime API (Audio and Text) with Azure OpenAI experiments with the [AOAI Realtime](https://github.com/Azure-Samples/AI-Gateway/blob/main/labs/realtime-audio/realtime-audio.ipynb)
- Model Context Protocol (MCP) experiments with the [client authorization flow](https://github.com/Azure-Samples/AI-Gateway/blob/main/labs/mcp-client-authorization/mcp-client-authorization.ipynb)
- Agentic experiments with [Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-foundry)
- [Model routing](https://github.com/Azure-Samples/AI-Gateway/blob/main/labs/model-routing/model-routing.ipynb) lab with OpenAI model based routing.
- [Function calling](https://github.com/Azure-Samples/AI-Gateway/blob/main/labs/function-calling/function-calling.ipynb) lab with a sample API on Azure Functions.

In the context of governance, Model DevOps ensures robust oversight of AI model development and deployment processes. This includes managing Azure Kubernetes Service (AKS) and Azure Container Apps (ACA) deployments, enforcing best practices throughout the model lifecycle via CI/CD pipelines, and utilizing infrastructure as code for consistency and auditability. Model DevOps also promotes collaboration between application and AI teams, supporting effective governance, compliance, and operational alignment across the organization.

### Security

Network isolation, policy enforcement, identity management, and data protection all work together to ensure that AI environments are secure.

As AI adoption accelerates across industries, securing AI systems post-deployment is no longer optional—it’s foundational. The security pillar of Solution Optimization for AI ensures that AI environments are resilient, compliant, and protected against evolving threats. This section outlines the key security considerations and capabilities that must be integrated into every AI solution to safeguard data, models, and infrastructure

- Level: Intermediate Advance
- Target Audience: Project Sponsor and Project Manager, Application Architects, Data Scientists, Infrastructure Architects, Application testers, and Security Architects
- Delivery Method: Discussion / Guidance
- Outcome: This engagement focuses on providing a comprehensive security review and optimization of AI implementation based on architectural patterns, WAF & CAF security best practices, Microsoft Defender for Cloud and Purview features for AI, Microsoft Cloud Security Benchmark to optimize an AI solution for security.

**Architectural Review**
- Review with customer if they require [custom authentication to Azure OpenAI Service through a gateway](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/azure-openai-gateway-custom-authentication)
- Review with customer if they are using several [data source for their RAG inferencing solution and how they are securing it](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/secure-multitenant-rag).
- For customers requiring adherence to regulatory compliance or strict security requirements, [review guidance on how to secure for regulated data](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/secure-compute-for-research).

**WAF Security**
- Leverage the [Design principles, Checklist, Tradeoffs and Recommendations in Well-Architected Framework Security Pillar](https://learn.microsoft.com/en-us/azure/well-architected/security/) to ensure alignment to security best practices in general.
- Leverage the guidance in [Well-Architected Framework Service guides](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/?product=popular) focusing on the security pillar of AI services and other Azure services that make up the workload for a more targeted review.

**CAF Security**
- Leverage the guidance in Secure AI stage of [Cloud Adoption Framework AI Adoption Scenario](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/secure) to discover AI security risks,  protect AI resource and data, detect AI security threats.

**Microsoft Defender for Cloud**
- Use the [Data and AI security dashboard](https://learn.microsoft.com/en-us/azure/defender-for-cloud/data-aware-security-dashboard-overview) which provides a centralized platform to monitor and manage data and AI resources, their associated risks, and protection status.
- Improve the AI security posture management by leveraging the [Defender Cloud Security Posture Management (CSPM) plan in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture).
- Analyze the [Recommendation for AI Security](https://learn.microsoft.com/en-us/azure/defender-for-cloud/recommendations-reference-ai) in the Azure portal and plan for remediation of high severity ones.
- Analyze and respond to [alerts for AI services](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads) in the Azure portal that might come from AI services from Microsoft Defender for Cloud and any Microsoft Defender plans enabled.
- [Enable threat protection for AI services](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection) and gain application and end-user context for identifying threats to generative AI applications in real time and respond to security issues.
- [Discover generative AI workloads](https://learn.microsoft.com/en-us/azure/defender-for-cloud/identify-ai-workload-model) which provides a comprehensive view of your organization's AI Bill of Materials (AI BOM).  
- Improve the [security posture of generative AI apps](https://learn.microsoft.com/en-us/azure/defender-for-cloud/explore-ai-risk), by identifying vulnerabilities in generative AI libraries that exist in your AI artifacts such as container images and code repositories.

**Microsoft Purview**
- Enable Microsoft Purview data security and compliance protections for generative AI apps using [Data Security Posture Management (DSPM) for AI](https://learn.microsoft.com/en-us/purview/ai-microsoft-purview) in Purview

**Microsoft Cloud Security Benchmark**
- Ensure alignment to [security baselines for Azure](https://learn.microsoft.com/en-us/security/benchmark/azure/security-baselines-overview) services particular of the AI services.

**Complete Accreditation**
- An assesment is available to help reinforce key concepts. This assesment consists of 25 questions. You will have a total of 60 minutes to respond. The Minimum score to be sucessful on this assesment is 80%.

| Type of Accredition | Accredition Link |
| ----------------- | ----------------- |
| Solution Optimization for AI Apps & Agents | **[Complete Accreditation](https://learningplayer.microsoft.com/activity/successfactors/s9275755/launch)** |

## Resources, Readiness and References

The below documentation can assist you and customer by providing valuable information and references:

- [Azure AI Architecture Patterns and implementation steps](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-architecture-patterns-and-implementation-steps/ba-p/3979934)
- [Create Azure API Management instance - Bicep | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/quickstart-bicep?tabs=CLI)
- [Import and publish your first API in Azure API Management | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish)
- [Policies in Azure API Management | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-policies)


