---
title: "MyOpenID for Your Domain - The Easiest Way to Use Your URL as an OpenID"
date: 2008-04-17 15:56:49 -0500
external-url: http://readwrite.com/2008/04/17/myopenid_for_your_domain
hash: a54534ba6300936a8dc47ad881cf2015
year: 2008
month: 04
scheme: http
host: readwrite.com
path: /2008/04/17/myopenid_for_your_domain

---

OpenID, a technology that allows users to sign in to new supporting websites through a single trusted ID provider of their choice, is notoriously hard for non-developers to implement and in many cases use.   One of the biggest challenges may have been eliminated, however, by the recent release of a new service called MyOpenID for Domains.


The service makes it remarkably easy for anyone to create OpenID accounts through their own domain, using the MyOpenID authentication service.  


For example, my new OpenID is http://openid.marshallk.com/marshallk, based on my personal site marshallk.com.  It was really easy to set up and now I can offer other users of my site their own marshallk.com OpenID as well. (Hi Mom!)


How It's Done

MyOpenID for Domains lets you set up OpenIDs in one of two formats:  Wildcard subdomains like member.yourdomain.com or as a single subdomain + path like openid.yourdomain.com/member.




I chose the single subdomain plus member path because I want to be able to use other subdomains for other purposes.  


It's really easy to set up either path.  For my WordPress blog I just filled out the form below, then I had to call my webhost (Bluehost - great customer service, terrible uptime) and ask them to make a small edit to my DNS record.  I gave them this information:


Name: openid.marshallk.com
Type: CNAME
Value: www.myopenid.com 


They made the change needed, basically setting up a redirect, in less than 5 minutes.  Other hosts will let you edit your own DNS info.  I then posted a page on my blog with a particular URL and a short code for MyOpenID to detect.  That's it - I was done.  Now I can use my own domain name as an OpenID.  The next step was to make sure that my user identity page was looking spiffy.


If MyOpenID ever closes its doors, it will be easy for me to edit my DNS record back and keep my OpenID URL from becoming a 404 out of my control.  I'll also now be able to verify that I am in fact the owner of marshallk.com.


Limitations of the Service

This is the easiest way I've found to use my own domain name as an OpenID.  There are other ways to do it but they've always given me far more trouble than they should.  This service from MyOpenID is also an easy way to offer and administer OpenID accounts to other users of a particular website.


MyOpenID is a good OpenID provider.  MyOpenID for Domains does require that you use their service in particular, however.  There are many different OpenID providers offering many different advanced features.  Check out SpreadOpenID.org for a comparison of many different providers.


As you can see below, my MyOpenID profile is now tied to my domain.  All I need now is the ability to put HTML links in my summary info, display recent items in an RSS feed of my choice on this page and some other customization options.  Then I'll be doing great.


Watch this space for more forthcoming news on big increases in OpenID usability.
