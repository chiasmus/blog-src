## Setup

First, clone this repo.

```
git clone git@github.com:chiasmus/blog-src.git
```

From within wherever you cloned `blog-src`:

```
cd /path/to/blog-src
git submodule init
git submodule update
```

This will setup the `output` folder.

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
