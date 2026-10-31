---
title: "Select is switch/case for concurrency!"
date: "2023-11-20"
categories: 
  - "old-comics"
tags: 
  - "concurrency"
---


![Animals explain the select concurrency statement](/assets/images/select.anim.png)

*An early try at programming-with-cartoons, in the spirit of [\_why's Poignant Guide](https://poignant.guide/). Current work is at [home](/).*

<details class="comic-transcript inline-block">
  <summary class="button m1-4 md:p-4 md:text-center font-bold cursor-pointer">read the transcript!</summary>


<h3>bubble 1: guy asks bird</h3>

What is select?

<h3>bubble 2: bird explains</h3>

    It's a control structure for concurrency.  And Rob Pike, one of Golang's developers, says 
    it's the reason channels and goroutines are built-in to the language.

<h3>bubble 3: guy asks "how does it work?"</h3>

  Bird answers "It waits until 1 channel is ready.  Kind of like case, and then runs the code in
  the corresponding branch."   

<h3>bubble 4: bird explains lines in Rob Pike's example</h3>

{% highlight golang linenos %}
select {
    case v1 := <-c1:
        fmt.Printf("received %v from c1\n", v1)
    case v2 := <-c2: // bird says here it is fanning in from c1 and c2 to stdout
        fmt.Printf("received %v from c2\n", v1) 
    case c3 <- 23:
        fmt.Printf("sent %v to c3\n", 23)
    default: // giraffe says you can give a default if no channel is ready
        fmt.Printf("no one was ready to communicate\n")
    }
{% endhighlight %}

Finally a cow explains if more than 1 channel is ready, then select picks on branch pseudorandomly.
            </details>




