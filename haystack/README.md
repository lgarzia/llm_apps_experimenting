[Haystack](https://github.com/deepset-ai/haystack)
[Prompt-Hub](https://prompthub.deepset.ai/)
Haystack is an end-to-end NLP framework that enables you to build applications powered by LLMs, Transformer models, vector search and more. Whether you want to perform question answering, answer generation, semantic document search, or build tools that are capable of complex decision making and query resolution, you can use the state-of-the-art NLP models with Haystack to build end-to-end NLP applications solving your use case.

Core Concepts
* Pipelines
* Nodes - Each Node achieves one thing. Such as preprocessing documents, retrieving documents, using language models to answer questions and so on.
* Agent - An Agent is a component that is powered by an LLM, such as GPT-3. It can decide on the next best course of action so as to get to the result of a query.
* Tools - You can think of a Tool as an expert, that is able to do something really well. Such as a calculator, good at mathematics. Or a WebRetriever, good at retrieving pages from the internet. A Node or pipeline in Haystack can also be used as a Tool. A Tool is a component that is used by an Agent, to resolve complex queries.
* DocumentStores: A DocumentStore is database where you store your text data for Haystack to access. Haystack DocumentStores are available with ElasticSearch, Opensearch, Weaviate, Pinecone, FAISS and more. For a full list of available DocumentStores,

[docs](https://docs.haystack.deepset.ai/docs)

Langauge revolves around Pipeline Components
* Crawler - The Crawler scrapes the text from a website and creates a Document object out of it. For example, you can use the Crawler to turn the contents of a website into Documents to use for search.

* DocumentClassifier
* DocumentLanguageClassifier
* EntityExtractor
* FileClassifier
* FileConverter
* PreProcessor

[medium - haystack](https://medium.com/aimonks/haystack-an-alternative-to-langchain-carrying-llms-bf7c515c9a7e)

PromptNode: tool that enables you to perform question-answering tasks
provide it with query, documents, and specific templates. 

Several document stores: 
* Elasticsearch
* In Memory
* SQL
* FAISS
...
Pipeline to manage dataflow

Ready-Made Pipelines
* ExtractiveQAPipeline
* GenerativeQAPipeline
* FAQPipeline
* TranslationWrapperPipeline

Agent
* Uses reasoning and combination of nodes, pipelines, and web queries to find answer
* Agent uses tools
[Use Hugging Face](https://medium.com/@cobusgreyling/build-a-chatbot-conversational-app-with-haystack-huggingface-8d43c1690b13)
[Reranker](https://medium.com/@cobusgreyling/ahaystack-developed-a-reranker-component-to-solve-llm-long-context-vulnerability-71af12a98fcb)

-----------
Nodes is Pipeline Components
https://docs.haystack.deepset.ai/docs/nodes_overview

* Custom Components - these are the components you can create yourself.
Data Handling - these are all the components you can use to preprocess and handle your data.
* Semantic Search - these are the components that are best for semantic search pipelines.
* Prompts and LLMs - these are all the components that bring the power of large language models to your search systems.
* Routing- these components route data to other components in the pipeline.
* Utility Components - these are all the helper components, such as the components used to join answers or documents, summarize documents, translate them, and more.
* Extras - these components are not part of the Haystack core. They live in a separate repo called haystack-extras.