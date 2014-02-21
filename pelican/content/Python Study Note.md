Title: Python Study Note (Last update: 2014-2-21)
Date: 2014-2-21 14:00
Category: Python
Tags: Python
Slug: Python Study Note
Author: we.taper
Summary: My Python Study Note.

#Python Study Note

##2014-02-17

**About Unicode**
*(python 3.3)*
When using `\xxx` to display Unicode characters, the encoding of the source file
also counts. e.g, if you type:

		s = '\xc4'
		print(s)
	
In a GBK based file, interpreter says:

		Error:
		UnicodeEncodeError: 'gbk' codec can't encode character '\xc4' in 
		position 2: illegal multibyte sequence
	
On the other hand, inside a UTF-8 file:

		'Ä'

**About Statements**
*Refer to: Page 320, Learning Python 5th, O'Reilly, ISBN: 978-1-449-35573-9*

![Statements](Statement_In_Python.png "Statements in Python")

![Statements_2](Statement_In_Python_2.png "Statements in Python")

**About ++/--**

In python, there is no ++/-- operator, see [Stack Overflow][s_o] and 
[Python IAQ][p_iaq] for more. 

However `++x` makes sense, which means `+(+(x))`,
so basically it's simply `x`.

[s_o]:http://stackoverflow.com/questions/3654830/why-are-there-no-and-operators-in-python
[p_iaq]:http://norvig.com/python-iaq.html

**About Assignment Statements**

*Refer to: Page 340, Learning Python 5th, O'Reilly, ISBN: 978-1-449-35573-9*

![Assignment Statements](Assignment_Statements.png "Assignment Statements Examples")

**Argumented Assignment, Performance**

If the subject is mutable and supports this operation, an augmented assignment 
may run even quicker by choosing an in-place update operation instead of an 
object copy. 
