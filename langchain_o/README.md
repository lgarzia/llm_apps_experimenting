LangChain is a framework for developing applications powered by language models.

The most common and most important chain that LangChain helps create contains three things:

LLM: The language model is the core reasoning engine here. In order to work with LangChain, you need to understand the different types of language models and how to work with them.

* LLMs: this is a language model which takes a string as input and returns a string

* ChatModels: this is a language model which takes a list of messages as input and returns a message
    * content
    * role
        * HumanMessage
        * AIMessage
        * SystemMessage
        * FunctionMessage
    *predict
    *predict_messages


Prompt Templates: This provides instructions to the language model. This controls what the language model outputs, so understanding how to construct prompts and different prompting strategies is crucial.

* Most LLM applications do not pass user input directly into an LLM. Usually they will add the user input to a larger piece of text, called a prompt template, that provides additional context on the specific task at hand.
* They bundle up all the logic for going from user input into a fully formatted prompt.


Output Parsers: These translate the raw response from the LLM to a more workable format, making it easy to use the output downstream.

* Convert text from LLM -> structured information (e.g. JSON)
* Convert a ChatMessage into just a string
* Convert the extra information returned from a call besides the message (like OpenAI function invocation) into a string.

PromptTemplate + LLM + OutputParser

* input variable
* prompt template
* language model
* output parser

[Model I/O](https://python.langchain.com/docs/modules/model_io)
The core element of any language model application is...the model. LangChain gives you the building blocks to interface with any language model.
[Prompt Templates](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/)
* A template may include instructions, few-shot examples, and specific context and questions appropriate for a given task.
* LangChain strives to create model agnostic templates to make it easy to reuse existing templates across different language models.

Prompts:
* Connecting to feature store
* Custom prompt templates
    * string
    * chat
    * requires input_variables that exposes what input variable the prompt template expects
    * format method to returns the formatted prompts
* Few-shot prompt template
* Few-shot examples for chat models
* Prompt templates
    * f-string
    * jinja2
* MessagePromptTemplate
    * AIMessagePromptTemplate
    * SystemMessagePromptTemplate
    * HumanMessagePromptTemplate
    * ChatMessagePromptTemplate
* Partial prompt templates
* Composition - compose multiple prompts together
* Serialization - store prompts as files
* Prompt pipelining -> user friendly interface for composing different parts of prompts together
* Example selectors
    * large number of examples, need to select which ones to include in prompt
    * select by length (stay within context window)
    * Select by maximal marginal relevance (MMR) - most similar & maximize diversity
    * Select y n-gram overlap
    * Select by similarity

Language Models:
* LLMs: take a text string as input and returns a text string
* Chat Models: Language model but takes a list of Chat Messages as input and return a Chat message
* LLMs in LangChain refer to pure text completion models. The APIs they wrap take a string prompt as input and output a string completion. OpenAI's GPT-3 is implemented as an LLM. Chat models are often backed by LLMs but tuned specifically for having conversations.
Instead of a single string, they take a list of chat messages as input. Usually these messages are labeled with the speaker (usually one of "System", "AI", and "Human"). And they return an AI chat message as output. GPT-4 and Anthropic's Claude are both implemented as chat models.
* LLMs
    * Large Language Models (LLMs) are a core component of LangChain. LangChain does not serve its own LLMs, but rather provides a standard interface for interacting with many different LLMs.
    * Asynch API
    * Fake LLM
    * Caching
    * Serialization - save the configuration for a given LLM (e.g. temperature)
    * Streaming - handle streaming response
    * Tracking token usage
* Chat Models
    * Messages
        * AIMessage
        * HumanMessage
        * SystemMessage
        * ChatMessage (arbitrary role parameter)
    * Caching
    * Human input chat model
    * Prompts
        * ChatPromptTemplate
        * MessagePromptTemplate
    * Streaming
* Output parsers
Output parsers are classes that help structure language model responses. There are two main methods an output parser must implement:
    * List parser
    * Datetime parser
    * Enum parser
    ...
**Retrieval**
Many LLM applications require user-specific data that is not part of the model's training set. The primary way of accomplishing this is through Retrieval Augmented Generation (RAG). In this process, external data is retrieved and then passed to the LLM when doing the generation step.

* Document Loaders - We provide integrations to load all types of documents (HTML, PDF, code) from all types of locations (private s3 buckets, public websites).
* Document transformers - This involves several transformation steps in order to best prepare the documents for retrieval. One of the primary ones here is splitting (or chunking) a large document into smaller chunks.
* Text embedding models - 
* Vector stores - 
* Retrievers - **self proclaimed** adding most values
    * Parent Document Retriever: This allows you to create multiple embeddings per parent document, allowing you to look up smaller chunks but return larger context.
    * Self Query Retriever: User questions often contain a reference to something that isn't just semantic but rather expresses some logic that can best be represented as a metadata filter. Self-query allows you to parse out the semantic part of a query from other metadata filters present in the query.
    * Ensemble Retriever: Sometimes you may want to retrieve documents from multiple different sources, or using multiple different algorithms. The ensemble retriever allows you to easily do this.
* Indexing: Here, we will look at a basic indexing workflow using the LangChain indexing API.
The indexing API lets you load and keep in sync documents from any source into a vector store. Specifically, it helps:
Avoid writing duplicated content into the vector store
Avoid re-writing unchanged content
Avoid re-computing embeddings over unchanged content
All of which should save you time and money, as well as improve your vector search results.
**Chains**
Using an LLM in isolation is fine for simple applications, but more complex applications require chaining LLMs - either with each other or with other components.
LangChain provides the Chain interface for such "chained" applications. We define a Chain very generically as a sequence of calls to components, which can include other chains. The base interface is simple:

**Memory**
Most LLM applications have a conversational interface. An essential component of a conversation is being able to refer to information introduced earlier in the conversation. At bare minimum, a conversational system should be able to access some window of past messages directly. A more complex system will need to have a world model that it is constantly updating, which allows it to do things like maintain information about entities and their relationships.

We call this ability to store information about past interactions "memory". LangChain provides a lot of utilities for adding memory to a system. These utilities can be used by themselves or incorporated seamlessly into a chain.

**Agents**
The core idea of agents is to use an LLM to choose a sequence of actions to take. In chains, a sequence of actions is hardcoded (in code). In agents, a language model is used as a reasoning engine to determine which actions to take and in which order.

**Callbacks**
LangChain provides a callbacks system that allows you to hook into the various stages of your LLM application. This is useful for logging, monitoring, streaming, and other tasks.

You can subscribe to these events by using the callbacks argument available throughout the API. This argument is list of handler objects, which are expected to implement one or more of the methods described below in more detail.
