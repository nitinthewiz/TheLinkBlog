---
title: "United Airlines Bankruptcy and Newsbots"
date: 2008-09-12 03:13:03 +0000
external-url: http://www.grouplens.org/node/259
hash: b1867bf1636845595e7e6d35bd815bfc
year: 2008
month: 09
scheme: http
host: www.grouplens.org
path: /node/259

---

There's a very interesting story on Hot Hardware (of all places) about how two news robots interacted to help kickoff the (false!) rumor that UAL was going bankrupt, leading to a huge selloff in the stock.  Apparently the news bot for a newspaper moved the story to the front page because someone read it during a "low news time" -- during which even a single read was a lot.  Google News saw the story on the page, and picked the date up from the top of the page, since there was no date on the article.  This date was the current date, not the six years ago date of the original story.  An analyst saw the story on Google News, and a billion $ later, the rest was history.

As a recommender researcher, the scariest part of the story is the inference drawn from that single view of the article, which looked at the time -- in the wee hours -- like a statistically significant indicator that the article was becoming interesting.  This problem reoccurs in recommenders all the time: if we're looking to make recommendations of items that are not popular, we'll often be recommending based on not very much data.  

John

