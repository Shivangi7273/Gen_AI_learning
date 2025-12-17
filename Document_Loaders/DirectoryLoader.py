from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()
docs2 = loader.lazy_load()

for document in docs2:
    print(document.metadata)

print(len(docs)) ## total number of pages of all the pdfs
print(docs[21].page_content, docs[21].metadata)

"""Lazy Loading means that a load will only occur once the object is needed, thus not loading unnecessary data. When you disable Lazy Loading you say that you will load yourself by calling load."""

