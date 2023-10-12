https://docs.llamaindex.ai/en/stable/

LlamaIndex (formerly GPT Index) is a data framework for LLM applications to ingest, structure, and access private or domain-specific data.

Applications built on top of LLMs often require augmenting these models with private or domain-specific data. Unfortunately, that data can be distributed across siloed applications and data stores. It’s behind APIs, in SQL databases, or trapped in PDFs and slide decks.

That’s where LlamaIndex comes in.

* Data connectors ingest your existing data from their native source and format. These could be APIs, PDFs, SQL, and (much) more.
* Data indexes structure your data in intermediate representations that are easy and performant for LLMs to consume.
* Engines provide natural language access to your data. For example:
* Query engines are powerful retrieval interfaces for knowledge-augmented output.
* Chat engines are conversational interfaces for multi-message, “back and forth” interactions with your data.
* Data agents are LLM-powered knowledge workers augmented by tools, from simple helper functions to API integrations and more.
* *Application integrations tie LlamaIndex back into the rest of your ecosystem. This could be LangChain, Flask, Docker, ChatGPT, or… anything else!*

High Level Concepts
LlamaIndex helps you build LLM-powered applications (e.g. Q&A, chatbot, and agents) over custom data.

Retrieval Augmented Generation
* Indexing Stage
    * Data Connectors
    * Documents/Nodes
    * Data Indexes 
* Querying stage
    * The key challenge in the querying stage is retrieval, orchestration, and reasoning over (potentially many) knowledge bases.
    * Retrievers
    * Node Postprocessor
    * Response Synthesizer
* Pipelines
    * Query Engines
    * Chat Engines 
    * Agents - An agent is an automated decision maker (powered by an LLM) that interacts with the world via a set of tools. 


