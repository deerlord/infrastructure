FROM debian
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y wget
RUN apt install -y dnsmasq dnsmasq-utils
RUN mkdir -p /etc/dnsmasq/
RUN echo 'conf-file=/etc/dnsmasq/conf' > /etc/dnsmasq.conf
EXPOSE 53/udp
EXPOSE 53/tcp
EXPOSE 67/udp
CMD ["/usr/sbin/dnsmasq", "-k"]
