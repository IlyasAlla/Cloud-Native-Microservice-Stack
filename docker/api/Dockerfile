FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN pip install flask pymongo
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
