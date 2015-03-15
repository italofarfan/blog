#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Italo Farf\xe1n Vera'
SITENAME = u'Italo Farf\xe1n'
SITEURL = ''

PATH = 'content'

# Formating URLs
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
# FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


# Theme
THEME = "pelican-themes/pelican-bootstrap3"

# Plugins
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['tipue_search', 'pelican_youtube','liquid_tags.youtube']

# Blogroll
# LINKS = (('Leonardo Cloud', 'http://productos.viz-analytics.com/leonardo/'),
#          ('Viz Analytics', 'http://viz-analytics.com'),
#          ('Python España', 'http://www.es.python.org/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/italoFFVV'),
          ('github', 'https://github.com/italofarfan'),
          ('linkedIn', 'http://www.linkedin.com/in/italoffvv/'),
          ('Google Plus', 'https://plus.google.com/u/0/103161686610742017026/posts'),
          ('RSS', 'http://italofarfan.com/feeds/all.rss.xml'),
          )

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')


DEFAULT_PAGINATION = 10

CC_LICENSE = "CC-BY-NC-SA"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Disqus
# DISQUS_ID_PREFIX_SLUG = True
DISQUS_SITENAME = "italofarfan"
# ADDTHIS_PROFILE = 'ra-54f5b02c1a06d710'
GOOGLE_ANALYTICS = "UA-48330831-1"

# RSS/Atom feeds
# FEED_DOMAIN = SITEURL
# FEED_ATOM = 'atom.xml'
