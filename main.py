import streamlit as st

# Custom CSS for earthy theme and sidebar
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom, #d4e2c7, #3e4e55);
            font-family: 'Helvetica', sans-serif;
            color: #333;
        }

        .sidebar .sidebar-content {
            background-color: #f0f4f1;
            color: #555;
        }

        .sidebar .sidebar-header {
            font-size: 2rem;
            color: #2f3a34;
            font-weight: bold;
        }

        h1, h2, h3 {
            font-family: 'Georgia', serif;
            color: #2f3a34;
        }

        h1 {
            font-size: 3.5rem;
            font-weight: bold;
        }

        h2 {
            font-size: 2.5rem;
            font-weight: 600;
        }

        p, li {
            font-size: 1.2rem;
            line-height: 1.8;
            color: #4b5c44;
        }

        .stButton button {
            background-color: #8c8c7a;
            color: #fff;
            font-size: 1.2rem;
            border-radius: 10px;
            border: none;
            padding: 10px 20px;
            transition: background-color 0.3s ease;
        }

        .stButton button:hover {
            background-color: #a4bfa3;
        }

        .section-title {
            color: #4b5c44;
            font-size: 2.2rem;
            font-weight: 600;
            margin-bottom: 20px;
        }

        .section-content {
            padding: 20px;
            background-color: #e2e8d3;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }

        .contact-form input, .contact-form textarea {
            background-color: #f5f5f2;
            color: #333;
            border: 1px solid #a4bfa3;
            padding: 12px;
            border-radius: 8px;
            width: 100%;
            margin-bottom: 12px;
        }

        .contact-form button {
            background-color: #4b5c44;
            color: #fff;
            border: none;
            border-radius: 10px;
            padding: 12px 20px;
            font-size: 1.5rem;
            cursor: pointer;
        }

        .contact-form button:hover {
            background-color: #8c8c7a;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.title("Navigation")
st.sidebar.markdown("""
- [Home](#home)
- [About Me](#about-me)
- [Research](#research)
- [Publications](#publications)
- [Contact](#contact)
""")

# Home Section
st.title("Sara de la Salle - Researcher Portfolio")

st.header("Welcome to My Research Portfolio!")
st.write("""
    Hello, I am Sara de la Salle, a researcher specializing in neuropsychology and psychiatry. 
    My work focuses on the neural mechanisms of psychiatric disorders, with a particular interest in sensory processing, depression, and the effects of psychedelics.
    Feel free to browse through my work, publications, and get in touch if you'd like to collaborate.
""")

# About Me Section
st.header("About Me")
st.write("""
    I am currently a researcher at [Institution or University Name], specializing in the neural basis of psychiatric disorders. 
    My research interests include [Research Focus 1], [Research Focus 2], and the effects of various pharmacological interventions on mental health.
    I am deeply involved in clinical studies and research exploring treatments for mood disorders, including depression and anxiety.
""")

# Research Section
st.header("Research")
st.write("""
    Here are some of my recent projects and publications:
""")

# Example Research/Publication 1
st.subheader("Acute subanesthetic ketamine-induced effects on the mismatch negativity and their relationship to early and sustained treatment response in major depressive disorder")
st.write("""
    **Published**: Feb 2025  
    **Co-authors**: Jennifer L Phillips, Pierre Blier, Verner Knott  
    This study examines the effects of sub-anesthetic doses of ketamine on mismatch negativity (MMN), a neural marker, in patients with major depressive disorder.
    [View Article](#)
""")

# Contact Section
st.header("Contact Me")
st.write("""
    You can reach me at:
    - Email: [email@example.com]
    - LinkedIn: [LinkedIn Profile Link]
    - ResearchGate: [ResearchGate Profile Link]
""")

# Contact Form
st.header("Contact Form")
contact_form = """
<div class="contact-form">
    <form action="https://formsubmit.co/your-email@example.com" method="POST">
      <input type="text" name="name" placeholder="Your Name" required>
      <input type="email" name="email" placeholder="Your Email" required>
      <textarea name="message" placeholder="Your Message" required></textarea>
      <button type="submit">Send Message</button>
    </form>
</div>
"""
st.markdown(contact_form, unsafe_allow_html=True)
