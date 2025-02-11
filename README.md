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

**Step__Descending Order__Ascending Order__Subtraction__Result**

  1__________5432____________2345__________5432 - 2345___3087

  2__________8730____________0378__________8730 - 378____8352

  3__________8532____________2358__________8532 - 2358___6174 🎉

Once we reach 6174, repeating the process will always return 6174, so the process stops.

**Kaprekar’s Conjecture**

Any four-digit number (except repdigits like 1111, 2222, etc.) will reach 6174 in at most 7 steps.
If a number has less than 4 digits, leading zeros are added to make it four-digit (e.g., 0789 → 0789).

# Collatz Conjecture 🚀

The Collatz Conjecture (also called the 3x + 1 problem) is an unsolved problem in mathematics proposed by Lothar Collatz in 1937. It describes a sequence of numbers that always eventually reaches 1, no matter which positive integer you start with.

Collatz Conjecture Process 🔢

Start with any positive integer n.

If n is even, divide it by 2 → n = n / 2.

If n is odd, multiply it by 3 and add 1 → n = 3n + 1.

Repeat the process with the new value of n.

The sequence always reaches 1, though no one has been able to prove it for all numbers.

**Example:** Collatz Sequence for n = 12

Let's take 12 as an example:

**Step___n(Current Value)___Operation**

1__________12__________	Even → 12 / 2 = 6

2__________6___________	Even → 6 / 2 = 3

3__________3___________	Odd → 3 × 3 + 1 = 10

4__________10__________	Even → 10 / 2 = 5

5__________5___________	Odd → 5 × 3 + 1 = 16

6__________16__________	Even → 16 / 2 = 8

7__________8____________Even → 8 / 2 = 4

8__________4____________Even → 4 / 2 = 2

9__________2____________Even → 2 / 2 = 1 🎉

After 9 steps, we reach 1.

**Collatz Conjecture Properties**

No matter which number you start with, the sequence always seems to reach 1.

Some numbers take longer to reach 1 than others.

No mathematical proof exists that it works for all numbers, making it an open problem in mathematics.

