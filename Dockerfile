FROM python:3.12-alpine AS build
WORKDIR /src
COPY . .
RUN python3 tools/build.py && chmod -R a+rX dist

FROM nginx:1.27-alpine
RUN printf 'charset utf-8;\ncharset_types text/html text/css application/javascript application/json;\n' > /etc/nginx/conf.d/charset.conf
COPY --from=build /src/dist /usr/share/nginx/html
EXPOSE 80
