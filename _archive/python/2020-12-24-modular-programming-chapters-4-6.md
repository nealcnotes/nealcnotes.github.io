---
title: "Modular Programming - Chapters 4-6"
categories: 
  - "python"
---

- _Chapter 4 - Using Modules for Real-World Programming_
    - There's an example which shows the modular approach helps when requirements change. Though the example is long, it is also instructive. _Changing requirements is one of the primary software challenges._
    - There's code but there was a problem with fonts - so some of the example code didn't run.
- _Chapter 5 - Working with Module Patterns_
    - Encapsulation
        - Encapsulation is the idea that you hide information about "things" that a program is concerned with in objects using e.g. get/set methods. Although this is a widespread practice, it is also not obviously a good one in many cases, for example
            - [https://www.infoworld.com/article/2073723/why-getter-and-setter-methods-are-evil.html](https://www.infoworld.com/article/2073723/why-getter-and-setter-methods-are-evil.html)
    - Wrappers
        - A simple example involving banks doesn't show us the value of having wrapped the some functions from numpy, because they are themselves somewhat simple. It would be more instructive to wrap a complex abstraction into a simpler one.
    - Extensible modules
        - Introduces dynamic imports which allow original code to be written so it can be extended with modules that may be written in the future but are not available at the time the original code was being written.
        - He gives a simple but very powerful example calling importlib with a string formatted according to the chart format and output. Plugins and hooks are a similar concept. This example is worth studying.
- _Chapter 6 Creating Reusable Modules_
    - Another nice example program that converts e.g. distance, volume etc. units - long example so better if you clone the book's code from github.
    - The code in the book works, but if you try variations e.g. gallons to liters or add and subtract, per the test file comments, it doesn't work (at least right off the bat). Even so might be a good case to try to fix or debug or perhaps works slightly different from book examples.
