# test-app
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import requests
from PIL import Image
from io import BytesIO
#from config import GITHUB_PAT
import os
from dotenv import load_dotenv

# Load environment variables from .env or app.env file
load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
REPO_NAME = os.getenv('REPO_NAME')
FILE_PATH = os.getenv('FILE_PATH')

# Function to fetch data from the private GitHub repository
def fetch_private_data(token, username, repo, path):
    url = f"https://api.github.com/repos/{username}/{repo}/contents/{path}"
    headers = {
        'Authorization': f'token {token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_content = response.json()['content']
        decoded_content = base64.b64decode(file_content)
        return pd.read_excel(BytesIO(decoded_content))
    else:
        st.error("Failed to fetch data.")
        return None

# Fetch the data
data = fetch_private_data(GITHUB_TOKEN, GITHUB_USERNAME, REPO_NAME, FILE_PATH)

if data is not None:
    # Display the data in the Streamlit app
    st.title("Private Data Dashboard")
    st.write("Here is your private data:")
    st.dataframe(data)
else:
    st.write("No data to display.")

#Page Configuration
st.set_page_config(
    page_title="Frequency of choice and sociodemographic characteristics",
    page_icon="⭐️",
    layout="wide",
    initial_sidebar_state="expanded")

# Load the data
df = pd.read_excel('Cohort2.xlsx')

#re-encodeing
df['Housing'] = df['Housing'].astype('category').cat.rename_categories(
    {
        0: 'Own a home with appropriate adaptation if required',
        1: 'Family members/friend\'s home',
        2: 'Retirement village',
        3: 'Sheltered housing ',
    }
    )

df['Location'] = df['Location'].astype('category').cat.rename_categories(
    {
        0: 'Remain in current neighbourhood ',
        1: 'Move to other neighbourhood',
    }
    )

df['Provider'] = df['Provider'].astype('category').cat.rename_categories(
    {
        0: 'Family members/friends',
        1: 'Carers arranged by local authority',
        2: 'Carers arranged using direct payment scheme',
        3: 'Family members and carers',
    }
    )
df['Identity'] = df['Identity'].astype('category').cat.rename_categories(
    {
        0: 'Carer resepcts your beliefs/values-Yes ',
        1: 'Carer resepcts your beliefs/values-No',
    }
    )
df['Access'] = df['Access'].astype('category').cat.rename_categories(
    {
        0: 'Within 10 min access to community services',
        1: 'Within 20 min access to community services',
        2: 'Within 30 min access to community services',
        3: 'More than 30 min access to community services',
    }
    )

df['Tecno'] = df['Tecno'].astype('category').cat.rename_categories(
    {
        0: 'No use of monitoring technology',
        1: 'Yes, but only non-wearable sensors',
        2: 'Yes, including wearable smart devices',
        3: 'Yes, including cameras',
    }
    )
df['Cost'] = df['Cost'].astype('category').cat.rename_categories(
    {
        0: 'Up to £25',
        1: '£35',
        2: '£75',
        3: '£100 or more',
    }
    )
#rename columns
old_names = ['AGEBAND','D3ethn','D13inc','B3Care_1','B3Care_2','B3Care_3','Housing','Provider','Identity','Access','Tecno','Cost']
new_names = ['Age','Ethnicity','Income','Experience of care','Current Unpaid Care Receiver','Current Care Provider','Housing setting','Provider of care','Respect for their identity','Access to community services', 'No use of technology devices','Social care cost']
rename_diction = dict(zip(old_names,new_names))
df = df.rename(columns=rename_diction)

# Your GitHub username and Personal Access Token
username = "CareQualityEvaluation"
token = f"{GITHUB_PAT}"

# The raw URL of your image in the private repository
repo = "OPFPRU"
path_to_image = "images/access.png"
branch = "main"
url15 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/logo1.png"
url16 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/logo2.png"
url17 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/logo3.png"
url18 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/logo4.png"
url19 = f"https://raw.githubusercontent.com/CareQualityEvaluation/OPFPRU/main/images/logo5.png"

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


with st.sidebar:
    st.markdown("""<style>.big-font {font-size:20px !important;font-weight:bold}</style>""", unsafe_allow_html=True)
    st.markdown('<p class="big-font">Frequency of choice and sociodemographic characteristics: a quick description of what information you can find here.</p>', unsafe_allow_html=True)
    st.write('The upper part of the tab, provides you information on the population of 1820 individuals who completed the DCE survey and provided full data for analysis:')
    text = """
    * Frequency of choice: This dashboard presents an overview of the frequency breakdown of survey respondents' care attribute (or characteristic) preferences. It details how often each care attribute’s level was selected. 

    * Sociodemographic of the population: This dashboard presents an overview of the demographic breakdown of the total survey population. 
    """
    st.write(text)
    st.write("""
    The lower section of the tab offers subgroup analysis based on sociodemographic characteristics. It presents data on the frequency of service characteristic choices previously selected. This data indicates how often each level of care attribute was chosen within specific subgroups of the population, based on the demographic aspects selected earlier.
    """)
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
                                                            
# Frequency Breakdown Pie Chart
def makepie_figure (selected_attribute):
    colors = ['#FFD400','#2FC0BA','#64285D','#00636A']
    frequency = df[selected_attribute].value_counts().reset_index()
    frequency.columns = ['Labels', 'Frequency']
    pie_chart = go.Figure(data = [go.Pie(labels=frequency['Labels'], values=frequency['Frequency'])])

    pie_chart.update_traces(marker=dict(colors=colors,line=dict(color='#000000',width=2)))
    return pie_chart
    
#Static Histograms
def static_histogram_figure(input_df,demch_column):
    
    histogram_chart = px.histogram(input_df, x = input_df[demch_column],histnorm ='percent')
    histogram_chart.update_traces(marker_color='teal')
    histogram_chart.update_layout(title = demch_column, 
                                  yaxis_title="Percentage",
                                  bargap=.2, 
                                  xaxis=dict(titlefont=dict(size=20)),
                                  yaxis=dict(titlefont=dict(size=20)))
    return histogram_chart

    
#Subgroup Histograms
df['Gender'] = df['Gender'].apply(lambda x: "Female" if x == 2 else "non-Female")
df['Ethnicity'] = df['Ethnicity'].apply(lambda x: 'White British' if x in [1] else ('Indian' if x in [9] else ('Irish' if x in [2] else ('Other White' if x in [4] else ('African' if x in [14] else ('Chinese' if x in [12] else ('Caribbean' if x in [15] else ('Prefer not to say' if x in [19,20] else ('Other' if x in [3, 16, 11, 17, 18, 6, 8, 13, 7, 10, 5] else x)))))))))
df['Income'] = df['Income'].apply(lambda x: 'Low' if x in [1, 2, 3] else ('Med' if x in [4, 5, 6, 7] else ('High' if x in [8, 9, 10, 11] else ('Prefer not to say' if x == 12 else x))))
df['Age'] = df['Age'].apply(lambda x: '50-59' if x in [5] else ('60-69' if x in [6] else ('70-79' if x in [7] else ('80+' if x in [8,9] else ('Prefer not to say' if x ==997 else x)))))
df['Experience of care'] = df['Experience of care'].apply(lambda x: 'Yes' if x in [1] else ('No' if x in [2] else ('Unknown' if x in [3] else ('Prefer not to say' if x == 4 else x))))
df['Current Unpaid Care Receiver'] = df['Current Unpaid Care Receiver'].apply(lambda x: 'Yes' if x in [1] else ('No' if x in [2] else ('Unknown' if x in [3] else ('Prefer not to say' if x == 4 else x))))
df['Current Care Provider'] = df['Current Care Provider'].apply(lambda x: 'Yes' if x in [1] else ('No' if x in [2] else ('Unknown' if x in [3] else ('Prefer not to say' if x == 4 else x))))

def sub_histogram_figure_gender (input_filtered_df_gender,selected_attribute):
    color_discrete_map = {
        "Yes": "#2FC0BA",  
        "No": "#00636A",
        "Unknown": "#64285D",
        "Prefer not to say": "#FFD400",
        "Low": "#2FC0BA", 
        "Med": "#00636A", 
        "High": "#64285D", 
        "50-59": "#2FC0BA",
        "60-69": "#00636A", 
        "70-79": "#64285D", 
        "80+": "#FFD400"
    }
    
    histogram_chart = px.histogram(input_filtered_df_gender, 
                                   x = selected_attribute,
                                   histnorm ='percent',
                                   color=selected_demch, 
                                   barmode='group', 
                                   color_discrete_map=color_discrete_map) 

    histogram_chart.update_layout(title = 'Sub Group '+selected_demch, 
                                  yaxis_title="Percentage",
                                  xaxis_title = str(selected_attribute),
                                  bargap=.2,
                                  xaxis_range =[-1,5],
                                  xaxis=dict(titlefont=dict(size=20)),
                                  yaxis=dict(titlefont=dict(size=20)))
    return histogram_chart

 
#Layout

# Create containers
container1 = st.container(border = True)
container2 = st.container(border = True)
container3 = st.container(border = True)

with container1:
    col1,col2 = st.columns([1,1])  # Create two columns with 1:1 width

    with col1:
        st.markdown("""<style>.big-key-font {font-size:26px !important;font-weight: bold;}</style>""", unsafe_allow_html=True)
        st.markdown('<p class="big-key-font">Frequency of choice for the overall population (n= 1820)</p>', unsafe_allow_html=True)
        characteristics_explain={'Characteristics': ['Housing setting', 'Location', 'Provider of care','Respect for their identity','Access to community services ','No use of technology devices','Social care cost to the service user'],
        'Possible values ':['Own home with appropriate adaptation if required. Compared with other options (such as family member of friend’s home, retirement village or sheltered housing).',
                        'Staying in the same neighbourhood (compared with moving elsewhere).',
                        'Provider 1 = Receiving support from carers arranged by your local authority; Provider 2 = From carers arranged by you using a direct payment scheme or your own resources; Provider 3 = From both family members and carers (type of arrangement may vary). (Compared with receiving support from either family members or friends only).', 
                        'Receiving care from someone that respect your beliefs and values (compared with no respect for their identity).',
                        'Walking distance from community services in minutes.',
                        'No use of technology devices. Compared with use of technology: Yes, but only non-wearable sensors such as pressure mats or smoke alarm; Yes, including wearable devices to monitor vital signs such as smart watches; Yes, including cameras to monitor home environment.', 
                        'In £ per week. Please note that the possible values of weekly costs were illustrative. The actual cost to the service user would vary depending on where the person lives, and on their income and savings, since public funding of adult social care is means tested.']}

        df_characteristics_explain = pd.DataFrame(characteristics_explain)
        
        st.write("First choose a characteristic of care from the dropdown menu below to visualise its distribution among the population. Full details are provided here")
    
        with st.popover("Characteristics of care"):
            st.write("Care provision scenarios were described according the following characteristics and assigned possible values.")
            st.dataframe(df_characteristics_explain,hide_index=True)
            st.write("Please note that for housing, we combined all other options different from your own home into one category, as the individual alternatives were not statistically significant. The same applied to use of technology devices. Access to community services and social care costs to the service user were considered as continuous variables.")
            
        attributes_list = ["Housing setting", "Location", "Provider of care", "Respect for their identity", "Access to community services", "No use of technology devices", "Social care cost"]
        selected_attribute = st.selectbox('Select a preference characteristic', attributes_list,
                                          index=len(attributes_list) - 1)
        pie_chart = makepie_figure(selected_attribute)
        st.plotly_chart(pie_chart, use_container_width=True)


    
    with col2:  
        st.write("")
        st.markdown('<p class="big-key-font">Demographics of the total group (n= 1820)</p>', unsafe_allow_html=True)
        # demographic choice selector
        
        st.write("Then select a sociodemographic feature from the dropdown menu below to visualise the distribution of population percentages. Full details are provided here")
        
        subgroup_explain={'Characteristic': ['Age', 'Income', 'Experience of care'],
        'Subgroups compared':['Total number of respondents are divided into four age groups: 50-60, 60-70-,70-80 and 80+.','Total number of respondents are divided into three household income groups: low (≤ £30,000 per year), middle (£30,001-70,000 per year), and high (≥ £70,000 per year) income.', 'Total number of respondents are divided into two groups based on their previous experience of whether they were receiving care support or not: care user and no care user']}
        df_subgroup_explain = pd.DataFrame(subgroup_explain)
    
        with st.popover("Sociodemographic features"):
            st.write("Sociodemographic features considered are listed below.")
            st.dataframe(df_subgroup_explain,hide_index=True)

        demch_list = ["Age", "Income", "Experience of care"]
        selected_demch = st.selectbox('Select a demographic characteristic', demch_list, index=len(demch_list) - 1)
        if selected_demch == "Age":
            df = df.sort_values(by='Age', ascending=True)
        elif selected_demch == "Income":
            df['Income'] = pd.Categorical(df['Income'],
                                          categories=['Low', 'Med', 'High', 'Unknown', 'Prefer not to say'])
            df = df.sort_values(by='Income', ascending=True)
        elif selected_demch == "Experience of care":
            df['Experience of care'] = pd.Categorical(df['Experience of care'],
                                                      categories=['Yes', 'No', 'Unknown', 'Prefer not to say'])
            df = df.sort_values(by='Experience of care', ascending=True)
        else:
            pass

        histogram_1 = static_histogram_figure(df, selected_demch)
        st.plotly_chart(histogram_1, width=30, height=30)
        
with container2:
    col1, col2 = st.columns(2)  # Create two columns with equal width

    with col1:
        st.markdown('<p class="big-key-font">Frequency of choice according to subgroups</p>', unsafe_allow_html=True)
        st.write("Based on the care characteristic and demographic characteristic selected above, the following visualisation shows how often each care characteristic is chosen (percentage) within the selected sociodemographic groups.") 
        df = df.sort_values(by=selected_attribute,ascending=True)
        filtered_df = df[[selected_attribute, selected_demch]]
        if selected_demch =='Experience of care':
            filtered_df2 = filtered_df[filtered_df['Experience of care'].isin(['Yes', 'No'])]
            st.write("<p style='font-size:12px;'>Please note that respondents who answered ‘prefer not to say’ or ‘unknown’ were excluded from the analysis, as they accounted for less than 1% of the total responses.", unsafe_allow_html=True)
        elif selected_demch =='Age':
            filtered_df2 = filtered_df[filtered_df['Age'].isin(['50-59', '60-69', '70-79','80+'])]
            st.write("<p style='font-size:12px;'>Please note that respondents who answered ‘prefer not to say’ or ‘unknown’ were excluded from the analysis, as they accounted for less than 1% of the total responses.", unsafe_allow_html=True)
        else:
            filtered_df2 = filtered_df[filtered_df['Income'].isin(['Low','Med','High', 'Unknown', 'Prefer not to say'])]
        
        #st.dataframe(filtered_df2)
        histogram_5 = sub_histogram_figure_gender(filtered_df2, selected_attribute)
        st.plotly_chart(histogram_5, use_container_width=True, width=30, height=30)

# custom_css_key_findings = """
#     <style>
#     .my-container {
#      background-color: #d6f5f3;
#      padding: 20px; border: 3px solid #08636B
#      border-radius: 10px;
#     }
#     </style>
#     """


#     st.markdown("""<style>.big-key-font {font-size:26px !important;font-weight: bold;}</style>""", unsafe_allow_html=True)
#     st.markdown('<p class="big-key-font">Key Findings from the DCE Questions.</p>', unsafe_allow_html=True)
#     st.markdown(custom_css_key_findings, unsafe_allow_html=True)
#     # Use the custom class in a container
#     st.markdown('<div class="my-container">.</div>', unsafe_allow_html=True)
    with col2:
        custom_css_key_findings = """
        <style>
        .my-container {
         background-color: #d6f5f3;
         padding: 20px; border: 30px solid #c1f0ee
         border-radius: 10px;
        }
        </style>
        """
        st.markdown('<p class="big-key-font">Key messages</p>', unsafe_allow_html=True)
        st.markdown(custom_css_key_findings, unsafe_allow_html=True)
        st.markdown('<div class="my-container">This tab provides a comprehensive look at who the survey respondents are, what care attributes (or characteristic) they prioritise, and how these preferences vary across different demographic groups. By leveraging this data, you can better understand the needs and preferences of different segments of the population, allowing for more targeted and effective decision-making.</div>', unsafe_allow_html = True)
        if selected_attribute == 'Housing setting' and selected_demch == "Age":
            # Display additional text specific to sub-options
            st.markdown('''**:green-background[Total population analysis:]** :green-background[Respondents mostly chose to either live in a retirement village or in sheltered housing. There are nearly equal number of respondents who chose to live in a family member or friend’s home or live in their own a home with appropriate adaption if required.]''')
            st.markdown('<div class="my-container">Subgroup Analysis by age groups: Comparable results were observed across all age subgroups.', unsafe_allow_html = True)
        elif selected_attribute == 'Location' and selected_demch == "Age":
            # Display additional text specific to sub-options
            st.markdown('<div class="my-container">Total population analysis: More than half of all respondents chose to remain in their current neighbourhood', unsafe_allow_html = True)
            st.write("**Subgroup Analysis by age groups:** Comparable results were observed across all age subgroups.")
        elif selected_attribute == 'Provider of care' and selected_demch == "Age":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** The greatest number of respondents chose to have either a family member as a care provider or a carer that is arrange by the local authorities. Secondly, there are equal number of respondents that chose to have their care provider be arrange by local authority and respondents that chose to have their care provider be family members/friends. Lastly, the least number of respondents chose to arrange their own care providers using direct payment schemes.")
            st.write("**Subgroup Analysis by age groups:** Comparable results were observed across all age subgroups.")        
        elif selected_attribute == 'Respect for their identity' and selected_demch == "Age":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** More than half of all respondents chose to have a carer that respects their values and beliefs.")
            st.write("**Subgroup Analysis by age groups:** Comparable results were observed across all age subgroups.")        
        elif selected_attribute == 'Access to community services' and selected_demch == "Age":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** Most respondents opted to live within a 10-minute walking distance from community services. Other options were chosen equally.")
            st.write("**Subgroup Analysis by age groups:** Comparable results were observed across all age subgroups.")               
        elif selected_attribute == 'No use of technology devices' and selected_demch == "Age":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** Most respondents opted for no use of monitoring technology. Other options (monitoring technology types) were equally chosen.")
            st.write("**Subgroup Analysis by age groups:** Comparable results were observed across all age subgroups.")        
        elif selected_attribute == 'Social care cost' and selected_demch == "Age":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** The highest number of respondents chose to pay the highest costs per week.")
            st.write("**Subgroup Analysis by age groups:** Comparable results were observed across all age subgroups.") 
        else:
            st.write ("")

        if selected_attribute == 'Housing setting' and selected_demch == "Income":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** Respondents mostly chose to either live in a retirement village or in sheltered housing. There are nearly equal number of respondents who chose to live in a family member or friend’s home or live in their own a home with appropriate adaption if required.")
            st.write("**Subgroup Analysis by income groups:** Comparable results were observed across all three income subgroups.")
        elif selected_attribute == 'Location' and selected_demch == "Income":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** More than half of all respondents chose to remain in their current neighbourhood.")
            st.write("**Subgroup Analysis by income groups:** Comparable results were observed across all three income subgroups.")
        elif selected_attribute == 'Provider of care' and selected_demch == "Income":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** The greatest number of respondents chose to have either a family member as a care provider or a carer that is arrange by the local authorities. Secondly, there are equal number of respondents that chose to have their care provider be arrange by local authority and respondents that chose to have their care provider be family members/friends. Lastly, the least number of respondents chose to arrange their own care providers using direct payment schemes.")
            st.write("**Subgroup Analysis by income groups:** Comparable results were observed across all three income subgroups.")        
        elif selected_attribute == 'Respect for their identity' and selected_demch == "Income":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** More than half of all respondents chose to have a carer that respects their values and beliefs.")
            st.write("**Subgroup Analysis by income groups:** Comparable results were observed across all three income subgroups.")        
        elif selected_attribute == 'Access to community services' and selected_demch == "Income":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** Most respondents opted to live within a 10-minute walking distance from community services. Other options were chosen equally.")
            st.write("**Subgroup Analysis by income groups:** Comparable results were observed across all three income subgroups.")               
        elif selected_attribute == 'No use of technology devices' and selected_demch == "Income":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** Most respondents opted for no use of monitoring technology. Other options (monitoring technology types) were equally chosen.")
            st.write("**Subgroup Analysis by income groups:** Comparable results were observed across all three income subgroups.")        
        elif selected_attribute == 'Social care cost' and selected_demch == "Income":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** The highest number of respondents chose to pay the highest costs per week.")
            st.write("**Subgroup Analysis by income groups:** Comparable results were observed across all three income subgroups.") 
        else:
            st.write ("")

        if selected_attribute == 'Housing setting' and selected_demch == "Experience of care":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** Respondents mostly chose to either live in a retirement village or in sheltered housing. There are nearly equal number of respondents who chose to live in a family member or friend’s home or live in their own a home with appropriate adaption if required.")
            st.write("**Subgroup Analysis by experience of care:** Comparable results were observed across all subgroups.")
        elif selected_attribute == 'Location' and selected_demch == "Experience of care":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** More than half of all respondents chose to remain in their current neighbourhood.")
            st.write("**Subgroup Analysis by experience of care:** Comparable results were observed across all subgroups.")
        elif selected_attribute == 'Provider of care' and selected_demch == "Experience of care":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** The greatest number of respondents chose to have either a family member as a care provider or a carer that is arrange by the local authorities. Secondly, there are equal number of respondents that chose to have their care provider be arrange by local authority and respondents that chose to have their care provider be family members/friends. Lastly, the least number of respondents chose to arrange their own care providers using direct payment schemes.")
            st.write("**Subgroup Analysis by experience of care:** Comparable results were observed across all subgroups.")        
        elif selected_attribute == 'Respect for their identity' and selected_demch == "Experience of care":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** More than half of all respondents chose to have a carer that respects their values and beliefs.")
            st.write("**Subgroup Analysis by experience of care:** Comparable results were observed across all subgroups.")        
        elif selected_attribute == 'Access to community services' and selected_demch == "Experience of care":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** Most respondents opted to live within a 10-minute walking distance from community services. Other options were chosen equally.")
            st.write("**Subgroup Analysis by experience of care:** Comparable results were observed across all subgroups.")               
        elif selected_attribute == 'No use of technology devices' and selected_demch == "Experience of care":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** Most respondents opted for no use of monitoring technology. Other options (monitoring technology types) were equally chosen.")
            st.write("**Subgroup Analysis by experience of care:** Comparable results were observed across all subgroups.")        
        elif selected_attribute == 'Social care cost' and selected_demch == "Experience of care":
            # Display additional text specific to sub-options
            st.write("**Total population analysis:** The highest number of respondents chose to pay the highest costs per week.")
            st.write("**Subgroup Analysis by experience of care:** Comparable results were observed across all subgroups.") 
        else:
            st.write ("")

        

with container3: 
    col1,col2,col3,col4, col5 = st.columns([1,1,1,1,1])
        #images
    with col1: 
        #Display the image in Streamlit
        #st.image(image15, use_column_width=True)
        st.write("")
    with col2:
        #st.image(image16, use_column_width=True)
        st.write("")
    with col3:
        #st.image(image17, use_column_width=True)
        st.write("")
    with col4:
        #st.image(image18, use_column_width=True)
        st.write("")
    with col5:
        st.image(image19, use_column_width=True)
        
