import streamlit as st
import base64

# CSS for background, flip cards, and footer
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://wallpapercave.com/wp/wp3354900.jpg");
        background-size: cover;
        background-attachment: fixed;
    }

    .flip-card {
        background-color: transparent;
        width: 180px;
        height: 180px;
        perspective: 1000px;
        margin: auto;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.6s;
        transform-style: preserve-3d;
    }

    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        border-radius: 50%;
        overflow: hidden;
        border: 4px solid white;
    }

    .flip-card-front img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
    }

    .flip-card-back {
        background-color: #0077b5;
        color: white;
        transform: rotateY(180deg);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .linkedin-button {
        background-color: white;
        color: #0077b5;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;
        border-radius: 5px;
        cursor: pointer;
    }

    .linkedin-button:hover {
        background-color: #005f87;
        color: white;
    }

    .team-info {
        text-align: center;
        color: white;
        font-size: 14px;
        margin-top: 10px;
    }

    .footer {
        text-align: center;
        margin-top: 100px; /* Adjusted for spacing */
    }

    .footer img {
        width: 25px;
        height: 25px;
        margin: 0 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Helper function to encode images
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Team member data
team_members = [
    {
        "name": "Sharanya K M",
        "linkedin": "https://www.linkedin.com/in/sharanya-k-m",
        "image_path": r"C:\Users\shara\OneDrive\Desktop\chatbot-pdf\views\WhatsApp Image 2024-11-16 at 6.59.47 PM.jpeg",
        "email": "sharanyakmsharanya@gmail.com",
        "contact": "+918660779063",
    },
    {
        "name": "N Chaitra",
        "linkedin": "https://www.linkedin.com/in/chaitra-d-n",
        "image_path": r"C:\Users\shara\OneDrive\Desktop\chatbot-pdf\views\WhatsApp Image 2024-11-17 at 10.31.38 AM.jpeg",
        "email": "chaitranainoor@gmail.com",
        "contact": "+919019764340",
    },
    {
        "name": "Aruna Bhat",
        "linkedin": "https://www.linkedin.com/in/arunavishweshwarbhat",
        "image_path": r"C:\Users\shara\OneDrive\Desktop\chatbot-pdf\views\IMG_1079.jpeg",
        "email": "bhataruna30@gmail.com",
        "contact": "+919482037076",
    },
]

# Layout
st.markdown('<h2 style="text-align: center; color: white;">Meet Our Team</h2>', unsafe_allow_html=True)
st.markdown(
    """<h3 style='text-align: justify; font-size: 20px; color: white;'> Smart DocBotX is the brainchild of a 
    dedicated team of final-year engineering students driven by a passion for leveraging AI to solve real-world 
    problems. With expertise in AI, natural language processing, and user-centric design, the team has developed a 
    smart assistant to revolutionize document management. </h3> </br>""",
    unsafe_allow_html=True
)

cols = st.columns(len(team_members))

for idx, member in enumerate(team_members):
    with cols[idx]:
        encoded_image = get_base64_encoded_image(member["image_path"])
        st.markdown(
            f"""
            <div class="flip-card">
                <div class="flip-card-inner">
                    <!-- Front Side -->
                    <div class="flip-card-front">
                        <img src="data:image/jpeg;base64,{encoded_image}" alt="{member['name']}">
                    </div>
                    <!-- Back Side -->
                    <div class="flip-card-back">
                        <a href="{member['linkedin']}" target="_blank" class="linkedin-button">LinkedIn</a>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        # Add name, email, and contact information below the card
        st.markdown(
            f"""
            <div class="team-info">
                <strong>{member['name']}</strong><br>
                Email: {member['email']}<br>
                Contact: {member['contact']}
            </div>
            """,
            unsafe_allow_html=True,
        )

# Social media footer (non-clickable)
st.markdown(
    """
    <div class="footer">
    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook">
    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
    <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter"> <!-- Updated Twitter icon -->
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp">
</div>

    """,
    unsafe_allow_html=True
)
