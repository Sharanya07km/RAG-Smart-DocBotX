import streamlit as st

# Set up the title and background
st.title("Feedback")

# Background image styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpapercave.com/wp/wp3354900.jpg");
    background-size: cover;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Decreased font size for the title using Markdown and HTML
st.markdown(
    """
    <h3 style='text-align: justify; font-size: 20px; color: white;'>
    We value your thoughts! At Smart DocBotX, our goal is to provide you with the best experience possible, and your feedback plays a vital role in helping us achieve that. 
    Whether you have suggestions for improvements, comments about what you enjoyed, or constructive feedback on areas where we can do better, we want to hear from you. 
    Please take a moment to share your insights, and know that every piece of feedback is carefully reviewed by our team. 
    Thank you for helping us grow and improve!
    </h3>
    """,
    unsafe_allow_html=True
)

# Google Form URL
form_url = "https://forms.gle/W5X4fMkceNCDZHSj9"  # Replace with your Google Form URL

# Create a button that opens the Google Form in a new tab
if st.button("Give Your Feedback"):
    st.markdown(f'<meta http-equiv="refresh" content="0; url={form_url}">', unsafe_allow_html=True)
