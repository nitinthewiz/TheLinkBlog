---
title: "The Absurdly Underestimated Dangers of CSV Injection"
date: 2017-10-10 11:06:59 +0000
external-url: http://georgemauer.net/2017/10/07/csv-injection.html
hash: c9005c4f6fbf34be82b608bb75387fe6
year: 2017
month: 10
scheme: http
host: georgemauer.net
path: /2017/10/07/csv-injection.html

---

Interesting writeup on injecting formulas into CSV data to affect the behavior of the software that is reading the CSV. This example uses the preference that spreadsheets have to interpret formulas embedded in CSV files. Security risks like this can be surprising, even to very technical people, since the data isn't an executable itself.
