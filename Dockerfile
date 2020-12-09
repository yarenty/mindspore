FROM ubuntu:bionic
MAINTAINER fnndsc "yarenty@gmail.com"

#installing python
RUN apt-get update \
  && apt-get install -y python3.7 python3-pip mc \
  && python3.7 -m pip install pip \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3.7 python \
  && pip3 install --upgrade pip

# vi - nice to have (for simple sesting)
RUN apt-get -y install vim

# python 3.7 - again by default currently there is 3.6 - which doesn't work with mindspore
RUN apt -y install python3.7 curl python3-distutils \
  && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
  && python3.7 get-pip.py

# getting current version of mindspore
RUN pip3 install https://ms-release.obs.cn-north-4.myhuaweicloud.com/0.7.0-beta/MindSpore/cpu/ubuntu_x86/mindspore-0.7.0-cp37-cp37m-linux_x86_64.whl
# local tests
COPY test_mul.py /opt
COPY lenet.py /opt
COPY test_add.py /opt
COPY test_addN.py /opt

WORKDIR /opt

ENTRYPOINT ["bash"]
