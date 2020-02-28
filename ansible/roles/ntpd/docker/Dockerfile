FROM debian
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y ntp
COPY ntp.conf /etc/ntp.conf
EXPOSE 123/udp
CMD ["/usr/sbin/ntpd", "-n"]
