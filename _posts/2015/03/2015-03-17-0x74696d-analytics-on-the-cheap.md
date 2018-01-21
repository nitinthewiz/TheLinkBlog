---
title: "0x74696d | Analytics on the Cheap"
slug: 0x74696d-analytics-on-the-cheap
date: 2015-03-17 17:19:58 -0500
category: 
external-url: http://0x74696d.com/posts/analytics-on-the-cheap/
hash: 855ee279ac6d04aab954755dd5a497bf
year: 2015
month: 03
scheme: http
host: 0x74696d.com
path: /posts/analytics-on-the-cheap/

---

The technique I’m describing has one important constraint: messages have to be either idempotent or have a built-in ordering (ex. time series data), because there’s no way for the ingest servers to handle the ordering of messages otherwise. You won’t be able to come up with a “true” total ordering here either, but we’re okay with that on a statistical level.
