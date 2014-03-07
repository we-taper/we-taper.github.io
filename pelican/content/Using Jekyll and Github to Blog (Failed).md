Title: Using Jekyll and Github to Blog v0.1 (Failed)
Date: 2014-2-21 14:00
Category: Blogging
Tags: Jykell, unFinished
Slug: Using Jekyll and Github to Blog
Author: we.taper
Summary: Spent a whole day on Jykell, but failed. Turned to Pelican instead.

#Using Jekyll to Blog

**Note :**  
At last, i got myself fired by using Jykell. Ruby and Python's Pygments modulus 
just don't work with each other. And installing these softwares on windows is just
another nightmare for me. If you are a windows user, I sincerely advise you stop
trying Jekyll now! Another option is: Pelican!  
If you really want to continue, please do refer to my recommended blogs and websites
before you start rock, especially the [official guide][htrjow]

##What??

Jekyll is a static website generator. Github Page is a service provided by github.com which hosts user-uploaded static websites and display them, for **free**! This two combined - **A Free Web blog host under perfect control**. (Note: Everything on Github is open unless you purchase some plans. So there is no privacy concerns - You simply don't put private content on it!)

Github officially support Jykell. Everything hosted on Github Pages will be processed by Jykell. Since standard HTML files is also Jykell capable, you can use Github Pages without Jykell of course.

*Note :* 

This is a hardcore, time-consuming task which require much patience and time. Never try this if you are not a geek.

*Note 2:* 

Because I want to blog something but is tired of using existing blog services, I searched for a bit and find Jekyll 
as well as Hyde. They are both "static webpage generator" (See: [Wikipedia Static Webpage][w_sw]). Jekyll is based on Ruby while Hyde is based on python. There are two excellent articles comparing these two engines: 1.[Static Website Generators - Jekyll vs Hyde][swg_jvh], and 2.[Jekyll vs. Hyde - A Comparison Of Two Static Site Generators][jvh_ctss] (Both stored in my Evernote for backup). 

I choosed Jekyll because:  

1. It is under active development, the [Github Jekyll][gh_jk] has many recent commits just days ago. The last commit of Hyde is somewhat 6 months ago!  
2. There are many default templetes that I can simply `git clone xxx` to use for Jykell. As for Hyde, few were found.  
3. Author of Jekyll is also co-founder of Github! Therefore the future maintenance is guaranteed.  


##Pre-requirements (Important)

1. Installed Ruby  
	For simplicity, I choosed [RubyInstaller][rbi] to install Ruby on my Windows. Once installed, you will got a powerful tool: `gem` to install ruby modulus.
		
	+ Switch **gem** Source to *http://ruby.taobao.org/* to improve downloading speed.   
		See: [RubyGems 镜像 - 淘宝网][rbgm_tb] for more.

	+ Installed DevKit 
		Otherwise you can't just install Jykell with bundle (see below). See [Github DevKit][gh_dk].

2. Installed Python  
	Compared with Ruby, installing python on windows is just simple. As for Linux and Mac, they already have python come within system. See: [Python Download][py]

##Let's Rock

1. Installed Bundler  
	Yet another ruby modulus installation tool. Recommended on [Github Official help][gh_oh_1]. It said,*"You can still install Jekyll with the command gem install github-pages, but you may run into trouble down the line."*, But I haven't tried that.
	Follow the tips on [Github Official help][gh_oh_1].

2. Install Jekyll with Bundler  
	Just folow tips on [Github Official help][gh_oh_1]. Becareful that your should `cd` into the directory where the `Gemfile` exists, or you will always get a `Bundler::GemfileNotFound` error. Also, remember to change the source to ruby.taobao.org as mentioned in **Pre-requirements**.

4. Install easy_install and Pygments
	Using the right python (2.7.x) and install Pygments through easy_install scripts. 
	See [Link 1][l_1] to install easy_install and find easy_install inside python 
	installation directory (usually under folder "Scripts"), run `easy_install Pygments`.

3. Cook the Git Book  
	Learn about git from [Git Guide][gt_gi], I also wrote an article about it: [My Git Guide]({filename}/Git Book Note.md)

4. Clone others' work  
	Well, My time is limited (I've already spent a whole day on it). And open source is fascinating. Why not copy?

	Some personal recommendations:  
	1. <https://github.com/JeremyWei/jeremywei.github.com>
	2. <http://www.madhur.co.in>

	A really good List of Websites build on Jekyll:[Jekyll Sites][jk_st]

##Some Notes to solve problems:

**Note :** The error message below have been simplified to save space. Watch your error output carefully, perhaps mine solution applies to your too!

* Error: `... fileutils.rb:247:in `mkdir': Invalid argument ...`  

	Problem: The new versioin of jekyll (>1.4.2) isn't stable enough! Downgrade!  
	Solution:
		gem uninstall jekyll  
		gem install jekyll --version "=1.4.2"  
	See: [StackOverflow Ask][sof_1]

* Error:  `Liquid Exception: Failed to get header. in xxx.markdown`   
or `spawn.rb:162: warning: cannot close fd before spawn`

	Problem: 
	
	1. The new version of pygments.rb (>0.5.0) doesn't cooperate with this Jekyll. Downgrade!  
	Note: According the official guide ([Link][htrjow]), version 0.5.0 and o.5.4 are OK.
	2. The new Python 3 don't work with Jekyll. Use Python 2.7.5.
	
	Solution:
	1.
			gem uninstall pygments.rb  
			gem install pygments.rb --version "=0.5.0"  
	2. Install Python 2.7.x (remember to install Pygments later)  
		You can with both 2.7.x and 3.x version installed but use %PATH% environment to change the default python intepretor. Google about "Changing Path on Windows"
		
	See: [Jekyll on Windows: Pygments not working][sof_2]

* Note: Do not install Ruby in a complicated path including characters like "(", ")", etc. I got errors when doing so. Instead installing to the default "X:\Rubyxx\" is OK.
##Some Good Articles to help you smooth through this process:

1. A blog by 阮一峰[搭建一个免费的，无限流量的Blog----github Pages和Jekyll入门][ryf]  
	Contains much about how to setup standard Jekyll websites. Good for those who want to hack the Websites themselves.

2. A blog teaches installing Jykell on Windows:[Running Jekyll on Windows][rjkow]

3. A comprehensive tutor to run Jykell on Windows (also Official): [How to Run Jekyll on Windows][htrjow]
	**Recommended!**

4. [写作环境搭建(git+github+markdown+jekyll)](http://site.douban.com/196781/widget/notes/12161495/note/264946576/)

5. [使用Github Pages建独立博客](http://beiyuu.com/github-pages/)

6. [Play with Jekyll](http://blog.skydark.info/programming/2012/03/23/play-with-jekyll/)

7. [完善本地搭建的jekyll环境(Windows)](http://www.cnblogs.com/yevon/p/3310857.html)
	**Recommended!**
	
8. [Jekyll在Windows下面中文编码问题解决方案](http://www.cnblogs.com/aleda/articles/Jekyll-in-Windows-following-Chinese-encoding-problem-solutions.html)


[w_sw]:https://github.com/hyde/hyde
[swg_jvh]:http://www.distractable.net/tech/static-site-generators-jekyll-vs-hyde
[jvh_ctss]:http://philipm.at/2011/jekyll_vs_hyde.html
[gh_jk]:https://github.com/jekyll/jekyll
[rbi]:http://rubyinstaller.org
[rbgm_tb]:http://ruby.taobao.org/
[gh_oh_1]:https://help.github.com/articles/using-jekyll-with-pages#installing-jekyll
[gh_dk]:https://github.com/oneclick/rubyinstaller/wiki/Development-Kit
[py]:http://www.python.org/download/
[gt_gi]:http://git-scm.com/book/en/

[jk_st]:https://github.com/jekyll/jekyll/wiki/Sites
[ryf]:http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html
[sof_1]:http://stackoverflow.com/questions/21137096/jekyll-error-running-jekyll-serve
[rjkow]:http://www.madhur.co.in/blog/2011/09/01/runningjekyllwindows.html
[sof_2]:http://stackoverflow.com/questions/17364028/jekyll-on-windows-pygments-not-working
[htrjow]:https://github.com/juthilo/run-jekyll-on-windows/#install-the-jekyll-gem
[l_1]:https://pypi.python.org/pypi/setuptools#windows