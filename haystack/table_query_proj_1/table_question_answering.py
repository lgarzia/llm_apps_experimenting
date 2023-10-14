# https://docs.haystack.deepset.ai/docs/table_qa
# https://haystack.deepset.ai/tutorials/15_tableqa
# https://docs.haystack.deepset.ai/reference/reader-api#tablereader
# https://huggingface.co/models?pipeline_tag=table-question-answering
# https://docs.haystack.deepset.ai/reference/retriever-api#tabletextretriever
# Indexing Data
# Retrieval

# %%
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import TableReader, TableTextRetriever
from haystack.pipelines import Pipeline

# %%
document_store = InMemoryDocumentStore(embedding_dim=512)
document_index = "document"

# %%
import pandas as pd

table = pd.read_parquet('all-the-news-trimmed_1.parquet')
table = table[['title_cleaned', 'section']]
table = table.fillna('')
# %%
from haystack import Document

doc = [Document(content=table, content_type="table", id="1")]
document_store.write_documents(doc)
# %%
retriever = TableTextRetriever(
    document_store=document_store,
    query_embedding_model="deepset/bert-small-mm_retrieval-question_encoder",
    passage_embedding_model="deepset/bert-small-mm_retrieval-passage_encoder",
    table_embedding_model="deepset/bert-small-mm_retrieval-table_encoder",
    embed_meta_fields=["title_cleaned", "section"]
)

# %%
document_store.update_embeddings(retriever=retriever)
# %%
# download from Hugging Face model hub
reader = TableReader(model_name_or_path="google/tapas-base-finetuned-wtq")
# %%
table_qa_pipeline = Pipeline()
table_qa_pipeline.add_node(component=retriever, name="TableTextRetriever", inputs=["Query"])
table_qa_pipeline.add_node(component=reader, name="TableReader", inputs=["TableTextRetriever"])
# %%
prediction = table_qa_pipeline.run("Who is Paris Hilton?")
# %%from haystack.utils import print_answers
from haystack.utils import print_answers

print_answers(prediction, details="minimal")

# %%
