---
title: "WordPress 2.9, oh so fine"
date: 2009-12-19 05:44:31 +0000
external-url: http://wordpress.org/development/2009/12/wordpress-2-9/
hash: 94cabe39deab212f833bf08635c6e766
annum:
    year: 2009
    month: 12
hostname: wordpress.org
---

I want to make you mine, all the time… oh wait. Hello. I’m here on behalf of the entire WordPress development team and community to announce the immediate availability of WordPress version 2.9 “Carmen” named in honor of magical jazz vocalist Carmen McRae (whom we’ve added to our Last.fm WP release station). You can upgrade easily from your Dashboard by going to Tools > Upgrade, or you can download from WordPress.org. 

The coolest new stuff from a user point of view is:


Global undo/”trash” feature, which means that if you accidentally delete a post or comment you can bring it back from the grave (i.e., the Trash). This also eliminates those annoying “are you sure” messages we used to have on every delete.
Built-in image editor allows you to crop, edit, rotate, flip, and scale your images to show them who’s boss. This is the first wave of our many planned media-handling improvements.
Batch plugin update and compatibility checking, which means you can update 10 plugins at once, versus having to do multiple clicks for each one, and we’re using the new compatibility data from the plugins directory to give you a better idea of whether your plugins are compatible with new releases of WordPress. This should take the fear and hassle out of upgrading.
Easier video embeds that allow you to just paste a URL on its own line and have it magically turn it into the proper embed code, with Oembed support for YouTube, Daily Motion, Blip.tv, Flickr, Hulu, Viddler, Qik, Revision3, Scribd, Google Video, Photobucket, PollDaddy, and WordPress.tv (and more in the next release).

2.9 provides the smoothest ride yet because of a number of improvements under the hood and more subtle improvements you’ll begin to appreciate once you’ve been around the block a few times. Here’s just a sampling:


We now have rel=canonical support for better SEO.
There is automatic database optimization support, which you can enable in your wp-config.php file by adding define('WP_ALLOW_REPAIR', true);.
Themes can register “post thumbnails” which allow them to attach an image to the post, especially useful for magazine-style themes.
A new commentmeta table that allows arbitrary key/value pairs to be attached to comments, just like posts, so you can now expand greatly what you can do in the comment framework.
Custom post types have been upgraded with better API support so you can juggle more types than just post, page, and attachment. (More of this planned for 3.0.)
You can set custom theme directories, so a plugin can register a theme to be bundled with it or you can have multiple shared theme directories on your server.
We’ve upgraded TinyMCE WYSIWYG editing and Simplepie.
Sidebars can now have descriptions so it’s more obvious what and where they do what they do.
Specify category templates not just by ID, like before, but by slug, which will make it easier for theme developers to do custom things with categories — like post types!
Registration and profiles are now extensible to allow you to collect things more easily, like a user’s Twitter account or any other fields you can imagine.
The XML-RPC API has been extended to allow changing the user registration option. We fixed some Atom API attachment issues.
Create custom galleries with the new include and exclude attributes that allow you to pull attachments from any post, not just the current one.
When you’re editing files in the theme and plugin editors it remembers your location and takes you back to that line after you save. (Thank goodness!!!)
The Press This bookmarklet has been improved and is faster than ever; give it a try for on-the-fly blogging from wherever you are on the internet.
Custom taxonomies are now included in the WXR export file and imported correctly.
Better hooks and filters for excerpts, smilies, HTTP requests, user profiles, author links, taxonomies, SSL support, tag clouds, query_posts and WP_Query

All of this and more is reflected in the over 500 tickets, bugs, and enhancements that WP developers in this release cycle.

This release included code from over 140 contributors, here’s everyone we were able to identify: aaroncampbell (Aaron Campbell), abackstrom (Adam Backstrom), aldenta (John Ford), alexkingorg (Alex King), [amilanov], antonylesuisse (Antony Lesuisse), apeatling (Andy Peatling), apokalyptik (Demitrious Kelly), arena (André Renaut), batmoo (Mohammad Jangda), Ben Dunkle, BenBE1987,  Benjamin Flesch, bookchiq (Sarah Lewis), brianwhite,  c0nstruct,  caesarsgrunt (Caesar Schinas), CalebKniffen (Caleb Kniffen), chrisbliss18,  chrisscott (Chris Scott),  christoph179,  coffee2code (Scott Reilly), [cross country flight], Curioso, davecpage (Dave Page), dcole07 (Dan Cole), dd32 (Dion Hulse), demetris (Δημήτρης Κίκιζας), Denis-de-Bernardy, dj-wp,  dwright,  eddieringle (Eddie Ringle), error (Michael Hampton), ewestp,  fabifott,  filosofo (Austin Matzko), greenshady (Justin Tadlock), gsnedders/link92 (Geoffrey Sneddon), hailin (Hailin Wu), hakre,  hanilovesme,  Harald Nesland, harrym,  holizz (Tom Adams), ikonst,  jacobsantos (Jacob Santos), janeforshort (Jane Wells), jamescollins (James Collins), jdub (Jeff Waugh), jeff_ (Jean-François “Jeff” VIAL), jeremyclarke (Jeremy Clarke), JeremyVisser (Jeremy Visser), jikamens,  jmulley,  Joern_W,  johanee (Johan Eenfeldt), johnbillion (John Blackbourn), johnjamesjacoby (John James Jacoby), johnjosephbachir (John Joseph Bachir),  JonathanRogers,  joostdevalk (Joost de Valk), Jose Carlos Norte, josephscott (Joseph Scott), junsuijin, kevinB (Kevin Behrens), kometbomb, lilyfan (IKEDA Yuriko), [lostinlafayette], madhyde,  MattyRob, mdawaffe (Michael Adams), Mittineague, miqrogroove, morfiusx,  mrmist (David McFarlane), mtdewvirus (Nick Momrik), mysz, nacin (Andrew Nacin), nanochrome, nao (Naoko  McCracken), nathanrice (Nathan Rice), nbachiyski (Николай Бачийски), niallkennedy (Niall Kennedy), nickohrn (Nick Ohrn), ninjaWR (Ryan Murphy), noel (Noël Jackson), Otto42 (Samuel Wood), pairg, peaceablewhale (Franklin Tse), prettyboymp (Michael Pretty), ProDevStudio, ramiy, redsweater (Daniel Jalkut), ruslany, sambauers (Sam Bauers), scribu, Sewar,  Simek,  simonwheatley (Simon Wheatley), sirzooro (Daniel Frużyński), sivel (Matt Martz), skeltoac (Andy Skelton), snakefoot, stephanreiter (Stephan Reiter), strider72 (Stephen Rider), taco1991,  takayukister (Takayuki Miyoshi), tellyworth, tenpura,  usermrpapa,  utkarsh,  Viper007Bond, vladimir_kolesnikov (Vladimir Kolesnikov), VoxPelli (Pelle Wessman), [voyou1], wahgnube, waltervos, westonruter (Weston Ruter), wnorris (Will Norris), xenlab (Eric Marden), yoavf (Yoav Farhi). Wowza!

2.9 has been an exciting development cycle, and I must say it has whetted our appetite for 3.0, which is coming next (probably this spring) and will include at the very least the merge of MU with the WordPress core, and a new default theme. We can’t wait to start working on it. But first, some Carmen McRae tunes and a beer. Join us!  

(After you upgrade, of course!)

