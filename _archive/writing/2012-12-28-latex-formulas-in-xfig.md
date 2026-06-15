---
title: "LaTeX formulas in xfig"
category: writing
tags: 
  - "latex"
---

To add LaTeX formulas to xfig

1. add a text element, and enter LaTeX including $$
2. edit the text element properties, and mark it special
3. export as PDF/Latex
4. in the LaTeX file, include the figure using \\resizebox{\\textwidth}{!}{ \\input{thefilename.pdf\_t} }
