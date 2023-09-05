FROM python:3.11
EXPOSE 5000
WORKDIR /app
# Install production dependencies.
COPY . .
RUN pip install -r requirements.txt
# Before trying to use app in Docker desktop, modify CMD as in Dockerfile (works with Docker)
# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app