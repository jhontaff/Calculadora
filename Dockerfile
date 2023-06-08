FROM node:lts
WORKDIR /
COPY calculadora.html .
COPY calculadora.js .
COPY calculadora.css .

RUN npm install -g http-server

EXPOSE 2020
CMD ["http-server", "-p", "2020"]



