Title: Read Different Encoding in Java
Date: 2014-3-4
Tags: Java
Author: we.taper
Summary: Show how to read files in different encodings in Java

Read Different Encoding in Java
====================================

Encoding could be quite a problem when reading text-based files. The Java `Scanner` can constructed with specified encoding: `new Scanner (InputStream, Encoding)`. However, this doesn't help when we don't know the encoding of files programs are reading. So we have to detect the encoding before reading it.

1. Detect Encoding
--------------------

There is a method in InputStreamReader called `getEncoding();`. However, it never return the correct encoding of file but rather the encoding used by this stream, which is always GBK on my machine.

I found a library on Internet to detect encodings: [juniversalchardet][JUCD] which  is a Java port of 'universalchardet', the encoding detector library of Mozilla. 
[JUCD]:http://code.google.com/p/juniversalchardet/

Using it is quite straight forward if you have previous experience with using external packages. Read the `ReadMe` file inside downloaded source archive and here you go.

**License Note:** The library is subject to the Mozilla Public License Version 1.1. Alternatively, the library may be used under the terms of either the GNU General Public License Version 2 or later, or the GNU Lesser General Public License 2.1 or later.

However, this library failed to get the encoding of my files too many times, so I found another project powered by IBM and used by many Companies: [ICU - International Components for Unicode][icu]. License is quite complicated though, the library is open-sourced.

[icu]:http://site.icu-project.org/	

Using is also very simple. My example:

	public static String getEncoding(File textFile) throws FileNotFoundException, IOException {
		com.ibm.icu.text.CharsetDetector cd = new com.ibm.icu.text.CharsetDetector();
		java.io.FileInputStream fis = new java.io.FileInputStream(textFile);
		java.io.BufferedInputStream bis = new java.io.BufferedInputStream(fis);
		cd.setText(bis);
		CharsetMatch cm = cd.detect();
		return cm.getName();
	}

**Note: ** The `InputStream` must support `mark`, i.e. the `InputStream.markSupported()` must return `true`. Support `mark` or not is invariant for a specified stream, e.g. `BufferedInputStream` supports while `FileInputStream` doesn't support.

**See :** [StackOverflaw - Java : How to determine the correct charset encoding of a stream](http://stackoverflow.com/questions/499010/java-how-to-determine-the-correct-charset-encoding-of-a-stream)