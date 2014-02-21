Title: Git Book Note (Last update: 2014-2-21)
Date: 2014-2-21 14:00
Category: Programming
Tags: Git, VCS
Slug: Git Book Note
Author: we.taper
Summary: My Git Study Note, based on Git Documentation.

#Git Start

**Note: ** Most of the content below are based on the book available on Git Documentation: [Git book][g_b]
[g_b]:http://git-scm.com/doc
<br>
##1. Basic concept

*See: *[Git book - chapter 1.3](http://git-scm.com/book/en/Getting-Started-Git-Basics)

1. Git is a "mini file system"
    
    Git use a special *"snapshot"* to store changes made to file(see Git book, chapter 1.3).
	Git knows every change you made to the file by calculating a SHA-1 checksum of files. Git 
	does most things locally so you can work without a network connection. Nearly all operations 
	on git are "adding files", which means you can experiment on anything without worrying if 
	you can get back to the original state. Also, every git clone copies everything on the 
	*"master"* branch, therefore even the main server where *"master"* code resides is shot, 
	everything can be recovered.

2. The three states of files inside *"Git file system"*
    
    One simple diagram:

![Three states](http://git-scm.com/figures/18333fig0106-tn.png)

**  What we do on git?**

**  A General Workflow on Git**

> 1. You modify files in your working directory.
> 2. You stage the files, adding snapshots of them to your staging area.
> 3. You do a commit, which takes the files as they are in the staging area 
and stores that snapshot permanently to your Git directory.

###1.1 Install Git

*See  *[Git book - chapter 1.4](http://git-scm.com/book/en/Getting-Started-Installing-Git)

I personally like the git plugin *EGit* (found on Eclipse Market) for Eclipse 
since I use Eclipse on Windows.

###1.2 Configure Git

*See  * [Git book - chapter 1.5](http://git-scm.com/book/en/Getting-Started-First-Time-Git-Setup)

Since I don't want to consider too much about git, skip this.

###1.3 Get help
-------------
*see  *[Git book - chapter 1.6](http://git-scm.com/book/en/Getting-Started-First-Time-Git-Setup)

Code:

    git help <verb>
    git <verb> --help
    man git-<verb>     #For Linux manual page



##2. Let's Rock

### 2.1 Get a Git Repository
*See :* [Git book - chapter 2.1](http://git-scm.com/book/en/Git-Basics-Getting-a-Git-Repository)

Basically, we first *create* a repository somewhere, then others can *clone* this repository. After
cloning or creating, you can *add* files and then commit to the repository.

####Command List

    # Create
    git init
    # Add
    git add FileName(support *)
    # Commit
    git commit -m 'Commit Comment'
    # Clone
    git clone [url]
    # Clone Examples
    git clone git://github.com/schacon/grit.git NameOfDirectory # Git transfer protocol
    git clone http(s)://github.com/schacon/grit.git # HTTP(s)
    git clone user@server:/path.git # SSH

###2.2 Record change to Repository
*See :*[Git book - chapter 2.2](http://git-scm.com/book/en/Git-Basics-Recording-Changes-to-the-Repository)

The full Life Cycle of a File:

![Life Cycle](http://git-scm.com/figures/18333fig0201-tn.png)

**Note: ** Unadded file are **not** tracked, so Git **doesn't care** about this files.

####Staged

When files added (under the control of Git) once modified, it need to be staged to the staging
area. Command of stage is the same as add:

    git add FileName # "add" is multi-purpose, can add and stage files.

####Ignored files.

File *.gitignore* store patterns of file names which will be ignored by git. Rules
are as follows:

+ Blank lines or lines starting with # are ignored.
+ Standard glob patterns work.
+ You can end patterns with a forward slash (/) to specify a directory.
+ You can negate a pattern by starting it with an exclamation point (!).

    **Glob patterns** are like simplified regular expressions that shells use. An **asterisk (*)**
	matches zero or more characters; **[abc]** matches any character inside the brackets (in this 
	case a, b, or c); a **question mark (?)** matches a single character; and **brackets** enclosing 
	characters separated by a hyphen([0-9]) matches any character in the range (in this case
	0 through 9) .
    
    *See:  *[Unix Man Page][ump] and [Wikipedia Page][wp_gp]

[ump]:http://unixhelp.ed.ac.uk/CGI/man-cgi?glob+7
[wp_gp]:http://en.wikipedia.org/wiki/Glob_%28programming%29

####See *"What happens?"*

To see the general status of *"Which file have been modified but unstatged"* or *"Which file have
been staged but uncommited?"*, use:

    git statue

For more detailed information about what actually changed inside files, use `diff`:

See the difference between **Working Directory** and **Staging Area**

    git diff
    
See the difference between **Staging** and **Repository(Commited)**

    git diff --staged
    
####Now Commit

    git commit  
	# Will open a editor to edit the "Commiting Message"

    git commit -a  
	# Will makes Git automatically stage every file that is already tracked  
	before doing the commit, letting you skip the git add part

####Remove files

Remove from tracked file list:

    git rm FileName
    
Remove from staged directory (file is kept in working directory):

    git rm --cached FileName

**Note: **Deleting files on harddrive doesn't delete them from git's tracked file list.
Instead ther are marked "delete" when you type `git status`

####Moving Files

**Note :** "Rename" == "Moving to the *Same* directory"

    git mv file_from file_to

Above is equal to:

    mv file_from file_to
    git rm file_from
    git add file_to

###2.3 : Skipped
###2.4 Git Basics - Undoing Things

*See *: [Git book- chapter 2.4](http://git-scm.com/book/en/Git-Basics-Undoing-Things)

####Git Command

+ Change last commit  

        git commit --amend

    This command takes your staging area and uses it for the commit. If you’ve made no
	changes since your last commit (for instance, you run this command immediately after
	your previous commit), then your snapshot will look exactly the same and all you’ll 
	change is your commit message. The same commit-message editor fires up, but it already
	contains the message of your previous commit. You can edit the message the same as
	always, but it overwrites your previous commit.

+ Unstage File

        git reset HEAD <file>...
    
+ Unmodifyed a File

        git checkout -- <file>...  
		# Note: This cannot be undone since the file hasn't be commited
		and therefore not recorded by git.
    
## Branching


###What a Branch Is

*See :* [ Git book - chapter 3.1](http://git-scm.com/book/en/Git-Branching-What-a-Branch-Is)

**Note :** Here I tried to make everything simple but if you wnat a true picture
of how  branch works in Git, please refer to the original document.

Git take **snapshot** of every version (commit) of your files. A **Branch** is just a 
diverged series of snapshots. Think of a tree which start with a **master** trunk, then
it can stretches out different **branches**. All this branches are linked with their 
parent (either a **master** trunk or a derived **branch**) with **nodes** - the mother 
snapshot they all share. To go back to a older version or another branch, just trace 
back to the *mother snapshot* and choose a different route.

Diagram of branches (named in *pointer* style):

![Branch](http://git-scm.com/figures/18333fig0309-tn.png)

Basic Branching and Merging
----------------------------
*See :* [Git book - chapter 3.2](http://git-scm.com/book/en/Git-Branching-Basic-Branching-and-Merging0)

**Git commands:**

+ Create a branch:

        git branch NAME

+ Switch to a branch:

        git checkout NAME
        
+ Create and Switch (shortened):

        git checkout -b iss53 #equal:git branch iss53 \ git checkout iss53
        
+ Delete a branch:

        git branch -d NAME

+ Merge a branch:

        git merge NAME 
		# Note: the "NAME" branch will be merged into current branch you are working on.
    
**Note :** 

1. Switch (chekout):

    Git resets your working directory to look like the snapshot of the commit that the 
	branch you check out points to. It adds, removes, and modifies files automatically 
	to make sure your working copy is what the branch looked like on your last commit 
	to it.

2. Merge:

    1. "Fast-forward":

        When the commit pointed to by the branch you merged in is directly upstream of 
		the commit you’re on, Git moves the pointer forward. To phrase that another way,
		when you try to merge one commit with a commit that can be reached by following
		the first commit’s history, Git simplifies things by moving the pointer forward
		because there is no divergent work to merge together — this is called a "fast 
		forward".
    
    2. Resolve Conflicts:
        If you changed the same part of the same file differently in the two branches 
		you’re merging together, Git won’t be able to merge them cleanly. Git hasn’t 
		automatically created a new merge commit. It has paused the process while you 
		resolve the conflict. If you want to see which files are unmerged at any point 
		after a merge conflict, you can run `git status`
        
        Git adds standard conflict-resolution markers to the files that have conflicts, 
		so you can open them manually and resolve those conflicts. Your file contains a 
		section that looks something like this:
        
			<<<<<<< HEAD
			contact : email.support@github.com<br>
			=======
			please contact us at support@github.com<br>
			>>>>>>> iss53
        
        This means the version in **HEAD** (your master branch, because that was what 
		you had checked out when you ran your merge command) is the top part of that 
		block (everything above the `=======`), while the version in your **iss53** 
		branch looks like everything in the bottom part. In order to resolve the conflict,
		you have to either choose one side or the other or merge the contents yourself.
        
        After you’ve resolved each of these sections in each conflicted file, run `git add` 
		to add each file to mark it as resolved. Staging the file marks it as resolved in 
		Git. If you want to use a graphical tool to resolve these issues, you can run 
		`git mergetool`, which fires up an appropriate visual merge tool and walks you 
		through the conflicts
        
        After you exit the merge tool, Git asks you if the merge was successful. If you 
		tell the script that it was, it stages the file to mark it as resolved for you.
        
        If you’re happy with that, and you verify that everything that had conflicts has 
		been staged, you can type `git commit` to finalize the merge commit.


###Working with remote branch

*See :*[Git book - chapter 3.5](http://git-scm.com/book/en/Git-Branching-Remote-Branches) 
as well as [Git book - chapter 2.5](http://git-scm.com/book/en/Git-Basics-Working-with-Remotes)

**What ? :** Remote branches are just branches pointed to remote serves, taking the form 
of `(remote)/(branch)`. However, remote branches can be modified without noticing, so please
synchronize it frequently.

1. See Status

        git remote command  
    It lists the shortnames of each remote handle you’ve specified. If you’ve 
	cloned your repository, you should at least see origin — that is the default 
	name Git gives to the server you cloned from.
    
        git remote -v  
    It shows you the URL that Git has stored for the shortname to be expanded to.
    
        git remote show [remote-name]  
    It lists the URL for the remote repository as well as the tracking branch information. 

2. Add  
        git remote add [shortname] [url]  
    e.g.  
        git remote add pb git://github.com/paulboone/ticgit.git  
    Now you can use the string *pb* on the command line in lieu of the whole URL.
    
3. Fetch  
        git fetch [remote-name]  
    e.g.  
        git fetch pb  
    **Note :** The fetch command pulls the data to your local repository — it 
    doesn’t automatically merge it with any of your work or modify what you’re 
    currently working on. You have to merge it manually into your work when 
    you’re ready.  
    It’s important to note that when you do a fetch that brings down new remote 
    branches, you don’t automatically have local, editable copies of them. You 
    only have an `origin/remote` pointer that you can’t modify.  
    To merge this work into your current working branch, you can run `git merge 
    origin/remote`. If you want your own remote branch that you can work on, you
    can base it off your remote branch:  
        git checkout -b local_remote origin/remote

4. Push to Upstream  
        git push [remote-name] [branch-name]  
    This command works only if you cloned from a server to which you have write
    access and if nobody has pushed in the meantime. If you and someone else clone
    at the same time and they push upstream and then you push upstream, your push
    will rightly be rejected. You’ll have to pull down their work first and
    incorporate it into yours before you’ll be allowed to push. 

    You can push a local branch into a remote branch that is named differently.  
	
    	git push [remotename] [localbranch]:[remotebranch]  
    Like, if you didn’t want it to be called *a* on the remote, you could instead run:   
	
        git push origin a:awesomebranch  
    to push your local *a* branch to the *awesomebranch* branch on the remote project.

5. Rename  

        git remote rename OLD_NAME NEW_NAME  

6. Remove  

        git remote rm paul [remote-name]
    
    It removes a reference for the remote branch.

7. Delete Remote Branch

		 git push [remotename] :[bran	ch]  
	 e.g, If you want to delete your serverfix branch from the server, you run 
	 the following:  
	 	git push origin :serverfix
	 
	 **Note: **  A way to remember this command is by recalling the `git push 
	 [remotename] [localbranch]:[remotebranch]` syntax that we went over a bit 
	 earlier. If you leave off the [localbranch] portion, then you’re basically 
	 saying, “Take nothing on my side and make it be [remotebranch].”

7. Clone it.

         git clone [url]
         
     If you clone from this, Git automatically names it origin for you, pulls down 
	 all its data, creates a pointer to where its master branch is, and names it 
	 origin/master locally; and you can’t move it. Git also gives you your own master 
	 branch starting at the same place as origin’s master branch, so you have something
	 to work from. See:  
     ![Clone Remote](http://git-scm.com/figures/18333fig0322-tn.png)


***To Be Conitnued***