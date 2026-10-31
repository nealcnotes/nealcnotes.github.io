---
title: "wwhhhaattt vim 4 panel git merge???"
categories: 
  - "old-comics"
tags: 
  - "vim"
---


![Animals on vim's 4 panel merge screen](/assets/images/vim-mergetool.png)

*An early try at programming-with-cartoons, in the spirit of [\_why's Poignant Guide](https://poignant.guide/). Current work is at [home](/).*

You don't understand 4 panel vim merge - and git merge itself is complex - someone else's changes, and git in a strange state. (None of which the boss is interested in.) 

Luckily you can delay gratification: for example, you profit by learning basic vim editing commands, so you actually have the most powerful tool at your fingertips.  Don't take the cookie, invest about 5 more minutes - yes it looks complicated at first, but hold on, it's actually simple and fast, and you'll get 2 more cookies.

The bash commands you need:

git config merge.tool vimdiff
git config merge.conflictstyle diff3
git config mergetool.prompt false
git mergetool


You can work through this excellent example if you want to learn more details: [https://www.rosipov.com/blog/use-vimdiff-as-git-mergetool/](https://www.rosipov.com/blog/use-vimdiff-as-git-mergetool/)
