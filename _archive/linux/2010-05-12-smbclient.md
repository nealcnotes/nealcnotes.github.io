---
title: "smbclient"
date: "2010-05-12"
categories: 
  - "linux"
---

I run on a Debian machine, and I'm in a Windows environment. So from time to time I have to map some share on a machine and upload or download some file. Every time I panic because I don't remember how to do this smbclient stuff, so I'm just going to post it here. First, I have a file called authfile, which has in it 3 lines: \[sourcecode\] username = myusername password = mypassword domain = thedomain \[/sourcecode\]

Then say we have a server MX20 and a "share" called "Shared", then all I have to do is

\[sourcecode lang="bash"\] smbclient //MX20/Shared -A authfile \[/sourcecode\]

This logs me in, and then I can drill down to whatever folder they want and get and put the required files.
