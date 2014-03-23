Title: Pelican Configuration
Date: 2014-3-23
Tags: Pelican
Author: we.taper
Summary: Show how to configure pelican

Pelican Configuration
==============================

Pelican is rather simple. Please refer to the original document for more detailed instructions : [Settings - Pelican](http://docs.getpelican.com/en/3.3.0/settings.html#basic-settings).

Here's what I did:

*Note: * The settings should be changed mainly in the pelican configuration file. *How to locate the configuration?*: If you have *kick start* your website using quick starter, you will find the auto-generated configuration file `pelicanconf.py` in your website directory. Otherwise, create one with name you like.

### What I have changed.

	AUTHOR = 'WE-TapEr'
	SITENAME = "WE-TapEr's Blog"

	USE_FOLDER_AS_CATEGORY = 'True'
	# Blogroll
	LINKS =  (('Name', 'http://linkaddress.com/'),)

	# Social widget
	SOCIAL = (("E-Mail name", 'xxx@xx.com'),)

	TIMEZONE = 'Asia/Shanghai'

	# Set the maximum length (in words) of summary.
	SUMMARY_MAX_LENGTH = 10
