FROM ubuntu:bionic
MAINTAINER fnndsc "yarenty@gmail.com"

RUN apt-get update \
  && apt-get install -y python3.7 python3-pip \
  && python3.7 -m pip install pip \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3.7 python \
  && pip3 install --upgrade pip

RUN apt-get -y install vim

RUN apt -y install python3.7 curl python3-distutils \
  && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
  && python3.7 get-pip.py

RUN pip3 install https://ms-release.obs.cn-north-4.myhuaweicloud.com/0.2.0-alpha/MindSpore/cpu/x86_ubuntu/mindspore-0.2.0-cp37-cp37m-linux_x86_64.whl

COPY test_mul.py /opt
COPY test_add.py /opt

WORKDIR /opt

ENTRYPOINT ["bash"]
