import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import base64

# Set the title of the app
st.title('Presagio Profiler App')

# Welcome message
st.markdown("""
**Welcome to the Presagio Profiler App!**

Upload your CSV file and get an automated EDA report. You can also download a complete report by clicking the link below.
""")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

def get_html_download_link(html_string, filename="profile_report.html"):
    """Generates a link allowing the data in a given panda dataframe to be downloaded"""
    b64 = base64.b64encode(html_string.encode()).decode()
    return f'<a href="data:text/html;base64,{b64}" download="{filename}">Download HTML report</a>'

if uploaded_file is not None:
    # To read csv file with Pandas
    df = pd.read_csv(uploaded_file)

    # Generate the pandas profiling report
    st.write('Generating report...')
    profile = ProfileReport(df, explorative=True)
    report_html = profile.to_html()

    # Generate download link for the report
    st.markdown(get_html_download_link(report_html), unsafe_allow_html=True)

    # Attempt to display the report in the app (this may not work well for large reports)
    st.components.v1.html(report_html, height=1500, scrolling=True)
