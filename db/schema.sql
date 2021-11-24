CREATE DATABASE service;

\c service;


create table "resource" (
    id serial primary key
    , name varchar not null
    , created_at timestamp default now()
);

insert into "resource" (name)
values ('this'),
       ('that');
