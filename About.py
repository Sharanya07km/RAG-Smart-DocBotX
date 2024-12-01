import streamlit as st
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpapercave.com/wp/wp3354900.jpg");
    background-size: cover;
    background-attachment: fixed; /* Ensure background stays fixed when scrolling */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


st.title("About Smart DocBotX")
st.markdown(
    """<h3 style='text-align: justify; font-size: 20px; color: white;'>Smart DocBotX is an advanced AI-powered document 
    assistant designed to help users interact seamlessly with their documents. Whether it's PDFs or Word files supported 
    formats, Smart DocBotX processes your content and answers your queries with precision and accuracy. Powered by 
    cutting-edge natural language processing and retrieval-augmented generation (RAG) techniques, it enables dynamic 
    and intuitive conversations, ensuring users get the most out of their documents. From extracting insights to sourcing 
    references, Smart DocBotX is your go-to virtual assistant for efficient document management.. </h3> <h2>Our Vision</h2> <h3 
    style='text-align: justify; font-size: 20px; color: white;'>Our vision is to revolutionize the way users interact with their
    knowledge bases. We aim to eliminate the friction in finding, analyzing, and retrieving information from documents by combining 
    AI innovation with user-centric design. Smart DocBotX envisions a future where accessing and understanding information is as natural 
    as having a conversation, empowering individuals and organizations to focus on decision-making and creativity.</h3><h2>Why Smart 
    DocBotX?</h2> <h3 style='text-align: justify; font-size: 20px; color: white;'> In today's fast-paced world, 
    accessing relevant and accurate information efficiently is crucial. Smart DocBotX addresses this need by 
    combining advanced document retrieval with state-of-the-art language generation to provide precise, contextual 
    responses.</h3>""",
    unsafe_allow_html=True
)
