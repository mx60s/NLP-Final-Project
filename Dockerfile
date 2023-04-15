FROM jupyter/minimal-notebook:lab-3.5.0
#FROM python:3

# Add RUN statements to install packages as the $NB_USER defined in the base images.

# Add a "USER root" statement followed by RUN statements to install system packages using apt-get,
# change file permissions, etc.

# If you do switch to root, always be sure to add a "USER $NB_USER" command at the end of the
# file to ensure the image runs as a unprivileged user by default.

USER root

#RUN apt-get update && apt-get -y install python3-pip

#RUN apt-get update && apt-get install -y gcc 

#RUN apt-get install g++

RUN pip install --quiet --no-cache-dir --upgrade pip

#RUN git clone https://github.com/pytorch/fairseq && \
#    cd fairseq && \
#    git checkout v0.12.0 && \
#    pip install . && \
#    python setup.py build_ext --inplace && \
#    cd .

RUN git clone https://github.com/moses-smt/mosesdecoder.git && \
    export MOSES=${PWD}/mosesdecoder

RUN git clone https://github.com/glample/fastBPE.git && \
    export FASTBPE=${PWD}/fastBPE && \
    cd fastBPE && \
    apt-get install g++ &&g++ -std=c++11 -pthread -O3 fastBPE/main.cc -IfastBPE -o fast


COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
	rm -rf /tmp/requirements.txt #&& \
	fix-permissions "${CONDA_DIR}" && \
	fix-permissions "/home/${NB_USER}"

USER ${NB_UID}

WORKDIR "${HOME}"
