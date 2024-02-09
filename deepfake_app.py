import streamlit as st
import numpy as np
from tensorflow import keras

# Function to load the trained model
def load_model():
    model_path = 'deepfake_model.h5'  # Replace with the correct path to your trained model
    print(f"Attempting to load model from: {model_path}")
    model = keras.models.load_model(model_path)
    print("Model loaded successfully!")
    return model

# Placeholder for model loading and prediction function
def predict_deepfake(video_path):
    # Replace this with your actual model loading and prediction logic
    # For example, you can use a pre-trained model and appropriate preprocessing
    prediction = np.random.choice(['FAKE', 'REAL'], p=[0.4, 0.6])
    # Print or save the prediction for the entire sequence
    return prediction

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Your authentication logic here (e.g., database query, API call)
        # For simplicity, let's just consider any non-empty username/password as valid
        if username and password:
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password. Please try again.")

# Function for detection page
def detection():
    # Display sidebar with description
    st.sidebar.title("👇 DESCRIPTION 👇")
    st.sidebar.markdown(
        """
        " 📌 1. Protecting reputations: Expose misinformation and prevent fabricated scandals from harming individuals or businesses."

        " 📌 2. Combating fraud: Detect manipulated financial statements, fake identities, and deepfaked scams before they cause real damage."

        " 📌 3. Strengthening democracy: Safeguard elections by identifying deepfaked political propaganda and ensuring informed voting."

        " 📌 4. Securing the future: Lay the groundwork for a more reliable digital landscape where truth and trust can thrive."
        """
    )

    uploaded_file = st.file_uploader("Choose a video file", type=["mp4"])
    if uploaded_file is not None:
        st.video(uploaded_file)
        if st.button("Detect Deep Fake", key="detect_button"):
            prediction = predict_deepfake(uploaded_file)
            st.success(f"The video is predicted as: {prediction}")

# Main function for Streamlit app
def main():
    st.markdown(
        """
        <style>
            body {
                background-color: #87CEEB;
            }
            .app-container {
                padding: 20px;
                margin: 0;
            }
            .title {
                color: #800080 !important;
            }
            .footer {
                text-align: center;
                margin-top: 20px;
            }
            .footer a {
                margin: 0 10px;
                text-decoration: none;
                color: #fff;
                font-weight: bold;
                transition: all 0.3s ease;
            }
            .footer a:hover {
                color: #00f;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="app-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="title"> 🤖 🌐DeepVerify360🌐 🤖 </h1>', unsafe_allow_html=True)

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login()
    else:
        detection()

    st.markdown('</div>', unsafe_allow_html=True)

    # Logout button
    if st.session_state.logged_in:
        if st.button("Logout"):
            st.session_state.logged_in = False

    # Footer
    st.markdown(
        """
        <div class="footer">
            <a href="mailto:mangeshsshinde2016@gmail.com">📧 Email</a>
            <a href="https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile">🔗 LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
c
if __name__ == "__main__":
    main()
