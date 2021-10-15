FROM python:3.8

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --upgrade pip

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./Login.py"]
