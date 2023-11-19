import streamlit as st
import utils as utl
from views import home,Misson
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title='Main Page')

st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "Misson":
        Misson.load_view()
   
        
navigation()

