---
title: "How to keep less from clearing the screen"
categories: 
  - "linux"
tags: 
  - "bash"
---

I was finally getting desperate with R's history() command clearing my screen after showing me my history, totally useless. After some puttering around, i found that history() just ends up calling $PAGER, which for me was less. Typing h into history() confirmed that I was looking at less. So then googling how to get rid of less's behaviour turned up this page:

http://www.shallowsky.com/linux/noaltscreen.html

which gave the magic key as

export LESS="-X"

in .bashrc. this prevents less from opening an "alternate" screen when it runs. helps with manpages also. i don't know who or why anyone came up with this alternate screen nonsense.
