<!-- TODO: once we have the use cases created/delivered I think it would be great to come back to this and align specific learning based on use case to facilitate an easier ramp up before a delivery -->

# Elevate your AI Apps with App Dev Hackathon​ - Tools Overview 

This guide will cover the topics used in the hackathon and provide preparation material to facilitate the delivery. There are many technologies in the breadth of AI apps, so it can help to **target your learning based on the use case** your customer selects or brings for the hackathon. 

For a successful delivery you need to be familiar with Azure AI Services, Azure OpenAI, and prompt engineering. 


### Prerequisites
Before you start, make sure you have:
- An Azure account
- An Azure OpenAI resource with a model deployed: [Deployment Guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)

## 1. Azure OpenAI

**Azure OpenAI** is a service on Microsoft Azure that provides access to OpenAI's powerful language models, like **GPT-4**. It allows businesses and developers to integrate advanced AI capabilities, such as natural language processing, into their applications through the cloud, benefiting from Azure's security and scalability.

The GPT models from OpenAI work by responding to user input, called a **prompt**, with a generated text response. These models are powerful but highly dependent on the prompt's wording, so learning how to craft effective prompts is important for getting the best results. This is known as **prompt engineering**. 

Azure OpenAI services supports *using your own data*, which is a common ask from customers. The **RAG** (**R**etrieval-**A**ugmented **G**eneration) pattern in AI combines finding relevant information with generating answers. It first pulls in specific data related to a question, then uses an AI model to create a response that includes that data. This makes the AI's answers more accurate and informative.

