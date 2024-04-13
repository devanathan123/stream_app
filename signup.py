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
    signup()

    # Provide a link to sign up page
    st.markdown("Already Existing User? [Login here](Login)")


# Sign-up page
def signup():
    st.subheader("Sign Up")

    # Input fields for email, password, and confirm password
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    # Button to trigger sign-up
    if st.button("Sign Up"):
        if password == confirm_password:
            try:
                # Create a new user with email and password
                user = auth.create_user(email=email, password=password)
                st.success("Sign up successful. User ID: {}".format(user.uid))
            except firebase_exceptions.FirebaseError as e:
                st.error("Sign up failed: {}".format(e))
        else:
            st.error("Passwords do not match. Please retype the passwords.")

if __name__ == "__main__":
    main()

