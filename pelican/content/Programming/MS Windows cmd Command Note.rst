MS Windows "cmd" Command Note
###############################

:date: 2014-03-02
:tags: MS Windows, Batch
:author: we.taper

Convention:

| # with overline, for parts
| * with overline, for chapters
| =, for sections
| -, for subsections
| ^, for subsubsections
| ", for paragraphs


2014-02-26
================

Because I don't know how to open a file by a batch script. I studied the grammar of batch file in windows.

    %: 批处理变量引导符
        这个百分号严格来说是算不上命令的，它只是批处理中的参数而已（多个%一起使用的情况除外）
        引用变量用%var%，调用程序外部参数用%1至%9等等
        %0  %1  %2  %3  %4  %5  %6  %7  %8  %9  %*为命令行传递给批处理的参数
        %0 批处理文件本身，包括完整的路径和扩展名
        %1 第一个参数
        %9 第九个参数
        %* 从第一个参数开始的所有参数
        参数%0具有特殊的功能，可以调用批处理自身，以达到批处理本身循环的目的，也可以复制文件自身等等。
        *Note:* Dealing with %var% could be toublesome, I just use %1 to gets the first parameter.
        
This is a script to show the first parameter::

    @echo off
    echo %1
    pause


So to open ".rst" file with ReText::

    cd /d d:\Apps\ReText-4.1.1\
    python retext.py %1