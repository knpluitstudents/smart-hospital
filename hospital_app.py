import streamlit as st
import pandas as pd
import numpy as numpy 
import pickle
import os

st.set_page_config(
    page_title="Smart Hospital Patient Navigator",
    page_icon="",
    layout="wide"
)
st.markdown("""
<style>
    html,body,[class*="css"] {font-family:'Times New Roman', Times, serif;}
    #MainMenu {visibility:hidden;}
    header[data-testid="stHeader"]{display:none;}
    .stDeployButton {display:none;}
    footer{visibility:hidden;}
    .block-container{
        padding-top: 0 !important; padding-bottom:2rem !important;
        max-width:1100px !important;
    }
    div[data-testid="stForm"] {border:none; padding:0;}
    div.stButton > button{
        background: linear-gradient(135deg,#1a56db, #1e429f ) !important;
        color:white !important; border: none !important;
        border-radius_12px !important;  padding:0,75rem 2 rem !important;
        width= 100% !important; letter-spacing: 0.02em !important;
        box-shadow: 0 4px 14px #1a56db59 !important;
    }
        div.stButton > button:hover{
            background: linear-gradient(123deg, #1e429f, #1a56db) !important
        }
    div[data-testid="stChekbox"] label {
        font-size:14px !important; font-weight:500 !important;
        color:#37451 !important;
    }
</style>
"""), unsafe_allow_html=True)