### Learning Resources:
- Official [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- The quickstart for chat and completions using AI studio is a good place to begin:
    - [Azure OpenAI Chat quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart)
    - [Azure OpenAI Completions quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart)
    - I recommend at least building a console app to chat with your model in a language you're comfortable in. 
- Familiarize yourself with *Prompt Engineering*:
    - [Introduction to prompt engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)
    - [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)   
- [RAG quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/use-your-data-quickstart)

## 2. Azure AI Services

Azure AI Services encompass many technologies, such as: 

**Azure Speech Services**
Provides tools to convert spoken language into text, generate speech from text, translate spoken language in real-time, and recognize individual speakers, enabling seamless voice interactions and multilingual communication.

**Azure Language Services**
Offers capabilities to analyze text for sentiment and key information, build natural language understanding into applications, translate text across languages, and create Q&A systems, enhancing communication and content comprehension.

**Azure Vision Services**
Enables image and video analysis to detect objects, faces, and text, extract structured data from documents, and build custom image classification models, facilitating advanced visual content understanding and processing.

**Azure Translator**
Delivers real-time text and document translation across multiple languages, facilitating multilingual communication and content localization with support for a wide range of languages.

### Learning Resources **Azure Speech Services**:
- Official [AI Speech Overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview)
- Official [Speech Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)
- Official [Speech Studio Documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-studio-overview)
- Quickstart [Speech to Text](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text)
- Quickstart [Text to Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-text-to-speech)
- Useful reference for [Speech SDK](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-sdk)

### Learning Resources **Azure Language Services**:
- Official [AI Language Overview](https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview)
- Official [Language Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/language-service/)
- Quickstart [Get started with Language Studio](https://learn.microsoft.com/en-us/azure/ai-services/language-service/language-studio)
- Quickstart [Conversational language understanding](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/quickstart)
- Quickstart [Custom text classification](https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-text-classification/quickstart)
- Quickstart [Custom named entity recognition](https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-named-entity-recognition/quickstart)
- Quickstart [Orchestration workflow](https://learn.microsoft.com/en-us/azure/ai-services/language-service/orchestration-workflow/quickstart)
- Useful reference for [Language SDK](https://learn.microsoft.com/en-us/azure/ai-services/language-service/concepts/developer-guide)

### Learning Resources **Azure Vision Services**:
- Official [AI Vision Overview](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview)
- Official [Vision Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- Reference for new features or chances in AI Vision: [What's new in Azure AI Vision](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/whats-new)
- Get started with Vision Studio: [Vision Studio](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-vision-studio)
- Quickstart [Azure AI Vision OCR](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/client-library)
- Quickstart [Use the Face service](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/identity-client-library)
- Quickstart [Image Analysis 4.0](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40)


### Learning Resources **Azure Translator**:
- Official [AI Translator Overview](https://learn.microsoft.com/en-us/azure/ai-services/translator/translator-overview)
- Official [Translator Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/translator/)
- Quickstart [Translator Studio Preview](https://learn.microsoft.com/en-us/azure/ai-services/translator/document-translation/language-studio)
- Quickstart [Azure AI Translator client libraries (preview)](https://learn.microsoft.com/en-us/azure/ai-services/translator/quickstart-text-sdk?pivots=programming-language-csharp)
- Quickstart [Document Translation client libraries](https://learn.microsoft.com/en-us/azure/ai-services/translator/document-translation/quickstarts/client-library-sdks)

## 3. Learning By Use Case

### Learning Resources: Use Case 1:  Getting started with AI Agents

- [Create AI Agents with Azure OpenAI and Semantic Kernel](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-azure-open-ai-semantic-kernel-sdk/) 
- [Azure OpenAI Function Calling Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling)
- Github [Open AI SDK](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/openai/Azure.AI.OpenAI)
- Github [Open AI Samples](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/openai/Azure.AI.OpenAI/tests/Samples)
- Github Sample [Use Assistants and stream a run](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/openai/Azure.AI.OpenAI#use-assistants-and-stream-a-run)
- [Github Examples](https://github.com/openai/openai-dotnet/tree/main/examples)

### Learning Resources: Use Case 1.1 Explore Azure AI Studio Chat Playground

- [Quickstart: Get started using GPT-35-Turbo and GPT-4 with Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line%2Cpython-new&pivots=programming-language-studio)
- [Quickstart: Chat with Azure OpenAI models using your own data](https://learn.microsoft.com/en-us/azure/ai-services/openai/use-your-data-quickstart?tabs=command-line%2Cpython-new&pivots=programming-language-studio)

### Learning Resources: Use Case 2: Implement and deploy AI Agents with Azure Functions OpenAI Extension

- [Github OpenAI Chat Sample](https://github.com/Azure/azure-functions-openai-extension/tree/main/samples/chat)
- [Github OpenAI Assistant Sample](https://github.com/Azure/azure-functions-openai-extension/tree/main/samples/assistant)

### Learning Resources: Use Case 3: Implement AI Agents based on Azure OpenAI Assistants API

- [Quickstart: Get started using Azure OpenAI Assistants (Preview)](https://learn.microsoft.com/en-us/azure/ai-services/openai/assistants-quickstart?tabs=command-line%2Ctypescript&pivots=programming-language-csharp)
- [Azure OpenAI Assistants API (Preview)](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/assistants )

### Learning Resources: Use Case 3.1: Explore Azure OpenAI Assistants Playground in Azure AI Studio

- [Quickstart: Get started using Azure OpenAI Assistants (Preview)](https://learn.microsoft.com/en-us/azure/ai-services/openai/assistants-quickstart?tabs=command-line%2Ctypescript&pivots=programming-language-studio)

### Learning Resources: Use Case 3.2:  Use Azure Logic Apps as OpenAI Functions for the OpenAI Assistants API

- [](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/assistants-logic-apps)

### Learning Resources: Use Case 3.3: Create serverless and custom container Code Interpreter sessions in Azure

- [Call Azure Logic apps as functions using Azure OpenAI Assistants](https://learn.microsoft.com/en-us/azure/container-apps/sessions?tabs=azure-cli)
- [Azure Container Apps dynamic sessions overview](https://learn.microsoft.com/en-us/azure/container-apps/sessions-tutorial-semantic-kernel)
- [Tutorial: Use code interpreter sessions in Semantic Kernel with Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/sessions-custom-container?tabs=azure-cli)


### Learning Resources: Use Case 4: Implement RAG pattern with Azure AI Search

- [Azure Container Apps custom container sessions (preview)](https://github.com/Azure-Samples/azure-search-openai-demo)
- [](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator)


### Learning Resources: Use Case 5: Implement RAG pattern with Cosmos DB

- [Github Azure OpenAI Search Demo](https://learn.microsoft.com/en-us/samples/azurecosmosdb/cosmosdb-nosql-copilot/ai-samples/)
- [Github Chat With Your Data Solution Accelerator](https://learn.microsoft.com/en-us/training/modules/build-chat-bot-azure-cosmos-db-openai-blazor/)


### Learning Resources: Use Case 6: Implement Semantic Caching with Azure API Management

- [Enable semantic caching for Azure OpenAI APIs in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/azure-openai-enable-semantic-caching)

### Learning Resources: Use Case 7: 7. Organization-wide provisioning and monitoring of OpenAI Provisioned Throughput Unit (PTU) deployments with API Management

- [Azure OpenAI Landing Zone reference architecture](https://techcommunity.microsoft.com/t5/azure-architecture-blog/azure-openai-landing-zone-reference-architecture/ba-p/3882102)
- [GenAI gateway reference architecture using APIM](https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/dev-starters/genai-gateway/reference-architectures/apim-based)
- [Introducing GenAI Gateway Capabilities in Azure API Management](https://techcommunity.microsoft.com/t5/azure-integration-services-blog/introducing-genai-gateway-capabilities-in-azure-api-management/ba-p/4146525)
- [Manage your Generative AI APIs with Azure API Management and Azure Open AI](https://techcommunity.microsoft.com/t5/apps-on-azure-blog/manage-your-generative-ai-apis-with-azure-api-management-and/ba-p/4214178)
- [Github OpenAI Labs For GenAI Gateway](https://github.com/Azure-Samples/AI-Gateway)

## Finally
After identifying your customer's use case and completing the necessary learning on the relevant AI services, you will be well-prepared to effectively lead the hackathon event.

<!--I think it could be good to expand this section in the future if we have more first hand experience tips for the delivery -->
