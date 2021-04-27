FROM ubuntu:20.10
RUN apt update -y

# Installing text editors
RUN apt install vim -y
RUN apt install emacs -y
RUN apt install nano -y
RUN apt install less -y

#Installing networking tools
RUN apt install curl -y
RUN apt install net-tools -y
RUN apt install netcat -y

#Installing Python3 and pip3
RUN apt install python3 -y
RUN apt install python3-pip -y
 

WORKDIR /iSPY/
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .




ENTRYPOINT tail -f /dev/null
