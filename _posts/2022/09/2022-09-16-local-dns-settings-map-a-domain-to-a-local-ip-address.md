---
title:  "Local DNS Settings: Map a Domain to a Local IP Address" 
slug:  "local-dns-settings-map-a-domain-to-a-local-ip-address" 
date:   2022-09-16 12:55:38 -0700 
external-url:   http://wahldev.com/local-dns-settings-map-a-domain-to-a-local-ip-address/ 
year:   2022 
month:   09 
scheme:   http 
host:   wahldev.com 
path:   /local-dns-settings-map-a-domain-to-a-local-ip-address/ 
---

On Mac, do - 
> sudo nano /private/etc/hosts 
and plug in your local IP and give it a domain. That's all! No more typing out local IPs.

Of course, it'd be better if it's setup with DHCP and bind9, but this works just fine.