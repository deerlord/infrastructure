#!/bin/bash

DEVICE='test'

openssl genrsa -aes128 -passout pass:password -out ${DEVICE}.key 2048
openssl req -subj /CN=${DEVICE} -key ${DEVICE}.key -new -out ${DEVICE}.req
openssl x509 -sha256 -req -in ${DEVICE}.req -days 365 -signkey ${DEVICE}.key -out ${DEVICE}.crt -extensions ssl_client
chmod u-wx,g-rwx,o-rwx ${DEVICE}.*

