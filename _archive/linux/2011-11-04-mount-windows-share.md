---
title: "mount windows share"
category: linux
---

This worked on Debian to mount a windows share.

\[sourcecode lang="bash"\] sudo aptitude install smbfs sudo mount -t smbfs -o username=faltu,uid=1000,gid=1000 //mx2/shared /media/mxsh2

\[/sourcecode\]
