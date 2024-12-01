import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
#from langchain.llms import HuggingFaceHub
#from embeddings import TfidfEmbeddings
#from sentence_transformers import SentenceTransformer
#from langchain.embeddings import HuggingFaceEmbeddings
from sklearn.feature_extraction.text import TfidfVectorizer
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from docx import Document


def get_documents_text(docs):
    text_data = []
    for doc in docs:
        if doc.type == "application/pdf":
            pdf_reader = PdfReader(doc)
            text = "".join(page.extract_text() for page in pdf_reader.pages)
        elif doc.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            docx_reader = Document(doc)
            text = "\n".join(paragraph.text for paragraph in docx_reader.paragraphs)
        else:
            st.warning(f"Unsupported file type: {doc.type}")
            continue
        text_data.append({"text": text, "source": doc.name})
    return text_data


def get_text_chunks(text_data):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = []
    for item in text_data:
        chunks += [{"chunk": chunk, "source": item["source"]} for chunk in text_splitter.split_text(item["text"])]
    return chunks


# embeddings.py already contains the TfidfEmbeddings class
from embeddings import TfidfEmbeddings
from langchain.vectorstores import FAISS  # Import FAISS from LangChain community package

def get_vectorstore(text_chunks):
    # Print text_chunks to understand its structure
    #print(text_chunks)  # Debugging step to see the content of text_chunks

    # Extract the text content (assuming it should be under a 'text' key)
    texts = [item["chunk"] for item in text_chunks]  # Adjust this key if needed

    # Initialize the embedding model
    embedding_model = TfidfEmbeddings()
    embedding_model.fit(texts)  # Fit the model on texts

    # Create the FAISS vectorstore
    vectorstore = FAISS.from_texts(
        texts=texts, 
        embedding=embedding_model, 
        metadatas=[{"source": item["source"]} for item in text_chunks]
    )

    return vectorstore



    '''vectorizer = TfidfVectorizer()
    texts = [item["chunk"] for item in text_chunks]  # Extract the "chunk" text
    embeddings = vectorizer.fit_transform(texts).toarray()  # TF-IDF vectorization
    vectorstore = FAISS.from_texts(texts=texts, embedding=embeddings, metadatas=[{"source": item["source"]} for item in text_chunks])
    return vectorstore'''



def get_conversation_chain(vectorstore):
     prompt_template = PromptTemplate(
         input_variables=["context", "question"],
         template="""
         You are a helpful assistant designed to answer questions based on the provided context. Your responses should be accurate and directly related to the information in the context. If the question cannot be answered using the given context, politely inform the user that you don't have enough information to answer and suggest they ask a related question that might be covered in the knowledge base.

         Always include the sources of the information in your response.

         Context: {context}
         Question: {question}

         Answer:
         """
     )

     llm = ChatGroq(temperature=0.5, max_tokens=500)
     #llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
     #llm = ChatOpenAI(
         #temperature=0, # Ensuring the responses are deterministic (required)
         #max_tokens=500,
     #)

     memory = ConversationBufferMemory(
         memory_key='chat_history',
         return_messages=True,
         output_key='answer'  
     )

      #Create a conversational retrieval chain that uses the LLM, vector store, and memory
     conversation_chain = ConversationalRetrievalChain.from_llm(
         llm=llm,
         retriever=vectorstore.as_retriever(),
         memory=memory,
         combine_docs_chain_kwargs={"prompt": prompt_template},
         return_source_documents=True,
         verbose=True

     )
    
     return conversation_chain

