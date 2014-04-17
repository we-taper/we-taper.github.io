Title: Assertion - Another Way to Commment & Debug
Date: 2014-4-17 
Tags: Java, Programming, unFinished, unPolished
Author: we.taper

Assertion is a claim, which says that you believe something must be true. In Programming, it acts as an check of the status of something. For example, if you want to find the maximum value of an `int[]` array, you should make sure that is index lies within the range. So:

	assert withinRange(index);

Now, you can proceed to the next process with confidence.

0. Enable assertion
-------------------------

Assert code will be contained in *.class* file. However, JVM does run this code by default. This is because assertion is designed for programmers to debug and comment on their code. It is not intended to be included in published program. Therefore, by default assertion is disabled in JVM to prevent end user from seeing this. Before we use assert in our program, we must first enable it. We should enable them by passing `"-enableassertion"` or `"-ea"` to JVM. E.g.:

	java -ea ClassName

1. The Grammar
--------------------

Syntax for assertion is:

	assert Exp1;

or

	assert Exp1:Exp2;

Here, `Exp1` is the condition that you want to check and will return a boolean value. If the boolean is true, program proceeds normally. However, if your assertion is wrong and `Exp1` returns false, program stops immediately and there will be an `AssertionError` thrown with message provided by `Exp2` if available. Now, you can deal with this error with the message provided by `Exp2`.

2. An Example
-----------------------

Suppose you have two arraies, both sorted in ascending order. You would like to merge them together in good order. Here's a pesudocode:

	# Input array a,b
	resultArray = a new array of size(a+b)
	currentOne = last index of resultArray
	currentA = last index of a;
	currentB = last index of b;
	do{
		resultArray[currentOne] = MaximumOf(a[currentA],b[currentB])
		currentOne -= 1
		currentA -= 1 or currentB -= 1 (depends on which is added to resultArray)
	}while(currentOne >= 0)

Here we should assume that the index of resultArray, a, b (currentOne, currentA, currentB) are reasonable, so:

	# Input array a,b
	resultArray = a new array of size(a+b)
	currentOne = last index of resultArray
	currentA = last index of a;
	currentB = last index of b;
	do{
		assert currentOne, currentA, currentB within range;
		resultArray[currentOne] = MaximumOf(a[currentA],b[currentB])
		currentOne -= 1
		currentA -= 1 or currentB -= 1 (depends on which is added to resultArray)
	}while(currentOne >= 0)

The resulting code in java would be something like this:

	// Input a,b two arrays, return array
	array = new int[a.length+b.length];
	int aCurnt = a.length - 1, bCurnt = b.length - 1, arrayCurnt = array.length - 1;
	do{
		assert aCurnt >= 0 : "aCur:"+aCurnt;
		assert bCurnt >= 0 : "bCur:"+bCurnt;
		if(a[aCurnt] > b[bCurnt]) {
			array[arrayCurnt] = a[aCurnt];
			aCurnt -= 1; arrayCurnt -= 1;
		}else{
			assert a[aCurnt] <= b[bCurnt];
			array[arrayCurnt] = b[bCurnt];
			bCurnt -= 1; arrayCurnt -= 1;
		}
	}while( arrayCurnt >= 0 );
	return array;

3. Why Using Assertion
---------------------------

### Quick Prototype

Using assertions to quickly write down your thoughts and turn them in code. Forget about code to check the pre-conditions and post-conditions, just writen them inside assert block. Now you can run your code on the fly! Althought it may broke down for several times, the message AssertionError will provide you with enough information to debug, change and run your code again. This effectively speed up the development process, free your mind from caring about the pitifal of your code.

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