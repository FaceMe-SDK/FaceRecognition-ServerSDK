FROM ubuntu:20.04
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-opencv
RUN apt-get install -y libcurl4-openssl-dev libssl-dev
RUN mkdir -p /root/faceme_recog
RUN mkdir -p /root/faceme_recog/bin
RUN mkdir -p /root/faceme_recog/flask
RUN mkdir -p /root/faceme_recog/model
RUN mkdir -p /root/faceme_recog/python
WORKDIR /root/faceme_recog
COPY ./bin ./bin
COPY ./flask ./flask
COPY ./model ./model
COPY ./python ./python
COPY ./bin/linux_x86_64/libimutils.so /usr/lib
COPY ./bin/linux_x86_64/openvino /usr/lib
WORKDIR /root/faceme_recog/flask
RUN pip3 install -r requirements.txt
CMD [ "python3", "app.py"]
EXPOSE 8888
