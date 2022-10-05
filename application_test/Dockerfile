FROM ubuntu:20.04

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/America/Bogota /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt update -y
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt install -y python3 python3-pip 


ADD ./ /usr/src/app
RUN chmod ugo+rwx /usr/src/app/app/api
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi
#RUN flask shell

CMD ["uwsgi", "uwsgi.ini"]
