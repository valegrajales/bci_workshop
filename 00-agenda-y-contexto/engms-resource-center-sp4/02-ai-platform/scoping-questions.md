# Scoping Questions for Innovate with AI VBDs 

To ensure the success of our Innovate with AI engagements, it is essential to define and understand the scope clearly. The following questions will guide you through the critical considerations.  Please adjust this list to meet your needs and provide feedback to the team if you have suggestions for updates. 

These scoping questions are intended to be used with the Innovate with AI VBDs.

## Use Case Selection and General Readiness: 
- **Business use case(s)**
  - What are the top scenarios or use cases you want to achieve? 
    - If multiple, is there a priority ranking? 
  - Who are the intended users and stakeholders?
  - What will be the impact if you achieve success? 
  - How will you measure success? (Metrics, feedback surveys, etc.) 

- **Project Journey**
  - Where are you currently in the project flow? (Idea Generation, Concept Development, Technical Exploration, Detailed Design, Build, Testing, Launch, Post-Launch Support)
  - What previous steps have you taken? (e.g., user requirements workshop, POC, landing zone review)
  - What learning or skilling have you had related to this use case?

- **Team Familiarity**
  - Describe teams experience with below topics.
  - General Azure topics (portal, subscriptions, resource groups, permissions)
  - Specific Azure resources (App Service, Functions, SQL, Cosmos, Monitor, AKS)
  - General AI topics (LLMs, models, tokens, embeddings, prompts, agents)
  - Azure AI tools (Azure OpenAI, AI Studio, Playground Chat, Machine Learning Studio, Prompt Flow)
  - AI frameworks (langchain, semantic kernel, autogen)
  - Programming languages (Python, .NET, Java, etc.)
  - Development tools (git, VS Code, Docker, CI/CD tools)
   
- **Current Azure Environment**
  - Describe your current Azure environment (subscriptions, resource groups, deployed resource types, landing zones, virtual networking, etc.)

  
## Building a reliable AI app (Compute / Front End) 
  - What is the expected user load and usage patterns?
    - How many users?
    - What is their expected interaction level? (Daily, weekly, etc.)
    - Are there any expected patterns of high and low usage?
  - Should the system respond automatically to those patterns by scaling in and out as needed? (Or is manual scaling sufficient?)
  - Are there any specific performance benchmarks or metrics that the application must meet under varying loads?
  - What are the uptime requirements for the application?
    - Are there any SLAs or SLOs that your organization needs to meet for this application?
  - What level of fault tolerance is required for the application?
  - How critical is it for the application to maintain functionality during partial failures?
  - Does your organization currently use a microservices or other pattern for developing applications?
  - Is your organization familiar with containers and orchestrators?  (Like Docker and Kubernetes.)
  - Do you have a current practice of load and stress testing?
    - Will we need this type of testing for this application?
  - Do you have a preference of app hosting environment? (App Services, Container Apps, AKS, VMs, ...)
  
## Data management and ingestion 
- With what data will the AI solution be interacting? 
  - Policy documents, sales data, knowledge base articles, case details, … 
- Is this data all text or also includes images or videos?
- Should users be able to use the LLMs internal knowledge to generate answers?
- Should users be able to use live web searches to generate answers?
- Where is that data currently stored? 
  - SharePoint, Azure SQL, Postgress, … 
  - On Prem, Azure, another cloud 
- What is the format of the data? 
  - Structured: Database, JSON, or CSV file 
  - Unstructured: Notes, documents, images, power points 
  - Mix: Database with a free form notes field.  Documents with internal tables. 
- Is the data version controlled?
- What is the sensitivity or classification of that data?   
  - Does it contain PII, PHI, CJIS, IRS1075, PCI or other regulated data? 
- Does it need to be stored/processed in a particular cloud environment or geographic region? 
- Does the data change often or is semi-static? 
  - How often does it change? 
- How often will the data the AI is using need to be refreshed.   
- Does it need to be refreshed automatically (vs. manually)? 

## Implementing orchestration: 
- Is your team familiar with orchestration frameworks such as semantic kernel or langchain?
  - Do you have an existing preference for one? 
  - Do you have any existing orchestration tools or frameworks that you would like to integrate with or replace?
