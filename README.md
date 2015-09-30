# Welcome to my twisted mind

I'm not sure why I wrote that header.

Anyway, this is the repo for my [pelican](http://getpelican.com)-powered blog
on [this here](http://ajwrit.es) site.

## Docker

This thing here is Dockerized, a term here meaning you can use `pelican` from
within a `docker` container. If these words in that particular configuration
made little sense, please read the [Docker docs](https://docs.docker.com).

To set up:

```
docker-compose build
```

This will pull all the Python things needed to use `pelican`.

To serve up the site:

```
docker-compose up
```

Say you want to regenerate the site. Simply:

```
docker-compose run pelican make html
```
