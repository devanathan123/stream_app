import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import exceptions as firebase_exceptions

# Check if Firebase Admin SDK is already initialized
if not firebase_admin._apps:
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate(r"C:\Users\HP\PycharmProjects\stream\josn_key\private_key.json")
    firebase_admin.initialize_app(cred)


# Define Streamlit app layout
def main():
    st.title("Firebase Authentication with Streamlit")

    # Display login page by default
    login()

    # Provide a link to sign up page
    st.markdown("New user? [Sign up here](signup)")

# Login page
def login():
    st.subheader("Login")

    # Input fields for email and password
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Button to trigger login
    if st.button("Login"):
        try:
            # Sign in the user with email and password
            user = auth.get_user_by_email(email)
            #firebase_admin.auth.verify_password(password, user.password_hash)
            st.success("Authentication successful. User ID: {}".format(user.uid))
        except firebase_exceptions.FirebaseError as e:
            st.error("Authentication failed: {}".format(e))

if __name__ == "__main__":
    main()