def handle_userinput(user_question):
     response = st.session_state.conversation({'question': user_question})
     st.session_state.chat_history = response['chat_history']

     bot_responses = []
     for i, message in enumerate(st.session_state.chat_history):
         if i % 2 == 0:
             st.write(user_template.replace(
                 "{{MSG}}", message.content), unsafe_allow_html=True)
         else:
             bot_response = message.content
            
             if 'source_documents' in response:
                 sources = [doc.metadata['source'] for doc in response['source_documents']]
                 unique_sources = list(set(sources)) 
                 source_string = "\n\nSources: " + ", ".join(unique_sources)
                 bot_response += source_string

             st.write(bot_template.replace("{{MSG}}", bot_response), unsafe_allow_html=True)
             bot_responses.append(bot_response)


     if not st.session_state.get("response_saved", False):  # Avoid overwriting
         st.session_state.download_content = "\n\n".join(bot_responses)
         st.session_state.response_saved = True  # Mark the response as saved        

def main():
     page_bg_img = """
     <style>
     [data-testid="stAppViewContainer"] {
        background-image: url("https://wallpapercave.com/wp/wp3354900.jpg");
        background-size: cover;
     }
     </style>
     """
     st.markdown(page_bg_img, unsafe_allow_html=True)
     button_css = """
        <style>
        div.stButton > button {
            background-color: #4CAF50; /* Green background */
            color: white; /* White text */
            padding: 10px 24px; /* Padding for the button */
            top: 28%; /* Adjust this value to move the button vertically */
            left: 90%;
            font-size: 16px; /* Font size */
            font-weight: bold; /* Bold text */
            border: none; /* Remove border */
            border-radius: 12px; /* Rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
            transition: 0.3s; /* Smooth hover effect */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2); /* Shadow effect */
        }

        div.stButton > button:hover {
            background-color: #45a049; /* Darker green on hover */
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.3); /* Enhanced shadow */
        }

        /* Positioning the button */
        .sidebar .stButton {
            text-align: center; /* Center the button */
            margin-top: 10px; /* Space from top */
        }
        </style>
        """
     st.markdown(button_css, unsafe_allow_html=True)
     
     load_dotenv()
     
    #st.set_page_config(page_title="Chat with multiple PDFs",page_icon=":books:")
     st.write(css, unsafe_allow_html=True)

     if "conversation" not in st.session_state:
         st.session_state.conversation = None
     if "chat_history" not in st.session_state:
         st.session_state.chat_history = None
     if "download_content" not in st.session_state:
         st.session_state.download_content = ""

     st.header("Smart DocBotX 🤖📚")
     user_question = st.text_input("Ask a question about your documents:")
     if user_question and st.session_state.conversation:
         handle_userinput(user_question)

     with st.sidebar:
         st.subheader("Your documents 📚")
         pdf_docs = st.file_uploader(
             "Upload your Documents📄 here and click on 'Process'", accept_multiple_files=True)
# Check if the documents are already processed
         if 'processed' not in st.session_state:
            st.session_state.processed = False  # Initialize the processed flag

        # Show the "Process" button only if not processed
         if not st.session_state.processed:
            if st.button("Process"):
                if pdf_docs:  # Ensure files are uploaded
                    with st.spinner("Processing..."):
                        # Get PDF text
                        text_data = get_documents_text(pdf_docs)
                        # Get the text chunks
                        text_chunks = get_text_chunks(text_data)
                        # Create vector store
                        vectorstore = get_vectorstore(text_chunks)
                        # Create conversation chain
                        st.session_state.conversation = get_conversation_chain(vectorstore)

                        # Set the processed flag to True
                        st.session_state.processed = True
                else:
                    st.warning("Please upload at least one document before processing.")
         else:
            st.success("Documents processed successfully! 🎉")


     if st.session_state.download_content:
         st.download_button(
            label="Download Response ⬇️",
            data=st.session_state.download_content,
            file_name="chatbot_response.txt",
            mime="text/plain"
         ) 
    # Initialize session states for conversation
     if 'conversation_initialized' not in st.session_state:
        st.session_state.conversation_initialized = False
     if not st.session_state.conversation_initialized:
        st.session_state.conversation_history = []
        st.session_state.conversation_initialized = True           

if __name__ == '__main__':
     main()     