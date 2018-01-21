---
title: "Using AWS KMS to manage secrets in your Infrastructure | Fugue"
slug: using-aws-kms-to-manage-secrets-in-your-infrastructure-fugue
date: 2015-11-29 22:25:49 -0600
category: 
external-url: https://blog.fugue.co/2015-04-21-aws-kms-secrets.html
hash: a89386eb5a3837c25459b4fc8e150844
year: 2015
month: 11
scheme: https
host: blog.fugue.co
path: /2015-04-21-aws-kms-secrets.html

---

The new KMS service provides HSM-style key management that is both inexpensive and easy to use via a web service API. First, we'll look at what KMS is and how you can use it to manage encryption keys. Then, we'll look at credstash, a simple system that uses KMS and DynamoDB to safely store, distribute, and manage credentials in the cloud.
