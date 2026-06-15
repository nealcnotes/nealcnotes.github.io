---
title: "screensaver"
categories: 
  - "linux"
---

found a nice screen blurring command that relies on ImageMagick

`#!/bin/sh -e`

\# Take a screenshot #scrot /tmp/screen\_locked.png import -window root /tmp/screen\_locked.png

\# Pixellate it 10x mogrify -scale 10% -scale 1000% /tmp/screen\_locked.png

\# Lock screen displaying this image. i3lock -i /tmp/screen\_locked.png

\# Turn the screen off after a delay. sleep 60; pgrep i3lock && xset dpms force off

then we need xautolock, but there is no xautolock. so instead we try https://github.com/fgsch/xidle

which locks only from the command line, not from the .i3/config.  so we compile xautolock from source fromhttps://github.com/l0b0/xautolock

finally we need to add a line to an x startup script like .xsessionrc or .i3/config to add the line

`exec xautolock -time 1 -locker '~/.local/bin/fuzzy_lock.sh' &`
