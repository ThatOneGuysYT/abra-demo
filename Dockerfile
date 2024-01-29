FROM ubuntu

RUN apt-get update && apt-get -y install python3 python3-pip
RUN apt-get -y upgrade

RUN pip3 install flask

WORKDIR /app

COPY . .

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]