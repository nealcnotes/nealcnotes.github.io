---
title: "latex -&gt; text"
categories: writing
tags: 
  - "bash"
  - "latex"
---

$ catdvi -e 1 -U file.dvi | sed -re "s/\\\[U\\+2022\\\]/\*/g" | sed -re "s/(\[^^\[:space:\]\])\\s+/\\1 /g" > file.txt

from

[this link](http://stackoverflow.com/questions/530121/how-do-i-convert-latex-to-plain-text-ascii "convert latex to text")

More details from the original poster:

The -e 1 option to catdvi tells it to output ASCII. If you use 0 instead of 1, it will output Unicode. Unicode will include all the special characters like bullets, emdashes, and Greek letters. It also include ligatures for some letter combinations like "fi" and "fl." You may not like that. So, use -e 1 instead. Use the -U option to tell it to print out the unicode value for unknown characters so that you can easily find and replace them.

The second part of the command finds the string \[U+2022\] which is used to designate bullet characters (•) and replaces them with an asterisk (\*).

The third part eats up all the extra whitespace catdvi threw in to make the text full-justified while preserving spaces at the start of lines (indentation).

After running these commands, you would be wise to search the .txt file for the string \[U+ to make sure no Unicode characters that can't be mapped to ASCII were left behind and fix them.
