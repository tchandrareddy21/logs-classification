# Start FastAPI in the background
uvicorn fastapi_backend:app --host 0.0.0.0 --port 8000 --reload &

# Start Streamlit (Frontend)
streamlit run app.py --server.port 8501 --server.address 0.0.0.0