---
title: "Weblog Tools Collection: Ian Stewart On Child Themes - Part 1"
date: 2008-10-04 17:30:05 +0000
external-url: http://weblogtoolscollection.com/?p=4273
hash: 321f7435acc40b94dcfce7334a564176
year: 2008
month: 10
scheme: http
host: weblogtoolscollection.com
path: /
query:
    p: "4273"
---

Child themes are a trend which appears to be gaining traction everywhere you look. Theme authors such as Ian Stewart, Justin Tadlock and Darren Hoyt are just a few of the influential people pushing this concept. In order to try and grasp an understanding of child themes, I interviewed Ian Stewart of Themeshaper.com. His responses were so long, this interview will end up being published in two parts. Here is part 1.

1. First off, could you please explain what Child themes are in the simplest way possible?

A Child Theme is a WordPress theme that installs and activates just like any other WordPress theme—with 2 crucial differences. Firstly, it requires no PHP template files of it’s own to work. That’s because it uses the template files of a defined Parent Theme. The Parent Theme must be installed—but not activated—in your blog’s themes directory for the Child Theme to work.

Secondly, as of WordPress 2.7, template files located in your Child Theme folder will be used instead of the template file in your Parent Theme folder. Don’t like how the header is coded up for a particular theme you want to edit? Copy the header.php file from your Parent theme into your Child Theme folder and make the change there. WordPress, as of 2.7, will look for header.php (or any possible template file) in the Child Theme first and use the Child Theme template file instead. This new feature in WordPress 2.7 makes custom theming really exciting and even easier.

It’s really very simple to make your own Child Theme. So simple, I can tell you and your readers how to do it right here in four ridiculously easy steps. It’ll help you get your head around using a Child Theme if you follow along (with a test blog—this’ll be easy but our test theme isn’t going to be pretty).

1. Make a folder in your blog themes directory called “achildthemetest”.

2. Create a “style.css” file in that folder with the following code copy-pasted into that “style.css” file.

/*
Theme Name: A Child Theme Test
Theme URI:
Description: Trying out a Child Theme with the classic theme
Author:
Author URI:
Template: classic
Version:
*/

/*
For the sake of simplicity we're going to import
the classic stylesheet and override the styles.
You don't have to do this though. You can just
start fresh with new CSS or copy over large chunks of
the original styles and edit them here.
*/
@import url(../classic/style.css);

/*
Now, for a demonstration, let's make all the anchors red.
*/
a {
color:red;
}
3. Refresh your blog’s theme directory in the WordPress admin. You should see a theme called “A Child Theme Test”. It’s using the classic theme as a Parent Theme. If you look at the code  above you should see a line that starts with “Template” it’s there that we defined that Parent Theme as “classic”, the folder name of our Parent Theme (which could be any installed theme).

4. Activate your new Child Theme and check out your blog. Are all the links in the main content area red? Congratulations. You just made a WordPress Child Theme. You can now edit your WordPress theme of choice—in this instance, the Classic theme—through CSS alone without having to modify any of the original template files. (If you’re a more advanced WordPress developer you can also include a functions.php file in your Child Theme that lets you interact with WordPress and your themes just like a plugin. But that’s another story altogether.)

 2. What are some of the benefits that child themes offer versus stand alone themes?

There’s 2 main benefits for the end user when it comes to using a Child Theme versus editing a theme directly: Simplicity and Upgrade-readiness. To explain, I’ll tell you why I use a Child Theme of my own theme, Thematic, on ThemeShaper.com. That’s right, I’m not even editing my own theme directly on my own WordPress Theme blog.

Firstly, it really is just simpler. I currently have only 2 files in my Child Theme folder: style.css and functions.php. Everything else is coming from the same Thematic template files anyone can download and use. When I want to change the look of my theme, I do it in style.css. If I want to get really serious with theme changes, like, plugin-serious, I write some simple code in functions.php. I don’t think about my Parent Theme and, excepting the XHTML it eventually outputs and displays in my browser, I don’t even look at it. Except! Except when it comes time to upgrade.

When I need to upgrade Thematic, my Parent Theme, I can do so without worries. That’s because I haven’t touched the original template files. I haven’t edited the header. I haven’t edited the footer. I haven’t edited single.php. Or index.php. All my theme edits have been made in the stylesheet and functions file of my Child Theme.

Look at it this way: I have another blog I manage with a really fresh and distinctive design that I get compliments on all the time. Unfortunately, I made that design by hacking up and heavily modifying The Sandbox version 0.6. If I wanted to upgrade to a newer version of The Sandbox I’d have to recreate that design. That means I’d have to pull the theme apart, find all my changes, and reintegrate it with a newer version of the theme. If I’d made the modifications in a Child Theme upgrading would mean uploading a newer version of The Sandbox and, well, that’s it really. How long does it take to upload a theme? 10 seconds? When you’re using a Child Theme, upgrading turns from a day long affair into a 10 second chore that can be done while you’re reading weblogtoolscollection.com.

 3. Based on what I’ve seen, the child theme trend is really starting to gain traction thanks in large part to you and other theme designers. How long has the ability to develop child themes been available for WordPress? If it’s been available to develop for some time now, why is it that we are only now starting to see heavy development in this area?

As far as I can tell, Child Themes have been available since version 2.1. But I first heard about Child Themes when I entered the Sandbox Designs Competition (http://sndbx.org/). Every entry there is a Child Theme that defines The Sandbox as it’s Parent Theme and modifies the theme with CSS alone. Consequently, I think a lot of the credit for popularizing Child Themes needs to go to Scott Wallick (http://www.plaintxt.org/), co-creator of The Sandbox and organizer of the Sandbox Designs Competition.

But that brings us to why I don’t think there’s been much talk about Child Themes: I think there’s sort of a lack of faith amongst theme authors and users when it comes to what you can actually do with CSS. WordPress developer and theme author Ben Eastaugh thinks that “one reason it hasn’t been more widely publicized is that [modifying Parent Themes with CSS] wasn’t, as it stood, terribly useful” (http://extralogical.net/2008/08/theme-inheritance/). I’d disagree with that in principle but that sort of sums up the feeling of theme authors that have been ignoring this feature.

And, by the way, if you don’t think Child Themes can really do anything with CSS alone make sure you check out the winning entries in The Sandbox Designs competition (http://sndbx.org/results/) or the oft-mentioned and linked to CSS Zen Garden (http://www.csszengarden.com/).

But regardless of what you think you can do with CSS alone, now that WordPress 2.7 let’s you overwrite Parent template files from your Child Theme I expect we’ll be seeing more and more people using them.

Plus, there’s a few other WordPress developments in the works that’ll likely further popularize this method of theme modifying. Namely, the WordPress.com Themes Marketplace and allowing GPL Child Themes to be released through the WordPress Theme Directory.

4. Before we move on, could you explain what a theme framework is? Perhaps providing a few examples for the readers.

In my mind, a Theme Framework would be a theme that, at the very least, was made with clear intentions of being used to develop further themes. A starting point theme if you will.  I think a good Theme Framework also shows consideration of, or planning for, what can be done with Child Themes, now and in WordPress 2.7+. And that’s because, really, you shouldn’t be touching a framework if you can help it.

Think of WordPress as a framework where the contents of the database are output in a controlled fashion by your theme. We don’t go in and tinker with the WordPress core in order to make our themes work better (well, some people do but that’s another story again). The same thing with a theme framework. We can modify the theme framework with our Child Themes and leave the framework pristine for easy, safe upgrades.

This concludes part 1 of the interview. Stay tuned for Part 2 which will be arriving shortly.

