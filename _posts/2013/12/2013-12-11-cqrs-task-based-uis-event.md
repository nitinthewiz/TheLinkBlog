---
title: "CQRS, Task Based UIs, Event Sourcing agh!"
date: 2013-12-11 09:47:56 +0000
external-url: http://codebetter.com/gregyoung/2010/02/16/cqrs-task-based-uis-event-sourcing-agh/
hash: e6dffe102c89f2a3b49d6df793179657
annum:
    year: 2013
    month: 12
url-parts:
    scheme: http
    host: codebetter.com
    path: /gregyoung/2010/02/16/cqrs-task-based-uis-event-sourcing-agh/

---

Many people have been getting confused over what CQRS is. They look at CQRS as being an architecture; it is not. CQRS is a very simple pattern that enables many opportunities for architecture that may otherwise not exist. CQRS is not eventual consistency, it is not eventing, it is not messaging, it is not having separated models for reading and writing, nor is it using event sourcing. I want to take a few paragraphs to describe first exactly what CQRS is and then how it relates to other patterns.
