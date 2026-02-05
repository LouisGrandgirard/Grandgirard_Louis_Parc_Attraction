DROP TABLE IF EXISTS attraction;

CREATE TABLE attraction (
    attraction_id integer PRIMARY KEY ASC,
    nom text not null,
    description text not null,
    difficulte integer,
    visible bool default true,
    author_id integer,
    FOREIGN KEY(author_id) REFERENCES users(users_id)
);

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    users_id integer primary key ASC,
    name text not null,
    password text not null,
    role text default 'ADMIN'
);

DROP TABLE IF EXISTS critique;

CREATE TABLE critique (
    critique_id integer PRIMARY KEY ASC,
    attraction_id integer,
    name text,
    note integer,
    commentaire text,
    FOREIGN KEY(attraction_id) REFERENCES attraction(attraction_id)
);