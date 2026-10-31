---
title: "Bye bye flash, hello gnash"
category: linux
tags: 
  - "firefox"
  - "multimedia"
---

This afternoon I was finding my computer really bogged down. I was averaging 1.5 loads or so. After a bit of poking, I found the culprit (again), xulrunner. Killed it, was thinking Firefox was junk. Tried out midori and epiphany, they're nice, but I can't survive without vimperator anymore. Sad but true.

Then I realized that it's probably less Firefox and more flash. Uninstalled flash and installed mozilla-plugin-gnash on Debian testing. Youtube was dead. Though I don't like to admit it, this is a big problem. Did some more poking, found some "greasemonkey" scripts that are supposed to fix the problem etc, installed that, no dice. Then I went on a chat room and someone pointed me to

[https://fedoraproject.org/wiki/Common\_F13\_bugs#gnash-youtube-broken](https://fedoraproject.org/wiki/Common_F13_bugs#gnash-youtube-broken)

Basically says to kill all your cookies and block www.youtube.com from putting in cookies since there's some kind of bug with that. Then I turned off greasemonkey by clicking on the icon, and the video was playing but no sound! So I finally uninstalled the greasemonkey scripts and greasemonkey itself, restarted, and voila!

So now when the fix the bug, then presumably it will get all screwed up again.
