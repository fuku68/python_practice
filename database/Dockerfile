FROM ubuntu:latest
RUN apt-get update \
    && apt-get install -y mysql-server \
    && apt-get install -y locales \
    && locale-gen ja_JP.UTF-8 \
    && echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc

ADD ./db6/import.csv .
ADD ./db6/exec.sql .
CMD ["/bin/bash"]
