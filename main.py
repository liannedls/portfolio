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
    st.image("https://scholar.googleusercontent.com/citations?view_op=medium_photo&user=ltdVgxkAAAAJ", caption="Sara de la Salle - Google Scholar Profile")
    st.image("https://media.licdn.com/dms/image/C4E03AQFQm_KsPzQ3AQ/profile-displayphoto-shrink_200_200/0/1516803824945?e=1718236800&v=beta&t=example", caption="Sara de la Salle - LinkedIn Profile")
    st.write(
        "Welcome to my research portfolio! Here, you can explore my latest work, publications, and projects."
    )

# Research Section
elif page == "Research":
    st.header("Research Work")
    st.write("Here you will find details about my current and past research projects.")
    st.image("https://via.placeholder.com/800x300", caption="Research in Progress")
    st.markdown("- **Project 1**: Description of the project.")
    st.markdown("- **Project 2**: Description of the project.")

# Publications Section
elif page == "Publications":
    st.header("Publications")
    st.write("A list of selected publications:")
    st.image("https://via.placeholder.com/600x200", caption="Recent Publications")
    st.markdown("1. *Title of Paper 1* - Journal Name, Year")
    st.markdown("2. *Title of Paper 2* - Journal Name, Year")

# Contact Section
elif page == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out via email: [email@example.com](mailto:email@example.com)")
    st.write("Or connect on [LinkedIn](https://linkedin.com/in/sara-de-la-salle-19b8a250/)")

st.sidebar.write("© 2025 Sara de la Salle")
