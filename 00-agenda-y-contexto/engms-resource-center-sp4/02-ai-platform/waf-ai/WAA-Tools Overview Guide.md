# VBD - Well-Architected Assessment for Azure AI - AI Tools Overview

## Overview

This guide provides an overview of the primary tools and platforms available to support Azure AI workload assessments, evaluation, deployment, and responsible AI implementation. These tools are designed to help organizations assess their AI readiness, develop and test AI applications, and ensure responsible and ethical AI practices.

### Key Use Cases for Assessment Delivery

- **Pre-assessment**: Understanding current AI infrastructure and readiness
- **During assessment**: Evaluating AI workload architecture and best practices
- **Post-assessment**: Testing, evaluation, and monitoring of AI solutions
- **Implementation**: Building and deploying AI applications aligned with recommendations

---

## Microsoft Foundry (formerly Azure AI Foundry)

### Overview
[Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-foundry) is the central platform for designing, customizing, managing, and supporting AI applications and agents at scale. It provides an integrated environment for the entire AI development lifecycle.

### Key Capabilities
- **Project Management**: Organize and manage AI projects with collaborative tools
- **Model Catalog**: Browse, deploy, and manage foundation models (GPT-5, GPT-5-mini, o3-mini, specialized models). See Foundry models (sold directly by Azure): [gpt-5](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure#gpt-5), [gpt-5.1](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure#gpt-51), [gpt-5.2](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure#gpt-52).
- **Chat Playground**: Interactive interface to test and refine prompts before deployment
- **Evaluation Tools**: Assess model performance using built-in and custom metrics
- **Prompt Flow**: Visual workflow builder for developing LLM-based applications
- **RAG Integration**: Retrieval-Augmented Generation support for grounding prompts with customer data
- **Fine-tuning**: Customize models for domain-specific tasks
- **Model Monitoring**: Track deployment health, token usage, and model performance
 - **Guardrails**: Configure safety and policy guardrails

### Recommended Models for Assessment Report Generation
- **gpt-5**: GA; recommended for production report generation (limited-access registration required)
- **gpt-5-mini**: Cost-optimized alternative; no access request needed
- **gpt-5-nano**: Most cost-effective option for simple report generation; no access request needed
- **gpt-5.1-chat** (Preview): Chat-focused; preview/pilot-only; avoid production; no access request needed
- **gpt-5.2-chat** (Preview): Latest preview; preview/pilot-only; avoid production; no access request needed

Note: Confirm GA/preview status and retirement timelines in the "Current models" table. Avoid hard-coding version numbers in documentation; pin versions in deployment configuration and re-validate periodically via Microsoft Learn.

### Assessment Use
Use Microsoft Foundry to:
- Demonstrate current AI platform capabilities to customers
- Test assessment data with sample prompts
- Evaluate model performance for specific workload scenarios
- Build proof-of-concept AI solutions aligned with customer needs

---

## Azure OpenAI Service

### Overview
[Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/overview) provides access to OpenAI's language models via a managed service in Azure, with enterprise-grade security and compliance.

### Key Capabilities
- **Model Access**: Deploy specific model versions with guaranteed availability
- **Playground**: Browser-based interface for interactive model testing
- **Deployment Management**: Create and manage dedicated model endpoints
- **Content Filters**: Implement safety guidelines and content filtering
- **Fine-tuning**: Train custom models on customer data
- **Rate Limiting & Quota Management**: Control resource usage and costs
- **Audit Logging**: Track all API calls and model interactions

### Integration with Assessment
- Can optionally be used to help draft summaries and recommendations for the customer report
- Supports evaluation of customer-specific workload scenarios
- Enables creation of targeted recommendations based on model outputs

### Recommended Configuration for Assessment Reporting
- **Primary Model**: gpt-5 for general assessments and production report generation (limited-access registration required)
- **Cost-Optimized**: gpt-5-mini for bulk processing and large evaluations (no access request needed)
- **Fastest Setup**: gpt-5-mini or gpt-5-nano (no access request required)
- **Preview / Pilot**: gpt-5.2-chat (Preview) and gpt-5.1-chat (Preview) for trial evaluations; avoid production
- **Access Notes**:
	- gpt-5 and gpt-5-codex require limited-access registration
	- gpt-5-pro requires limited-access registration
	- gpt-5-mini, gpt-5-nano, and gpt-5-chat do not require registration
	- gpt-5.1 and gpt-5.1-codex families require limited-access registration; gpt-5.1-chat (Preview) does not require registration; avoid production
	- gpt-5.2 requires limited-access registration; gpt-5.2-chat (Preview) does not require registration; avoid production
	- Apply via the Limited Access Model application: https://aka.ms/oai/gpt5access; see overview: https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/limited-access
- **Lifecycle**: For GA/preview status and dates, see Current models: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-retirements#current-models
- **Lifecycle Example**: For clarity, e.g., "gpt-5-chat retirement no earlier than 2026-03-01" (always check the Current models table for updates)
- **Deployment**: Use managed endpoints with auto-scaling for predictable performance

---

## Prompt Flow

### Overview
[Prompt Flow](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/get-started-prompt-flow) is a suite of development tools for streamlining the end-to-end development cycle of LLM-based AI applications—from prototyping and testing to deployment and monitoring.

### Key Components
1. **Visual Flow Designer**: Build complex LLM workflows without extensive coding
2. **Built-in Evaluators**: Pre-configured metrics (groundedness, relevance, coherence, fluency, similarity)
3. **Custom Evaluators**: Create task-specific evaluation logic using Prompty language
4. **Prompt Tracing**: Track inputs, outputs, and context of each prompt execution
5. **Batch Run & Evaluation**: Process large datasets and generate evaluation reports
6. **Deployment**: Convert flows into production APIs and managed endpoints

### Evaluation Metrics Supported
- **Groundedness**: How well generated answers align with source information
- **Relevance**: Pertinence of responses to questions
- **Coherence**: Smoothness and naturalness of language flow
- **Fluency**: Grammatical correctness and vocabulary usage
- **Similarity**: Alignment between generated and ground-truth responses

### Assessment Use
- Develop evaluation flows to test assessment quality
- Create batch evaluation pipelines for automated scoring
- Deploy assessment-related prompts as production services
- Monitor prompt performance and model output quality over time

---

## Responsible AI Dashboard

### Overview
The [Responsible AI Dashboard](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai-dashboard) brings together multiple responsible AI tools in a comprehensive interface for model evaluation, fairness assessment, and error analysis.

### Key Components

| Component | Purpose |
|-----------|---------|
| **Model Overview** | Aggregate assessment of model performance and prediction distribution |
| **Fairness Assessment** | Evaluate how model predictions affect different demographic groups |
| **Error Analysis** | Identify patterns and cohorts where model performance degrades |
| **Data Analysis** | Explore dataset distributions and identify representation issues |
| **Model Interpretability** | Understand which features drive model predictions (global and local) |
| **Counterfactual Analysis** | Identify minimum feature changes needed to alter model outcomes |
| **Causal Analysis** | Distinguish correlation from causation in data and model predictions |

### Assessment Use
- Evaluate AI workload fairness and bias risks
- Identify edge cases and error patterns in customer AI solutions
- Provide evidence-based recommendations for model improvements
- Support compliance and audit requirements for responsible AI

### Responsible AI PDF Scorecard
Generate exportable scorecards documenting:
- Model performance metrics
- Fairness assessments
- Feature importance and interpretability
- Compliance and audit readiness

---

## Azure Machine Learning Model Monitoring (Preview)

### Overview
[Model monitoring for generative AI applications (preview)](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-monitor-generative-ai-applications) provides observability and quality tracking for deployed LLM applications.

### Key Capabilities
- **Production Monitoring**: Track model performance metrics in live deployments
- **Data Drift Detection**: Identify when input data distributions change
- **Quality Metrics**: Monitor groundedness, relevance, coherence, fluency, and similarity
- **Alert Management**: Configure alerts for performance degradation
- **Trend Analysis**: Visualize performance changes over time
- **Integrations**: Connect with Azure Monitoring and Application Insights

### Assessment Use
- Provide recommendations for monitoring deployed AI solutions
- Establish quality baselines and SLOs for AI workloads
- Enable proactive issue identification and response

See also: Foundry monitoring guidance for prompt flow deployments: https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/monitor-quality-safety. Use AML Prompt Flow monitoring (preview) for application observability; use Foundry quality/safety monitoring guidance to complement Foundry-managed deployments.

---

## Azure AI Search

### Overview
[Azure AI Search](https://learn.microsoft.com/en-us/azure/search/) provides information retrieval at scale, supporting both traditional and generative search scenarios.

### Key Capabilities
- **Vector Search**: Semantic search using embeddings
- **Hybrid Search**: Combine vector and keyword search
- **Indexing**: Scalable data indexing for large document collections
- **Retrieval-Augmented Generation (RAG)**: Ground LLM prompts with customer data
- **Semantic Ranking**: Improve search relevance with AI-powered ranking
- **Integration with Azure OpenAI**: Seamlessly connect search results to LLM prompts

### Assessment Use
- Evaluate current search and data retrieval infrastructure
- Recommend RAG architectures for customer-specific use cases
- Design knowledge base indexing strategies for AI workloads

See also: Quickstart: Use agentic retrieval in Azure AI Search: https://learn.microsoft.com/en-us/azure/search/search-get-started-agentic-retrieval

---

## Well-Architected Framework for AI

### Overview
The [Well-Architected Framework - AI](https://learn.microsoft.com/en-us/azure/well-architected/ai/get-started) provides design principles and best practices for building reliable, secure, and efficient AI workloads on Azure.

### Key Pillars
1. **Reliability**: Ensuring AI systems perform consistently and recover from failures
2. **Security**: Protecting AI systems from unauthorized access and misuse
3. **Cost Optimization**: Efficient resource utilization and cost management
4. **Operational Excellence**: Monitoring, automation, and incident response
5. **Performance Efficiency**: Optimizing compute and latency for AI workloads
6. **Responsible AI**: Ensuring fairness, transparency, and ethical AI practices

### Assessment Use
- Benchmark customer AI workloads against Well-Architected principles
- Identify gaps and provide targeted recommendations
- Link assessment findings to architectural improvements

---

## Reference Architectures & Learning Resources

### Official Microsoft References
- [Azure AI Architecture Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/):  Curated patterns for common AI scenarios (RAG, Agents, Evaluation, etc.)
- [Azure AI Services Decision Tree](https://learn.microsoft.com/en-us/azure/ai-services/): Guidance on selecting the right AI service
- [Generative AI Operations (GenAIOps) Maturity Model](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/concept-llmops-maturity): Framework for assessing and improving LLM operations practices
- [RAG Solution Design & Evaluation Guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide): End-to-end design and evaluation guidance for RAG workloads

### Learning Paths
- [Copilot Foundations](https://learn.microsoft.com/en-us/training/paths/copilot-foundations/): Current learning path aligned to Microsoft Foundry
- [Responsible AI Fundamentals](https://learn.microsoft.com/en-us/training/paths/responsible-ai-business-principles/): Ethical and responsible AI practices
 - [Operationalize AI responsibly with Azure AI Foundry](https://learn.microsoft.com/en-us/training/paths/operationalize-ai-responsibly/): Foundry guardrails and risk mitigation

---

## Assessment Platform: Microsoft Assessments

### Overview
The [Microsoft Assessments](https://learn.microsoft.com/en-us/assessments/) platform provides guided questionnaires and automated scoring for cloud and AI readiness.

### Key Features for AI Assessments
- **Structured Questionnaire**: Assessment questions aligned with Well-Architected Framework pillars
- **Automated Scoring**: Immediate calculation of capability scores (0-100 scale)
- **CSV Export**: Raw data export for custom reporting
- **Notes & Evidence**: Capture detailed rationale and customer context
- **Accessibility**: Cloud-based, browser-based interface; no installation required

### Assessment Workflow
1. **Day 1**: Conduct assessment interview using platform
2. **Day 2**: Export CSV and prepare initial findings
3. **Day 3**: Present recommendations aligned with assessment results

---

## Deployment and Operationalization Tools

### Prompt Flow Deployment
- **Managed Online Endpoints**: Deploy Prompt Flow applications as REST APIs
- **Container Deployment**: Package flows for Kubernetes or containerized environments
- **GitHub Integration**: CI/CD pipelines for automated deployment and testing

### Azure App Service / Container Apps
- Host custom AI applications and evaluation systems
- Auto-scaling for variable workloads
- Integration with Azure OpenAI and other AI services

### Azure DevOps & GitHub
- CI/CD pipelines for AI model and application deployment
- Integration with evaluation and monitoring systems
- Audit and compliance logging for deployments

---

## Security & Compliance Tools

### Azure Key Vault
- Secure storage of API keys and secrets
- Audit logging of all key access and usage

### Azure Private Link
- Private connectivity to Azure OpenAI and Azure AI services
- Prevent exposure to public internet

### Azure Policy & Governance
- Enforce responsible AI practices through policy
- Compliance with industry standards (HIPAA, SOC 2, etc.)

### Content Safety
- [Azure Content Safety Service](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/): Detect harmful content in AI model outputs

---

## Quick Reference: Tools by Assessment Phase

| Phase | Primary Tools | Secondary Tools |
|-------|---------------|-----------------|
| **Planning** | Microsoft Foundry (model catalog), Azure AI Search | Well-Architected Framework, Reference Architectures |
| **Assessment** | Microsoft Assessments Platform, Prompt Flow | Responsible AI Dashboard, Model Monitoring |
| **Evaluation** | Prompt Flow (evaluation flows), Responsible AI Dashboard | Azure OpenAI (testing), Content Safety |
| **Reporting** | Microsoft Assessments (CSV export), WAF AI Assessment summary deck (IP Share)| Responsible AI PDF Scorecard |
| **Recommendations** | Microsoft Foundry, Reference Architectures | GenAIOps Maturity Model, Learning Paths |
| **Deployment** | Prompt Flow (deployment), Azure App Service, GitHub | Azure OpenAI (inference), Azure AI Search (RAG) |
| **Monitoring** | Model Monitoring (preview), Application Insights | Content Safety, Responsible AI Dashboard |

---

## Resources & Links

- [Microsoft Foundry Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-foundry)
- [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/overview)
- [Prompt Flow Guide](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/get-started-prompt-flow)
- [Responsible AI Dashboard](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai-dashboard)
- [Responsible AI in Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-use-of-ai-overview)
- [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/)
- [Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
- [AI workloads on Azure (Well-Architected)](https://learn.microsoft.com/en-us/azure/well-architected/ai/get-started)
- [Well-Architected Framework AI workload assessment](https://learn.microsoft.com/en-us/azure/well-architected/ai/assessment)
- [GenAIOps Maturity Model](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/concept-llmops-maturity)
 - [Model Retirement Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-retirements)
 - [Current Models (GA/Preview status & dates)](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-retirements#current-models)
 - [Quickstart: Use agentic retrieval in Azure AI Search (Preferred)](https://learn.microsoft.com/en-us/azure/search/search-get-started-agentic-retrieval)
 - [Quickstart: Chat with Azure OpenAI Models Using Your Own Data (Secondary)](https://learn.microsoft.com/en-us/azure/ai-services/openai/use-your-data-quickstart)

