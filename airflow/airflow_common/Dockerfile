ARG IMAGE_VARIANT=slim-buster
ARG OPENJDK_VERSION=11
ARG PYTHON_VERSION=3.8


FROM apache/airflow:2.2.1-python${PYTHON_VERSION}

USER root

# Install OpenJDK-11
RUN apt update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME


RUN apt-get update
RUN apt-get -y install openssl wget

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

RUN cd /tmp
RUN mkdir -p /opt/airflow/jars
RUN wget "https://jdbc.postgresql.org/download/postgresql-42.3.1.jar"
RUN mv postgresql-42.3.1.jar /opt/airflow/jars/

