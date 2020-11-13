FROM debian
RUN apt update -y
RUN apt install -y python3.7
RUN apt install -y python3-pip
RUN pip3 install SpeechRecognition
RUN mkdir /opt/speech/
COPY ./speech.py /opt/speech
CMD ["python3", "/opt/speech/speech.py"]
111
