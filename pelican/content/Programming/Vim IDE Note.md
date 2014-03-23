Title: Vim IDE Note (last update: 2013-03-08)
Date: 2014-3-8 11:00
Tags: IDE, Vim
Author: we.taper

Vim IDE Note 
================================

Here's how I turned VIM into a modern IDE.

**Content**

+ Overall
	+ Plugin Management - Pathogen
+ Java Part
	+ Java code completion - VJDE



Overall
-----------------
### Plugin Management - Pathogen
Download from github: <https://github.com/tpope/vim-pathogen>

Extract to `~/.vim/autoload` or `%homepath%\vimfiles\autoload`.

Edit `vimrc`, add following:

	" For Pathogen Plugin manager
	call pathogen#infect() " Infect so that pathogen auto-install all plugins
	call pathogen#helptags() " Build up things inside 'doc' directory.

Then add plugins into `bundle` folder inside vimfiles. Pathogen will does everything else for you.
Java Part
-----------------
### Java code completion - VJDE
**Note: ** To make the bes to modern IDE like Eclipse, I strongly suggest you to try [eclim][eclim], a great tool which embed vim directly into Eclipse.

[eclim]:http://eclim.org

Using Script: [Vim JDE](http://www.vim.org/scripts/script.php?script_id=1213)

Download and extract to into `bundle` folder inside default folder (e.g. `~/.vim` under Linux) within a new `vjde` folder (so we can manage plugins better).

Then when editing Java files we can use <Ctrl+x><Ctrl+u> to invode auto completion (vjde will find all possible methods/fields inside).
