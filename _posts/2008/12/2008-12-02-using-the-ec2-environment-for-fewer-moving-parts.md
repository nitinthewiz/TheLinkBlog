---
title: "Using the EC2 environment for fewer moving parts"
date: 2008-12-02 06:37:00 -0600
external-url: http://www.37signals.com/svn/posts/1440-using-the-ec2-environment-for-fewer-moving-parts
hash: 963a4c3375c5ca4186b0dfa55c31f723
year: 2008
month: 12
scheme: http
host: www.37signals.com
path: /svn/posts/1440-using-the-ec2-environment-for-fewer-moving-parts

---

One highlight of Amazon’s EC2 is having a wide range of generally available services to help reduce moving parts.



We store part of our cluster configuration in S3. The server instances pull this configuration and bootstrap from there using a simple set of rake tasks and a server provisioning tool, Sprinkle. You could use SimpleDB for a similar purpose. One could serve as a backup of the other, given their similar APIs. Either way means fewer moving parts.



Another vital EC2 feature is passing arbitrary data to an instance. Many bundled images now automatically execute a blob of text you pass to the instance on boot as a shell script, like those supplied by Alestic. We use this to sync configuration scripts and packages from S3.



While reading Tim Dysinger’s article on using EC2 as a simple DNS, I thought this was a great way to remove the need for an internal DNS server on EC2 for smaller setups. We use a similar technique: specifying a single EC2 Security Group for a host as its identifier. Each server generates its hosts file every minute. Simple, effective and one fewer moving part.



Security groups are useful for describing roles and other identifying information about each host. We use this information to generate Nagios monitoring configuration files. For example, a security group named “role: app” will automatically enable HTTP checks and Passenger memory checks.



All this means less dependence on a centralized configuration server or pushing large sets of commands over SSH manually. While these techniques are effective, they require more moving parts and their own care and maintenance.



As your application’s complexity increases, you’ll thank yourself for the opportunity to reduce the complexity underneath it.

  

