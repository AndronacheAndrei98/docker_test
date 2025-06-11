FROM nginx:alpine

WORKDIR /usr/share/nginx/html

COPY index.html .

# Something very evident is wrong!
EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"] 