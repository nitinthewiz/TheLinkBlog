---
title: "EPUBReader Displays EPUBs in Firefox"
date: 2010-09-11 03:54:32 +0000
external-url: http://tidbits.com/article/11590?rss=
hash: 60c9c42637ac01cce6da8fa14a2e3f33
---

With Apple's release of the iBooks app and the iBookstore, EPUB-formatted ebooks have become increasingly prevalent. Surprisingly, though, there aren't many good ways to read an EPUB other than iBooks, especially if all you want is a quick look on your Mac.
 
 
O'Reilly Labs hosts Threepress's online Bookworm service, but it requires uploading a book and storing it online, which may be more effort than you want to go to. There's also a cross-platform, open-source application called Calibre that can convert and display EPUBs, but it's clunky and awkward to use. And there's a version of Stanza for the Mac, but unlike the Stanza iOS app, the Mac version strips all formatting and graphics from an EPUB, rendering some titles unreadable. Lastly, there's Adobe Digital Editions, an Adobe AIR-based application 
that's designed in part to help deal with DRM-protected ebook files across multiple machines; it's not terrible, but I'm not a big fan.
 
 
So I was happy to run across EPUBReader, a free add-on for the Firefox Web browser (whether running on the Mac, Windows, or Linux). Although most Firefox add-ons modify the Web experience in some way, EPUBReader simply takes advantage of Firefox's rendering engine to provide a custom display of an EPUB's contents within a Firefox window or tab. (Remember, EPUB files are XHTML inside of a Zip archive.) 
 
 
To install EPUBReader in Firefox, click the Add to Firefox button on the EPUBReader home page; you'll have to restart Firefox to complete the installation.
 
 
EPUBReader also tweaks Firefox's settings so clicking a .epub file on a Web page downloads it, processes it, and displays it. You can also drop a local EPUB file on Firefox's window, or double-click one, if you change the Open With application for .epub to Firefox in an EPUB's Get Info window. 
 
 
Unlike downloaded PDF files that you view in a Web browser and then "lose" once you close the tab containing the file, EPUBReader keeps every downloaded or displayed PDF in local storage called ePub-Catalog, which you can access from the Tools menu, the Bookmarks menu (at the bottom of the list), or via a button at the bottom of any EPUB you're reading. Even better, the ePub-Catalog window has a pop-up menu listing a few sites from which you can download additional EPUB-formatted titles.
 
 


Once you have an EPUB open within EPUBReader, the mechanics of reading it are nicely obvious. The table of contents appears in a resizable pane on the left side of the window and the actual book appears in the right side. Clicking an item in the table of contents displays the associated content on the 
right, and if there are navigation links within the content, clicking them moves you around in the text as well.
 
 

Most EPUBs will have their own formatting, specified by internal CSS files, but if you prefer, you can modify a number of display options in EPUBReader's preferences. In the table of contents, you can set the background and link colors, along with font and font size. The same background color and font options are available for the content, along with margin width and minimum column width. And if you just want to change the font size, a pair of buttons are available for increasing and decreasing size. (Oddly, Firefox's Zoom 
In command also works for increasing the size of all the text - table of contents and the actual book text. But the Zoom Out command works only on the book content pane unless you first click in the table of contents pane.)
 
 
Other buttons let you access the ePub-Catalog window, save the file to a separate location on your hard disk, and set a bookmark (although I couldn't figure out how the boomark feature worked). Finally, a pair of big green buttons let you jump to the previous and next chapters. All of these commands are also available as keyboard shortcuts (Control-click the toolbar to access a menu that lets you display the keyboard shortcuts; you can also hide the toolbar entirely this way).
 
 
There's no question that EPUBReader's interface elements are ugly - no Macintosh developer would be caught dead using such awful buttons - but for normal usage, EPUBReader gets out of the way and just displays an EPUB with a clickable table of contents. And whether I'm checking the EPUB version of one of our Take Control ebooks or taking a quick look at something I've found online or been sent, a quick click or drag to Firefox is all that's necessary to load the EPUB in EPUBReader. 

 
Read and post comments about this article | Tweet this article

WebCrossing Neighbors Creates Private Social NetworksCreate a complete social network with your company or group'sown look. Scalable, extensible and extremely customizable.Take a guided tour today <http://www.webcrossing.com/tour>

 
Copyright © 2010 Adam C. Engst. TidBITS is copyright © 2010 TidBITS Publishing Inc. If you're reading this article on a Web site other than TidBITS.com, please let us know, because if it was republished without attribution, by a commercial site, or in modified form, it violates our Creative Commons License.

