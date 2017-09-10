---
title: "Design Patterns: Architecture of an Autonomous Application"
date: 2013-12-11 10:20:33 +0000
external-url: http://msdn.microsoft.com/en-us/magazine/cc164125.aspx
hash: fcce8be3e0d9c5849b081e6e701cfb1c
year: 2013
month: 12
scheme: http
host: msdn.microsoft.com
path: /en-us/magazine/cc164125.aspx

---

A service should be a completely autonomous application. It's not an island though because you can ask it to perform services for you. But it is autonomous in the sense that it completely controls its data and it denies the outside world direct access to that data or to its objects. The only way to access its goodies is to send it a message asking it to perform a task for you. If it doesn't like the way you ask or who you are, it will refuse to perform the service. Nobody decides this on its behalf; it decides for itself.
