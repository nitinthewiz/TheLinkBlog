---
title: "Alex King: Fixing a MySQL Character Encoding Mismatch"
date: 2008-03-06 07:13:55 +0000
external-url: http://alexking.org/blog/2008/03/06/mysql-latin1-utf8-conversion
hash: 8a370f73d1a3b1f9261a8416a4f45a5b
---

We ran into an interesting MySQL character encoding issue at Crowd Favorite today while working to upgrade and launch a new client site.

Here is what we were trying to do: copy the production database to the staging database so we could properly configure and test everything before pushing the new site live. Pretty simple right? It was, until we noticed a bunch of weird character encoding issues on the staging site.



It turned out that while the database tables were set to a Latin-1 (latin1), the content that populated those tables was encoded as UTF-8 (utf8). A variety of attempts to fix this failed, but what succeeded was as follows:


Export the data as Latin-1. Because MySQL knows that the table is already using a Latin-1 encoding, it will do a straight export of the data without trying to convert the data to another character set. If you try to export as UTF-8, MySQL appears to attempt to convert the (supposedly) Latin-1 data to UTF-8 - resulting in double encoded characters (since the data was actually already UTF-8).
Change the character set in the exported data file from ‘latin1′ to ‘utf8′. Since the dumped data was not converted during the export process, it’s actually UTF-8 encoded data.
Create your new table as UTF-8 If your CREATE TABLE command is in your SQL dump file, change the character set from ‘latin1′ to ‘utf8′.
Import your data normally. Since you’ve got UTF-8 encoded data in your dump file, the declared character set in the dump file is now UTF-8, and the table you’re importing into is UTF-8, everything will go smoothly.

I can confirm that a half-dozen or so variations on the above do not work. This includes INSERT INTO newdb.newtable SELECT * FROM olddb.oldtable;.

Also, if you’re doing this for a WordPress1 site (like we were), keep in mind that copying over the production database will generally mean that WP-Cache is enabled. You’ll want to remember to turn that off. Yeah.  


This is a fairly common issue in older WordPress installs because the MySQL database default is commonly Latin-1, and older versions of WordPress did not specify the character set when creating the database tables (so they would default to Latin-1) and the default encoding in the WordPress settings is UTF-8. [back]

ShareThis

