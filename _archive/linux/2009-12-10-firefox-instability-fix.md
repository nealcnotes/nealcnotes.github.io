---
title: "Firefox Instability Fix"
category: linux
tags: 
  - "firefox"
---

I've been having fun with vimperator, but then my firefox on one of my (Debian) laptops became unstable. I'd rightclick on a field, and it would crash. I ran it from the commandline to see if there's any error messages, it would just say Segmentation fault. I didn't have time to get a tracer and see where it's crashing, and I did need to to work again quickly. I tried aptitude reinstall firefox, but that doesn't seem to do anything useful, since it reinstalls the same binary and it was still crashing; the problem wasn't in the binary or system-wide configuration (which I didn't touch). Then I had some intelligent instincts; I already guessed that the problem wasn't there, and so it had to be in my add-ons, like vimperator. But I didn't know which one. I've always tried to keep the number of addons that I use down; and the answer was simply

 `rm -rf ~/.mozilla` 

which blows all that add-on and everything else away. I keep my bookmarks on delicious, so that doesn't matter, and all my other addons are non-critical, so this didn't cost me anything except downloading some of them again if I felt like it. And it solved my problem.
