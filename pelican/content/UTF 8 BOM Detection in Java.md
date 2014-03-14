Title: UTF 8 BOM Detection in Java
Date: 2014-3-6 23:00
Category: Programming
Tags: Java, UTF-8
Author: we.taper

UTF 8 BOM Detection in Java
==================================

Have you ever encountered like this: Reading a file encoded in UTF-8, but always found it starts with a mysterious character which may be printed as "?" into screen but is not seen in any text editor. This is caused by the BOM of UTF-8 files.

What is BOM?
----------------

See this: [Wikipedia BOM](http://en.wikipedia.org/wiki/Byte_order_mark)

BOM is, put simply, some marks used to identify the encoding of text, but it is not necessarily required in UTF-8 standard, see:

> While there is obviously no need for a byte order signature when using UTF-8, there are occasions when processes convert UTF-16 or UTF-32 data containing a byte order mark into UTF-8. When represented in UTF-8, the byte order mark turns into the byte sequence. Its usage at the beginning of a UTF-8 data stream is neither required nor recommended by the Unicode Standard, but its presence does not affect conformance to the UTF-8 encoding scheme. Identification of the byte sequence at the beginning of a data stream can, however, be taken as a near-certain indication that the data stream is using the UTF-8 encoding scheme.

[Link To Document](http://www.unicode.org/versions/Unicode6.0.0/ch03.pdf)

Plus: [A discussion on ZhiHu](http://www.zhihu.com/question/20167122)

How to Deal with BOM
-----------------------

There could be many ways to do it but I found a simple solution. I figured out the unicode representation of BOM is `\uFEFF`. Therefore, if any UTF-8 file started with character `\uFEFF`, just remove the first character from it will sovle this problem.

How to Write files without BOM
-----------------------------------

Well, most text editors under Windows will automatically add BOMs to your UTF-8 files because this is favoured by Microsoft, the only exception I know of is notepad++, a great text editor for programmers (other exception? Feel free to inform me by E-mail). So basically you have to live with it on Windows.

Things get much better in Linux. With UTF-8 everywhere, Linux never use this BOM to identify a UTF-8-based file from ANSI-based file. Maybe I will never got to worry about BOM in Linux. Thanks for Microsoft's stupid idea to remind me of BOMs.