---
title: a simple cron file is better than cron-apt
category: [linux]
---

ive been trying to get cron-apt to download and install packages. i was able to get it to update and download, but never to install, and i dont want to know how to do it anymore. really all you need to do is put an executable file in /etc/cron.daily/cronaptitude with

#!/bin/bash aptitude update aptitude -y safe-upgrade

that's all i wanted, and its so much simpler than cron-apt. i know there's a \`\`safety'' issue with automatically upgrading, but ive stopped looked at specific packages years ago when i upgraded and havent had problems. sometimes X will break or the kernel will break, but this is not a problem. its easier to fix this when it happens once every couple of years than it is to not have cron upgrading automatically and then every week or 2 having a giant upgrade.

another thing which cropped up was that if i put that script in /etc/cron.daily then it works, but if i have root do crontab -e then it complains about paths. then in root's crontab you have to add the line

PATH=/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:$PATH
