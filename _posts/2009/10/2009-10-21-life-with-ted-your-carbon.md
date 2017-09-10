---
title: "Life With TED - Micromanaging Your Carbon Footprint"
date: 2009-10-21 04:39:13 +0000
external-url: http://radar.oreilly.com/2009/10/life-with-ted---micromanaging.html
hash: 763b46b58273d8bb2479f50803be1ea4
annum:
    year: 2009
    month: 10
url-parts:
    scheme: http
    host: radar.oreilly.com
    path: /2009/10/life-with-ted---micromanaging.html

---

I've been interested in having a better handle on my electrical consumption for a long time. Our family regularly goes through 1100-1200 kWh a month, and it's been frustrating that I couldn't really get a grip on where or when the power was really being used.  I want to get my power usage under control for three reasons:

I want to reduce my $180-a-month-and-climbing power bill.  Public Service Company of NH (PSNH) has one of the higher electricity rates in the country (we have a nuke we're still paying off, among other things.)
I'm seriously investigating adding solar to the mix, now that a 30% federal tax credit, a $6,000 state rebate, and lower prices for the panels have converged.  It would be great to get my usage down into the 600-800 kWh average output I've been told I can expect a month from a system, and zero out my PSNH bill on a yearly basis.
I'm a firm believer in reducing carbon emissions, I'd like my 14 year old son to have a world to grow up in.  I've already cut my fuel oil use in half (to a still awful 250 gallons a month in the winter, but it's a huge house...)  Cutting my electricity is the next low-hanging piece of fruit on the tree.



I had been tracking Google PowerMeter, a Google initiative that lets people monitor their energy usage online, but it was only available to customers of electric providers who were using so-called "Smart Meters". Smart Meters send usage data back to the provider, and PSNH isn't one of them.


Then, this week, Google announced on their blog that normal mortals could now order a device called The Energy Detective (or TED, as he's known by his friends...)  TED is made by Energy, Inc. out of South Carolina, and consists of a minimum of two components.  The first piece is an inductive current measuring device that lives out in your circuit breaker box.  The second is a gateway device that plugs into a wall socket and has an Ethernet jack.  Optionally, you can also get a stand-alone display, so that you don't need a computer to view your usage.


Wiring the sensor device into your box is fairly straightforward.  You clamp the two sensors around the mains as they come into the box.  You also have to wire the device to the two "hot" phases of your 220V service (which requires two free breakers in your box on different phases), and a third wire running to neutral.  If you have some basic electrical savvy, you can do it yourself, but I decided to wimp out, since my box is so crowded (after-effects of having a transfer switch put in for a generator...), so I shelled out the $85 to have an electrician put it in.


The gateway unit communicates with the sensor unit via signals sent over the house AC.  As with anything using the power lines to communicate, I found the unit was very particularly to which outlet I plugged it into.  It really doesn't like to share a circuit with a computer, for example. Neither of the two plugs which was actually next to a network hub would pick up a signal, but one in an adjacent room that happened to have a network jack did.


Once you have the gateway talking to the sensors and plugged into the network (it uses DHCP to get an address), you can surf to it using any browser.  I can even get to it using Safari on my iPhone.  The "home" screen is a dashboard, showing various statistics about current demand and your daily, weekly and monthly averages.  You can view the data in terms of kWh, dollars (once you tell TED how much you pay for power, it can even handle peak period and tiered pricing models), or pounds of CO2.


All of the ranges on the dials and bar-graphs are configurable, so if you want 3kWh to be "red", you can set it up that way.  You can also configure refresh rates.  Clicking on the "Graphing" tab lets you view your usages second to second, minute by minute, or by daily or weekly aggregates.


It's these graphs that I have found to be most useful.  You can start to see all sorts of interesting patterns, like the "heartbeat" of my furnace turning on and off at night, when the rest of the house is otherwise quiet.


I can also see the huge hump when my son wakes up in the morning, and proceeds to turn on every first floor light in the house.  I was even able to tell that my wife had turned on the dishwasher before she left for school one morning.

The hourly aggregates are better for looking at overall trends, as opposed to discrete events.  I was surprised to see that 3AM was actually a heavier usage period than noon on a weekday, although it makes sense in hindsight.  At 3AM, the furnace is running more, whereas with the house empty at noon, the relative warmth lets the furnace run less.



Using TED, I've been able to quickly find the critical items that I need to make sure get shut off when not used.  A big one is my Mac Pro, good for between 200 and 400 watts.  I now turn it off when I got to bed at night and leave for work.  The LCD TV and surround sound amplifier downstairs are another.  It's early days, but I've already been able to trim down about 20-30% of my daily usage. Once I have more than a few day's data in the system, the daily aggregates should be able to let me see how I'm doing at reducing my usages overall.  


There's also a nice feature, at least in concept, called load profiles.  The basic idea is that TED can figure out when certain appliances or other pieces of gear are turned on or off, based on the power drawn.  As I said, it's a nice idea in principal, but in reality, it only works if you have devices that draw very unique amounts of power, and do it consistently.  If you have two devices that both draw about the same amount of power, TED won't be able to tell the difference between turning one on, and turning the other one on.  And if the device doesn't draw the same current (plus or minus 10%) every time, it won't get tagged correctly.  But short of putting individual sensors on each device, TED does about as well as you could expect. 


If you set your firewall / router up right, you can even access TED from the web outside your house.  You can also use an iPhone app to monitor your usage, although it's pretty primitive.  For example, you can't see graphs of usage.  Also, if you password-protect TED (good if you're going to be putting it out on the web), you can't use the iPhone app, since it also passwords the API.  I've started playing around with writing a better app, using the publically documented API, with graphing and password support.


I started this article by talking about Google's PowerMeter, and TED does in fact integrate with PowerMeter.  But honestly, PowerMeter seems downright primitive after all the features that the native TED interface gives you.  For one thing, it's only available as a widget on Google's iGoogle page, something I never use (largely because it doesn't integrate with my Google Apps for Domains account...)  It also offers very little in the way of functionality, beyond a simple bar graph.  One nice thing it does have is a comparison bar, that tells you how your consumption compares to average households of various sizes.


A basic TED setup with one sensor unit and one gateway runs $200, a stand-alone display raises the price to $240.  If you want to monitor solar output as well, or have a two panel house, the prices are somewhat higher.  It's certainly not cheap, you can get a good netbook for that kind of money, but it will pay me back in a year if I can reduce my comsumption by a mere 10%.  Evidently, I'm not the only one who was interested in TED, because all the units are currently on a 4-6 week backorder at their site.


Of course, all TED is going to do is to tell me what, in a sense, I already know: turning things off saves energy.  But by quantifying it, and letting me see what really makes a difference, it lets me focus my energy on what matters.  And frankly, it's fun, at least at the moment, to see how low I can get my consumption at any given time.


   

