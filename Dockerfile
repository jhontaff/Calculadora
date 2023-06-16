FROM nginx
RUN rm /usr/share/nginx/html/index.html
COPY . /usr/share/nginx/html
EXPOSE 90:80
CMD ["nginx", "-g", "daemon off;"]
