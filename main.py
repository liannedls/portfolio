import streamlit as st

# Set up the page
st.set_page_config(page_title="Sara de la Salle - Research Portfolio", layout="wide")

# Header
st.title("Sara de la Salle")
st.subheader("Researcher | Scientist | Innovator")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Research", "Publications", "Contact"])

# Home Section
if page == "Home":
    st.image("https://via.placeholder.com/800x300", caption="Sara de la Salle")
    st.write(
        "Welcome to my research portfolio! Here, you can explore my latest work, publications, and projects."
    )

# Research Section
elif page == "Research":
    st.header("Research Work")
    st.write("Here you will find details about my current and past research projects.")
    st.markdown("- **Data Mining EEG Signals in Depression**: Explored the diagnostic value of EEG signals in depression using data mining techniques.")
    st.markdown("- **Effects of Ketamine on Resting-State EEG Activity**: Investigated how ketamine influences resting-state EEG activity and its relationship to perceptual/dissociative symptoms.")
    st.markdown("- **Predicting Antidepressant Treatment Response**: Leveraged machine learning approaches to predict antidepressant treatment response using EEG and clinical data.")

# Publications Section
elif page == "Publications":
    st.header("Publications")
    st.write("A list of selected publications:")
    st.markdown("1. *Data mining EEG signals in depression for their diagnostic value* - BMC Medical Informatics and Decision Making, 2015")
    st.markdown("2. *Effects of ketamine on resting-state EEG activity and their relationship to perceptual/dissociative symptoms in healthy humans* - Frontiers in Pharmacology, 2016")
    st.markdown("3. *Leveraging machine learning approaches for predicting antidepressant treatment response using electroencephalography (EEG) and clinical data* - Frontiers in Psychiatry, 2019")

# Contact Section
elif page == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out via email: [email@example.com](mailto:email@example.com)")
    st.write("Or connect on [LinkedIn](https://www.linkedin.com/in/sara-de-la-salle-19b8a250/)")

st.sidebar.write("© 2025 Sara de la Salle")
