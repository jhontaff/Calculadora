FROM nginx
#RUN rm /etc/nginx/conf.d/default.conf
COPY . /usr/share/nginx/html
EXPOSE 8090
CMD ["nginx", "-g", "daemon off;"]
