FROM node:lts

COPY calculadora.js /app/
COPY calculadora.html /app/
COPY calculadora.css /app/
COPY Jenkinsfile /app/

WORKDIR /app

RUN npm install

EXPOSE 80
CMD ["node", "calculadora.js"]



