Title: Markdown Showcase
Date: 2014-2-21 14:00
Tags: Markup Language
Slug: Markdown Showcase
Author: we.taper
Summary: Show how to use Markdown.

#Show how to use Markdown

# This is a title, level 1
## Next level title, level 2 ##

##Paragraph
- Intro

	> I
	> am
	> on the same
	> line.
	
	> I am on two  
	> lines.

Can you figure out why?

##Code blocks

	public static void main(){
		System.out.printf("Hello Markdown!");
	}
And a code inside text `println("I love she");` Do you know who is `she`?

A code to display "\`":

 ``This is ` used to add in-text code blocks``.

###HTML codes

<strong> Yes!! </strong>

&#8212; is the decimal-encoded equivalent of &mdash;

##For those who are tired of HTML escape mark

See this: &copy, isn't it simple. And another *AT&T*. Yeah!

<div class="footer">
	&copy; 2004 Foo Corporation
</div>

*link:*<http://www.google.com/>

*E-Mail:*<we.taper@mail.com>

*(Actually I don't quite understand HTML, but it's fun!)*


##Let's construct some list:

 1. List one;
 3. Oops, a wrong but acceptable;
 2. Oh, this is cool.
 232323. Wow, the Markdown interpreter is really intelligent.
 1. This may spoil me.
 4. Let's get back to the right way.
 5. Yes.(should be 7)
 * Another list 1
 - 2
 + 3
 	+ Indent.
 	- Let's have dinner.
 		* More indent!
 		* > And mix things together. (This seems to failed)
 		* `System.out.print("Text");`
 		
1\. I'm bit tired.
3\. Yes.

##Quotation 

Let me learn from the masters:

> Quote: *Keep It Simple Stupid* -> **K.I.S.S**

> And This: _Learn from your failure_

> And: __Look for the masters__

See how to escape special characters: \* A star! * Another star.

***
---
___
## At last, Let's get some visual image.

###Pictures

**A inline picture**

![Replace text if no picture](http://img.21cbh.com/uploadfile/2013/0325/20130325091356249.jpg "Optional title")

**A referenced picture**

![Again, replace text: unsupported png][pic_id]

[pic_id]:http://img.21cbh.com/uploadfile/2013/0325/20130325091356249.jpg "Title"

**Picture With Link**

[![IMAGE TEXT HERE](http://img.21cbh.com/uploadfile/2013/0325/20130325091356249.jpg)](http://www.google.com.hk)

###Links

I love Google:[Google](http://www.google.com.hk/ "Google's Title")

**Three types of links**

1. In-line: look above!
2. Referenced:
	1. [Text_1] [id_1]
	2. [Text_1] [id_2]
	3. [Text_3] [id_3]
	4. *You will understand how I love Google when you clicked the above links.*

[id_1]:http://www.google.co.jp/ "Google Japan"
[id_2]:http://www.google.co.uk/ "Google UK"
[id_3]:http://www.google.com/ "Google Original"


##Some Syntax of HTML

+ Use < br > to do "line feed"

#Last but not least, Escape The Markers
\*literal asterisks\*

__Markdown__ 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：

		\   反斜线
		`   反引号
		*   星号
		_   底线
		{}  花括号
		[]  方括号
		()  括弧
		#   井字号
		+   加号
		-   减号
		.   英文句点
		!   惊叹号



#Thanks
Who has taught me:

1. *wowubuntu.com* : [wowubuntu][id_wow]
2. Other Websites found via Google

[id_wow]:http://http://wowubuntu.com/markdown/ "wowubuntu"