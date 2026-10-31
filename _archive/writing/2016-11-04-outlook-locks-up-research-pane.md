---
title: "Outlook locks up, \"Research Pane\""
category: writing
tag: microsoft
---

Once every couple of weeks, my Outlook 2010 freezes up.  Whatever I click, I get "Research Pane," and nothing I type shows up.  I wondered if it was a keyboard issue, but other MS applications worked.  So after some Googling I found a solution.  Need to open VB (Alt-F11) and then the immediate window (Ctrl-G), and then type:

\[code\]

Application.Explorers(1).CommandBars("Research").Enabled = false

\[/code\]

Originally found this as one of the results here:

[http://superuser.com/questions/56265/stop-the-research-pane-appearing-in-microsoft-office](http://superuser.com/questions/56265/stop-the-research-pane-appearing-in-microsoft-office)
