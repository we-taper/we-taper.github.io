Title: Assertion - Another Way to Commment & Debug
Date: 2014-4-17 
Tags: Java, Programming, unFinished, unPolished
Author: we.taper

Assertion is a claim, which says that you believe something must be true. In Programming, it acts as an check of the status of something. For example, if you want to find the maximum value of an `int[]` array, you should make sure that is index lies within the range. So:

	assert withinRange(index);

Now, you can proceed to the next process with confidence.

0. Enable assertion
-------------------------

When you write assert in your java code, java compiler will compile them into binary code file *.class*. However, JVM does run this code by default. This is because assertion is designed for programmers to debug and comment on their code. It is not intended to be produce effect on published program. Therefore, by default assertion is disabled in JVM to prevent end user from seeing them. Before we use assert in our program, we must first enable it. We should enable them by passing `"-enableassertion"` or `"-ea"` option to JVM. E.g.:

	java -ea ClassName

1. The Grammar
--------------------

Syntax for assertion is:

	assert Exp1;

or

	assert Exp1:Exp2;

Here, `Exp1` is the condition that you want to check and will return a boolean value. If the boolean is true, program proceeds normally. However, if your assertion is wrong and `Exp1` returns false, program stops immediately and there will be an `AssertionError` thrown with message provided by `Exp2` (if available). Now, you can deal with this error with the message provided by `Exp2`.

2. An Example
-----------------------

Here's a case. I want to write a program to add two binary number of equal length together.

Here's a pesudo-code of my algorithm:

	Input two array representing the two integers
	Suppose the two array are legal binary numbers of equal size.
	pre = 0 # Here carries the calculation carried by previous calculation.
	now # Carries number in this calculation.
	while index >= 1
		/*
		 * Note: 
		 * sum	now	pre 
		 * 1 	1 	0
		 * 2	0	1
		 * 3	1	1
		 * Clearly: 
		 * now = sum % 2 
		 * pre = sum / 2
		 */
		now = (a[index - 1] + b[index - 1] + pre) % 2;
		pre = (a[index - 1] + b[index - 1] + pre) / 2;
		result[index] = now;
		index--;
	# Now I should be sure that index has reached 0 -- the beggining of nmber.
	result[index] = pre;
	return result;

In this code, I have many *preconditions* and *postconditions*. I should take care of this conditions otherwise my code would not run properly. So how do I check this conditions? One may use `if` to test and run your code only `if`'s condition is correct. However, some of this check isn't necessary in client program (some of them are used only to check whether programmer have correctly write his code). This code will have effect ont your client -- possibly reduce the efficiency. So what to do now:

1. Remove the code after you code after debug or
2. Using assertion

Solution one is plausible in small applications. But in a large scale program, it is almost impossible to note down all this ifs and remove them after debuggin. It's best to write this code using java assertions because they **DO NOT** run if client does not enable assertion in JVM. Thus, *it has no side effect on published program.*

Here's my solution:

	public int[] addBinaryNumberOrg(int[] a, int[] b) {
		assert a.length == b.length && a.length > 0 : "a:" + a.length + "b:"
				+ b.length; // case 1
		// assert a is 1 / 0, b is 1 / 0. case 2
		int pre; // Number carried in previous calculation.
		pre = 0;
		int now; // Number in this calculation.
		int[] result = new int[a.length + 1];
		int index = result.length - 1;
		while (index >= 1) {
			now = (a[index - 1] + b[index - 1] + pre) % 2;
			pre = (a[index - 1] + b[index - 1] + pre) / 2;
			result[index] = now;
			index--;
		}
		assert index == 0 : "i:" + index; // case 3
		result[index] = pre;
		return result;
	}

Here I use asser three times (2 + 1). But we can cleary see that case 1 and 2 should throw an `IllegalArgumentException`. But case 3 is clearly something should be and only be checked when developming the program. So here's my final code:

	public int[] addBinaryNumber(int[] a, int[] b) {
		if(a.length != b.length) {
			throw new IllegalArgumentException("Different length: a:"+a.length+" b:"+b.length);
		}
		for(int i = 0; i < a.length; i++) {
			if(! ( (a[i] == 0) || (a[i] == 1) ) ) {
				throw new IllegalArgumentException("Not a binary number a:"+Arrays.toString(a));
			}
			if(! ( (b[i] == 0) || (b[i] == 1) ) ) {
				throw new IllegalArgumentException("Not a binary number b:"+Arrays.toString(b));
			}
		}
		/** Number carried in previous calculation. */
		int carriedFromPre = 0;
		int[] result = new int[a.length + 1];
		int index = result.length - 1;
		while (index >= 1) {
			result[index] = (a[index - 1] + b[index - 1] + carriedFromPre) % 2;
			carriedFromPre = (a[index - 1] + b[index - 1] + carriedFromPre) / 2;
			index--;
		}
		result[index] = carriedFromPre;
		return result;
	}

3. Why Using Assertion
---------------------------

### Quick Prototype

Using assertions to quickly write down your thoughts and turn them into code. Forget about the code to check the pre-conditions and post-conditions, just writen them inside assert block. Now you can run your code on the fly! Althought it may broke down for several times, the message inside `AssertionError` will provide you with enough information to debug, change and run your code again. This effectively speed up the development process, free your mind from caring about the pitifal of your code.

### Commenting

Sometimes your want to comment some special situations in your code, like:

	if(a > b) {
		// process a;
	}else{
		// a <= b
	}

Now your have a choose of using assertion:

	if(a > b) {
		// process a;
	}else{
		assert a <= b : "A: " + a + "B: " + b;
	}

**What is the benefit?**

Wow, adding a new keyword in Java just to introduce a new way of commenting? Yeah, it may not be so obvious but ......
#To Be Continued

Reference
----------------
1.[Oracle Java SE Documentation](http://docs.oracle.com/javase/7/docs/technotes/guides/language/assert.html)
