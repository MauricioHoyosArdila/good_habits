FROM postgres:15.0-alpine

ENV POSTGRES_USER=postgres 
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=good_habits

EXPOSE 5432