---
layout: default
title: Feeds and Data
---

## Feeds

Link Thing provides feeds that allow you to subscribe to new posts in whatever way you wish. You can subscribe using RSS or JSON feeds.

RSS: [{{ site.url }}{% link feeds/feed.xml %}]({{ site.url }}{% link feeds/feed.xml %})

JSON: [{{ site.url }}{% link feeds/feed.json %}]({{ site.url }}{% link feeds/feed.json %})

There is also an iCalendar file that you can subscribe to using your calendar and see links on your calendar.

ICS: [{{ site.url }}{% link feeds/feed.ics %}]({{ site.url }}{% link feeds/feed.ics %})

## Full Archive

Link Thing is also a large database of {{ site.posts | size }} links! If you are curious to play with this database and so some analysis you can easily download the entire dataset.

The CSV file is the easiest to put into any spreadsheet and do quick analysis.

CSV: [{{ site.url }}{% link feeds/links.csv %}]({{ site.url }}{% link feeds/links.csv %})

If you would like to use standard RSS there is a full archive of all links in RSS format. This file is the only one that contains the body content for each link.

RSS: [{{ site.url }}{% link feeds/links.xml %}]({{ site.url }}{% link feeds/links.xml %})

If you would rather work with JSON there are multiple options. There is a JSON file that is a straight list of all posts in a reduced JSON Feed structure as well as a JSON file that is divided by hosts.

JSON (array): [{{ site.url }}{% link feeds/links.json %}]({{ site.url }}{% link feeds/links.json %})

JSON (host): [{{ site.url }}{% link feeds/links-by-host.json %}]({{ site.url }}{% link feeds/links-by-host.json %})

### Validation

Convenience links to validate the feeds.

- [RSS](https://validator.w3.org/feed/check.cgi?url=https%3A//links.thingelstad.com/feeds/feed.xml)
- [JSON](https://validator.jsonfeed.org/?url=https%3A%2F%2Flinks.thingelstad.com%2Ffeeds%2Ffeed.json)
- [ICS (icalendar.org)](https://icalendar.org/validator.html?url=https://links.thingelstad.com/feeds/feed.ics)
- [ICS (iCal4j)](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Flinks.thingelstad.com%2Ffeeds%2Ffeed.ics)

