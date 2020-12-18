import app1
import app2
import app3
import streamlit as st
PAGES = {
    "HOME": app1,
    "CLASSIFY EMAIL(with trained model)": app2,
    "CLASSIFY EMAIL(train new model)":app3
     
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()