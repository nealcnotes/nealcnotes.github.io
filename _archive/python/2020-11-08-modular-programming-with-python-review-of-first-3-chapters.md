---
title: "Modular Programming with Python - review of first 3 chapters"
categories: 
  - "python"
tags: 
  - "syntax"
---

Review Post - Modular Python by Erik Westra, Chapters 1-3

- Functions are one of the most powerful tools in programming. As with any powerful tool, they also raise many questions and issues. Python has a specific terminology around functions, along with how to organize them into files that define Python modules. This book teaches firstly, Python modules as files that have Python functions, and secondly, modular programming in general. Modular programming is organizing large programs into pieces that you can reuse as requirements change. In this post I review how the book explains Python modules from the perspective of files of Python functions for those of us who want to learn how python modules work.
- Chapter 1: Introducing Modular Programming
    - The introduction has some good basic goals. However the very first modular program uses very slightly advanced points that are irrelevant for the purpose of explaining modules, for example module-level global variables and exceptions. That said, for programmers who are not beginners, this is fine.
    - The next example, though somewhat simpler, similarly glosses over concepts which Westra hasn't really introduced yet. The example packages a group of animal modules (toy Python functions in toy Python files) into an animal package, along with its initialization file - although we are still trying to learn what a module is . Next is an example of a larger program that might tell us why and how modularization improves our codebase and workflow.
    - Westra next shows us how to implement a module involving a cache. He gives us the definition of the module-level global variable we first saw, along with some public and private module functions. Overall this first chapter doesn't teach us anything specific, and I recommend skimming it just to get an idea of his approach.
- Chapter 2: Writing your first Modular Program
    - This chapter involves an inventory control system with modules for a report generator, data storage, and a user interface. The code covers a number of details that help us understand the size and scope of a program that begins to benefit from a modular approach.
    - Though seeing a big program is useful, the program again goes into many technical details that aren't relevant to the modular programming concept - Westra acknowledges this and clearly says "don't worry too much about the details of these functions"
    - In the implementation of the main program we see how to import the modules we created - this is the important point. This too is a chapter we can skim.
- Chapter 3: Using Modules and Packages
    - Here we begin to actually learn how to create and use a directory (called a package) of Python module files.
    - From the outset Westra discusses packages within packages - this is a potentially confusing concept that he illustrates well, early, and consistently so that we can understand the principles clearly.
    - He diagrams directory trees and how these relate to packages which makes these clear. He next discusses initialization of modules - giving specific code examples, presented well and clearly.
    - After that, Westra goes into what the import statement does - likewise, specific, succinct and thorough.
    - Relative imports are likewise complex and so a major source of confusion. But again Westra diagrams the situation helpfully and clearly. He gives straightforward diagrams, and then writes the exact code that executes the depicted relative import. This method lets us quickly understand how the relative import system works.

[https://unique-creator-5551.ck.page/af9941ff97/index.js](https://unique-creator-5551.ck.page/af9941ff97/index.js)
