from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import os
from langchain.chains.question_answering import load_qa_chain

# Replace book.pdf with any pdf of your choice
loader = UnstructuredPDFLoader("Rich-Dad-Poor-Dad.pdf")
pages = loader.load_and_split()
os.environ["OPENAI_API_KEY"]="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"
embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(pages, embeddings).as_retriever()

# Choose any query of your choice
query = "Who is Rich Dad?"
docs = docsearch.get_relevant_documents(query)
# chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
chain = load_qa_chain(ChatOpenAI(temperature=0), chain_type="stuff")
output = chain.run(input_documents=docs, question=query)
print(output)