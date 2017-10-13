---
title: "The Value of Optimizing for Resilience - DZone Performance"
date: 2017-10-10 01:39:18 +0000
external-url: https://dzone.com/articles/the-value-of-optimising-for-resilience
hash: a3dcab75394736f84e8be394a37c4bec
year: 2017
month: 10
scheme: https
host: dzone.com
path: /articles/the-value-of-optimising-for-resilience

---

Good read and I like this term **resilience** better than **survivability**, which is what I typically use to describe these qualities. I also like the concept that this is built into the services but also the teams behind them.

> If the checkout team adopted Defensive Architecture techniques they could combine a [Circuit Breaker](https://www.martinfowler.com/bliki/CircuitBreaker.html), a [Bulkhead](https://www.amazon.co.uk/dp/1680502395/), and a Feature Toggle in anticipation of registration errors. If the registration service struggled under load the Circuit Breaker would regulate registration requests to allow a percentage to succeed, and the Bulkhead would warn the checkout frontend to skip registration for some customers.

Great terms and concepts to consider in system and team design! 👍
