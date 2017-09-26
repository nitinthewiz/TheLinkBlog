---
title: "Never Give Up, Retry: How Software Should Deal with Failures"
date: 2017-09-25 11:57:44 +0000
external-url: http://allyouneedisbackend.com/blog/2017/09/15/how-backend-software-should-retry-on-failures/
hash: 53aee275f77ebb93d63d1c481c2e1407
year: 2017
month: 09
scheme: http
host: allyouneedisbackend.com
path: /blog/2017/09/15/how-backend-software-should-retry-on-failures/

---

It’s hard to quantify the number of system issues in various systems I've seen through the years that are the result of poor retry logic in code. Retry logic is the close cousin of exception handling and these two areas are where a lot of large system failures cause huge challenges. Pessimistic retries around services you depend on can make a **huge** difference in real system performance.
