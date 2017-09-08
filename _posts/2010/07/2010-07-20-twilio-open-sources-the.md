---
title: "Twilio Open Sources Stashboard, the Status Dashboard"
date: 2010-07-20 17:44:03 +0000
external-url: http://www.twilio.com/blog/2010/07/twilio-open-sources-stashboard-the-status-dashboard.html
hash: b2e474fe8accaf6e2df45e5a45c05483
annum:
    year: 2010
    month: 07
hostname: www.twilio.com
---

Some of you may have noticed Twilio's shiny new API Status page at http://status.twilio.com.We're excited to announce that Twilio finally has a modern status page and not only that, we open source it! Yup, you too can download the code and host your own SaaS or API status page. Learn more at http://www.stashboard.org.


Introducing Stashboard


Stashboard is a status dashboard for APIs and software services. It's similar to the Amazon AWS Status Page or the Google Apps Status Page. Businesses and individuals have come to rely on hosted APIs and cloud service providers for email, CRM, sales, phones and more, however, many have poor or non-existent status pages. Enter Stashboard! 


Stashboard is designed to provide a generic status dashboard for any hosted service or API. The code can be downloaded, customized, and run on any Google App Engine account.



  Manage the status of many API or SaaS services


 Set custom status messages and icons such as Up/Down


 Show historical status for each service


 Runs on Google App Engine so it's independent of your in-house infrastructure (unless your app is on GAE)


 Full REST API for both getting and setting status information


 CNAME to http://status.yourapp.com


 Rich client or basic rendering architecture


Stashboard is written in Python and hosted on Google App Engine.


Head over to stashboard.appspot.com to try the latest version.


It's Got APIs, Too



 Twilio's new status page and Stashboard also support a full REST API to let you both push and pull events and service status information.


(1) Getting status data: using the REST API you can request status data and integrate realtime data into your web application. For example, at Twilio we use the REST API to add a banner to the top of our internal intranet to inform all employees about the status of our APIs.



 (2) Putting status data: you can also add new events and change status information using the Stashboard REST API (using the authenticated methods). For example, you could wired up your Nagios, PagerDuty, or internal application alerts to automatically update your status page.


We hope you enjoy Stashboard! Drop us a line if you deploy it for your app or have any questions.
