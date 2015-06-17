#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# SITEURL = 'http://italofarfan.github.io'
SITEURL = 'http://italofarve.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
SOCIAL = SOCIAL + (('rss', SITEURL + '/' + FEED_ALL_ATOM),)

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "italofarfan"
GOOGLE_ANALYTICS = "UA-53001666-1"
ADDTHIS_PROFILE = 'ra-54f5b02c1a06d710'
