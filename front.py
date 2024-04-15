import streamlit as st
import pyrebase
import requests

firebaseConfig = {
  'apiKey': "AIzaSyD4BW3b9_7ZwO2pJ6Xp_imLc1YIkk-8y-U",
  'authDomain': "fir-ec695.firebaseapp.com",
  'projectId': "fir-ec695",
  'storageBucket': "fir-ec695.appspot.com",
  'messagingSenderId': "651558941637",
  'appId': "1:651558941637:web:be19b9b60cc38aadd111ac",
  'measurementId': "G-TH3ZJPWKM1"
}

# Initialize Pyrebase app
fb = pyrebase.initialize_app(firebaseConfig)
auth = fb.auth()

# Streamlit app layout
def main():
    st.title("Firebase Authentication with Streamlit")

    # Input fields for email and password
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")

    # Button to trigger sign-in
    if st.button("Sign In"):
        try:
            # Sign in the user with email and password
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("Authentication successful. User ID: {}".format(user['localId']))
        except Exception as e:
            st.error("Authentication failed: {}".format(e))

if __name__ == "__main__":
    main()
