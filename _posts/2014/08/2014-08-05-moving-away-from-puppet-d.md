---
title: "Moving away from puppet: SaltStack or Ansible? - Ryan D Lane"
date: 2014-08-05 15:59:04 +0000
external-url: http://ryandlane.com/blog/2014/08/04/moving-away-from-puppet-saltstack-or-ansible/
hash: 0c544b8a7ebeb6f317a88709699ca5aa
---

Over the past month at Lyft weve been working on porting our infrastructure code away from Puppet. We had some difficulty coming to agreement on whether we wanted to use SaltStack (Salt) or Ansible. We were already using Salt for AWS orchestration, but we were divided on whether Salt or Ansible would be better for configuration management. We decided to settle it the thorough way by implementing the port in both Salt and Ansible, comparing them over multiple criteria.
