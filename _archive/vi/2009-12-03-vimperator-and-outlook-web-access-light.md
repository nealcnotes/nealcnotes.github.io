---
title: "vimperator and Outlook Web Access Light"
categories: 
  - "vim"
tags: 
  - "microsoft"
---

So one feature of vimperator which has made it indispensable to me is Ctrl-I on a web form textbox. When vimperator receives Ctrl-I, it opens a gvim instance on the textbox, you can edit in gvim, and then vimperator puts your result back into the textbox. Amazingly useful; it's let me write better emails than I did when I was just typing into a textbox and trying to send off the email without any editing ability. Some websites use Flash or some other kind of textboxes though (such as Google Docs), but now I deal with them manually by opening gvim myself and pasting a tmpfile because I'm so used to the advantage of having gvim on textboxes.

Another nuisance has been editing emails using Outlook Web Access. Since I use Firefox, it forces me into Outlook Web Access Light, which is one nuisance (I bet if I just change the browser ID using a Firefox plug-in then I could get the full Outlook Web Access). But the main nuisance is that once I'm in OWA Light, then when I'm composing an email using Ctrl-I, then OWA Light likes to timeout after about 3 minutes and the textbox disappears, and so when I'm done composing another lovely epistle in gvim, then my writings disappear when vimperator doesn't find the textbox that OWA Light helpfully closed. I needed a way for gvim to save a duplicate copy whenever I'm using OWA, and gvim being the incredible machine that it is, there's a 1-liner in .vimrc that does the trick:

`   autocmd VimLeave  vimperator-exchange* :write! >> /home/me/vimp.exch.txt   `

That's it. Whenever gvim is about to leave a file beginning with vimperator-exchange\*, then it writes an extra copy to vimp.exch.txt so if OWA Light closed the box, I still have it.

There might be a more elegant way to do this; for a while I was trying to get a unique script id using but it wasn't worth it. I like this solution now anyway.
