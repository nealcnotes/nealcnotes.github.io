---
title: bash completion for vim and latex
categories: 
  - linux
tags: 
  - latex
  - vim
---

I want bash to complete .tex whenever I type vim file. and there's a file.tex in the directory. This was driving me nuts since it was completing all the LaTeX aux files etc whenever I did it, but I found (again) /etc/bash\_completion which has the line

complete -f -X '\*.@(o|so|so.!(conf)|a|rpm|gif|GIF|jp?(e)g|JP?(E)G|mp3|MP3|mp?(e)g|MPG|avi|AVI|asf|ASF|ogg|OGG|class|CLASS)' vi vim gvim rvim view rview rgvim rgview gview

which is obviously the line in question. all i did was add (aux|out|log to these filetypes and put that line in my bashrc and its working much better. frankly this was just lucky, since i dont think more than about 50-200 people in the world really understand bash completion very well.

there's an incredible programmer i came across who wrote something interesting called [compleat](http://limpet.net/mbrubeck/2009/10/30/compleat.html).

also i rediscovered FIGNORE, which is a list of file extensions for bash to ignore on all completions. just export it from your .bashrc.
