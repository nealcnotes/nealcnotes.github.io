---
layout: post
author: Neal C
title: Author name wrong in Git repo?
category: [git]
tags: [rebase, rename]
---

The Author name is wrong, or we need to change it, fast.
To fix the Author Name etc on all commits in a github repo, an easy way is

{% highlight bash linenos %}
git rebase -r --root --exec "git commit --amend --no-edit --reset-author"
git push -f
{% endhighlight %}

Read all the details on Stackoverflow [here](https://stackoverflow.com/a/1320317)
