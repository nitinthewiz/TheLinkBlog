---
title: "Electronics: The Adventure Begins"
date: 2008-03-25 04:32:25 +0000
external-url: http://whereslou.com/2008/03/24/electronics-the-adventure-begins
hash: 03310b7c5d2b37904dcce1bf849b32ef
---

Finally got started doing some real work on the electronics project I’m taking part of with my friend Kevin. A number of parts were picked up today at ABC Electronics and a few a/d converter chips were picked up at AEI Electronics. I have to say AEI/Acme isn’t what it used to be when it was on Washington… The wall of IC chips was nowhere to be seen - it’s become more of a high-end home audio gear shop or something.

In any case! First thing first was wiring up the rabbit so it can be worked on. That meant soldering a 50 pin header on the development board in the array of holes provided. This is essentially a direct connection to all of the lines coming out of the rabbitcore daughter board itself.

Then I was looking at the main prototyping area. A lot of what I’m going to be doing a very work-in-progress and I didn’t want to commit to a particular chipset yet, so I decided to leave the developer board and jump onto a breadboard.

 840

The breadboard had a convenient locking edge normally used to connect multiple boards together. In this case I used it as a “stand” for the rabbit development board.

Next is the issue of getting lines down to the board. I have some wire-wrapping sockets used to prototype on perf-board, so I stuck one in from the bottom up. I was originally thinking of doing point to point wiring of lines as I needed them, but it occurred to me it would be more organized and useful in the long term to wire the lines from the header to the socket in a one-for-one pattern.

844

Ain’t that pretty? This way the silkscreen printing that labels the rabbit lines on the header both sides of the board can be used when grabbing the same lines from the socket.

So on the “bottom” of the dev board there’s a socket which is the right size to jam standard gauge solid wire to drop connections down to the breadboard.

847

If look at the large size on this one you’ll see this socket has brought forward PA0-PA7 and PB0-PB7. Inside the micro those are port A and B you can read/write as entire bytes. To test the work so far I’ve put some LEDs and flashed a program which wrote different byte values to port A, which came through just great once I realized I had the LEDs in backwards. (Sort of rusty :).)

The chip you see punched down there is the analog to digital converter. That’s what all those pins are going to be needed for because it’s a monster for i/o lines - it needs 4 lines to select input and 8 lines to read data back, and handful of others to latch, clock, and signal. Bit of a pain really - we’ll probably switch to a serial ADC at some point - but this one has some advantages right now. It’s easy to work with because it’s the old-school 10 pins per inch, it’s got 16 analog lines in which is huge, and it was a part the store had on hand.

So yeah. Hook that bad boy up next.

