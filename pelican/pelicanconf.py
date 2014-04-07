#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site Information
AUTHOR = 'WE-TapEr'
SITENAME = "A Blog"
SITESUBTITLE = "about Coding."
SITEURL = ''
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'en'

# This help me to catogorize the posts.
USE_FOLDER_AS_CATEGORY = 'True'

#----------------------------------------------------------------------------------
# Links

# Used create a GitHub ribbon.(Theme dependent)	
GITHUB_URL = "https://github.com/we-taper"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll (Theme dependent)
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('My Previous Blog', 'http://ovelinux.blog.sohu.com/'),)

# Social widget (Theme dependent)
SOCIAL = (("My E-Mail (Don't click, copy link and alter it to correct form, thx)", 'we.taper[WhateverInsideIsUseless]qq.com'),)

#----------------------------------------------------------------------------------
# Appearence

# Change theme.
THEME = "themes/brownstone"

# Set the posts (in summary) displayed per page. (Otherwise, all posts in that category will be displayed)
DEFAULT_PAGINATION = 7
# Set the maximum length (in words) of summary.
SUMMARY_MAX_LENGTH = 10

#----------------------------------------------------------------------------------
# Pelican Settings

# Set output path to parent folder
OUTPUT_PATH = '../'


#----------------------------------------------------------------------------------
# Others

# Add comment function via Disqus. (Theme dependent)
DISQUS_SITENAME = "taper"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

