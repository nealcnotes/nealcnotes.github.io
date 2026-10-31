---
title: "wicd-client --no-tray for ion3"
category: linux
tags: [wireless]
---

i use ion3 as my window manager, and it doesn't have a tray, and wicd-client assumes you have a tray... couldn't get wireless working until i saw a post somewhere where someone mentioned you could do

wicd-client -n or wicd-client --no-tray

which is exactly what i needed. somehow for gui-based apps i don't rtfm, probably because generally tfm has nothing useful, but this time i see the manpage is great.
