-- Supplied sample. Temporary tables vanish when this psql connection closes.
CREATE TEMP TABLE authors (
 id integer PRIMARY KEY, name text NOT NULL UNIQUE
);
CREATE TEMP TABLE articles (
 id integer PRIMARY KEY,
 author_id integer REFERENCES authors(id),
 title text NOT NULL UNIQUE CHECK (length(trim(title)) > 0),
 published boolean NOT NULL DEFAULT false,
 views integer NOT NULL DEFAULT 0 CHECK (views >= 0)
);
INSERT INTO authors VALUES (1,'Asha'),(2,'Ben'),(3,'Chen');
INSERT INTO articles VALUES
 (1,1,'SQL notes',true,10),
 (2,1,'API notes',false,0),
 (3,2,'Testing notes',true,5),
 (4,NULL,'Draft',false,0);
