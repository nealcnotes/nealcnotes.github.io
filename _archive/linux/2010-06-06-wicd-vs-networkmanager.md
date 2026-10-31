---
title: "wicd vs NetworkManager"
category: linux
tags: 
  - "wireless"
---

spent the better part of an hour wrestling with wicd to try to get it to connect to my linksys WPA2. but it kept saying "incorrect password" even though i could see both passwords and i could see they were the same. tried password versus preshared key, no luck. pulling my hair out, then i had the thought to try nm-applet. it saw the networks, and then it said it connected, though i couldn't ping google -- immediately did a aptitude purge wicd and rebooted, ran nm-applet and voila, here i am posting over WPA2. something is wrong with wicd.
