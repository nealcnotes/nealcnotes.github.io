---
title: "Goroutines and channels - simple!"
date: "2023-11-11"
categories: 
  - "old-comics"
tags: 
  - "concurrency"
  - "syntax"
---


![Animals explaining goroutines and channels](/assets/images/goroutine.channel.png)

*An early try at programming-with-cartoons, in the spirit of [\_why's Poignant Guide](https://poignant.guide/). Current work is at [home](/).*

A few animals marked up an introduction to goroutines and channels from [https://go.dev/talks/2012/concurrency.slide#20](https://go.dev/talks/2012/concurrency.slide#20) ! You can copy paste the below into a file, say simple.go, and run it with go run simple.go  

{% highlight golang linenos %}
package main

import ("fmt"
    "math/rand"
    "time")

func main() {
    c := make(chan string)
    go boring("boring!", c)
    for i := 0; i < 5; i++ {
        fmt.Printf("You say: %q\\n", <-c) // Receive expression is just a value.
    }
    fmt.Println("You're boring; I'm leaving.")
}

func boring(msg string, c chan string) {
    for i := 0; ; i++ {
        c <- fmt.Sprintf("%s %d", msg, i) // Expression to be sent can be any suitable value.
        time.Sleep(time.Duration(rand.Intn(1e3)) \* time.Millisecond)
    }
}
{% endhighlight %}

Portions of this page are modifications based on work created and [shared by Google](https://developers.google.com/readme/policies) and used according to terms described in the [Creative Commons 4.0 Attribution License](https://creativecommons.org/licenses/by/4.0/).
