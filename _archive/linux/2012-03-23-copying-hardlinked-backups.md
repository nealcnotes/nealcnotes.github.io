---
title: "copying hardlinked backups"
category: linux
tag: bash
---

have 2 external drives, and i use backintime to backup my main hd to one of these drives.  now i want to copy the 1st external usb drive to the 2nd, but backintime uses hardlinks, and i need to preserve these.  rsync can do it, but evidently takes a long time, so easier to use

\[sourcecode lang="bash"\]

cp -avr

\[/sourcecode\]

sometimes the simplest solution is the best.
