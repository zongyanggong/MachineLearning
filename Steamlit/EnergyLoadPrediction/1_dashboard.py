import time

import streamlit as st
import pandas as pd
import base64
import pymongo

st.set_page_config(
    page_title="Dash board App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    [data-testid="stSidebar"]  {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: 250px;
        background-repeat: no-repeat;
        background-position: 4px 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('CollegeAhuntsic_Logo.png')

st.sidebar.header('Dashboard `Version 2`')

client = pymongo.MongoClient("localhost")
db = client.lorawan
collection = db.livedata
placeholder = st.empty()

while(True):
    df = pd.DataFrame(list(collection.find()))
    df = df.drop(['_id'], axis=1)
    df = df.set_index('date')
    df = df.sort_values('date', ascending=False)

    with placeholder.container():
        st.markdown('### Inside condition')
        col31, col32, col33, col34 = st.columns(4)
        col31.metric("Temp.", format(df.iloc[0]['t1'], '.2f') + " °C",
                     format(df.iloc[0]['t1'] - df.iloc[1]['t1'], '.2f') + " °C")
        col32.metric("Humidity.", format(df.iloc[0]['rh_1'], '.2f') + " %",
                     format(df.iloc[0]['rh_1'] - df.iloc[1]['rh_1'], '.2f') + " %")
        col33.metric("Appliance", format(df.iloc[0]['appliances'], '.2f') + " wh",
                     format(df.iloc[0]['appliances'] - df.iloc[1]['appliances'], '.2f') + " wh")
        col34.metric("Light", format(df.iloc[0]['lights'], '.2f') + " wh",
                     format(df.iloc[0]['lights'] - df.iloc[1]['lights'], '.2f') + " wh")
        # Row A
        st.markdown('### Outside Weather')
        col11, col12= st.columns(2)
        col11.metric("Temp.", format(df.iloc[0]['t_out'], '.2f') +" °C", format(df.iloc[0]['t_out'] - df.iloc[1]['t_out'], '.2f') + " °C")
        col12.metric("Humidity.", format(df.iloc[0]['rh_out'], '.2f') +" %", format(df.iloc[0]['rh_out'] - df.iloc[1]['rh_out'], '.2f') + " %")



        col21, col22, col23, col24 = st.columns(4)
        col21.metric("Press.", format(df.iloc[0]['press_mm_hg'], '.1f') + " mmHg",
                     format(df.iloc[0]['press_mm_hg'] - df.iloc[1]['press_mm_hg'], '.1f') + " mmHg")
        col22.metric("Windspeed", format(df.iloc[0]['windspeed'], '.2f') + " mph",
                     format(df.iloc[0]['windspeed'] - df.iloc[1]['windspeed'], '.2f') + " mph")
        col23.metric("Visibility.", format(df.iloc[0]['visibility'], '.2f') + " m",
                     format(df.iloc[0]['visibility'] - df.iloc[1]['visibility'], '.2f') + " m")
        col24.metric("Tdewpoint", format(df.iloc[0]['tdewpoint'], '.2f') + " °C Td",
                     format(df.iloc[0]['tdewpoint'] - df.iloc[1]['tdewpoint'], '.2f') + " °C Td")



        st.dataframe(df)
