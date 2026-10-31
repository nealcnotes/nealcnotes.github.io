---
title: "Wireless on Fujitsu Lifebook P7230 under Debian Squeeze"
category:
  - "linux"
tags: 
  - "wireless"
---

Finally got wireless working on the Fujitsu Lifebook P 7230 under Debian squeeze (testing).

- First, for a long time, I'd get errors regarding missing firmware and ucode missing errors in dmesg.
    
    \[ 75.707413\] iwl3945 0000:03:00.0: iwlwifi-3945-1.ucode firmware file req failed: -2 
    \[ 75.707522\] iwl3945 0000:03:00.0: Could not read microcode: -2
    
    business\_kid on linuxquestions.net suggested finding a firmware package, and I found it was the missing package firmware-iwlwifi. After this I still didn't see the wireless networks on wicd, pixellany next suggested trying iwconfig wlan0 up; iwlist wlan0 scan. This was the first I'd seen of wlan0, I'd always used eth1 before. After running these commands I saw an ESSID of a network that the other computers here were using, so I knew the card was working and wicd wasn't.
- I found a box under wicd's Preferences for wireless interface and entered wlan0, and then wicd saw the network.
- I now needed the WEP key -- no Internet yet , and I tried looking in the Windows network configuration screens on the windows computers here, but it was greyed or blocked out. Then I tried the DSL wireless router at 192.168.0.1 since that's what it said in the manual, didn't work. After a while I found it at 192.168.1.1, and got the WEP key. It went in the Hex key, not the WEP passphrase.
- But still no Internet, I powercycled the router and then all the computers lost the Internet. Turns out you have to powercycle the router and plug and unplug the DSL filter at the phone jack.
- Also I had to comment out the various scripts I had in /etc/network/interfaces other than lo for eth0

I used to enjoy this kind of thing, but now I don't really enjoy tinkering with Linux anymore. I think it's because Linux used to be new and interesting and different, but now I use it for real stuff and I need it to work without me tinkering with it. And years of tinkering has gotten old. It's just not that much fun anymore, it's something that I don't look forward to with Linux. But I still can't live without Linux's interfaces (ion and wmii window managers), flexibility, stability, and all that other stuff. I'd probably spend as much time fighting Windows as I do Linux, just in different ways.
