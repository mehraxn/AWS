# AWS AI and Machine Learning Service Recognition

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

This guide teaches service recognition, not machine-learning implementation. First identify whether the requirement calls for a ready-made AI capability, access to foundation models, or a custom machine-learning lifecycle.

AWS service names and AI guidance were checked on **2026-07-25**. AI outputs are probabilistic: accuracy, fairness, safety, latency, and suitability must be evaluated for the particular use case.

## AI and ML Foundations

- **Artificial intelligence (AI)** is the broad field of systems performing tasks associated with human intelligence.
- **Machine learning (ML)** learns patterns from data to make predictions or generate outputs rather than relying only on explicitly coded rules.
- **Deep learning** uses multilayer neural networks and supports many modern vision, speech, and generative systems.
- **Training** fits model parameters using data. **Inference** applies a trained model to new input.
- A **foundation model (FM)** is trained broadly and can be adapted to multiple tasks.
- A **large language model (LLM)** is a foundation model focused on understanding and generating language.
- A **prompt** supplies instructions and context for inference. A **token** is a unit a model processes; it is not necessarily a word.
- **Fine-tuning** changes a model using task-specific examples. It is different from prompting or retrieving external context.
- **Embeddings** represent content as numeric vectors so semantically related items can be found with vector search.

## Three Selection Layers

| Requirement | Typical choice |
|---|---|
| Add a ready-made capability such as transcription, translation, document extraction, or image analysis | A pretrained AI service |
| Build a generative-AI application using managed access to foundation models | Amazon Bedrock |
| Build, train, tune, deploy, and operate custom ML models with lifecycle control | Amazon SageMaker AI |

The next-generation **Amazon SageMaker** is a broader unified data, analytics, and AI platform. The original ML service was renamed **Amazon SageMaker AI** in 2024. This guide uses SageMaker AI when referring specifically to building, training, and deploying ML models.

## Generative AI Concepts

Generative AI produces new text, images, audio, code, or other content based on learned patterns and input context. Foundation-model output can be plausible but incorrect, incomplete, biased, unsafe, or unsupported. This failure mode is commonly called a **hallucination**.

### Retrieval-augmented generation

Retrieval-augmented generation (RAG) retrieves relevant information from a data source and adds it to the model's context before generation. A typical process is:

1. Split source documents into chunks.
2. Create embeddings and store them in a vector index.
3. Embed the user's question and retrieve similar chunks.
4. Add the retrieved context to the prompt.
5. Generate a response and, where supported, return source citations.

RAG can improve grounding and freshness, but it does not guarantee truth. Poor source data, permissions, chunking, retrieval, or prompts can still produce a wrong answer.

## Amazon Bedrock

Amazon Bedrock is a fully managed service for building generative-AI applications with foundation models. It provides model inference APIs and managed capabilities such as Knowledge Bases for RAG, Guardrails, model evaluation, agents, and supported customization methods.

Choose Bedrock when the team wants to build with existing foundation models without managing the underlying model-serving infrastructure. Model availability, features, Regions, context limits, and pricing change; consult the current documentation rather than memorizing a provider list.

Bedrock Guardrails can help filter or detect configured content categories and sensitive information. Guardrails are one control, not proof that every output is safe or accurate.

## Amazon SageMaker AI

Amazon SageMaker AI is a fully managed ML service for building, training, and deploying ML models. It supports notebooks and development environments, data preparation, training jobs, model evaluation, deployment endpoints, batch inference, monitoring, pipelines, and MLOps-related workflows.

Choose SageMaker AI when the requirement calls for custom model development, algorithm or framework control, training infrastructure, deployment choices, model monitoring, or an end-to-end ML lifecycle.

Bedrock and SageMaker AI are not mutually exclusive. An architecture can use Bedrock for foundation-model inference and SageMaker AI for custom models, evaluation, or other ML workloads.

## Pretrained AI Service Recognition

| Service | Input | Primary output or purpose | Recognition cue |
|---|---|---|---|
| [Amazon Rekognition](amazon-rekognition/01-overview.md) | Images or video | Labels, faces, moderation signals, and visual analysis | “Analyze what is in an image or video” |
| [Amazon Textract](amazon-textract/01-overview.md) | Scanned or digital documents | Text, forms, tables, queries, and document fields | “Extract structured data from invoices or forms” |
| [Amazon Comprehend](amazon-comprehend/01-overview.md) | Text or documents | NLP insights such as entities, key phrases, sentiment, and classification | “Understand or classify text” |
| [Amazon Translate](amazon-translate/01-overview.md) | Text | Translated text | “Convert one written language to another” |
| Amazon Transcribe | Audio | Speech converted to text | “Create a transcript or subtitles” |
| [Amazon Polly](amazon-polly/01-overview.md) | Text | Synthesized speech audio | “Read text aloud” |
| [Amazon Lex](amazon-lex/01-overview.md) | Voice or text utterances | Conversational intent and bot interaction | “Build a chatbot or voice bot” |
| [Amazon Kendra](amazon-kendra/01-overview.md) | Enterprise documents and queries | ML-powered enterprise search results | “Search organizational knowledge using natural language” |
| Amazon Personalize | Interaction and item data | Personalized recommendations or ranking | “Recommend products or content to each user” |

