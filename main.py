import streamlit as st
import pandas as pd

# Set up the page
st.set_page_config(page_title="Sara de la Salle - Research Portfolio", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        .main-container {
            max-width: 900px;
            margin: auto;
            text-align: center;
        }
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
        .header-text {
            font-size: 36px;
            font-weight: bold;
            color: #2C3E50;
        }
        .subheader-text {
            font-size: 24px;
            font-weight: normal;
            color: #7F8C8D;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.image("https://upload.wikimedia.org/wikipedia/en/thumb/8/89/McGill_University_Logo.svg/1280px-McGill_University_Logo.svg.png", width=200)
st.markdown('<p class="header-text">Sara de la Salle</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader-text">Researcher | Scientist | Innovator</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Research", "Publications", "Contact"])

# Home Section
if page == "Home":
    st.image("https://scholar.googleusercontent.com/citations?view_op=medium_photo&user=ltdVgxkAAAAJ", caption="Sara de la Salle - Google Scholar Profile")
    st.image("https://media.licdn.com/dms/image/C4E03AQFQm_KsPzQ3AQ/profile-displayphoto-shrink_200_200/0/1516803824945?e=1718236800&v=beta&t=example", caption="Sara de la Salle - LinkedIn Profile")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/EEG_brainwaves.png", caption="EEG Brainwave Study")
    st.write("Welcome to my research portfolio! Explore my latest work, publications, and projects.")

# Research Section
elif page == "Research":
    st.header("Research Work")
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e4/EEG_cap.jpg", caption="EEG Cap Used in Research")
    research_projects = pd.DataFrame({
        "Project": [
            "Data Mining EEG Signals in Depression",
            "Effects of Ketamine on Resting-State EEG Activity",
            "Predicting Antidepressant Treatment Response"
        ],
        "Description": [
            "Explored the diagnostic value of EEG signals in depression using data mining techniques.",
            "Investigated how ketamine influences resting-state EEG activity and its relationship to perceptual/dissociative symptoms.",
            "Leveraged machine learning approaches to predict antidepressant treatment response using EEG and clinical data."
        ]
    })
    st.table(research_projects)

# Publications Section
elif page == "Publications":
    st.header("Publications")
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2d/Neuroscience_brain_diagram.png", caption="Neuroscience Research")
    publications = pd.DataFrame({
        "Title": [
            "Data mining EEG signals in depression for their diagnostic value",
            "Effects of ketamine on resting-state EEG activity and their relationship to perceptual/dissociative symptoms in healthy humans",
            "Leveraging machine learning approaches for predicting antidepressant treatment response using electroencephalography (EEG) and clinical data"
        ],
        "Journal": [
            "BMC Medical Informatics and Decision Making, 2015",
            "Frontiers in Pharmacology, 2016",
            "Frontiers in Psychiatry, 2019"
        ]
    })
    st.table(publications)

# Contact Section
elif page == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out via email: [email@example.com](mailto:email@example.com)")
    st.write("Or connect on [LinkedIn](https://www.linkedin.com/in/sara-de-la-salle-19b8a250/)")

st.sidebar.write("© 2025 Sara de la Salle")
