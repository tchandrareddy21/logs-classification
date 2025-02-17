FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000 8501
CMD ["bash", "start.sh"]