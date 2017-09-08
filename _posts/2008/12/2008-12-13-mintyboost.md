---
title: "MintyBoost"
date: 2008-12-13 08:12:42 +0000
external-url: http://www.friday.com/bbum/2008/12/13/mintyboost/
hash: 2d04ffc06dc3439a046675474b7b52c4
annum:
    year: 2008
    month: 12
hostname: www.friday.com
---


At left is a “Minty Boost v2.0” that Roger and I put together over the course of a couple of evenings.

The Minty Boost is a tiny power supply designed to provide power or to charge most USB devices.

Including the iPhone 3G, which really wants somewhere around 500ma to charge.  Normally, to achieve that level of current, the devices have to negotiate with each other.

The MintyBoost is a “dumb” USB power source in that it mimics the wall wart (very very tiny wall wart) style USB power supplies, providing enough bias on the data lines to make the device pull current without going into “negotiation” mode.




As a power supply, the Minty Boost is both smart and efficient.  It is built around Linear Technology’s LT1302 Micropower High Output Current Step-Up Adjustable and Fixed 5V DC/DC Converter.

Combining the chip with a handful of discrete components creates a power supply that produces a steady 5 volts @ 600 milliamps.  It is designed for use with 2x 1.5 volt cells and will continue to operate even until the combined voltage output by the in-series cells drops to 2 volts.  When not in use, the chip draws extremely little current.

I’m using GreenBatteries.COM’s Ultra Low Self Discharge cells. These rechargeable batteries are specifically designed not to self-drain over time when not in use.   Perfect for remote controls and camera flashes that don’t get used all the time (or are used rather intermittently when you think about it).

I’ll likely pick up a set of the high-capacity non-ULSD rechargeables.

The whole assembly is hot-glued into an Altoids tin (with a bit of electrical tape as insulation).  Very convenient packaging and it is still quite easy to pop out the batteries.

It works quite well, though differently than other battery packs.  Namely, the device actually charges the iPhone’s battery.   That is, it isn’t an extender.   As such, the iPhone will happily suck whatever current — 600ma, in this case — out of the device until either the iPhone’s battery is charged or the charger is drained.   

The one caveat is that the device can actually drain the iPhone’s battery as the current falls.  You need to keep an eye on things and pull the charger’s plug once the iPhone’s battery icon changes from “charging” to “powered”.

A small bit of inconvenience given that the device is around $20 and I don’t ever have to click “OK” on the “external device may be incompatible with your phone” dialog.

You can buy the kits from Lady Ada’s store.   It is fairly straightforward to solder together, too.

Alternatively, you can try to grab the parts yourself.  I had a hard time finding the LT1302 power supply chip at a reasonable price (including shipping).  Turned out to be cheaper just to buy the kits.



