---
title: Get rid of black lines and grey backgrounds under LaTeX2html formulas
category: writing
---

This was a problem for some time. Whenever I had an inline formula $x^2$ for example, there'd be an ugly, distracting line under it in LaTeX2html. Found the fix today, [at this Wiki site at Drexel.](http://www.physics.drexel.edu/liki/index.php/Latex2html#Black_underlines_with_inline_equations) Copying out the relevant portion for future use:

> for those of us with root access, the following is a global hack-fix (i.e. it will fix the problem for all users):
> 
> In your file /usr/share/latex2html/l2hconf.pm replaced the line
> 
> $DVIPSOPT = ' -Ppdf -E';
> 
> with
> 
> $DVIPSOPT = ' -E';
> 
> The " -Ppdf" option supposedly does some extra formatting steps to optimize the output for pdf printing, but it ends up confusing latex2html in missing an entire row of pixels. It is non-essential and removing this option eliminates the problem. There are better fixes, see for details, that are more involved; but for those of us who regularly update our systems, or at least update latex2html whenever our distro has an update available, this hack-fix works just fine in the hopes that our distro will pick up and fix this bug on the next update of latex2html (in which case the more detailed fixes will have been over-written anyway).

My problem with grey backgrounds is also solved at this Drexel site by adding these lines to my ~/.latex2html-init:

> \# Force white background and black text $BODYTEXT = "text=\\"\\#000000\\" bgcolor=\\"\\#FFFFFF\\""; # This ensures that some figures do not end up with a grey background $WHITE\_BACKGROUND = 1; # Tell LATEX: $LATEX\_COLOR = "\\\\pagecolor{white}";
