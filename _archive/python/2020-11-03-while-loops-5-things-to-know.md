---
title: "While loops: 5 things to know"
categories: 
  - "python"
tags: 
  - "syntax"
---

## Number 1: what is a while loop:

Loops cause computers to repeat certain calculations in certain ways. While loops are one of the basic building blocks of programs. They can be a simple way to cause the program to repeat a particular set of instructions while a specific condition holds.

For example, we may want to repeatedly add numbers, sales or units, to find a total. While loops tell a computer to repeatedly perform such an instruction while a certain condition holds. Continuing the example, we may have a sales log file. Whenever a sale occurs, a program may add row a with the date, order number, quantity, price, and part number.

We may want to write a new program that instructs the  
computer to read rows of the logfile and sum up the quantity\*price. The while loop would help us total amount over the whole logfile, reading and summing while there are rows of data.

But we can do more complex tasks, such as finding sales up to Jan 1 of this year, by adding a condition to the while that the date is before jan 1 of this year. Similarly we can sum while the subtotal is below $20,000, which would tell us how long and what transactions let to that amount.

Though powerful, we face a learning curve when starting to write while loops. Here we cover 2 main categories of issues.

## While Condition

### Number 2: Never stopping

The while loop repeats the instructions while a certain condition holds, and stops repeating when that condition no longer holds. So the condition in the while loop needs to correctly capture all situations when the instructions are supposed to

- run, and
- stop

The classic error is the runaway while loop  
here the stop is not reached:

i = 0
while i < 10:
    print(i)

### Number 3: Never starting

Another classic is one where the loop never runs to begin with

i = 10
while i < 10:
    print(i)

## Issues with updating

### Number 4: updating issues

The other key issue is that the while loop typically needs to update some aspect of the data, such as a variable or a file  
Often some arithmetic or complex logic is involved. These lead to many issues and need to be thoroughly understood while example with

i = 0
while i <= 10:
    print(i)
    i = i \* 1.1

will never end because multiplication by 0 always results in 0. 
Similarly

i = 0.1
while i <= sqrt(i):
    i = sqrt(i)
    print(i)

will never terminate because although i gets larger each time through the loop, it will never reach 1 since sqrt(x) < 1 for all x

### Number 5: The off-by-1 error

The last is the off-by-1. Often loops have a small issue with the  
update or with the while condition that causes errors that are  
either 1 more or 1 less than the desired outcome in some way.  
For example we may want to print 10 numbers but get 11:

i = 0
while i <= 10:
    print(i)
    i += 1

or we may get 9 numbers:

i = 1
while i < 10:
    print(i)
    i += 1

There are likewise 2 ways to get 10 numbers, only one of which might  
be desired outcome

i = 1
while i <= 10:
    print(i)
    i += 1

or

i = 0
while i < 10:
    print(i)
    i += 1
