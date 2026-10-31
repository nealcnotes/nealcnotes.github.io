---
title: "cryptsetup and quickfix"
categories: 
  - "linux"
tags:
  - "vim"
  - "bash"
---

2 unrelated things which I fixed up today. First, a few days ago my Fujitsu P7320, which I am very fond of, had its HD fail. So it's off being repaired, presumably returning with a fresh HD. I used it often to transfer files between my various machines using git - although git is a dvcs, i was also using it to sync machines, leading to lots of illogical commits, which I'm sure some purist would say is appalling, but it works and works fast, and so far I haven't had trouble. But now that the Fujitsu is out, I needed to use a thumbdrive. Last time I used one for syncing, i lost it for some time, then weeks later found when the snow in my driveway melted. (Amazingly, it still worked.) But while it was lost I was always worried about whether there were any important passwords cc's etc on the drive. I determined to never use an unencrypted thumbdrive again. So today I had to get it encrypted in a hurry, and I found the relevant commands and they were simple, so here they are: \[sourcecode lang="bash"\] cryptsetup luksFormat /dev/sdX cryptsetup luksOpen /dev/sdX thumbdrive # enter password mkfs.ext2 /dev/mapper/thumbdrive mount /dev/mapper/thumbdrive /media/thumbdrive # do whatever \[/sourcecode\]

Much easier than I was expecting.

The second thing I rediscovered was quickfix on vim with g++. I was doing some simple editing of a single C++ file, and I wanted quickfix working again but I forgot everything. Here's the lines from the .vimrc that make it go:

\[sourcecode lang="vim"\] set errorformat=%f:%l:\\ %m,In\\ file\\ included\\ from\\ %f:%l:,\\^I\\^Ifrom\\ %f:%l%m set makeprg=g++\\ -Wall\\ -pedantic\\ %\\ -lm\\ -lgsl\\ -lgslcblas\\ -o\\ %< \[/sourcecode\]

That's it. obviously later when using a makefile for real, I'll have to modify the makeprg and make it.. just make.. but this works quick and dirty.
