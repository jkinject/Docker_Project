FROM nginx:alpine

LABEL Jungkyu Jang

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
