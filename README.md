# Kaprekar's Constant (6174) Problem 🚀

The Kaprekar 6174 Problem is a famous number theory problem discovered by D.R. Kaprekar. It involves a mathematical process that, when repeatedly applied to a four-digit number (with at least two distinct digits), always leads to 6174 in a few iterations. This number is known as Kaprekar's Constant.

**Steps to Perform the 6174 Process**

Choose any four-digit number (not all digits identical, e.g., 1111 is invalid).

Arrange the digits in descending order and ascending order to form two numbers.

Subtract the smaller number from the larger one.

Repeat the process with the result.

You will always reach 6174 in at most 7 iterations.

**Example:** Applying Kaprekar’s Process
Let's take 3524 as an example:

**Step	Descending Order	Ascending Order	 Subtraction	Result**

  1	         5432	             2345	       5432 - 2345	3087

  2	         8730	             0378	       8730 - 378	  8352

  3	         8532	             2358	       8532 - 2358	6174 🎉

Once we reach 6174, repeating the process will always return 6174, so the process stops.

**Kaprekar’s Conjecture**

Any four-digit number (except repdigits like 1111, 2222, etc.) will reach 6174 in at most 7 steps.
If a number has less than 4 digits, leading zeros are added to make it four-digit (e.g., 0789 → 0789).
