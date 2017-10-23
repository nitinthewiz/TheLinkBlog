---
title: "A feature request for blogging tool vendors"
slug: a-feature-request-for-blogging-tool-vendors
date: 2010-12-05 10:32:55 -0600
external-url: http://scripting.com/stories/2010/12/05/aFeatureRequestForBlogging.html
hash: 1fca034de1f08ddc7261e0f416cde5c1
year: 2010
month: 12
scheme: http
host: scripting.com
path: /stories/2010/12/05/aFeatureRequestForBlogging.html

---

I wrote a bunch of web content management tools in the mid-late 90s and early part of the last decade (we still don't have a name for it!) that turned into what we now think of blogging tools. The category that's led by WordPress, Typepad and Blogger (and Posterous and Tumblr and certainly others). 

Along the way a bunch of features fell by the wayside. One of them in particular is so important I'd like to pitch all the vendors of today's blogging tools. If one of them does, I'll put at least a year (Murphy-willing) into developing tools that work with the feature. I think that's a pretty good deal, when you realize how little work the feature will take. 

Here's the deal. You all support the MetaWeblog API. That's great. When I save a blog post using newPost or editPost, allow me to include in the struct a new element called postSource, which contains the source code for the post. This is not executable code like Java or Python or C, its structured text in XML form that the post was rendered from. 

That's the punchline, now here's the background.

There's a lot of power in separating content from the rendering of the content. All of today's blogging tools have that concept to a degree. A series of posts flows through a set of templates and is rendered into a set of pages that are part of the blog website. But the posts themselves don't have the separation. When you write the post you're writing in HTML. For most people, most of the time, that's what they want. But if we have the ability to make tools that have the separation, we can build higher-level, more powerful editors that are also easier. In fact, I already have such an editor. I just can't use it with your blogging environment.

You just have to store the XML text along with the HTML text, and when I getPost, send it back to me. It's a black box you don't have to look into (but you should probably verify that it's just XML and not executable bits).

