FROM python:3.8-slim as app
RUN pip install flask
COPY . .
EXPOSE 8000
CMD ["flask", "--app", "main", "run", "-p", "8000","--host=0.0.0.0"]
