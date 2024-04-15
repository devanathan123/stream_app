import streamlit as st
import pyrebase
import requests

firebaseConfig = {
  'apiKey': "Your-API-Key",
  'authDomain': "Your-Auth-Domain",
  'projectId': "Your-Project-ID",
  'storageBucket': "Your-Storage-Bucket",
  'messagingSenderId': "Your-Messaging-Sender-ID",
  'appId': "Your-App-ID",
  'measurementId': "Your-Measurement-ID"
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
