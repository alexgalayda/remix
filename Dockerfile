FROM nvidia/cuda:12.0.1-cudnn8-devel-ubuntu22.04

ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update --fix-missing && \
    apt-get upgrade -y

RUN apt-get install -y \
        software-properties-common \
        wget \
        curl \
        make \
        cmake \
        libopencv-dev

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update --fix-missing
RUN apt install -y \
	python3.11 \
	python3.11-dev

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
RUN update-alternatives --config python3

RUN wget https://bootstrap.pypa.io/pip/get-pip.py && \
    python3 ./get-pip.py && rm ./get-pip.py
RUN pip3 install --upgrade pip

RUN pip3 install torch==2.0 torchvision==0.15.1 --index-url https://download.pytorch.org/whl/cu118
RUN pip3 install transformers diffusers[torch]
