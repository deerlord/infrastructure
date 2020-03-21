FROM debian
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y squid
CMD ["/usr/sbin/squid", "--foreground"]
