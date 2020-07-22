FROM debian
RUN apt update -y
RUN apt upgrade -y
COPY app /opt/
WORKDIR /opt/app/
RUN python3 -m venv venv
RUN source venv/bin/activate && \
  pip install -r requirements.txt
