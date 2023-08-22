FROM postgres:15.0-alpine

ENV POSTGRES_USER=postgres 
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=soccer_matches

EXPOSE 5432