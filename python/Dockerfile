
FROM python:3-alpine

# Add your instructions to dockerize the application
# App must run on port 8000
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000:8000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000"]

#CMD [ "python", "./api.py" ]