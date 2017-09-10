---
title: "Backing up a MediaWiki wiki"
date: 2012-06-16 00:47:56 +0000
external-url: http://www.mediawiki.org/wiki/Manual:Backing_up_a_wiki
hash: e321d1691fdbec6ca920681a86bea8d0
year: 2012
month: 06
scheme: http
host: www.mediawiki.org
path: /wiki/Manual:Backing_up_a_wiki

---

Invoking the dumpBackup.php via cron and storing the resulting XML some place safe seems like a good failsafe to making sure you don't lose your data.

<blockquote>
To create an XML dump, use the command-line tool dumpBackup.php, located in the maintenance directory of your MediaWiki installation. Run the command as phpdumpBackup.php without any arguments to display a brief description of the syntax. You need to specify whether you want a full dump of the complete history of every page, or just the current contents of each page. Prior to MediaWiki 1.16: If an attempt to use dumpBackup.php fails with a message about insufficient permissions, ensure that you have a properly configured AdminSettings.php file. Instructions on creating the file are at Manual:AdminSettings.php.
</blockquote>

