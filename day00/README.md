# Day 00 - Python Bootcamp

### Exercise 00: Blockchain

So right now we don't know much about the implementation of this blockchain, all we have is a file with some lines like the one above. But you might have noticed a pattern — some lines start with multiple zeros. So let's write a Python script that can take some text from its standard input and then print only the lines that start with exactly 5 zeros.

Note that the data has been corrupted, so you have to be very careful. That is, only lines that meet certain criteria are considered valid:

- Correct rows are 32 characters long.
- They start with exactly 5 zeros, e.g. a line starting with 6 zeros is NOT considered correct.

So for the example above, your script should print:

```
00000254b208c0f43409d8dc00439896
0000085a34260d1c84e89865c210ceb4
0000071f49cffeaea4184be3d507086v
```

Your code should take the number of lines as an argument, such as the following:

`~$ cat data_hashes_10lines.txt | python blocks.py 10`

This way, the program will stop when it has processed 10 lines. Note that with this approach, the program may hang if the number of lines in a file is less than the number in the argument. This is not considered an error.

### Exercise 01: Decypher

Could you find out how Sherlock figured it out and write a Python script that could be used to decrypt any message like this? (If you want to solve this mystery yourself — don't look at the checklist right away). It should run like this:

`~$ python decypher.py "Have you delivered eggplant pizza at restored keep?"`

and print out the answer as a single word without spaces.

### Exercise 02: Track and Capture

So, as input, your code is given a 2D "image" as text in a file `m.txt`. The file contains five characters over three lines, like this:

```
*d&t*
**h**
*l*!*
```

You may notice that there is a pattern of stars with the letter M. All your code has to do is print 'True' if this M pattern is present in a given input image, or 'False' otherwise. Other characters (outside the M pattern) should be different, so these examples should print 'False':

```
*****
*****
*****
```

```
*s*f*
**f**
*a***
```

If a given pattern is not 3x5, then the word 'Error' should be printed instead. The code file should be named `mfinder.py`.

If you do this, Lestrade will upload this code to the police servers and all the terrorists will be located by the cameras in no time.

And Sherlock will be ready for another challenge organized by a mysterious man hiding behind the letter M. Sometimes it seems that these puzzles are designed especially for him...
