---
layout: default
title: Feeds and Data
---

## Feeds

Link Thing provides feeds that allow you to subscribe to new posts in whatever way you wish. You can subscribe using RSS or JSON feeds.

RSS: [{{ site.url }}{% link feeds/feed.xml %}]({{ site.url }}{% link feeds/feed.xml %})

JSON: [{{ site.url }}{% link feeds/feed.json %}]({{ site.url }}{% link feeds/feed.json %})

## Full Archive

Link Thing is also a large database of {{ site.posts | size }} links! If you are curious to play with this database and so some analysis I also make the entire database easily downloadable.

The CSV file is the easiest to put into any spreadsheet and do quick analysis.

CSV: [{{ site.url }}{% link feeds/links.csv %}]({{ site.url }}{% link feeds/links.csv %})

If you would rather work with JSON there is also a JSON file that has all links in it.

JSON: [{{ site.url }}{% link feeds/links.json %}]({{ site.url }}{% link feeds/links.json %})
