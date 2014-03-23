#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'WE-TapEr'
SITENAME = "WE-TapEr's Blog"
SITEURL = ''
USE_FOLDER_AS_CATEGORY = 'True'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'
	
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('My Previous Blog', 'http://ovelinux.blog.sohu.com/'),)

# Social widget
SOCIAL = (("My E-Mail (Don't click, copy link and alter it to correct form, thx)", 'we.taper[在]qq.com'),)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Set output path to parent folder
OUTPUT_PATH = '../'

# Set the maximum length (in words) of summary.
SUMMARY_MAX_LENGTH = 10