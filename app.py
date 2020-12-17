import app1
import app2
import streamlit as st
PAGES = {
    "HOME": app1,
    "CLASSIFY EMAIL": app2
     
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()