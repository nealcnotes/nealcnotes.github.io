---
title: "debian-multimedia GPG error"
categories: 
  - "linux"
tags:
  - "bash"
---

well I'll see if this fixes the error that's been breaking my nightly cron-apt.

\[sourcecode lang="bash"\] sudo su gpg --keyserver hkp://pgpkeys.mit.edu --recv-keys 07DC563D1F41B907 gpg --armor --export 07DC563D1F41B907 | apt-key add - \[/sourcecode\]

it doesn't work. now just tried:

\[sourcecode lang="bash"\] sudo aptitude install debian-multimedia-keyring \[/sourcecode\]

if that works its definitely superior.
