# Structure of the Source Code

## Adding New Content

Posts and pages are written in Markdown. Put any content in the `content` folder in their respective places:

```
├── content
│   ├── images
│   ├── pages
│   └── posts

```

Post filenames have the form `YYYY-MM-DD-TITLE_OF_POST.markdown`.

They must begin with the following data at the top of the `*.markdown` file:

```yml
title: Hello World
date: 2015-10-24 18:06
tags: tags, are, separated, by, commas

You would then write your content here.

Look, another paragraph!
```

# Setup

## git

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

## Local Development

To set up:

```
docker-compose build
```

This will pull all the Python things needed to use `pelican`.

To create the output for the site:

```
docker-compose run pelican make html
```

You must run this when you update the content.

To serve up the site:

```
docker-compose up
```

Check what the IP of the development server is:

```
docker-machine ip default
```

This will output the IP of the dev server, e.g. `192.168.99.100`.
The output of this command is the IP you want to visit, with port `8000` appended to the URL. So for example, if the output was `192.168.99.100`, then you would go to `http://192.168.99.100:8000` in your browser.



