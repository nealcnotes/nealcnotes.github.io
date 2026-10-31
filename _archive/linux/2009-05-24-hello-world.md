---
title: daylight savings time on dualboot debian
category: [linux]
---

been having some trouble with time on a dualboot debian laptop. i tried

dpkg-reconfigure tzdata then edit /etc/rcS and set UTC=yes

but it didn't work. the answer was just to do

date --set=whatevertime

i also found my previous notes on this problem, which were

> so the machine was refusing to change the time using hwclock --systohw then i tried hwclock --systohw --directisa
> 
> and it succeded, dont know if it will survive a reboot though.
> 
> then i tried hwclock --systohw --directisa --localtime and it survived!!!! i dont know. also i added a parameter to the rcS init file for --directisa

but i don't remember anything about directisa or rcS init or why i would do that.
