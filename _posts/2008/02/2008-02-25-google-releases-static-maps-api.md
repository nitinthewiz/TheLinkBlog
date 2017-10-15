---
title: "Google Releases Static Maps API"
date: 2008-02-25 00:11:19 -0600
external-url: http://www.programmableweb.com/2008/02/25/google-releases-static-maps-api
hash: 4c5ec95aa466cdabecb27b19d710b23b
year: 2008
month: 02
scheme: http
host: www.programmableweb.com
path: /2008/02/25/google-releases-static-maps-api

---

If you want a dead-simple way to create custom maps without needing to worry about JavaScript or programming then the just announced Google Static Maps API may be your answer. Googles new API allows you to generate the maps using a regular URL (ala REST) along with parameters specifying location, size, etc and it returns a unique GIF image with that map. We have created a Static Maps API profile with the details. Here are some notes from their announcement:   The Google Static Maps API returns a GIF-format image in response to a HTTP request via a URL. For each request, you can specify the location of the map, the size of the image, the zoom level, the type of map, and the placement of optional markers at locations on the map. You can additionally label your markers using alpha characters, so that you can refer to them in a key.  You embed a Static Maps API image within a webpage inside an img tags src attribute. When the webpage is displayed, the browser requests the image from the the Static Maps API and it renders within the image location.        A few other details of note:   Usage: A Google Static Maps API query request looks like the following and takes parameters like size (width and height in pixels), zoom-level, type (roadmap or mobile), and any marker placements: http://maps.google.com/staticmap?parameters  Usage limits: Theres a query limit of 1000 unique image requests per user per day. For developers that may expect to hit this limit the best strategy is to use a caching mechanism to store generated images on their own servers. API key: The only requirement to use the API is to sign-up for an API key, which works for both this as well as the standard Google Maps API. Google offers a wizard to help walk you through the process of creating a Static Maps map.  Share This
