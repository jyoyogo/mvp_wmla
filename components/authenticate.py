import os
import yaml
import streamlit as st
import streamlit_authenticator as stauth
# ------------------------------------
# Initialise Streamlit state variables
# ------------------------------------
def initialize_st_state_vars():
    """
    Initialize Streamlit state variables
    Returns:
        Nothing
    """
    if "authentication_status" not in st.session_state:
        st.session_state["authentication_status"] = None

# ----------------------------------
# Get authorization code after login
# ----------------------------------
def get_auth_config():
    """
    Gets auth_code state variable.
    Returns:
        parsed yaml data for credential.
    """
    try:
        with open('config.yaml') as file:
            config = yaml.load(file, Loader=stauth.SafeLoader)
        return config
    except Exception as e:
        raise RuntimeError("check credential yaml file")
    
# ----------------------------------
# Set authorization code after login
# ----------------------------------
def set_user_credential():
    """
    Sets auth_code state variable.
    Returns:
        Boolean
    """
    config = get_auth_config()
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    if 'username' in st.session_state:
        authenticator.username = st.session_state['username']
    return authenticator

# ----------------------------------
# Validate Credential
# ----------------------------------
def validate_credential():
    """
    Validate user credential in another pages, not main
    Returns:
        Boolean
    """
    if 'authentication_status' not in st.session_state or 'logout' not in st.session_state:
        return False
    else:
        if not st.session_state['authentication_status']:
            return False
        else:
            authenticator = set_user_credential()
            st.session_state['name'], st.session_state['authentication_status'], st.session_state['username'] = authenticator.login("Login", "main")
            return st.session_state['authentication_status']
