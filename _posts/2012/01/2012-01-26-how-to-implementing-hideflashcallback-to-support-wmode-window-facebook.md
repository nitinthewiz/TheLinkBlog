---
title: "How-To: Implementing hideFlashCallback to support \"wmode=window\" - Facebook Developers"
slug: how-to-implementing-hideflashcallback-to-support-wmode-window-facebook
date: 2012-01-26 11:40:26 -0600
external-url: https://developers.facebook.com/blog/post/637/
hash: f115ab1396e4abb1a4351b17a605d64b
year: 2012
month: 01
scheme: https
host: developers.facebook.com
path: /blog/post/637/

---

One of the Pro-Tips we mentioned late last year in our Games Tutorial to Developers creating Flash based Apps was to use wmode=opaque whenever possible. Setting wmode to any value other than "opaque" or "transparent" prevents any HTML content from being displayed at a higher z index than the Flash object. This results in Dialogs, Notifications and Ticker Flyouts being displayed under the Flash object and creates a pretty poor user experience on Canvas.
