import pandas as pd

from haystack import Document

table = pd.DataFrame()
docs = [
    Document(content=table,
             content_type="table",
             meta={}),
    ...
]
document_store.write_documents(docs)