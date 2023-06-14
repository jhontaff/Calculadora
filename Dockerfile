FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY . /usr/share/nginx/html
EXPOSE 8090:80
CMD ["nginx", "-g", "daemon off;"]
