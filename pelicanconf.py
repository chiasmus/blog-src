#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'AJ'
TAGLINE = u"writes code, prose."

SITENAME = u"In which a nerd writes stuff on the internet."
SITEURL = ''

# Hur hurr totally my face
USER_LOGO_URL = '/images/me.jpg'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Paths
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Code', 'https://bitbucket.org/astrohckr'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/astrohckr'),)

DEFAULT_PAGINATION = 10

THEME = '/home/aj/Code/pelican-themes/pelican-svbhack'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
