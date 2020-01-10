FROM python:3.8

#ADD . /code
#
#WORKDIR /code
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#CMD ["ls"]
#
#CMD ["python", "/code/runFlask.py"]



#RUN adduser -D flask
#
#WORKDIR /home/flask
#
#COPY requirements.txt requirements.txt
#RUN python -m venv venv
#RUN venv/bin/pip install -r requirements.txt
#
#
#
#COPY app app
#
#ENV FLASK_APP runFlask.py
#
#[]
#

WORKDIR /code
ENV FLASK_APP runFlask.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]