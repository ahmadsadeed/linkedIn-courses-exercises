#!/usr/bin/env python3
""" Deciding how many bags of chips to buy for the party """

import threading

# data race and race conditions are not same issues!!!

bags_of_chips = 1  # start with one on the list
pencil = threading.Lock()


def cpu_work(work_units):
    x = 0
    for work in range(work_units * 1_000_000):
        x += 1


def barron_shopper():
    global bags_of_chips
    cpu_work(1)  # do a bit of work first
    with pencil:
        bags_of_chips *= 2
        print('Barron DOUBLED the bags of chips.')


def olivia_shopper():
    global bags_of_chips
    cpu_work(1)  # do a bit of work first
    with pencil:
        bags_of_chips += 3
        print('Olivia ADDED 3 bags of chips.')


if __name__ == '__main__':
    shoppers = []
    for s in range(5):
        shoppers.append(threading.Thread(target=barron_shopper))
        shoppers.append(threading.Thread(target=olivia_shopper))
    for s in shoppers:
        s.start()
    for s in shoppers:
        s.join()
    print('We need to buy', bags_of_chips, 'bags of chips.')

'''- Data races and race conditions are two different potential problems in concurrent programs that people often 
confuse with each other probably because they have similar sounding names with the word race in them. Data races can 
occur when two or more threads concurrently access the same memory location. If at least on of those threads is 
writing to, or changing that memory value, that can cause the threads to overwrite each other or read wrong values. - 
That's a pretty straightforward definition, which makes it possible to create automated tools to identify potential 
data races in code. And to prevent those data races, you need to ensure mutual exclusion for the shared resource. A 
race condition, on the other hand, is a flaw in the timing or ordering of a program's execution that causes incorrect 
behavior. In practice, many race conditions are caused by data races, and many data races lead to race conditions. 
But those two problems are not dependent on each other. - It's possible to have data races without a race condition 
and race conditions without a data race. Olivia and I invited Steve and gang over to play video games next weekend, 
so we need to figure out how many bags of chips we need to buy to keep them all fed. Our shopping list is shared 
resource, and this pencil serves as a mutex to protect it. Only the person or thread with the pencil can view or 
modify the shopping list. - I'll go first. I see that our shopping list already has one bag of chips. With the Steve 
and gang coming over, I think we need three more. So, one plus three, that means we need four bags. - Well, 
I always overestimate the amount of chips we need for party, so I'm going to double that. I see we have four, 
two times four is eight. Great, we need eight. Now, let's rewind that and see how else those operations could've 
played out if our two threads got scheduled differently. (whirring) - I'll go first first. - Hold on, I'll go first 
this time. I see one bag of chips, but I like to over estimate so I'll double that. One times two is two. - Thanks. 
Now I'll add three bags to that. Two plus three is five. Hm, five bags is less than the eight we calculated last 
time. (grunts) - Don't tell me we're not going to have enough chips for the party! - It's okay, we'll fix this. - 
Phew. - Even though we're using this pencil as a mutex to protect against a data race, the potential for a race 
condition still exists because the order in which our threads execute is not deterministic. When deciding how many 
bags to buy, if my thread runs first to add three bags before Baron doubles it, that gives us eight. But if Baron 
instead runs first to double to original value before I add three bags, then we end up with five. - The race 
condition we created here is fairly straightforward, but in practice, race conditions can be really hard to discover. 
And that's because a program might run correctly for millions of times while you're building and testing it, 
so you think everything's fine. You release the finished program, and then one time, things happen to execute in a 
different order and that causes an incorrect result. Unfortunately, there's not a single catchall way to detect race 
conditions. Sometimes putting sleep statements at different places throughout your code can help to uncover potential 
race conditions by changing the timing and, therefore, order in which threads get executed. That said, 
race conditions are often a type of heisenbug, which is a software bug that seems to disappear, or alter its 
behavior, when you try to study it. Running debuggers and doing things to affect the timing of your code in search of 
a race condition may actually prevent the race condition from occurring. '''
