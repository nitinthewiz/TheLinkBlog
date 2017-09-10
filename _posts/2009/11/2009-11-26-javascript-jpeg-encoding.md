---
title: "Javascript JPEG Encoding"
date: 2009-11-26 05:33:34 +0000
external-url: http://ajaxian.com/archives/javascript-jpeg-encoding
hash: 78642628e3078852d36ab45936615fd1
annum:
    year: 2009
    month: 11
url-parts:
    scheme: http
    host: ajaxian.com
    path: /archives/javascript-jpeg-encoding

---



Andreas Ritter has managed to encode JPEGs in Javascript. This blog post explains how he did it, shows some benchmarks, and provides a demo and a downloadable library so you can play along at home.


It was surprising that it was that easy to get the first js-encoded jpeg displayed in the browser. Of course I didn't want to stop there. I wanted to optimize things as much as I could to make the encoder fast. This took me several days. I found optimized encoder versions for flash and haxe floating around the net (Faster JPEG Encoding with Flash Player 10) and tried the optimizations used there in my javascript version. As you can seen in the benchmarks below I was quite successful.

Another idea was to use the new web workers to do the heavy lifting in an separate thread, not blocking the gui. This is something flash can't do. So I created a version using a web worker for the encoding.


The API gives you a JPEGEncoder or an alternative JPEGEncoderThreaded. Usage is straightforward:

PLAIN TEXT
JAVASCRIPT:




 


var myEncoder = new JPEGEncoder([quality])


var JPEGImage = myEncoder.encode(CanvasPixelArray,[quality])


 






I think the results show that JavaScript is quite fast (at least in Safari and Chrome). A little over 4 seconds for the non-threaded version is a very good [sic] result, when compared to the 3,3 seconds the optimized flash jpeg encoder takes. Please note, that JavaScript has no static types, no byte array, no Vector-class and is not pre-compiled. Taking these facts into account Nitro and V8 are faster than the ActionScript 3 VM.

Comparing the different browsers Nitro and V8 are a magnitude faster than TraceMonkey. Firefox 3.6b2 shows some improvements, but it's still a long way. Probably the Mozilla guys should consider adopting Nitro or V8?


He used the  AS3 (ActionScript) JPEG encoder as a starting point. It's worth noting there's also a PNGEncoder there too; that's a port waiting to happen.


  

