---
title: "LaunchBar 5.0.1 Runs on Snow Leopard, Adds Clipboard History"
slug: launchbar-5-0-1-runs-on-snow-leopard-adds-clipboard-history
date: 2009-10-20 19:36:20 -0500
external-url: http://tidbits.com/article/10662
hash: 9a4fed9acb92655d19dc1d9b025fbd22
year: 2009
month: 10
scheme: http
host: tidbits.com
path: /article/10662

---

Any reader of TidBITS or my Take Control books is probably aware that I couldn't live without LaunchBar, from Objective Development Software. (See, for example, "Curing Your LaunchBar Addiction," 6 August 2007, or "Take Control of Exploring & Customizing Snow Leopard".) LaunchBar is so crucial to my moment-by-moment Mac usage that I can barely tolerate a Mac that lacks it; I just sit there, slack-jawed, inert, unable to proceed and get anything done. Naturally, in the run-up to Snow Leopard, I was concerned over whether my LaunchBar dependency would be rudely interrupted. But, no problem: LaunchBar 5, which had been 
available as a beta since December 2008, was already in "release candidate" form, and I happily started using it several months ago.
 
 
On 20 October 2009, LaunchBar 5.0.1 was released. Despite the ".1" designation, this marks LaunchBar's emergence from its "release candidate" phase; so, since we at TidBITS generally prefer to keep silent about betas and other unfinished software, this release is my earliest opportunity to discuss LaunchBar 5, the first official version compatible with Snow Leopard.
 
 
LaunchBar is one of those utilities I'd describe as massively explorable: it has far more features than I'm truly familiar with. In fact, I use it actively in a surprisingly limited set of ways. So instead of trying to list everything that LaunchBar can do - which you can explore for yourself, by downloading LaunchBar or by reading its documentation online - I thought I'd let you peek over my shoulder and watch how I actually use it.
 
 
First, a few introductory words about what LaunchBar is. Periodically, LaunchBar indexes certain resources on your hard disk, such as your applications, preference panes, browser bookmarks and history, and services (you can configure what it indexes and how often); it also has some built-in actions of its own. LaunchBar is effectively invisible until you summon it with its hot-key shortcut. By default, that's Command-Space, but I've changed it to Control-Space on my machines. When you summon LaunchBar, its small bar-shaped window appears just below the menu bar; you can now "talk" to LaunchBar, either by normal typing or with keyboard shortcuts. The "normal typing" is often an abbreviation; LaunchBar is smart about matching 
abbreviations to things in its index, and learns as you use it. When you're done, which you generally signal by pressing Return, LaunchBar recedes into invisibility once again. So my normal interaction is entirely through the keyboard (though LaunchBar does also have some drag-and-drop features) and goes like this: Summon, type, dismiss. This happens quite often: sometimes about once a minute, and occasionally much more frequently. 
 
 
So what precisely am I doing so frequently with LaunchBar? Here's a quick rundown of my most common uses:
 
 
Summon an application. To specify the application, I type its abbreviation. So, to summon TextMate, I say Control-Space, TM, Return; to summon BBEdit, it's Control-Space, BB, Return; and so on. I say "summon" because I use this technique whether or not the application is already running. LaunchBar does have an application switcher - Control-Space, Command-R, and a list of running applications appears - but I find it simpler to ignore entirely the distinction between running and non-running applications. In fact, I use LaunchBar to switch applications more than I use Mac OS X's own Command-Tab switcher, or the Dock, because when I want an application I want it by name, and don't have the time or inclination to search for an 
obscure icon.
 
 
Open a System preference pane. LaunchBar indexes and abbreviates various things besides applications, and among those, preference panes are probably the most important in my daily usage. I open preference panes quite a bit for one reason or another, and for reaching a specific pane quickly, the System Preferences window, or even the System Preferences menu, just doesn't cut it. To open the Sound preference pane, for example, even if System Preferences isn't running, it's Control-Space, SOUND, Return, and kaboom, I'm there.
 
 
Operate on an application. Sorry, that phrase is a bit fuzzy because it has to cover a bunch of stuff I do by starting as if to summon an application but then pressing a keyboard shortcut instead of Return. For example, to see the BBEdit application file on disk, it's Control-Space, BB, Command-Return; to do a Finder Get Info on BBEdit, it's Control-Space, BB, Command-I.
 
 
Open a recent document. This actually falls under the previous paragraph's topic ("operate on an application"), but it's so important to me that it needs special treatment here. LaunchBar associates a document with the application that recently opened it, so I can open a recent document by starting with its application. I love this, because it accords with how I actually think: the Finder's list of recent documents is just a meaningless jumble to me, and switching to an application and looking in its File  >  Open Recent list is clumsy. Instead, to open a document recently opened (say) with BBEdit, it's Control-Space, BB, Right-Arrow. This presents a list of BBEdit's recent documents, which I can navigate with arrow keys or 
by typing an abbreviation; Return opens the selected document (with BBEdit). This feature works only with applications whose recent documents list LaunchBar can actually see, thus excluding some clunkers like Microsoft Word and Excel; but such is life.
 
 
Open a Finder document with a specific application. This was always useful, but has become even more important to me now that Mac OS X has repudiated any creator code-based association between a document and the application that created it (see "Snow Leopard Snubs Document Creator Codes," 6 September 2009). Let's say I'm in the Finder, and I select the document I want to open. Let's say I want to open it with BBEdit. Then it's Control-Space and hold down Control-Space for an extra moment; this is called Instant Send, and means that LaunchBar accepts the selection and awaits further instructions. Those instructions can be a specification for an application. So the whole 
process goes: Control-Space (and hold), BB, Return. That causes the Finder selection to be opened with BBEdit. Mac OS X itself has various ways to tell a document to open with a specific application, but in my view this beats them all. I particularly appreciate this feature when a document is multivalent, such as an HTML file, which can be usefully opened with a text editor for editing or with a browser for viewing.
 
 
Search on the Web. LaunchBar includes a bunch of "search templates", meaning it knows how to submit a word or phrase as a search term to specific search engines. Safari has a Google field, but LaunchBar is like having a Google field, a Wikipedia field, and an eBay field - and more - all rolled into one. When I say Control-Space, G, Return, LaunchBar doesn't vanish; instead, its little bar-shaped window turns into a text field, where I can type a search term and then press Return again. This causes the search term I typed to be sent to Google in my browser. Moreover, this feature works with Instant Send. So if, as not infrequently happens, a friend emails me saying something like, "Hey, check out item 150381062374 in eBay," I 
select "150381062374" directly in that email message and type Control-Space and hold, EB, Return. Effectively, I'm taken straight to that very listing in eBay.
 
 
Delve into clipboard history. Why a clipboard with a memory isn't built into Mac OS X is a mystery to me. I've used various clipboard history utilities in the past, such as CopyPaste and PTHPasteboard; I still appreciate them, and they typically have power clipboard features that LaunchBar lacks. But right now LaunchBar's clipboard history, new in version 5, is plenty good enough for me; in fact, it boasts more features than I actually use. The way I've set it up, I press Shift-Control-Option-Command-V (easier for me to remember than the default Option-Command-Backslash) and LaunchBar displays a list of the last 20 things that got copied to the system clipboard; I select one and 
press Return to paste it into the frontmost application.
 
 
And that, in a nutshell, sums up my typical, constant use of LaunchBar. To be sure, none of this qualifies me as a LaunchBar power user; really, it's almost shameful how few of LaunchBar's capabilities I actively take advantage of. Of the many other things LaunchBar can do, some are beyond my everyday habits, and some I actively dislike. For example, I don't like the feature where you type a URL directly to go to it in your browser, because it doesn't interface with my browser history and bookmarks to offer "smart" suggestions as I type, the way Safari's own address field does. And I really dislike LaunchBar's iTunes browsing interface, because when you navigate in LaunchBar to a song by way of its album and ask to play that 
song, it makes iTunes play the album out of order.
 
 
In general, though, such infelicities don't matter, and neither does my apparently shallow use of LaunchBar. What matters is that I use LaunchBar constantly and automatically, and that my use of LaunchBar makes me nimble where LaunchBar-less users are slow. To switch tasks, I don't need to know where an application lives on disk or what its icon looks like; I don't need to play with the Dock or even the Command-Tab switcher. And LaunchBar's commands, and my frequently used abbreviations, are so ingrained in my fingers, it's almost as though just thinking the application's name brings it frontmost or opens a recent or selected document with it.
 
 
To try this all-but-mindreading utility for yourself, download the 30-day free trial (2.74MB). LaunchBar 5.0.1 is compatible with Mac OS X 10.4 or later, and costs €24 (€9 to upgrade from an earlier version).
 
 

 
Read and post comments about this article | Tweet this article

VMware Fusion. The most seamless way to run Windows on
your Mac. Backed by nearly a decade of proven virtualization
technology. Try VMware Fusion today for only $79.99.
Visit: <http://www.tidbits.com/about/support/vmware-fusion.html>

 
Copyright © 2009 Matt Neuburg. TidBITS is copyright © 2009 TidBITS Publishing Inc. If you're reading this article on a Web site other than TidBITS.com, please let us know, because if it was republished without attribution, by a commercial site, or in modified form, it violates our Creative Commons License.
