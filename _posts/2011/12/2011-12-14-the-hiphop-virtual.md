---
title: "The HipHop Virtual Machine"
date: 2011-12-14 15:39:31 +0000
external-url: https://www.facebook.com/note.php?note_id=10150415177928920
hash: 6f655f6db82603e7703c6203f431f390
year: 2011
month: 12
scheme: https
host: www.facebook.com
path: /note.php
query:
    note_id: "10150415177928920"
---

We're always looking for ways to make our computing infrastructure more efficient, and in 2010 we deployed HipHop for PHP to help support the growing number of Facebook users. While HipHop has helped us make significant gains in the performance of our code, its reliance on static compilation makes optimizing our code time consuming. We were also compelled to develop a separate HipHop interpreter (hphpi) that requires a lot of effort to maintain. So, early last year, we put together a small team to experiment with dynamic translation of PHP code into native machine code. What resulted is a new PHP execution engine based on the HipHop language runtime that we call the HipHop Virtual Machine (hhvm). We're excited to report that Facebook is now using hhvm as a faster replacement for hphpi, with plans to eventually use hhvm for all PHP execution. 
