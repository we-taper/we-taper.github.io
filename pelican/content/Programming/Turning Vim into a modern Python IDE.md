Title: Commented: Turning Vim into a modern Python IDE
Date: 2014-3-7 23:00
Tags: Vim, IDE
Author: we.taper

Commented: Turning Vim into a modern Python IDE
============================================

This is an annotated version of the original website:[Turning Vim into a modern Python IDE](http://sontek.net/blog/detail/turning-vim-into-a-modern-python-ide)

**Note: ** This commenting isn't finished and is unlikly to be finished in the future. Please scroll to the bottom to get the reason.

Contents

+ Intro
+ Basic Editing and Debugging
	+ Code Folding
	+ Window Splits
	+ Snippets
	+ Task lists
	+ Revision History
+ Syntax Highlighting and Validation
	+ Pep8
+ Tab Completion and Documentation
+ Code Navigation
	+ Buffers
	+ Fuzzy Text File Search
	+ File Browser
	+ Refactoring and Go to definition
	+ Searching
+ Integration with Git
+ Test Integration
	+ django nose
	+ py.test
+ Virtualenv
+ Django
+ Random Tips

Intro
-----------------------

Back in 2008, I wrote the article Python with a modular IDE (Vim). Years later, 
I have people e-mailing me and commenting daily asking for more information, e
ven though most of the information in it is outdated. Here is the modern way t
o work with Python and Vim to achieve the perfect environment

Because one of the most important parts about a development environment is the a
bility to easily reproduce across machines, we are going to store our vim conf
iguration in git:

	$ mkdir ~/.vim/
	$ mkdir ~/.vim/{autoload,bundle}
	$ cd ~/.vim/
	$ git init
	
**Comment: **  
1. Under Windows, the `.vim` should be `vimfiles`  
2. `~` means the home directory in `*nix`, which is typically `C:\Users\USER_NAME\` under Windows 7 or later. (Run `echo %homepath%` in `cmd` to see yours).  
3. The second line `mkdir ~/.vim/{autoload,bundle` is to create two folder `autoload` and `bundle`, which will be used in another Vim plugin *[Pathogen][pathogen]*. This plugin quite easy to install. Just follow the instruction on its GitHub Homepage.

[pathogen]:https://github.com/tpope/vim-pathogen/

###Install Pathogen

1. `git clone` it. (Don't know git? Then just goto the website and download the `pathogen.vim` file inside `autoload`.)  
2. Copy `pathogen.vim` into `~/.vim` or `%homepath%\vimfiles` or etc. (See `:help runtimepath` under vim for more information about this.  
3. Add this to `vimrc`:  

	execute pathogen#infect()
	syntax on
	filetype plugin indent on

	(Don't know `vimrc`? Type `:help vimrc` in vim to get helped.)  
	About `filetype`: In Vim `:help filetype`
	
4. Now any plugins you wish to install can be extracted to a subdirectory under `~/.vim/bundle`, and they will be added to the `'runtimepath'`.

Back to Intro
-----------------
You'll need to add the following to your ~/.vimrc so that pathogen will be loaded properly. Filetype detection must be off when you run the commands so its best to execute them first:

	filetype off
	call pathogen#runtime_append_all_bundles()
	call pathogen#helptags()	

**Comment: **  

1. Although `filetype` is off, the `filetype plugin` and `filetype indent` can still be on.  

2. `pathogen#runtime_append_all_bundles()` is alias for `pathogen#incubate()`. It means (found this inside the `pathogen.vim` file):

	> For each directory in the runtime path, add a second entry with the given
	> argument appended.  If the argument ends in '/{}', add a separate entry for
	> each subdirectory.  The default argument is 'bundle/{}', which means that
	> .vim/bundle/*, $VIM/vimfiles/bundle/*, $VIMRUNTIME/bundle/*,
	> $VIM/vim/files/bundle/*/after, and .vim/bundle/*/after will be added (on
	> UNIX).
 
	(Sorry that I don't under stand this...)
	
	I personally suggest your change this to `pathogen#incubate`

3. About `pathogen#helptags()`

	> Invoke `:helptags` on all non-$VIM doc directories in `runtimepath`.

Now lets add all of the vim plugins we plan on using as submodules to our git repository:

	git submodule add http://github.com/tpope/vim-fugitive.git bundle/fugitive
	git submodule add https://github.com/msanders/snipmate.vim.git bundle/snipmate
	git submodule add https://github.com/tpope/vim-surround.git bundle/surround
	git submodule add https://github.com/tpope/vim-git.git bundle/git
	git submodule add https://github.com/ervandew/supertab.git bundle/supertab
	git submodule add https://github.com/sontek/minibufexpl.vim.git bundle/minibufexpl
	git submodule add https://github.com/wincent/Command-T.git bundle/command-t
	git submodule add https://github.com/mitechie/pyflakes-pathogen.git
	git submodule add https://github.com/mileszs/ack.vim.git bundle/ack
	git submodule add https://github.com/sjl/gundo.vim.git bundle/gundo
	git submodule add https://github.com/fs111/pydoc.vim.git bundle/pydoc
	git submodule add https://github.com/vim-scripts/pep8.git bundle/pep8
	git submodule add https://github.com/alfredodeza/pytest.vim.git bundle/py.test
	git submodule add https://github.com/reinh/vim-makegreen bundle/makegreen
	git submodule add https://github.com/vim-scripts/TaskList.vim.git bundle/tasklist
	git submodule add https://github.com/vim-scripts/The-NERD-tree.git bundle/nerdtree
	git submodule add https://github.com/sontek/rope-vim.git bundle/ropevim
	git submodule init
	git submodule update
	git submodule foreach git submodule init
	git submodule foreach git submodule update

(Typing above commands one by one could be really tedious. If you can, write a script yourself to accomplish this.)

**About Git Submodule**

The `submodule` functions as if there are some other git repositories in your git repository. It helps programmers to control the plugin they depend on and keep them all up-to-date.

Thats it! Now that we've got our vim configuration in git!

Now lets look at how to use each of these plugins to improve the power of vim:

Basic Editing and Debugging
------------------------------------
### Code Folding

Lets first enable code folding. This makes it a lot easier to organize your code and hide portions that you aren't interested in working on. This is quite easy for Python, since whitespace is required.

In your ~/.vimrc just add:

	set foldmethod=indent
	set foldlevel=99
	
Then you will be able to be inside a method and type `'za'` to open and close a fold.

**Comment: **

1. `foldmethod`

	Set the kind of folding used for the current window. Possible values:
		|fold-manual|	manual	    Folds are created manually.
		|fold-indent|	indent	    Lines with equal indent form a fold.
		|fold-expr|		expr	    'foldexpr' gives the fold level of a line.
		|fold-marker|	marker	    Markers are used to specify folds.
		|fold-syntax|	syntax	    Syntax highlighting items specify folds.
		|fold-diff|		diff	    Fold text that is not changed.

2. `foldlevel`

	Sets the fold level: Folds with a higher level will be closed.
	Setting this option to zero will close all folds.  Higher numbers will
	close fewer folds.
	This option is set by commands like |zm|, |zM| and |zR|.

### Window Splits

Sometimes code folding isn't enough; you may need to start opening up multiple windows and working on multiple files at once or different locations within the same file. To do this in vim, you can use these shortcuts:

	Vertical Split : Ctrl+w + v
	Horizontal Split: Ctrl+w + s
	Close current windows: Ctrl+w + q
	
I *(the author. But taper also favours this)* also like to bind Ctrl+<movement> keys to move around the windows, instead of using Ctrl+w + <movement>:

	map <c-j> <c-w>j
	map <c-k> <c-w>k
	map <c-l> <c-w>l
	map <c-h> <c-w>h
	
### Snippets

The next tweak that really speeds up development is using snipmate. We've already included it in our bundle/ folder so its already enabled. Try opening up a python file and typing 'def<tab>'. It should stub out a method definition for you and allow you to tab through and fill out the arguments, doc string, etc.

I also like to create my own snippets folder to put in some custom snippets:

	$ mkdir ~/.vim/snippets
	$ vim ~/.vim/snippets/python.snippets

Put this in the file:

	snippet pdb
		import pdb; pdb.set_trace()

Now you can type pdb<tab> and it'll insert your breakpoint!

**Comment: ** I didn't try this. Seems useless for me now.

### Task lists

Task lists

Another really useful thing is to mark some of your code as TODO or FIXME! I know we all like to think we write perfect code, but sometimes you just have to settle and leave a note for yourself to come back later. One of the plugins we included was the tasklist plugin that will allow us to search all open buffers for things to fix. Just add a mapping to open it in ~/.vimrc:

	map <leader>td <Plug>TaskList

Now you can hit <leader>td to open your task list and hit 'q' to close it. You can also hit enter on the task to jump to the buffer and line that it is placed on.

**Comment: **

1. If you don't this, there maybe a Error Message everytime starting GVim:

		Error detected while processing XXXXXXX\vimfiles\bundle\t
		asklist\plugin\tasklist.vim:
		line  369:
		E227: mapping already exists for \t
			
	It may be caused by mapping keys which is already mapped to something else. So remap it will solve this problem.

2. A description of this plugin found:

		This script is based on the eclipse Task List. It will search the file for FIXME, TODO, and XXX (or a custom list) and put them in a handy list for you to browse which at the same time will update the location in the document so you can see exactly where the tag is located. Something like an interactive 'cw'
	
3. About `<leader>`

	`<leader>` is a key name in vim, usually means "\" on keyboard.
	
### Revision History

The final basic editing tweak I suggest everyone start utilizing is the Gundo plugin. It'll allow you to view diff's of every save on a file you've made and allow you to quickly revert back and forth:
	
![Pic1](http://i.imgur.com/2NrPS.png)

Just bind a key in your .vimrc to toggle the Gundo window:

	map <leader>g :GundoToggle<CR>
	
### Syntax Highlighting and Validation

Simply enable syntax highlighting in your ~/.vimrc:

	syntax on                           " syntax highlighing
	filetype on                          " try to detect filetypes
	filetype plugin indent on    " enable loading indent file for filetype

Because we enabled pyflakes when we added it as a submodule in ~/.vim/bundle, it will notify you about unused imports and invalid syntax. It will save you a lot of time saving and running just to find out you missed a colon. I like to tell it not use the quickfix window:

	let g:pyflakes_use_quickfix = 0
	
![Pic2](http://i.imgur.com/ZfjFe.png)

### Pep8

The final plugin that really helps validate your code is the pep8 plugin, it'll make sure your code is consistent across all projects. Add a key mapping to your ~/.vimrc and then you'll be able to jump to each of the pep8 violations in the quickfix window:

	let g:pep8_map='<leader>8'

### Tab Completion and Documentation

Vim has many different code completion options. We are going to use the SuperTab plugin to check the context of the code you are working on and choose the best for the situation. We've already enabled the SuperTab plugin in the bundle/ folder, so we just have to configure it to be context sensitive and to enable omni code completion in your ~/.vimrc:

	au FileType python set omnifunc=pythoncomplete#Complete
	let g:SuperTabDefaultCompletionType = "context"

Now we just enable the menu and pydoc preview to get the most useful information out of the code completion:

	set completeopt=menuone,longest,preview

![Pic3](http://i.imgur.com/g4lxP.png)

We also enabled the pydoc plugin at the beginning with all the submodules; that gives us the ability to hit <leader>pw when our cursor is on a module and have a new window open with the whole documentation page for it.	

EOF - END
===============
Why? I ended this commenting just because I want to explorer about the functionality about Vim Scripts myself - not to be led by someone else without knowing anything detailed about Vim.

Actually, it's never good to get things done in a hurry by following other's guidance - You will lose the fun and skill acquired when really *hack* into something!

Sorry, though.
