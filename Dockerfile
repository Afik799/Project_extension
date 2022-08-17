FROM python:3.7-alpine
COPY . /rest_app
WORKDIR /rest_app
RUN pip install -r requirements.txt
CMD ["python3", "rest_app.py"]
