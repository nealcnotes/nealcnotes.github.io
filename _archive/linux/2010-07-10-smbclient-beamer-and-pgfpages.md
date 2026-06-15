---
title: "smbclient, beamer, and pgfpages"
categories: 
  - "writing"
tags: 
  - "latex"
---

Today's problem is that I need to print slides for a poster session that I'm going to. I've never printed to the color printer, so I don't know the share name. Simple:

\[sourcecode lang="bash"\] smbclient -L server.com \[/sourcecode\]

prints all the shares from that server, so then I can just grep the output since I have an idea how the admins name the printers (based on room number, floor, and printer model). I found the share name and made a little shell script that prints to the share. I also found that there's a number of commands one can send through smbclient to the server and share, such as:

\[sourcecode lang="bash"\] smbclient -d3 //server.com/printershare -A authfile -c "queue" \[/sourcecode\]

and even

\[sourcecode lang="bash"\] smbclient -d3 //server.com/printershare -A authfile -c "help queue" \[/sourcecode\]

for example. Then there's "cancel". However on my particular setup, I didn't see any print jobs listed when I gave the "queue" command even though I knew there was one queued up. Maybe it'd been sent to some 3rd intermediate machine, or maybe it was already in the printer's memory.

Next, I needed to get my beamer slides printed to the color printer. I printed them, and it turns out they're shrunk down for no reason (but they're color, so that's good). I need them normal size to paste onto the poster board. To do that, I found the beamer manual giving an example using pgfpages (which had a few typos and again used a4paper which is a nuisance since I'm in the USA). Had to investigate pgfpages.sty (since pgfpages has no documentation, surprise). The correct command to get pgfpages to print on my system this time was:

\[sourcecode lang="tex"\] \\usepackage{pgfpages} \\pgfpagesuselayout{resize to}\[letterpaper, landscape, shrink=5mm\] \[/sourcecode\]

For a while my problem was using curly rather than square brackets for the 3 parameters. Now the problem is that the color laserjet 2500L just prints pages of junk rather than the slides. In the process of dealing with that I found that I could "login" to the print share by doing

\[sourcecode lang="bash"\] smbclient -d3 //server.com/printershare -A authfile \[/sourcecode\]

and then issue commands like "cancel 1" and "cancel 100" directly. They all succeed, but I never get to actually see the queue.

Finally the other struggle with this morning and afternoon has been with the HP Color Laserjet 2500L itself. Downloading the manual is essential, since the printer has nothing but hieroglyphics on its panel. I don't know why people think that a red button with a triangle automatically means cancel print job. In any case, reading the manual is essential, since a button was flashing with some hieroglyphic next to it, and I discovered this meant paper jam, which gave me the impetus to actually pull out the toner cartridge (which I'd never done, I don't maintain this printer) and then find the paper and replace the cartridge. And somehow, now, my slides are actually printing in color.

I think one important thing is to do dvips to get the postscript output rather than making a PDF file and converting to PS using pdf2ps. The file seems alot smaller. It is very slowly printing right now, which suggests to me that one of the older jobs where I did pdf2ps is printing, instead of my latest jobs using dvips.
