---
title: "How the python logger works in a few simple examples"
categories: 
  - "python"
---

this had also been a mystery to me. the python docs on the logger were pretty unintelligible, and i've used print statements for years, and i could see that the python logger seemed to be doing something, its just i couldn't figure out what. so now the mystery is partially resolved. i think some examples might be the best way to learn about it. they added examples to the latest python docs which helped me alot, but i think some more might be useful.

the python logger is pretty intense, it's designed to scale up to a project with multiple packages and modules. there's a lot going on. to begin with, lets focus on a case with a single module

```

import logging
if __name__ = '__main__':  
    logging.basicConfig()
    mylogger = logging.getLogger('myfirstlogger')
    mylogger.debug('hello world')
```

this should setup a simple logger which does the equivalent of print. since mylogger is defined in the global scope, you can use it where you'd use a print statement. but it doesn't give you any advantage over print. the first new thing you can do with logging is set the level. there's predefined levels logging.DEBUG==10, logging.INFO=20, logging.WARNING=30, logging.ERROR=40, and logging.CRITICALERROR=50. you can generate a log entry at any of these levels with mylogger.info('whatever') or mylogger.criticalerror('whatever'). however i use print statements mostly for debugging, so i am focused on logging.DEBUG and logging.INFO only. in fact, there's inner loops which i sometimes want to debug but not always, and so i need levels lower than 10 for example. that's easy, you can use mylogger(1, 'whatever') to have a level 1 message. and what would you do with a level 1 message? you can set the minimum level of the logger using setLevel:

```

import logging
if __name__ == '__main__':  
    logging.basicConfig()
    mylogger = logging.getLogger('myfirstlogger')
    mylogger.debug('hello world')
    mylogger.setLevel(5)
    mylogger.log(6, 'this will be printed')
    for i in range(10): mylogger.log(4, 'these will not since their level is too low')
    mylogger.setLevel(3)
    for i in range(10): mylogger.log(4,'but these will since we lowered the level')
```

pretty straightforward. however there's one more feature of the logging system which makes it truly useful, which is that loggers form a hierarchy based on their names. notice the line mylogger=logging.getLogger('myfirstlogger'). this defines a top-level logger. we can create child loggers using mychildlogger = logging.getLogger('myfirstlogger.child') for example. the level of the child logger, if unset, is inherited from the parent. but it can be set independently also.

each function in your module can have its own child logger, so you can turn on and off logging within each function, or have them relay the log messages up to the parent whenever you like.

```

import logging
def dothis():
    dothislogger = logging.getLogger('myfirstlogger.dothis')
    dothislogger.debug('wont be printed since we\'re inheriting the level from myfirstlogger')
    dothislogger.setLevel(logging.DEBUG)
    dothislogger.debug('will be printed')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    myfirstlogger = logging.getLogger('myfirstlogger')
    myfirstlogger.debug('wont be printed since the level is INFO')
    dothis()
```

so you can set whatever levels you need in all your child loggers, and they will relay relevant messages up to the parent loggers.

what i've covered so far gives us a lot of functionality over print statements -- but there's quite a lot more to explore in the logging system. it's a full-industrial-strength system with quite a bit more features, some of which i don't think i'll ever need, but others which may come in handy.
