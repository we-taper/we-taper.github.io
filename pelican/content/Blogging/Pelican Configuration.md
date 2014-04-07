Title: Using Pelican and Github to Blog - Configuration
Date: 2014-3-23
Tags: Pelican, unFinished, unPolished
Author: we.taper
Summary: Show how to configure pelican

Configuration File
================================

Pelican is rather simple to configure. Please refer to the original document for more detailed instructions : [Settings - Pelican](http://docs.getpelican.com/en/3.3.0/settings.html#basic-settings).

Here's what I did:

**Note: ** The settings should be changed mainly in the pelican configuration file.  
*How to locate the configuration?*: If you have *kick start* your website using quick starter, you will find the auto-generated configuration file `pelicanconf.py` in your website directory. Otherwise, create one with name you like.

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


## Configure Themes

Changing themes in pelican can be quite convenient. Just download the theme and setting up in Pelican cofiguration file. 

### Where to find themes?

Several methods: 

+ Try Google. 
+ Copy other's website. 
+ Download themes in pelican's github page:[Pelican Themes](https://github.com/getpelican/pelican-themes). Here's a website to preview these themes: [Pelican themes](http://pelicanthemes.com) (In fact, this website is just a previewer of screenshot.png located inside the pelican-themes repository.)

**Note: ** When cloning pelican-themes, make sure to add `--recursive` option to git so that all submodules linked by these repository will be cloned (Othervise you will find some folders empty after cloning). And this might take some time so the best policy would be have a look of the screenshot first directly inside github.

I personally recommand the **brownstone** or **cebong** theme.

### Pelican-themes

Pelican provide a built-in theme manager which you can assess by command:

	pelican-themes -h  # This calles the help.
	pelican-themes -l  # This lists all the themes installed.
	pelican-themes -vl # The -v (verbose) gives us more detailed information to the output - here it lists the place where themes locate.

There exist, by default, two themes in pelican - *notmyidea* and *simple*. You can install additional theme by running command

See more at [Pelican Doc - Pelican-theme](http://docs.getpelican.com/en/3.3.0/settings.html#basic-settings)

**Note: ** I don't recommend you to install themes for compatibility reasons: If you switch to another computer or OS, you will have to reinstall these themes so that pelican can recognize them. Instead, you can copy the theme you want into blog folder and push them to github. Therefore, when you clone your own blog some elsewhere, you theme will always be ready for use.

### Setting up themes in Pelican configuration

To specify a theme:

	THEME = "Name Of Theme Installed"
	# You can view installed themes by pelican-themes - vl
	# Or, if you don't want to install, type:
	THEME = "Path To Theme"
	# Path can either be relative or absolute.

For more details, please visit: [Pelican Doc - themes](docs.getpelican.com/en/3.3.0/settings.html#themes)

## Using Disqus

You can add commenting functionality suppport by add Disqus to your blog. Disqus is a blog comment hosting service for websites and online communities that uses a networked platform. See [Wikipedia Disqus](http://en.wikipedia.org/wiki/Disqus)

1. Register an account on Disqus
2. On Disqus, choose *"Add Disqus to Your Site"* and finish the process.
3. Find your shorname, which is ususally the same as in : `http://xxx.disqus.com/` (xxx is your shortname).
4. In Pelican configuration file, add following:

		DISQUS_SITENAME = "Your Short Name Here"

Done!

Something about Editing Blogs
========================================
Link
## to internal content.

*See :*[Linking to internal content][ltic]

Replace URL with these:

To file: 	 

	{filename}path/to/file  

To tags:  

	{tag}tagname  

To Category:  

	{category}foobar  

**Note: **

1. Pelican does not support referenced link of this type.
2. The `{filaname}` is actually `{filaname}`, don't put some real file name here or pelican will recognize it as Category name.



[ltic]:http://docs.getpelican.com/en/3.3.0/getting_started.html#linking-to-internal-content


##Creating Pages

In Pelican, user can generate some special webpage which will have its own link in your homepage like the traditional *About Me* page seen in most blogs.

To do this, you simple put webpage of these kind inside a special folder named `pages`. All webpage there will have its own link on your homepage.

