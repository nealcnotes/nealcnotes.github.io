---
title: "Don't do anything when closing lid"
categories: 
  - "linux"
---

I have a 17" desktop-replacement type laptop which I'd like to be able to close from time to time and use the lid as a writing surface. But when I close the lid, I don't want any kind of suspend etc since I have a separate monitor and keyboard so I can still use the machine while the lid is closed. So far what worked was to edit /etc/acpi/lid.sh and put in "exit 0" at the top, which prevents acpi from doing anything at all when a lid event occurs. I can see the lid events in /etc/acpi/events/lidbtn seem to just execute /etc/acpi/lid.sh so i think this might continue to work for a while.
