#This uses a lightweight python image as it is a small python program
FROM python:3.9-slim

#Chooses the directory of inside the container
WORKDIR /app

#This copies the script into the container
COPY calculator.py .

#This exposes a port to access it on here it is set to 5050,
#therefore can be accessed on localhost:5050
ENV PORT 5050
EXPOSE $PORT

#This runs the calculator program
CMD ["python", "calculator.py"]
