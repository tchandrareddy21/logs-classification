import streamlit as st
import requests
import pandas as pd
from exception import LoggerException
from logger import logging
import io, sys
import subprocess
import time

FASTAPI_URL = "http://127.0.0.1:8000/classify/"

st.title("Logs Classification App")

# Function to start FastAPI in the background
def start_fastapi():
    if "fastapi_process" not in st.session_state:
        st.session_state.fastapi_process = subprocess.Popen(["python", "fastapi_backend.py"])
        time.sleep(3)  # Wait for FastAPI to start


# Start FastAPI automatically
start_fastapi()

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
try:
    if uploaded_file is not None:
        st.write("✅ File uploaded successfully!")
        logging.info("File uploaded successfully!")

        # Display the uploaded file
        df = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded file:", df.head())
        logging.info("Preview of uploaded file:", df.head())

        if st.button("Classify Logs"):
            # Send file to FastAPI
            logging.info("Classify Logs button is clicked!")
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            logging.info("Calling backend sever")
            response = requests.post(FASTAPI_URL, files=files)

            if response.status_code == 200:
                # Convert received CSV content into a DataFrame
                output_csv = response.content
                df_classified = pd.read_csv(io.BytesIO(output_csv))

                st.success("Classification complete! Download the classified file below.")
                logging.info("Classification complete!")
                # Display classified results
                st.write(df_classified.head())

                # Download link for the classified CSV
                st.download_button(
                    label="Download Classified Logs",
                    data=output_csv,
                    file_name="classified_logs.csv",
                    mime="text/csv"
                )
            else:
                logging.error("Failed to classify the logs. Please try again.")
                st.error("Failed to classify the logs. Please try again.")


except Exception as e:
    raise LoggerException(e, sys)