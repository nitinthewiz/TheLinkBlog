---
title: "How To: Port Your Landline to Twilio, Forward to Your Mobile Phone"
slug: how-to-port-your-landline-to-twilio-forward-to-your-mobile-phone
date: 2010-08-19 15:57:55 -0500
category: 
external-url: http://blog.twilio.com/2010/08/how-to-port-your-212-landline-to-twilio-forward-to-your-mobile-phone.html
hash: 9e53b95e4b72c42bd7228376fb2b1b97
year: 2010
month: 08
scheme: http
host: blog.twilio.com
path: /2010/08/how-to-port-your-212-landline-to-twilio-forward-to-your-mobile-phone.html

---

I read a post today in the Wall Street Journal about how early adopters want to get 212 numbers, one of the earliest area codes in New York City, for their cell phones.  Across the United States there are regions where literally all numbers in an area code have been allocated.  As the logic goes, there is a vanity element to having an older number -- in the case of New York City that number begins with 212.


While these numbers are scarce and coveted by some, they actually aren't unattainable.  They're available for purchase on Ebay, and even occasionally come up for inventory here at Twilio (we've constantly got an open order for more).  But what's the best way to get one?



Take Your Landline Number With You
For many New Yorkers, and people around the world, having a landline phone is becoming less important.  But why give up that awesome number you've had for years when you disconnect your landline service and go completely digital?  You can simply port the number to Twilio, and then forward it to your mobile phone.  Want to give out the 212 to friends, put it on your business card, and then forward to whatever number is on your mobile?  Done, and we'll show you just how easy it is to set up call forwarding in this post as well.


How to Port a Number

Porting a number into Twilio is free, and usually takes 2-3 weeks depending on what carrier you're porting from.



 To get started with porting, log into your Twilio account and make sure you've upgraded to a paid account.  Once the number is in, it will cost $1/month to hold onto it, so you'll need some funds to cover that.  Once you're in and have added funds, head over to the phone numbers page and select the "Port a Number" button.


Fill out the porting form and submit it to get things rolling.  Later on, you'll get an email from Twilio asking for a recent phone bill and a signed letter of authorization for us to move your number from your current carrier to Twilio.  At that point, our porting team takes over and moves things along, and gives you updates along the way.
Edit: If you don't have a phone number you want to port, or just want to try out call forwarding first, you can buy U.S. local Twilio numbers for just a dollar a month, and when you upgrade to a paid account and put in $20, you keep your $30 free trial as well. 


How to Configure Call Forwarding

Once you've got your number ported to Twilio, you'll probably want to set it up to receive inbound calls and forward them to your mobile phone.  There are several ways to do this:



* code up a call forwarding application of your own using TwiML
* configure a simple hosted call forwarding app or "Twimlet" from Twilio Labs
* set up a call forwarding flow using Twilio's OpenVBX drag-and-drop interface

Building Your Own App

It's literally 3 lines of XML, hosted on your server and publicly accessible with a URL that you can use to configure your Twilio number. You might just try using a public Dropbox, since its a static file.


forwardcall.xml
<Response>


<Dial>415-390-2337</Dial>


</Response>




Setting Up the Call Forwarding Twimlet

Twimlets are simple stateless applications hosted by Twilio.  Multiple Twimlets can be chained together to create sophisticated apps (great for rapid prototyping), and the Forward Twimlet is a simple app you can use to send incoming calls to your Twilio out to your mobile phone.


In this example, I'm going to forward calls to my Twilio number on to the Twilio company phone, but you can do this with any number you wish.  Each Twimlet comes with a simple URL generator, just fill out the form and copy the URL it creates.





You'll paste this URL into the voice application box next to your Twilio number.




Configuring Call Forwarding Using OpenVBX

We recently launched an open source project called OpenVBX, which provides a simple drag-and-drop user interface for building voice applications.  I think of it kind of like self-hosted Wordpress, for the phone.  To use it, you'll need a hosting environment that runs PHP... or you can take advantage of one-click installs from Dreamhost or Standing Cloud to make things super easy.


To set up call forwarding, add a new call flow and use the Dial applet to connect incoming calls to your Twilio number to your mobile phone, like this:



  


Photo credit: Flickr





  

