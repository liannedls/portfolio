import streamlit as st

# Title and Description
st.title("Sara de la Salle - Researcher Portfolio")
st.write("""
    Welcome to the official portfolio of **Sara de la Salle**. 
    Sara is an expert in [field of research] with a focus on [specific research topics]. 
    Below, you can explore her recent publications, projects, and professional background.
""")

# Section for Research Interests
st.header("Research Interests")
st.write("""
    Sara's primary research interests include:
    - [Research Topic 1]
    - [Research Topic 2]
    - [Research Topic 3]
    - [Research Topic 4]
    
    More information on her work can be found in the links below.
""")

# Section for Publications
st.header("Publications")
st.write("""
    Below are some of Sara's recent publications:
""")

# Add a list of publications with links
publications = [
    {"title": "Title of Publication 1", "link": "https://link_to_publication1.com"},
    {"title": "Title of Publication 2", "link": "https://link_to_publication2.com"},
    {"title": "Title of Publication 3", "link": "https://link_to_publication3.com"},
]

for pub in publications:
    st.markdown(f"[{pub['title']}]({pub['link']})")

# Section for Projects
st.header("Projects")
st.write("""
    Sara has worked on several high-impact projects in her field:
""")

# Add a list of projects with descriptions
projects = [
    {"name": "Project 1", "description": "Description of project 1.", "link": "https://link_to_project1.com"},
    {"name": "Project 2", "description": "Description of project 2.", "link": "https://link_to_project2.com"},
    {"name": "Project 3", "description": "Description of project 3.", "link": "https://link_to_project3.com"},
]

for project in projects:
    st.write(f"**{project['name']}** - {project['description']}")
    st.markdown(f"[More Info]({project['link']})")

# Section for Contact
st.header("Contact")
st.write("""
    You can reach Sara via the following methods:
    - Email: [sara@email.com](mailto:sara@email.com)
    - LinkedIn: [Sara de la Salle on LinkedIn](https://www.linkedin.com/in/saradelasalle)
    - ResearchGate: [Sara de la Salle on ResearchGate](https://www.researchgate.net/profile/Sara-De-La-Salle)
""")

# Section for CV/Resume
st.header("CV / Resume")
st.write("""
    You can download Sara's CV below:
""")
st.markdown("[Download CV](https://link_to_CV.com)")

# Add any additional sections if needed
