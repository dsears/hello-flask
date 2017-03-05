FROM python:2.7
RUN apt-get -y update && apt-get -y upgrade
RUN pip install --upgrade pip && pip install flask
COPY . /app
WORKDIR /app
CMD ["bash", "run.sh"]
