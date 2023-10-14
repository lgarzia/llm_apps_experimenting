# %%
import os

from haystack.nodes import PromptNode

provider = "openai"
API_KEY = os.environ.get('OPENAI_API_KEY')
prompt_node = PromptNode(model_name_or_path="openai-gpt", api_key=API_KEY)
# %%
result = prompt_node.prompt(query="Who is the father of Arya Stark?", 
                            documents=[{"text": "Ned Stark is the father of Arya Stark."}],
                            prompt_template="deepset/question-answering")
# %%
from haystack.document_stores import ElasticsearchDocumentStore

document_store = ElasticsearchDocumentStore()
documents = [
    Document()
]
document_store.write_documents(documents)

# %%
from haystack import Pipeline

p = Pipeline()
p.add_node(component=retriever, name="Retriever", inputs=["Query"])
p.add_node(component=prompt_node, name="PromptNode", inputs=["Retriever"])
result = p.run(query="Who is the father of Arya Stark?")

# %%
from haystack.nodes import EmbeddingRetriever, PromptNode
