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

Link Thing is also a large database of {{ site.posts | size }} links! If you are curious to play with this database and so some analysis I also make the entire database easily downloadable.

The CSV file is the easiest to put into any spreadsheet and do quick analysis.

CSV: [{{ site.url }}{% link feeds/links.csv %}]({{ site.url }}{% link feeds/links.csv %})

If you would rather work with JSON there is also a JSON file that has all links in it.

JSON: [{{ site.url }}{% link feeds/links.json %}]({{ site.url }}{% link feeds/links.json %})

Lastly there is also an OPML file with all links outlined by year and month.

OPML: [{{ site.url }}{% link feeds/links.opml %}]({{ site.url }}{% link feeds/links.opml %})

### Validation

Convenience links to validate the feeds.

- [RSS](https://validator.w3.org/feed/check.cgi?url=https%3A//links.thingelstad.com/feeds/feed.xml)
- [JSON](https://validator.jsonfeed.org/?url=https%3A%2F%2Flinks.thingelstad.com%2Ffeeds%2Ffeed.json)
- [ICS (icalendar.org)](https://icalendar.org/validator.html?url=https://links.thingelstad.com/feeds/feed.ics)
- [ICS (iCal4j)](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Flinks.thingelstad.com%2Ffeeds%2Ffeed.ics)

