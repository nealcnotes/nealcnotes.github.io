---
title: "irssi, skype, pulseaudio, and wacom on vista"
date: "2010-03-20"
category:
  - "linux"
---

did a few things today. found irssi again, for some reason it wasn't in aptitude for a while. now it is. great, i can ask questions on irc.debian.org again. by the way i tried logging into that and irssi was failing ,and i found it was about clearing the hostname. googleable whatever it was.

then i was having a problem since skype wasn't working with pulseaudio which somehow installed itself. i was worried that maybe squeeze had standardized on pulseaudio. asked (using irssi) and got the helpful advice to aptitude purge pulseaudio. with a little hesitation i did it, it had a bunch of dependencies all with "pulse" in their names so i purged all of them. and then ALSA and skype were back, and i was glad. i need skype a lot more than i need pulseaudio.

finally got to the vista laptop and the wacom bamboo was not moving the cursor. did another 15min of goofing and found that you can remove the "preference" file which resets the driver. (i dl'd and reinstalled the driver and it didn't help.) and now the wacom is working. whew.
