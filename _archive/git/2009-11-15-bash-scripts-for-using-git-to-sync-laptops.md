---
title: "bash scripts for using git to sync laptops"
categories: 
  - "git"
tags: 
  - "bash"
---

I have 3 Debian laptops which I use daily. One at home, one at school, and one which I carry in my backpack. I'm also a backup nut. I have 4 external drives totaling 3.25T of storage which are for storing and backing each other up. For years I used rsync with linked files, which was alright but always had issues -- sometimes the links wouldn't propagate back properly for no apparent reason. I'd have the impression that things were working well when ... really there was just the latest snapshot available.

Recently I've switched to unison for backing up things like photos and videos, which works great and has a nice GUI. It makes snapshots and just synchronizes the drives, with minimal muss and fuss.

But for my daily work, I want something with some history, like I had hoped to get from rsync, so I can revert a file to its previous state. I wanted something which wouldn't have a 'main' copy and then child copies but rather where each laptop could function stand-alone and then quickly synchronize with the others whenever they were available. I wanted something which could run over ssh. I suspected git might do some of it, but I am surprised now how much of what I wanted, git does, and does well.

So I tried out git for while, but git has a steep learning curve. So steep that its the kind of thing which I abandon if I don't get traction quickly, since I have little time to learn technical tools like this, especially tools which are not documented for beginners. (I've had that issue with OpenBSD, which seems like a nice OS, and which I've installed, but I've run into issues within the first day and then had to reformat over with Debian testing.)

However git has something which is an absolutely remarkable solution to this problem. There is an excellent, friendly git IRC channel at irc.freenode.net/#git. Several people there have given me such valuable advice specific to my situations that came up in the beginning that I've learned git to the point where it's a tool that helps me so much I can't do without it. There's lots of primers and introductions out there, but I didn't find one that really cut it for me; it is sorely needed, but the IRC channel makes up for its absence.

One key piece of advice I got was to avoid git push and pull in the beginning, and rather use git fetch and merge only. This was good advice, since you get a better sense of what each piece is doing, and it works.

So I wrote a couple of bash scripts which I use everyday and which I like. First I have in my .bashrc a line like

`   export GITDIRS=~/proj1:~/proj2:~/proj3   `

Whenever I need to sync up laptops I run the following bash script I call gitac (for git-add commit):

`#!/bin/bash  IFS=:  for gitdir in $GITDIRS; do      echo $gitdir      pushd $gitdir      git add .       git commit      popd  done`

and then I ssh to the target laptop and run gitfr (for gitfrom):

`#!/bin/bash  IFS=:   for gitdir in $GITDIRS; do     echo $gitdir      pushd $gitdir      git fetch $1:$gitdir HEAD      git merge FETCH_HEAD      popd  done`

These work superfast and sync my laptops better than I could've asked for from rsync. I can see the commits graphically using gitk which is nice.

When I'm syncing my laptops it isn't always a sensible time to do a significant commit on all my projects, but with git you can have several branches, one for daily working commits and another for significant commits -- I've yet to completely work that out and also find out how to propagate such branch information. git is flexible about how you use it, and if it works, then it works. Another thing I like is that none of the machines is "central"; in fact, I view them all as backing each other up. In particular, I don't need the external drives for backing up my daily work anymore, they're only for photos, videos, and things like that.

The only obvious issue is if I edit the same file on 2 different laptops and then sync, then I get merge conflicts, as would be expected. At first this was a problem, but now I generally remember to start a work session by gitfr from my backpack laptop to keep everything sync'd up.
