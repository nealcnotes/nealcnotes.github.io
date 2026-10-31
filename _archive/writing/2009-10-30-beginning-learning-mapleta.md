---
title: Beginning learning MapleTA
category: writing
---

MapleTA has been something I've been meaning to learn for some time now. I use MapleTA that others have written in my classes, but I want to learn it so I can write my own questions. But it's been problematic since I've never seen any language reference or user guide or anything, so I looked briefly at questionbank source code of others but couldn't find the motivation to really figure it out. Finally the other day I found a user guide. I read it yesterday on the train, and found some examples which I'm typing in and running. That's good, but I must say the user guide could really use a bit of work by a professional technical writer. It's usable, but it could be a lot better, and that would really open up MapleTA to a lot of people. They made it very GUI-based, but it's not at all stand-alone, you do need to read the user guide. I also don't know Maple itself, so I have to learn that. (I know Mathematica, I wonder if there's a MathematicaTA, but in any case we've adopted MapleTA.) I found that I really only need to start in Chapter 7.

A few glitches in the user guide:

- in chapter 7, the Color example doesn't work. Furthermore, it asks you to click on 'insert/edit response area', but this button is unlabeled, you have to hover over all the buttons in the Add Question window and find the tooltip.
- The Maple source code for the random set example is hyphenated at line breaks, so I typed in pos-int when the proper Maple function is posint. This also happened in the determinant example, but it was more obvious what to do there.
- Chapter 8 has a random plane question and takes us through the Show Designer dialog, but in Chapter 7 we've already defined random variables (and polynomials and matrices) directly in the algorithm section, so Show Designer is a step backwards.
- chapter 8 perimeter has an unexplained evalf in the maple-graded response for the grading code. how come other times we don't need evalf and this time we do?
- chapter 8 gradient field question uses some maple libraries, so i guess they assume you know maple fairly well before you try mapleta. might be good to have a little more explanation for people new to maple itself; for me id never probably take the time to learn maple unless it was to write up new material in mapleta, since ive already invested the time in mathematica.
- the string match question section 8.8 has you enter the plotmaple command from the previous example into the algorithm box but doesnt use it since its got nothing to do with the example.
- the sketch example in the latex section doesnt seem to work, though it seems like it would be really useful if it did work. when i converted and uploaded there was no graphing area.

I also discovered that

- an "algorithmic variable" is a very general thing. It can contain code, images, plots, and lambda functions. Seems to be mostly for keeping Maple-rendered MathML of expressions.
- And that Maple-graded question means only that it by default runs Maple on a string formed using the student's answer.
- There's a fairly clunky link between MapleTA and Maple, you have to put things in maple("whatever"), and only Maple can render MathML, so this leads to a large frequently recurring expression like maple("printf(MathML:-ExportPresentation($matrix))");
- there's a small note that we should wrap random variables in parentheses otherwise we get syntax errors if they're negative along the lines of 5+-2.
- its a little surprising that mapleta can do things like assume(x>=0, x<=1) and then have code based on that like the chapter 8 increasing function example. how does it check every point in the interval? or, in other places like chapter 7, that it can generate 2 random numbers and then have a condition afterwards that $b cannot equal $a. what does it do, backtrack if they're equal?
- mapleta doesn't save the questionbank that you're working on automatically if you logout! all the examples i entered upto now vanished when i logged out. that is a big problem.
- ive noticed even in the questions that im using from other people that maple's graphs are often slightly off. for example when we do the x^3-x plot question in chapter 8, it doesnt actually go through the origin. this causes a lot of confusion, how is it possible that a program at maple's level of usage and adoption makes this kind of plotting error in a simple 2d graph? shouldnt this have been a release-stopping bug in v1 of maple?
- i didn't really get why you would want to input the mapleta in latex, but i just ran it, and it actually looks good. its kind of \`\`pretty printed'' which is good. and the native qu format seems pretty ugly, every line needs to be started with the question bank number and some other number, and there's no vim style files. so i guess doing the latex is nice, i will do it that way as much as i can. though the variables all have to have this \\var{} notation which is clunky.

well that's it for today. not a bad run, and i did learn quite a bit about maple and mapleta.
