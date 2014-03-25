Title: Using Pelican and Github to Blog - Configuration
Date: 2014-3-23
Tags: Pelican, unFinished, unPolished
Author: we.taper
Summary: Show how to configure pelican

Configuration File
--------------------------------

Pelican is rather simple. Please refer to the original document for more detailed instructions : [Settings - Pelican](http://docs.getpelican.com/en/3.3.0/settings.html#basic-settings).

Here's what I did:

*Note: * The settings should be changed mainly in the pelican configuration file. *How to locate the configuration?*: If you have *kick start* your website using quick starter, you will find the auto-generated configuration file `pelicanconf.py` in your website directory. Otherwise, create one with name you like.

### What I have changed.

	AUTHOR = 'xxxx'
	SITENAME = "Your Blog's Name"
	# See, ' and ", both can be used for String literals. These is the feature of Python.

	USE_FOLDER_AS_CATEGORY = 'True'
	# Blogroll
	LINKS =  (('Name', 'http://linkaddress.com/'),)

	# Social widget
	SOCIAL = (("E-Mail name", 'xxx@xx.com'),)

	TIMEZONE = 'Asia/Shanghai'

	# Set the maximum length (in words) of summary.
	SUMMARY_MAX_LENGTH = 10


### Configure Themes

Changing themes in pelican can be quite convenient. Just download the theme and setting up in Pelican cofiguration file. 

#### Where to find themes?

Several methods: Try Google. Copy other's website. Download themes in pelican's github page:[Pelican Themes](https://github.com/getpelican/pelican-themes) 

#### Pelican-themes

Pelican provide a built-in theme manager which you can assess by command:

	pelican-themes -h  # This calles the help.
	pelican-themes -l  # This lists all the themes installed.
	pelican-themes -vl # The -v (verbose) gives us more detailed information to the output - here it lists the place where themes locate.

There exist, by default, two themes in pelican - *notmyidea* and *simple*. You can install additional theme by running command

See more at [Pelican Doc - Theme](http://docs.getpelican.com/en/3.3.0/settings.html#basic-settings)

Something about edit Blogs
=====================

##Link to internal content.

*See :*[Linking to internal content][ltic]

Replace URL with these:

To file: 	 

	{filename}path/to/file  

To tags:  

	{tag}tagname  

To Category:  

	{category}foobar  

**Note :**

1. Pelican does not support referenced link of this type.
2. The `{filaname}` is actually `{filaname}`, don't put some real file name here or pelican will recognize it as Category name.



[ltic]:http://docs.getpelican.com/en/3.3.0/getting_started.html#linking-to-internal-content


##Creating Pages

In Pelican, user can generate some special webpage which will have its own link in your homepage like the traditional *About Me* page seen in most blogs.

To do this, you simple put webpage of these kind inside a special folder named `pages`. All webpage there will have its own link on your homepage.

