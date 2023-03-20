import streamlit as st
from components import authenticate as authenticate

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("## Welcome to Stock-Intelligence App!👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    ### **👈 Select a translator from the sidebar**
    
    ### Features
    - Translation Console like Google or Papago style
    
    The function is only available when logged in, Accounts can only be issued in consultation with the Financial AI Center.
   """
)

authenticate.initialize_st_state_vars()
if not st.session_state["authentication_status"]:
    authenticator = authenticate.set_user_credential()
    name, authentication_status, username = authenticator.login("Login","main")
    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Some content')
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')
