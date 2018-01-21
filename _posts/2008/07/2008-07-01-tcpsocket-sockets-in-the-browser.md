---
title: "TCPSocket: Sockets in the browser"
slug: tcpsocket-sockets-in-the-browser
date: 2008-07-01 13:50:36 -0500
category: 
external-url: http://ajaxian.com/archives/tcpsocket-sockets-in-the-browser
hash: 4efbcabcc3ce896e41a35171bfe1a073
year: 2008
month: 07
scheme: http
host: ajaxian.com
path: /archives/tcpsocket-sockets-in-the-browser

---

Michael Carter of Orbited has written about how he now likes to call Comet sockets in the browser, and has an implementation available that looks like this:

PLAIN TEXT
JAVASCRIPT:







var conn = new TCPSocket(hostname, port)





conn.onopen = function() &#123; alert('connection opened!') &#125;


conn.onread = function(data) &#123; alert('RECEIVE: ' + data) &#125;


conn.onclose = function(data) &#123; alert('connection closed!') &#125;





conn.send('Hello World');









The above code code is all you need to know. It will open a TCP connection to hostname:port, and will send the data Hello World. Any data the server sends back will be alerted with the onread handler.

The exact mechanism behind this innovation is pretty straightforward: Orbited is a router and firewall for incoming TCPSocket connections from the browser. It uses Comet techniques to establish bi-directional communication with the browser, then forwards all data over a raw TCP socket to the end point. Configuration allows access control enforcement so that the TCPSocket can only be connected to pre-approved end-points, so that the Orbited server isnt an open relay.

While this presents a paradigm shift in the way developers are tackling real-time, web-based applications today, its actually a return to the original method of writing network applications. Instead of writing applications based on web frameworks and throwing a Comet server in the mix, you can simply use the client-server architecture where the browser is the client, and the server is an arbitrary TCP server.