- Do you need to manage complex workflows involving multiple AI models or services?
- Do you need to support support dynamic task execution and chaining?
- Do you require the ability to integrate with external APIs or services?
- Are there specific data sources or types of data that need to be orchestrated in a particular way?
- Do you need built-in support for error handling and retries?
- Do you need to support both synchronous and asynchronous operations?

## Prompt Development, Engineering and Evaluation: 
- Does the team have familiarity with prompt engineering?
- Will the users be able to set and store their own self defined prompts, aka personas?
- Does the team have familiarity with prompt evaluations?
- What are some typical interactions we expect from users?
- Will we have access to Subject Matter Experts?
- For quesiton/answer type systems can those SMEs help evaluate generated answers and craft "known good answers" to a select set of questions?
- Should the application collect user feedback about the interactions?
  - Should we use that feedback to improve the system over time?  Who will be responsble for this task?

## DevOps and Continuous Testing: 
- What infrastructure will be used to support the development and deployment of the application?
- What level of automation is required for build, deployment, and monitoring processes?
- Are there specific tools or platforms that the team prefers for continuous integration and continuous deployment (CI/CD)?
- Are there any specific practices or methodologies (e.g., Agile, Scrum) that the team will follow?
- Do you already have systems or approaches for managing the application's configuration across different environments (dev/test/prod)?
- What version control systems will be used to track changes to the application's code and configuration?
- Does your team currently practice infrastructure as Code?
  - If yes, what tools do you use? (bicep, terraform, ...)
  - If not, do you intend to adopt it for this project?
- Are you currently using any particular application testing tools?
- Is automated functional testing a goal of this project?
  - Integrated into the CI/CD pipelines or on demand?

## Security and Monitoring: 
### Security
- What security measures are currently in place for your cloud applications?
  - Have you done any security assessments to check if these measures are aligned with industry standards and best practices?
- How familiar is your team with Responsible AI and securing AI applications specifically?
- Are there any regulatory compliance requirements that your AI application must meet? (e.g., GDPR, HIPAA)
- Are there any specific security frameworks or standards that your organization follows (e.g., NIST, ISO 27001)?
- What identity and access management (IAM) solutions are you currently using?
  - Do you use multi-factor authentication (MFA) for accessing cloud resources?
- How do you handle secrets management (e.g., API keys, passwords)?
- Do you have a process for regular security audits and vulnerability assessments?
- Are you using any specific tools for monitoring and logging security events?
- How do you plan to handle incident response and remediation for security breaches?
- What is your approach to securing the development lifecycle (e.g., secure coding practices, code reviews)?
- Do you have a dedicated security team or personnel responsible for cloud and AI application security?
- Are there any specific security challenges you have faced or anticipate facing with your AI application?
### Monitoring
- What tools are you currently using for monitoring your cloud applications?
  - Are you currently using any observability platforms (e.g., Azure Monitor, Prometheus, Grafana)?
  - Are these tools capable of monitoring AI-specific metrics and performance?
- How do you handle logging and log management for your applications?
  - Do you have centralized logging in place?
- How do you currently handle anomaly detection and incident response?
- Do you have any existing dashboards or reports for monitoring application performance?
- How familiar is your team with setting up and configuring monitoring for AI applications?
- What metrics are most important for you to monitor in your AI applications?
  - Generation quality metrics (e.g., accuracy, groundedness)
  - Performance metrics (latency, requests/sec)?
  - Risk and Safety (violence, hateful content)
- Are you familiar with monitoring tools specific to AI, such as Azure Open AI Studio Metrics?

## Managing performance, cost and consumption: 
- How do you currently monitor and manage the performance of your cloud applications?
- Are there specific performance metrics that you track regularly?
- How do you currently manage resource consumption for your applications?
  - Do you have automated processes for scaling resources up and down based on demand?
- What tools or platforms do you use for cost management and optimization in your cloud environment?
  - Are you familiar with Azure Cost Management and Budgets?
- How do you handle cost allocation and chargeback within your organization?
- Are you familiar with the cost implications of different AI model types and sizes?
- Do you have any existing budgets or cost constraints for this AI project?
- Do you have any experience with reserved instances or savings plans to reduce costs?
- Are there any specific challenges you have faced or anticipate facing in managing the performance, cost, and consumption of your AI applications?