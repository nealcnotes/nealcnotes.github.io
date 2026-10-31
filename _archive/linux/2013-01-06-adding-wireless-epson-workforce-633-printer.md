---
title: "adding wireless epson workforce 633 printer"
categories: 
  - "linux"
tags: 
  - "wireless"
---

1. add yourself to the lpadmin group using `sudo usermod -a -G lpadmin tom /etc/init.d/cups restart`
2. printer should see router so connect them and get the confirmation printout which has the IP
3. go to http://localhost:631/
4. add printer, give 1 word for printer name. URL will be socket://IP from printout. cups already has the driver, add Epson Workforce 630
5. lp -d printername whatever.pdf
6. [debian wiki on printing](http://wiki.debian.org/SystemPrinting "debian wiki on printing")
7. [cups printing documentation](http://www.cups.org/documentation.php/options.html "cups documentation")
