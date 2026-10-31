---
title: "wireless on debian toshiba satellite"
categories: 
  - "linux"
tags: wireless
---

1. lspci, look for wireless network
2. the drivers are proprietary, non-free so google for the driver and install.  in this case it was firmware-iwlwifi.
3. wireless-tools
4. wicd (networkmanager also may have been helpful at some time, but i think its best to have only 1 of them installed.)
5. reboot and check the hardware wireless switch is on.  (removed something called avahi-auto ipd because i wasnt getting connection and i thought it was interfering, turned out to be the wireless switch, doesn't seem to have messed anything up either way and i don't know what it  does.)
