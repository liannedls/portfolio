import streamlit as st

# Title of the webpage
st.title("Sara de la Salle - Researcher Portfolio")

# Home Section
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

# Example Research/Publication 2
st.subheader("Ontario healthcare workers who sought treatment for their mental health during the first five waves of the COVID-19 pandemic")
st.write("""
    **Published**: Feb 2025  
    **Co-authors**: Judith M Laposa, Duncan Cameron, Kim Corace, Randi E McCabe  
    This paper explores the demographic profile of healthcare workers who self-referred for mental health treatment during the COVID-19 pandemic in Ontario.
    [View Article](#)
""")

# Example Research/Publication 3
st.subheader("The ketamine chameleon: history, pharmacology, and the contested value of experience")
st.write("""
    **Published**: Jan 2025  
    **Co-authors**: Danny Diep, Julien Thibault Lévesque, Kyle Greenway  
    This review discusses the history and pharmacology of ketamine, as well as its subjective effects in medical and recreational contexts.
    [View Article](#)
""")

# Example Research/Publication 4
st.subheader("Electrocortical Profiles in Relation to Childhood Adversity and Depression Severity: A Preliminary Report")
st.write("""
    **Published**: Nov 2024  
    **Co-authors**: Natalia Jaworska, Bronwen Schryver, Verner Knott  
    This study investigates the relationship between electroencephalographic (EEG) activity, childhood adversity, and depression severity.
    [View Article](#)
""")

# Example Research/Publication 5
st.subheader("Longitudinal experiences of Canadians receiving compassionate access to psilocybin-assisted psychotherapy")
st.write("""
    **Published**: Jul 2024  
    **Co-authors**: Hannes Kettner, Julien Thibault Lévesque, Kyle Greenway  
    This research examines the long-term effects of psilocybin-assisted psychotherapy in Canadians receiving compassionate access to the treatment.
    [View Article](#)
""")

# Additional Publications Section

# Additional Research/Publication 6
st.subheader("Acute and Enduring Effects of Naturalistic Psychedelic Use Among Indigenous Peoples in Canada and the United States")
st.write("""
    **Published**: Aug 2022  
    **Co-authors**: Sophia Gran-Ruaz, Dawn D Davis, Monnica T Williams  
    This study explores the effects of naturalistic psychedelic use among Indigenous peoples in Canada and the U.S., focusing on racial trauma and healing.
    [View Article](#)
""")

# Additional Research/Publication 7
st.subheader("N-methyl-D-aspartate receptor antagonism impairs sensory gating in the auditory cortex in response to speech stimuli")
st.write("""
    **Published**: Jul 2022  
    **Co-authors**: Joelle Choueiry, Judy McIntosh, Verner Knott  
    This study investigates how NMDAR antagonism impacts sensory gating in response to auditory stimuli in healthy individuals.
    [View Article](#)
""")

# Additional Research/Publication 8
st.subheader("Ethnoracial Inclusion in Clinical Trials of Ketamine in the Treatment of Mental Health Disorders")
st.write("""
    **Published**: Jul 2022  
    **Co-authors**: Timothy Michaels, Lebert Lester, Monnica T Williams  
    This paper explores the racial disparities in ketamine clinical trials and the importance of ethnoracial inclusion in mental health research.
    [View Article](#)
""")

# Additional Research/Publication 9
st.subheader("Synchronized Auditory Gamma Response to Frontal Transcranial Direct Current Stimulation (tDCS) and its Inter-Individual Variation in Healthy Humans")
st.write("""
    **Published**: May 2022  
    **Co-authors**: Urusa Shah, Molly Hyde, Verner Knott  
    This study examines the effects of frontal tDCS on the auditory gamma response and its variability across individuals.
    [View Article](#)
""")

# Additional Research/Publication 10
st.subheader("Transcranial Alternating Current Stimulation (Tacs) Alters Auditory Steady-State Oscillatory Rhythms and Their Cross-Frequency Couplings")
st.write("""
    **Published**: Jan 2022  
    **Co-authors**: Joelle Choueiry, Mark Payumo, Verner Knott  
    This article investigates how TACS alters auditory steady-state oscillations, focusing on their cross-frequency couplings.
    [View Article](#)
""")

# CV Section
st.header("Curriculum Vitae (CV)")
st.write("""
    You can view or download my CV using the link below:
""")
st.markdown("[Download CV](#)")

# Contact Section
st.header("Contact Me")
st.write("""
    You can reach me at:
    - Email: [email@example.com]
    - LinkedIn: [LinkedIn Profile Link]
    - ResearchGate: [ResearchGate Profile Link]
""")

# Optional: If you want a contact form
st.header("Contact Form")
contact_form = """
<form action="https://formsubmit.co/your-email@example.com" method="POST">
  <input type="text" name="name" placeholder="Your Name" required>
  <input type="email" name="email" placeholder="Your Email" required>
  <textarea name="message" placeholder="Your Message" required></textarea>
  <button type="submit">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
