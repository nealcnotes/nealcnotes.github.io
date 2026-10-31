---
title: "Skype 2.1.0.81 on Debian Squeeze/sid"
categories: 
  - "linux"
---

Finally got it working. It worked a long time ago under 1.0.0.something, then debian updated and it broke for years. I don't have time to work it out, then a few days ago I lost my cellphone and so I needed to figure it out. A few google searches and I found a thread on skype where people had the identical problems to mine. Eventually many of them fixed it by mucking with the Options/Sound Preferences and choosing cards. [Here's the thread.](http://forum.skype.com/index.php?showtopic=101629)

So I tried a bit, then I unplugged the headphones from the USB hub and plugged directly into the side USB port on the Dell 9300. Still no good. Then I went into alsamixer and found the sound card under USB audio, and raised all the levels including Auto Gain Control and raised all the capture settings under that panel, and it worked! Hopefully it will keep working for a while. I didn't remember that Skype charges 2.1c to phone landlines, which I didn't really like, but I guess it's not bad. I don't yak much on the cell anyway, probably around 100-200 min max per month, so hopefully the cost won't be too much.
