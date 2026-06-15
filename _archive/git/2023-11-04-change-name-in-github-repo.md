---
title: "change Author name &amp; email across all commits in github repo"
categories: 
  - "git"
---

To change the Author Name etc on all commits in a github repo, an easy way is

git rebase -r --root --exec "git commit --amend --no-edit --reset-author"  
git push -f

Can read more at https://stackoverflow.com/a/1320317
