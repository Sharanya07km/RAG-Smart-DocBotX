# RAG-Smart-DocBotX
 Retrieval-Augmented Generation System
# Smart DocBotX 🤖📚
## Overview
Smart DocBotX is a Retrieval-Augmented Generation (RAG) application designed to streamline the process of extracting insights from unstructured documents like PDFs and Word files. With a conversational AI interface, users can upload documents, ask natural language questions, and receive context-aware answers. This tool is ideal for legal, academic, and business workflows, saving time and improving decision-making by providing accurate responses with source references.

## Features
1. Document Upload & Processing: Accepts PDFs and Word documents to extract textual data.

2. Contextual Question Answering: Allows users to ask questions and retrieve precise, relevant answers.

3. Source Referencing: Provides the original document source for every answer.

4. Multi-Document Analysis: Processes multiple files simultaneously for cross-referencing.

5. Downloadable Responses: Users can download chat interactions for future use.


## Installation
Prerequisites

Ensure the following dependencies are installed on your system:

-Python 3.8+

-Streamlit

-PyPDF2

-Python-Docx

-FAISS

-LangChain

-TfidfVectorizer (from sklearn)

-dotenv

## Usage
* Upload Documents
* Navigate to the sidebar and upload PDFs or Word documents.
* Click Process to extract and index the text.
* Ask Questions
* Enter a question in the text input field.
* Receive answers with contextual accuracy and source references.
* Download Responses
After interaction, click the Download Response button to save your conversation as a text file.

## Architecture

## Tools and Libraries

-Streamlit: For building the interactive UI.

-LangChain: For implementing RAG pipelines and conversational chains.

-PyPDF2 & python-docx: For extracting text from PDFs and Word files.

-FAISS: For efficient vector-based similarity search.

-TfidfVectorizer: For generating lightweight, efficient text embeddings.

## Workflow

-Document Ingestion: Extracts text from uploaded documents.

-Text Splitting: Divides text into manageable chunks for indexing.

-Vectorization: Uses TF-IDF embeddings for semantic search.

-Conversation Chain: Combines retriever and LLM (ChatGroq) to generate contextual answers.



## Demo

### Application Interface
![Application Interface](https://github.com/Sharanya07km/RAG-Smart-DocBotX/blob/main/Screenshot%20(125).png)

### Document Upload
![Document Upload](https://github.com/Sharanya07km/RAG-Smart-DocBotX/blob/main/Screenshot%20(122).png)

### Chat Interaction
![ Chat Interaction](C:\Users\shara\OneDrive\Pictures\Screenshots\Screenshot (129).png)