These services reduce the need to build a model from scratch, but customers still design application logic, permissions, data handling, testing, monitoring, and human review.

## Common Service Confusions

- **Rekognition vs Textract:** general visual analysis versus document text, forms, and tables.
- **Comprehend vs Translate:** analyze what text means versus convert text between languages.
- **Transcribe vs Polly:** speech-to-text versus text-to-speech.
- **Lex vs Polly:** conversational interface versus voice output.
- **Kendra vs OpenSearch Service:** managed enterprise search experience versus a broader managed search and analytics engine.
- **Personalize vs SageMaker AI:** managed recommendation capability versus a custom ML lifecycle.
- **Bedrock vs SageMaker AI:** foundation-model application building versus broad custom ML building, training, deployment, and operations.

## Security and Data Governance

- Use least-privilege IAM permissions for model invocation, training, data sources, indexes, and service APIs.
- Encrypt data at rest and in transit, and review AWS KMS permissions for customer-managed keys.
- Classify prompts, documents, images, audio, training data, embeddings, outputs, and logs before processing them.
- Use private network connectivity where supported and required, but verify each service and Region.
- Do not place secrets in prompts, tags, resource names, or logs.
- Review service-specific data processing, retention, abuse-detection, and model-provider terms for the exact configuration.

Amazon Bedrock documentation states that model providers do not have access to Bedrock service deployment accounts, logs, prompts, or completions. That statement is service-specific; it must not be generalized into “AWS never stores or processes customer AI data.” Customers remain responsible for configuration, content, access, retention choices, and legal requirements.

## Responsible AI

AWS describes responsible-AI dimensions including fairness, explainability, privacy and security, safety, controllability, veracity and robustness, governance, and transparency.

Practical controls include:

- Define the intended use and prohibited use before release.
- Evaluate representative and adversarial inputs.
- Measure quality with use-case-specific criteria rather than a universal accuracy claim.
- Use grounding, citations, guardrails, and deterministic application checks where useful.
- Require human oversight for consequential or high-risk decisions.
- Monitor production drift, harmful output, retrieval quality, latency, and cost.
- Provide a fallback or escalation path when confidence or safety is insufficient.

The AWS Responsible AI Policy states that generative AI may produce inaccurate or inappropriate content and that consequential uses require appropriate risk evaluation, safeguards, testing, and human oversight.

## Cost and Latency Trade-offs

Pretrained services usually charge according to processed requests or content. Bedrock cost varies with model, inference mode, input/output usage, customization, agents, knowledge bases, and supporting resources. SageMaker AI cost can include notebooks, training, hosting, batch processing, storage, and monitoring.

A larger or more capable model may cost more and respond more slowly without necessarily being the best model for a narrow task. Cache only where data sensitivity and freshness allow it, limit unnecessary context, test smaller models, and monitor both quality and cost.

## CPP Recognition Scenarios

1. Extract tables from expense documents: Textract.
2. Detect sentiment in product reviews: Comprehend.
3. Convert a recorded meeting to text: Transcribe.
4. Turn an article into spoken audio: Polly.
5. Analyze product photos: Rekognition.
6. Translate support messages: Translate.
7. Build a conversational bot: Lex.
8. Recommend items from customer behavior: Personalize.
9. Build a RAG assistant using foundation models: Bedrock.
10. Train and deploy a custom predictive model: SageMaker AI.

## Common Exam Traps

- “AI service” does not automatically mean SageMaker AI; prefer the purpose-built service when it directly matches the task.
- Bedrock provides foundation-model capabilities but does not guarantee correct answers.
- RAG adds retrieved context; it is not the same as fine-tuning.
- Guardrails supplement evaluation, authorization, and human oversight rather than replacing them.
- A service being managed does not transfer responsibility for customer data, permissions, output use, or compliance to AWS.
- Do not use the former name “Amazon SageMaker” when specifically referring to the renamed ML service, SageMaker AI; distinguish it from the broader next-generation SageMaker platform.

## Knowledge Check

1. Which service extracts tables and form fields from documents?
2. What is the direction of conversion for Transcribe and Polly?
3. Why does RAG not guarantee an accurate response?
4. When is SageMaker AI more appropriate than Bedrock?
5. What customer responsibilities remain when using a pretrained AI service?

## References

Checked **2026-07-25**.

- [Choosing an AWS machine learning service](https://docs.aws.amazon.com/decision-guides/latest/machine-learning-on-aws-how-to-choose/guide.html)
- [Amazon Machine Learning documentation](https://docs.aws.amazon.com/machine-learning/)
- [Amazon Bedrock overview](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Data protection in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)
- [What is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [What is Amazon SageMaker?](https://docs.aws.amazon.com/next-generation-sagemaker/latest/userguide/what-is-sagemaker.html)
- [AWS Responsible AI](https://aws.amazon.com/ai/responsible-ai/)
- [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/)
