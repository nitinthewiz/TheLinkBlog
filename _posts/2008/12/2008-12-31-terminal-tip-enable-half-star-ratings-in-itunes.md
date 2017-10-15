---
title: "Terminal Tip: Enable half-star ratings in iTunes"
date: 2008-12-31 10:00:00 -0600
external-url: http://www.tuaw.com/2008/12/31/terminal-tip-enable-half-star-ratings-in-itunes/
hash: a597ba58568ec4b83f93f35927377b78
year: 2008
month: 12
scheme: http
host: www.tuaw.com
path: /2008/12/31/terminal-tip-enable-half-star-ratings-in-itunes/

---

Filed under: Terminal Tips Do you like giving ratings to songs in iTunes? If so, then you've probably noticed that you are only able to rate songs on a full-star basis, not enough granularity for some music fans... there's a longstanding AppleScript hack to enable half-stars, but now there's an easier way around this issue. Macworld's Rob Griffiths found a work around, involving a simple Terminal tip to enable half-star ratings. To enable half-star ratings, close iTunes, and open Terminal (/Applications/Utilities). Once you have Terminal opened, type the following command and press enter:  defaults write com.apple.iTunes allow-half-stars -bool TRUE When you reopen iTunes and rate a song, you will be able to give half-stars. That simple. If you wish to make things normal again, open Terminal and type the same command, replacing "TRUE" with "FALSE."TUAWTerminal Tip: Enable half-star ratings in iTunes originally appeared on The Unofficial Apple Weblog (TUAW) on Wed, 31 Dec 2008 11:00:00 EST.  Please see our terms for use of feeds. Read | Permalink | Email this | Comments     
