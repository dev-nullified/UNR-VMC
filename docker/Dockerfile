FROM python:3.8

# Build Requirements file from pipenv
ENV FLASK_APP wsgi.py



WORKDIR /code

# Install pipenv
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

# Create requirements file 
COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock
COPY wsgi.py /code/wsgi.py
COPY .env /code/.env

RUN pipenv install



# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
#COPY . .
CMD ["pipenv", "run", "flask"]