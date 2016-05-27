Title: Transform to reStructuredText
Date: 2014-3-2 14:00
Tags: Markup Language
Author: we.taper

# Transform to reStructuredText

Because the Markdown language no longer satisfy my requirements, I started to learn reStructuredText,
another markup language initially built for writing python documentation just like in javadoc or etc.

**Update:** 

I have already given up reStructuredText and switched back to markdown. Thus this file will not be udpated.

It is not that markdown has been updated with more features. It is because reStructuredText relies on too many external packages, and it is not popular enough to give us easy access on all platforms and web browsers. For example, the edito ReText (mentioned below) is complicated to setup on windows. Also, there is no firefox plugin to view reStructuredText. All these violates the principle of K.I.S.S. and I decided to fall back to markdown. If needed, I will write sophisticated documents using *Latex* and publish the pdf output.

## Prepare some Editors

### For Windows
Because I have an Windows 8 OS on my PC, there is much trouble to get me some ready-to-use reStructuredText
editors. After some search, found:

+ [ReText](http://sourceforge.net/p/retext/home/ReText/), a WYSIWYG reStructuredText editor (also supports
  Markdown, what a surprise!)
+ [Online reStructuredText Editor](http://rst.ninjs.org/), well, Internet is a great tool for those who
  does not want to bother installing software. But for me, Internet access sometimes could be troublesome.
+ Also [MarkItUp](http://markitup.jaysalvat.com/home/), a universal markup jQuery editor. I don't know 
  jQuery but this is interesting.
  
#### Install ReText

ReText is written in python using PyQT4, so theoretically it could run on any OS. It could be downloaded
from sourceforge's [homepage](http://sourceforge.net/p/retext/home/ReText/), or from [git](http://sourceforge.net/p/retext/git/).

1. Basic Requirements

	Package needed:
	
	[python](http://python.org/) — we recommend using version 3.2 or higher  
	[python-qt4](http://www.riverbankcomputing.co.uk/software/pyqt/intro)  
	[python-markups](http://pypi.python.org/pypi/Markups)  
	
	1. Install python(Skipped);
	2. Install python-qt4
	
		There exits PyQT4 Windows installers :[Find it here](http://www.riverbankcomputing.co.uk/software/pyqt/download). Be careful to choose the corresponding edition.
		
		Follow the installation guide and installing could be just "clicks".
		
	3. Install python-markups
	
		Code:
		
			easy_install -i  http://pypi.douban.com/simple/ markups
		
		Note: `-i  http://pypi.douban.com/simple/` for better speed in China.
		
	4. Some recommended packages in *README*
	
		We also recommend having these packages installed:

		* [python-markdown](http://packages.python.org/Markdown/) — for Markdown
		  language support
		* [python-docutils](http://docutils.sourceforge.net/) — for reStructuredText
		  language support
		* [python-enchant](http://pypi.python.org/pypi/pyenchant) — for spell checking
		  support
		  
	Since installation maybe just a line of code `pip install xxx` or `easy_install xxx`, I skipped this part.
	
2. Run ReText

	Running a python program is simple. After downloading and unpackaging the source code, you just have you tell python to start this program by:
	
		python retext.py
	
	Then everything done and enjoy it.
	
After words: To be honest, ReText is really ... too simple, the real time display is too troublesome - you have to scroll the webpage yourself to go to the editing place. Even the online editor (metioned above) is far better.

### For Linux

#### Also ReText

##### Ubuntu PPA Source

PPA Link: [PPA for Dmitry Shachnev](https://launchpad.net/~mitya57/+archive/ppa)

*HowTo Add PPA Source?*

Code:

	sudo add-apt-repository ppa:user/ppa-name  
	sudo apt-get update  
	sudo apt-get install xxx  
	

So now:

Code:

	sudo add-apt-repository ppa:mitya57/ppa  
	sudo apt-get update  
	sudo apt-get install 

**Note :**

ReText is provided in ubuntu source, there is no need to add extra ppa-source!

Installed Package:

	python3-markups (version 0.3-1) will be installed  
	python3-pyqt4 (version 4.10.3-1ubuntu1) will be installed  
	python3-sip (version 4.15.2-1ubuntu1) will be installed  
	retext (version 4.1.0-1) will be installed

However, extra packages are required to parse files.Please choose the right version of package. For example, following package does not meet the requirements:

	docutils-common (version 0.11-2) will be installed  
	python-docutils (version 0.11-2) will be installed  
	python-enchant (version 1.6.5-2build1) will be installed  
	python-markdown (version 2.3.1-1) will be installed  
	python-roman (version 1.4.0-2ubuntu1) will be installed  

Instead, I should install the version for python 3:

	Installed packages:  
	python3-docutils (0.11-2)  
	python3-enchant (1.6.5-2build1)  
	python3-markdown (2.3.1-1)   
	python3-roman (1.4.0-2ubuntu1)


	
## reStructuredText Syntax

Compared with Markdown, reStructuredText is rather big and comprehensive. There are many good documents to read, I personally suggest:

1. [A quick start](http://docutils.sourceforge.net/docs/user/rst/quickstart.html)
2. The [Quick Reference](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
3. And crack the [Cheat Sheet](http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt)
4. A good Introduction in Chinese [reStructuredText简明教程](http://jwch.sdut.edu.cn/book/rst.html)
5. Another Introduction in Chinese [reStructuredText 简明教程](http://gsnippet.googlecode.com/svn/blog/html/reStructuredTEXT.html)
##Some Notes