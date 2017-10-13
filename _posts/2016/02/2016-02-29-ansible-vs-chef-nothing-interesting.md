---
title: "Ansible vs Chef · Nothing interesting..."
date: 2016-02-29 16:36:55 +0000
external-url: http://tjheeta.github.io/2015/04/15/ansible-vs-chef/
hash: 70245037f64f32bbc1ec2f8028dfd50b
year: 2016
month: 02
scheme: http
host: tjheeta.github.io
path: /2015/04/15/ansible-vs-chef/

---

I wrote an earlier post about evaluating Ansible as an alternative to Chef. So after spending many years with Chef, I’ve found that Ansible is a lot easier to manage with startups. It’s easier to train developers, it’s easier to manage inventory and orchestration, and it works reasonably well on the scale of thousands of hosts. And less face it, if you have more than that, you’ll have to start partitioning. If you’re using Puppet, you’ll have multiple puppet masters, I’m assuming the same with Salt. For Chef, there’s the enterprise offering which gets pretty expensive and then you’ll have to deal with a slow search, so invariably there’s some usage of chef-solo going on and some self-configuration. But for most use cases, Ansible is just fine and is quick to both setup and is ridiculously easy to maintain. This is a fairly advanced post comparing Chef to Ansible and the patterns that are available.
