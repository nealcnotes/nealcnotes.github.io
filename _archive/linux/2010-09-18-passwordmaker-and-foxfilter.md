---
title: "PasswordMaker and FoxFilter"
date: "2010-09-18"
categories: 
  - "linux"
---

To make PWM not enter a password into the "Allow website" form from FoxFilter, you

- Add a new account to PWM.
- It needs to use chrome://foxfilter\* to calculate generated password
- Automatically populate should be unchecked
- I also have a (perhaps unnecessary) autopopulation pattern chrome://foxfilter\*,
- Under Advanced Autopopulate you need field TextPassword, type text, value blank

I hope I never have to figure that out again. Probably better to just use LeechBlock for what I was trying to do anyway.
