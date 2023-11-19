import streamlit as st
import utils as utl
from views import home,Misson,testpage,data_view
import pandas as pd
import plotly.express as px
from auth import *

st.set_page_config(layout="centered", page_title='Main Page')

st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    
    # Check if route is None or invalid, then redirect to home
    if not route:
        home.load_view()
    elif route == "home":
        home.load_view()
    elif route == "Misson":
        Misson.load_view()
    elif route == "data_view":
        data_view.load_view()
    elif route == "testpage":
        testpage.load_view()
   
        
navigation()
