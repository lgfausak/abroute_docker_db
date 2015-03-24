# abroute_docker_db - autobahn initialize database
this simply initializes a database for docker

## Overview

The postgres container defined herein can do one thing:

* create a db and then run web server idle just to hang the app

I don't understand how to initialize a data only container
and use it with fleet or compose.  There is an issue with persistent
data. So, this lets us define a compose which can be run the first time, we
probably need another compose for the 'second' time to use the
existing container with the existing data.  this is too hard.

Initial DB Creation

```
docker run -name abdata tacodata/abroute_docker_db
```

Once you have a database instance (called abdata) you use it like this:

```
docker run -name pgsql --volumes-from abdata tacodata/abroute_docker_postgres absql 
```

These two commands need to be run the first time, but, after that, you don't ever run the init
command again.  init is destructive, destroy the current database and recreates
a blank one.

Since the abinit command simply waits in a web server, you can depend on
it working for a compose, which requires that the image be up.

## Docker Container Layout

![alt text][docker_containers]

The containers this repo is working on is the top one 'Postgres' and the 'db' container.
When we run our abinit script we create a volume suitable for mounting. In our example
above the init run creates an instance called 'abdata'. 'abdata' is represented by 'db'
in the picture. abdata provides two volumes. /var/lib/postgres contains the data for the database.
It is initialized with the 'adm' user and the 'sys' user.  It is suitable to
build an application on top. Also, the /run/postgresql is mountable and contains
the runtime information (basically the pid).


[docker_containers]:https://github.com/lgfausak/sqlauth/raw/master/docs/docker_containers.png "Docker Containers"
