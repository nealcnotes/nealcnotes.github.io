---
title: "ALSA and Flash"
date: "2010-07-03"
category: linux
tags: 
  - "multimedia"
---

I've long wanted to do this, and I don't know how it was so simple all along. I have 2 external USB DACs, which go to 2 amps for 2 rooms. there's also the multichannel audio on the Dell 9300 itself, and for a while I was trying to get Skype working (I've given up, though it would be nice to run off of Linux it just doesn't work reliably enough so I've gotten the Belkin Desktop Internet Phone which is working out rather nicely for now.

So I've had to learn how to identify and select the various audio devices that pop in and out over time, along with the random cruft that keeps changing things every few weeks. The biggest problem in all of it was getting Flash, and Youtube, to work. It just selects the default ALSA device. I had seen the ALSA wiki a few times, but somehow I just never saw that one part where they tell you how to redirect the default ALSA sound device.

All you do is run aplay -L, and find the device you want for default. it will look like:

iec958:CARD=PCM2702,DEV=0 Burr-Brown Japan PCM2702, USB Audio IEC958 (S/PDIF) Digital Audio Output default:CARD=default USB Audio CODEC , USB Audio Default Audio Device

so the Burr-Brown, by the way, is a FUBAR II DAC which is nice.. and the USB Audio CODEC is the other DAC I have. I don't know why the label is "default", but to get it to be the default ALSA device, all i did was make an .asoundrc file with the single line:

pcm.!default front:default

(default would be PCM2702 to get the other one probably) and that's it. Flash is running through the DAC into the amp and out the speakers in my room. Because the device name is "default" I'm pretty sure I'll have to muck with the .asoundrc file when I reboot, since I don't think that's its permanent designation, but atleast it's playing through the speakers I want it to play through.
