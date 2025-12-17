from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("C:/Shivangi/My_Learning/2_LangChain/Document_Loaders/books/dl-curriculum.pdf")
pdf_doc = loader.load()
# text = """"""

# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(encoding_name="cl100k_base", chunk_size = 100, chunk_overlap = 10)

text_splitter = CharacterTextSplitter(chunk_size = 100, chunk_overlap = 10, separator= ' ')
# text = text_splitter.split_text(text=text)
doc = text_splitter.split_documents(pdf_doc)

print(doc[1].page_content)
print(doc[1])
