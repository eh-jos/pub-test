import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import requests
from PIL import Image
from io import BytesIO
from config import GITHUB_PAT
import os
from dotenv import load_dotenv

# Page Configuration
st.set_page_config(
    page_title="Older People Preferences Dashboard",
    page_icon="⭐️",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.markdown("""<style>.big-font {font-size:20px !important;font-weight:bold}</style>""", unsafe_allow_html=True)
    st.markdown('<p class="big-font">Older people preferences dashboard</p>', unsafe_allow_html=True)
    st.write(
        "This tab gives an overview and key messages from the research project. It also provides an overview of the dashboards and what they represent."
    )
    with st.popover("More details"):
        url ='https://www.opfpru.nihr.ac.uk/projects/current-projects/preferences-for-new-models-of-social-care/'
        link_text = 'here'
        st.write(f'To know more about the research project please see [{link_text}]({url})')
        
    st.write("© Michela Tinelli, LSE 2024")
    st.write("All rights reserved")

#CSS Customization


main_id = "stApp"
sidebar_header_id = "stSidebarHeader"
sidebar_id = "stSidebarUserContent" 
sidebar_nav_id = "stSidebarNavItems"
sidebar_popover_id  = "stPopover"
expander_id = "stExpander"
main_style = f""" <style> [data-testid="{main_id}"] {{ background-color: #FFFFFF; }} </style> """ 
sidebar_header_style = f""" <style> [data-testid="{sidebar_header_id}"] {{ background-color: #2FC0BA; }} </style> """ 
sidebar_nav_style = f""" <style> [data-testid="{sidebar_nav_id}"] {{ background-color: #2FC0BA; }} </style> """ 
sidebar_style = f""" <style> [data-testid="{sidebar_id}"] {{color:#FFFFFF; background-color: #00636A; }} </style> """
sidebar_popover_style = f""" <style> [data-testid="{sidebar_popover_id}"]{{color: #64285D;}} </style>""" 
expander_style = f""" <style> [data-testid="{expander_id}"]{{color: #64285D;}} </style>""" 
st.markdown(main_style, unsafe_allow_html=True)                                                             
st.markdown(sidebar_header_style, unsafe_allow_html=True) 
st.markdown(sidebar_nav_style, unsafe_allow_html=True)    
st.markdown(sidebar_style, unsafe_allow_html=True)
st.markdown(sidebar_popover_style, unsafe_allow_html= True)   
st.markdown(expander_style, unsafe_allow_html= True)                                                             

# Your GitHub username and Personal Access Token
username = "CareQualityEvaluation"
token = f"{GITHUB_PAT}"

# The raw URL of your image in the private repository
repo = "OPFPRU"
path_to_image = "images/access.png"
branch = "main"

# Construct the URL
url = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/access.png"
url2 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/cost.png"
url3 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/provider.png"
url4 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/housing.png"
url5 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/identity.png"
url6 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/location.png"
url7 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/tech.png"
url8 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/elder1.png"
url9 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/elder2.png"
url10 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/chart1.png"
url11 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/chart2.png"
url12 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/chart3.png"
url13 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/chart4.png"
url14 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/relaxing-at-home.png"
url15 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/logo1.png"
url16 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/logo2.png"
url17 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/logo3.png"
url18 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/logo4.png"
url19 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/logo5.png"
url20 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/Picture2.png"
# Make a request to get the image, using the token for authentication
#logos
response19 = requests.get(url19, auth=(username, token))
image19 = Image.open(BytesIO(response19.content))
response18 = requests.get(url18, auth=(username, token))
image18 = Image.open(BytesIO(response18.content))
response17 = requests.get(url17, auth=(username, token))
image17 = Image.open(BytesIO(response17.content))
response16 = requests.get(url16, auth=(username, token))
image16 = Image.open(BytesIO(response16.content))

response15 = requests.get(url15, auth=(username, token))
image15 = Image.open(BytesIO(response15.content))

#header image
response14 = requests.get(url14, auth=(username, token))
image14 = Image.open(BytesIO(response14.content))
response20 = requests.get(url20, auth=(username, token))
image20 = Image.open(BytesIO(response20.content))

#icons
response = requests.get(url, auth=(username, token))
image = Image.open(BytesIO(response.content))

response2 = requests.get(url2, auth=(username, token))
image2 = Image.open(BytesIO(response2.content))

response3 = requests.get(url3, auth=(username, token))
image3 = Image.open(BytesIO(response3.content))

response4 = requests.get(url4, auth=(username, token))
image4 = Image.open(BytesIO(response4.content))

response5 = requests.get(url5, auth=(username, token))
image5 = Image.open(BytesIO(response5.content))

response6 = requests.get(url6, auth=(username, token))
image6 = Image.open(BytesIO(response6.content))

response7 = requests.get(url7, auth=(username, token))
image7 = Image.open(BytesIO(response7.content))

response8 = requests.get(url8, auth=(username, token))
image8 = Image.open(BytesIO(response8.content))

response9 = requests.get(url9, auth=(username, token))
image9 = Image.open(BytesIO(response9.content))

response10 = requests.get(url10, auth=(username, token))
image10 = Image.open(BytesIO(response10.content))

response11 = requests.get(url11, auth=(username, token))
image11 = Image.open(BytesIO(response11.content))

response12 = requests.get(url12, auth=(username, token))
image12 = Image.open(BytesIO(response12.content))

response13 = requests.get(url13, auth=(username, token))
image13 = Image.open(BytesIO(response13.content))

# Layout
# Create containers
container1 = st.container(border = True)
container2 = st.container(border = True)
container3 = st.container(border = True)

with container1:
    st.markdown("""<style>.big-title-font {font-size:28px !important;font-weight: bold;}</style>""", unsafe_allow_html=True)
    st.markdown('<p class="big-title-font">Preferences and willingness to pay for new models of social care for older people with high care needs in England</p>', unsafe_allow_html=True)

    

    st.write("---")
    st.empty()

    st.markdown("""<style>.big-key-font {font-size:26px !important;font-weight: bold;}</style>""", unsafe_allow_html=True)
    st.markdown('<p class="big-key-font">Background of the research project</p>', unsafe_allow_html=True)

    st.write(
        "The objective of our study was to understand how preferences from different components of care are shaped by individual demographic, socioeconomic and needs-related factors. Building on evidence from the first phase of our study – where we gathered insights from previous research and a series of focus groups – we conducted a survey to understand variations in preferences."
    )
    st.write("We recruited a sample of people aged 50 years or older living in England, drawn from the general population, with the help of a survey agency. The survey included general questions about preferences relating to care and support. Specific questions formed a discrete choice experiment (DCE) to explore how participants would trade-off different features of social care arrangements when thinking about their own (current or future) circumstances, if they were to have high care needs.")
    
    with st.popover("More details on DCE"):
        url = 'https://eprints.lse.ac.uk/73723/1/Tinelli_Applying%20discrete%20social%20experiments%20in%20social%20care%20research_published_2016%20LSERO.pdf'
        link_text = 'More about DCE, click here'
        st.write('DCEs are used in health services research, particularly by health economists, but have seldom been applied to social care studies. They enable researchers to measure the strength of preferences between alternative scenarios or types of service provision (9). Each alternative is described by several attributes or components of care. Survey participants are invited to choose between different models of care, each described in terms of those attributes. Participants’ choices indicate how their preferences are influenced by, and the relative importance they attach to, each attribute. A DCE thus provides a measure of the relative value attached to the different alternatives. It also provides information on how much individuals are willing to accept compromises in some attributes to gain more of other attributes that they value.  Details about the questionnaire can be requested contacting the team (m.tinelli@lse.ac.uk)')
        st.write(f'[{link_text}]({url})')

    st.markdown("""
        The visualisations listed below describe key findings from the DCE questions. 
        <a href='#section-collection-of-dashboards' class='jump-link'>Click here to jump to Collection of Dashboards</a>
        <script>
            // Add smooth scrolling to all links
            document.querySelectorAll('a.jump-link').forEach(anchor => {
                anchor.onclick = function (e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                };
            });
        </script>
        """, unsafe_allow_html=True)

    st.empty()
    st.write("---")

custom_css_key_findings = """
    <style>
    .my-container {
     background-color: #d6f5f3;
     padding: 20px; border: 3px solid #08636B
     border-radius: 10px;
    }
    </style>
    """

with container2:

 
    #Display the image in Streamlit
    st.image(image14, use_column_width = True)


    st.markdown("""<style>.big-key-font {font-size:26px !important;font-weight: bold;}</style>""", unsafe_allow_html=True)
    st.markdown('<p class="big-key-font">Key findings from the DCE questions</p>', unsafe_allow_html=True)
    st.markdown(custom_css_key_findings, unsafe_allow_html=True)
    # Use the custom class in a container
    st.markdown('<div class="my-container">Housing setting, provider of care, identity, use of technology devices, access to community services, and costs of care significantly influence decisions between different care options. The main factor influencing people’s choice is who provides support with the care task (preferred option: receiving support from carers arranged by the local authority), followed (in order of importance) by receiving care from someone who respects their beliefs and values, housing setting (preferred option: own home with appropriate adaptation if required), not using technology devices, lower weekly cost, and closer access to community facilities. Participants were willing to pay a substantial amount (over £100 per week indicatively) or to live beyond walking distance (over 30-minute walk) to receive care from family members or friends (only) rather than receiving support from carers arranged by their local authority.</div>', unsafe_allow_html=True)


    with st.expander("Key findings according to different sociodemographic groups"):
        text = '''
        * **Comparison by Age:** Older people have stronger preferences than younger people (within our sample of people aged 50+) for living in their own homes with appropriate adaptations if required and for not using technology. In contrast, their preferences are likely to be less strong for: receiving care from other options beyond family members or friends; receiving care from someone who respects their beliefs and values; and access to community services. Younger participants are willing to pay to receive care from a source other than their preferred carer or to receive care from someone who respects their beliefs, but they are not willing to accept longer walking times to local amenities for these same changes. For the other attributes, the age group willing to pay more is also willing to accept longer walking times.
    
        * **Comparison by Income:** Trends in data showed that the higher the income group, the greater the likelihood that individuals would be willing to pay more for receiving care from someone who respects their beliefs and values, as opposed to not having this characteristic; for receiving support from both family members and carers (or other carer arrangements), in contrast to relying solely on family members or friends; and for living in their own home with appropriate adaptations if needed, compared to considering other options. Individuals in higher income groups expressed a marginal preference to relocate to another neighborhood or city, as opposed to continuing to reside in their current neighborhood. Conversely, those in low-to-medium income groups expressed a slight preference to stay in their current neighborhood compared to moving to another neighborhood or city. Moreover, individuals in higher income groups demonstrate a lower likelihood of selecting a care model without technology when compared to individuals in other income groups. However, the willingness to pay (WTP) to live closer to community services is consistent across all income groups.
    
        * **Comparison by Experience of Care:** Individuals with experience of care are likely to value slightly more any other care arrangement (compared with relying solely on family members or friends), with people willing to pay more to receive support from carers arranged by the local authority (compared to care by family members or friends only). However, the direction of the results was opposite when we consider willingness to accept longer walking times (AWD): those with experience of care are less willing to walk further to local amenities for the same change. Other preferences are comparable across groups, using both WTP and AWD metrics.
        '''
        st.write(text)
    

with container3:
    st.markdown("""<style>.big-key-font {font-size:26px !important;font-weight: bold;}</style>""", unsafe_allow_html=True)
    #st.markdown('<p class="big-key-font">Collection of dashboards</p>', unsafe_allow_html=True)

    st.markdown('<p id="section-collection-of-dashboards" class="big-key-font">Collection of dashboards</p>', unsafe_allow_html=True)

    st.write(
        "This collection of dashboards was produced using Streamlit to enhance comprehension and interpretation of the DCE findings and to explore data in a more engaging and insightful way.")
    with st.popover("More details on Streamlit"):
        st.write("https://streamlit.io/ is an open-source Python library that makes it easy to create and share custom web applications for machine learning and data science.")        
        
    st.write("\n\nThe dashboards include four separate sets of visualizations:")
    st.page_link("pages/02_Frequency of choice and sociodemographic characteristics.py", label="**Demographic characteristics and frequency of choice:**", icon="1️⃣")
    st.write("\n\n Interactive bar charts and pie charts illustrating the demographic profile of respondents and how frequently different choices were made.")
    st.page_link("pages/03_Strength of preference for care characteristics.py", label="**Strength of preferences between service characteristics:**", icon="2️⃣")
    st.write("\n\n Interactive bar charts illustrating the relative importance and strength of preferences for various service characteristics.")
    st.page_link("pages/04_Trade-off between care characteristics.py", label="**Trade-off between characteristics:**", icon="3️⃣")
    st.write("\n\n Interactive bar charts showing how respondents trade-off between different service characteristics.")
    st.page_link("pages/05_Probability of people using different care options.py", label="**Service uptake probability:**", icon="4️⃣")
    st.write("\n\n More visualizations predicting the likelihood of service uptake based on the analyzed DCE data."
    )
    st.empty()
    
    
    st.write("---")
    st.markdown("""<style>.big-key-font {font-size:26px !important;font-weight: bold;}</style>""", unsafe_allow_html=True)
    st.markdown('<p class="big-key-font">The team</p>', unsafe_allow_html=True)


    st.write(
        "Authors of the research: Magdalena Walbaum, Michela Tinelli, Martin Knapp, and Raphael Wittenberg, Care Policy Evaluation Centre (CPEC) at the LSE.\n\nAuthors of the visualizations: Michela Tinelli, Eha Joshi, and Vencky Sharma, CPEC at the LSE."
    )
    st.empty()
    st.write("---")

    st.markdown("""<style>.big-key-font {font-size:26px !important;font-weight: bold;}</style>""", unsafe_allow_html=True)
    st.markdown('<p class="big-key-font">Disclaimer</p>', unsafe_allow_html=True)

    st.write(
        "Please note that this research was funded through the National Institute for Health and Care Research (NIHR) Policy Research Unit in Older People and Frailty (funding reference PR-PRU-1217-2150). As of 01.01.24, the unit has been renamed to the NIHR Policy Research Unit in Healthy Ageing (funding reference NIHR206119). The views expressed are those of the author(s) and not necessarily those of the NIHR or the Department of Health and Social Care."
    )
    st.empty()
    col1,col2,col3,col4, col5 = st.columns([1,1,1,1,1])
        #images
    with col1: 
        #Display the image in Streamlit
        st.image(image15, use_column_width=True)
    with col2:
        st.image(image16, use_column_width=True)
    with col3:
        st.image(image17, use_column_width=True)
    with col4:
        st.image(image18, use_column_width=True)
    with col5:
        st.image(image19, use_column_width=True)
    


