---
title: "Useful git aliases"
category: git
---

Here's some useful git configurations and aliases.  The way you make a git alias is as follows:

```
$
```

You can use git config to also set various items such as the diff.tool, which uses gvimdiff whenever you use git difftool.  This makes the diffs much more visually understandable since you can scroll and see more context.

color.ui=auto
diff.tool=gvimdiff
alias.loga=log --oneline -15 --graph --decorate --all
alias.rev=remote -v
alias.lst=ls-tree --abbrev -l HEAD
core.pager=less -r
