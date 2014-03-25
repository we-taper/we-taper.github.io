Title: Pentadactyl - Use Vim in Firefox
Date: 2014-3-23
Tags: Firefox, Vim
Author: we.taper
Summary: Show how to use Pentadactyl in Firefox.

Pentadactyl - Use Vim in Firefox
====================================

Introduction
------------------

As a crazy lover in Vim, You will expect Vim-like key-bindings everywhere. Here's a firefox plugin to embed Vim into my favorite browser firefox. This plugin is developed by the original maintainer of Vimperator - another plugin in firefox to implement Vim into firefox. They changed to this new plugin to make the best of new js engine in firefox 4 (and later).

**Note: ** You should at least have used Vim before to read throught this guide, otherwise there would be many unfamiliar things which would caused quite a pain if you continue.

Usage
--------------

# Basic

Install it from official firefox plugin center.

You might get quite confused when you first use Pentadactyl since it hide almost everything inside firefox. So, to bring back something familiar, use command:

	:set guioptions+=xxxxx

If you have some familarity of Vim, you certainly understands how to type this command into firefox. Pentadactyl provides a very user-friendly input window for you. As you type the command, some suggestions show up automatically. You will find, in these suggestions, some parameter you can put to replace the "xxxxx" in above command. For example, you can add Bookmark bar , Toolbar and Status bar to current window by:

	:set guioptions+=BsT

Actually, you will certain guess if there is a `set guioptions-=xx`. Yes, there is! What does it mean? Guess it yourself.

# Quick Start

Using Pentadactyl is really easy for those who has already use Vim. I always like first look at the *Quick-Start tutorial* os everything. Here's the quick start guide for Pentadactyl: [Quick-Start](dactyl://help/tutorial) (You should have Pentadactyl installed to open this link.)

Tip:

+ Normal scrolling mode in Vim command mode works the same for Pentadactyl.
+ Use `Ctrl+n`, `Ctrl+p` for navigating between tabs and `H`, `L` for history.
+ Use `y` to copy text. **Note: ** Use `Y` (captalized) to copy current text into system clipboard instead of `y`. (See more at `:help copying`).
+ At start up, Pentadactyl will execute contents inside `~/.pentadactylrc`. This is the place where you can prepare your own working environment (just like `vimrc`). `~` means the home path, which depends on the underlaying OS.
+ Sometimes we get so familiar with the default key-bindings in firefox, here `Ctrl-V` will pass all the following commends directly to firefox. (This is called `pass through` mode.)