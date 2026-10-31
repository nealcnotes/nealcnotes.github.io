---
title: "delicious and vimperator"
tags: 
  - "firefox"
  - "vim"
---

I've been trying to figure out how to use delicious with vimperator. I installed the delicious vimperator plugin and now I have the :delicious command, which doesn't seem to do anything as far as I can tell. I asked a couple of times on the freenode/#vimperator channel, which is very nice, but nobody seemed to know.

However I recently rediscovered :set guioptions+=mTB, which shows that, indeed, the regular Firefox is back there. And then it occured to me how to do it. CTRL-v is the pass-through to Firefox, and so CTRL-v CTRL-d opens the delicious bookmark page, and CTRL-v CTRL-b opens the delicious sidebar (if you have the regular delicious plug-in). This occured to me because, though I liked y for yanking the current address, I had to lookup CTRL-v CTRL-v to paste it since p doesn't work. So:

<table border="1"><tbody><tr><td>Firefox Passthrough</td><td>CTRL-v</td></tr><tr><td>Paste from Clipboard</td><td>CTRL-v CTRL-v</td></tr><tr><td>Toggle Delicious Sidebar</td><td>CTRL-v CTRL-b</td></tr><tr><td>Add Bookmark to Delicious</td><td>CTRL-v CTRL-d</td></tr></tbody></table>
