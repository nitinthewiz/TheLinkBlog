---
title: "Google PowerMeter Installation and First Impressions"
date: 2009-10-13 22:43:04 +0000
external-url: http://www.thedeets.com/2009/10/13/google-powermeter-installation-and-first-impressions/
hash: 57aa7680d3b70fbf3498a723af6b48d3
annum:
    year: 2009
    month: 10
url-parts:
    scheme: http
    host: www.thedeets.com
    path: /2009/10/13/google-powermeter-installation-and-first-impressions/

---

Google announced last week that they had formed a device partnership with a company called T.E.D. to provide hardware to power their PowerMeter service.

For those of you unfamiliar with the service, it’s a real-time energy monitoring service with a web-based interface, so you can see exactly how much energy (and money) your home is consuming in real time. 

I ordered the TED5000-G. At the time, it cost $199.95. They sell a digital display you can stick on a counter or bookshelf with the 5000-C model for $239.95, but I planned to use the web interface so didn’t see the need for that.

It showed up in around 2 days via FedEx, although they now appear to be backordered for 3-6 weeks due to high demand from the Google partnership. 

Installation
There are a couple stages to the installation process. 

1. Install a set of clamps in your circuit breaker box. I wouldn’t recommend doing this if you’ve never worked with electricity before. Ask a friend for help. The most important tip I’ve heard for this step is to make sure the clamps are both facing the same direction in order to get accurate readings. Here is an excellent video explaining the install process:




2. Hook up the gateway. The gateway is a cube that plugs into an AC outlet and your ethernet router. Information gathered by the clamps is transmitted to the gateway through the home’s power grid and stored in the gateway. 

3. Configure the software. T.E.D.’s software is called Footprints. It resides on the gateway and is accessed through a browser. For Windows computers, one can browser to http://TED5000 to access it. However, that address doesn’t resolve on a Mac, and whoever has ted5000.com is seeing a spike in traffic. Instead, you have to figure out the IP address of the gateway. This is undocumented, which led to some Googling, which led to this set of instructions, which didn’t happen to work for me but probably will for many of you. In my case, I ended up hooking up an old Dell, browsing to http://TED5000 to make sure I could see it, then running the following command line: ping TED5000

Which responded with the IP location of the gateway. That address allows me to see the web interface on a Mac (and iPhone).

Once found, the Footprints software asks for a few data points to improve its data. Utility costs and cost structures being the primary info, so have a power bill on hand. This will allow Footprints to calculate your real-time cost for energy.

4. Browsing from iTouch.
 The Footprints website is iTouch and iPhone friendly, so you can view your energy dashboard and doubletap to zoom in on specific metrics. For example, here is my current current:




5. Monitoring Changes.
 The immediate feedback provided by this software is fascinating. Flipping a light switch on/off is reflected on the meter in a few seconds. So far, I’ve noticed the impact of our clothes dryer (wouldn’t want to run that thing 24/7), refrigerator when it kicks into chill mode, running computers, the additional energy needed to watch YouTube videos, and the impact of charging cell phones (looks like around 8 cents/night for my Treo).

6. Profiles.
 If you have appliances that you’re particularly interested in tracking, you can set up profiles for up to 5 in Footprints. To do this, you tell Footprints that you’re going to flip on something significant, then Footprints notes the power consumption profile of that appliance. This would allow you to break out the use pattern and energy costs associated with, say, an A/C unit. 

7. iGoogle Integration.
 The whole point of the Google partnership, as I understand it, is to be able to push this data to Google for additional uses. This includes viewing on iGoogle, but I think the larger benefit could be trending and benchmarking reports based on shared energy data. I haven’t figured out how to do this yet. Drop a link in the comments if you happen to know a good source of information for this. Google’s documentation on this is sending me in circles. The model I purchased didn’t have the Google PowerMeter firmware installed when shipped. I downloaded that, updated the device, then went to Edit > Activate Google Powermeter. Google asks for a zip code (or other location data) which they’ll likely use to look for energy consumption patterns.




Apparently, my 3 bedroom house is consuming energy at levels comparable to a 1 bedroom apartment. That won’t likely be sustainable. 

This is the first time in my life that I’ve had even the slightest understanding of how my home uses energy. It’s a very cool thing. 

By the way, some utilities around the country are installing power meters and providing web interfaces where utility customers can see how  their energy consumption compares to others in their community. That seems like a great way to educate consumers about what they could be doing to painlessly save energy in their homes. Will Xcel Energy do this?



   

