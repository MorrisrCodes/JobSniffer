import streamlit as st
import utils as utl
from views import home,Misson,testpage,data_view

st.set_page_config(layout="centered", page_title='Main Page')

st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "Misson":
        Misson.load_view()
    elif route == "testpage":
        testpage.load_view()
    elif route == "data_view":
        data_view.load_view()

navigation()

