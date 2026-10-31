---
title: "sudoers nopasswd"
categories: 
  - "linux"
---

how do you get it to stop asking for the password for me on my single-user laptop? the sudoers manpage was written by someone who was very fascinated by grammar and not by clear explanation. but this seems to be working:

%sudo ALL = NOPASSWD : ALL

for now...
