---
title: "Type rendering: operating systems"
date: 2010-10-15 15:16:22 +0000
external-url: http://blog.typekit.com/2010/10/15/type-rendering-operating-systems/
hash: 46d058f7a8bd0b744eb31dbee7395171
annum:
    year: 2010
    month: 10
hostname: blog.typekit.com
---

This is our second post in an ongoing series about type rendering on the web. Read the first and third posts.

As we dig into type rendering on the web, we’ll begin by looking at text rendering engines. We are all familiar with operating systems like Windows and Mac OS X, but within each OS are smaller, specialized components available for use by applications like web browsers. APIs such as Core Text on Mac OS X, and DirectWrite and GDI on Windows, are examples of these components and are responsible for rasterizing fonts’ vector outlines. Let’s examine screenshots of web type as rendered by each of these APIs, and talk about the application independence of rendering engines.



The screenshots below were taken by visiting this test page that features two Typekit fonts, FacitWeb and Minion Pro. FacitWeb, occupying the top row of each screenshot, has a 120px capital R, a 21px subhead, and 12px text. Minion Pro, across the bottom of each screenshot, has a 130px capital R, a 24px subhead, and 14px text. The detail images are zoomed to 300%.

Core Text
Core Text is a rendering engine available on Mac OS X and iOS. In fact, it’s part of a suite of APIs called Core Foundation that underlies much of the slick interaction and glossiness for which Apple user interfaces are loved. It’s no surprise that Apple-rendered text reflects this same slickness, some would argue to the detriment of legibility. Core Text type tends to respect a typeface’s designed shape, which essentially means thicker letters (rather than pixel grid strictness). This can make letters, as well as spaces within and among letters, seem blurry at paragraph sizes. However, at very large sizes Core Text type looks natural and smooth. Part of its success at large sizes has to do with y-direction antialiasing, which is especially noticeable in the subtle curves of large letters — compare the detail images of Core Text’s capital R with those of GDI, which does not antialias vertically.


Above: Core Text rendering of FacitWeb (above) and Minion Pro (below).

Look closely at the detail images and you’ll notice that some pixels are tinted with color. This is called sub-pixel antialiasing, which uses the vertically-oriented thirds of red, green, and blue light within each pixel of an LCD screen to effectively triple the horizontal resolution of text. At reading distance from the screen, our eyes cease to notice colored sub-pixels and we instead see sharper text than we otherwise would. Or at least, that’s the idea. For some folks, the sub-pixels are always noticeable and this amounts to an annoying color fringe effect on the edges of letters.

DirectWrite
If Apple sub-pixel antialiased text is true to typeface design at the expense of some blurriness, Microsoft sub-pixel antialiased text is crisp and legible at the expense of style (and at the cost of many font production hours, but we’ll get to that in a future post). As Joel Spolsky once noted, there is a philosophical difference between the two companies’ approaches, and this is evident as we compare Apple’s Core Text to Microsoft’s DirectWrite.


Above: DirectWrite rendering of FacitWeb (above) and Minion Pro (below).

DirectWrite, the latest and greatest text rendering engine for Windows, is available on Windows 7 and Windows Vista. It is markedly clearer, smoother, and has less intense color fringing than Core Text and older Windows text rendering engines. As with Core Text, there is y-direction antialiasing for smooth curves. (Compare, however, the bottom edges of paragraph text in DirectWrite with those of Core Text; Both engines use y-direction antialiasing, but Core Text’s closer adherence to actual glyph outlines translates to subtle antialiasing smudges below the baseline. Microsoft engines clean this up.) And as with Core Text, sub-pixels in DirectWrite are used not only to antialias text but also to space letters horizontally, which means letters can sit more naturally next to one another than in Microsoft’s older text rendering engine, GDI.

Graphics Device Interface (GDI)
The GDI text rendering engine, available on Windows 7, Windows Vista, and Windows XP, actually comes in two flavors: GDI and GDI+. GDI+ is superior and has been included with Windows since XP, so when I talk about GDI here I’m actually referring to GDI+. Another bit of disambiguation: text rendering engines like GDI and DirectWrite both use, but are paradigmatically different than, the sub-pixel antialiasing algorithm ClearType. Antialiasing is just one function of text rendering engines, which are also responsible for Unicode mapping, OpenType features, and integration with other APIs like web browser layout engines.

In keeping with another philosophical difference between Apple and Microsoft, Windows operating systems provide users with several antialiasing preferences from which to choose: ClearType (sub-pixel antialiasing), Standard (grayscale antialiasing), or no antialiasing (black and white text without any smoothness). By default, ClearType is enabled in Windows 7 and Windows Vista, and Standard is enabled in Windows XP. We’ll revisit these preferences in our next post about web browsers, some of which have their own font smoothing options.

GDI with ClearType antialiasing enabled

Above: GDI rendering of FacitWeb (above) and Minion Pro (below) with ClearType enabled.

As you see here, and as most Windows 7 and Windows Vista users see when they browse the web, GDI-rendered type with ClearType enabled – unlike DirectWrite or Core Text – does not antialias text in the y-direction. Note the abrupt, staircase-like curves in the capital R detail. This text also exhibits sub-pixel antialiasing with significant color fringing, perhaps because this early breed of the ClearType algorithm had yet to be refined.

There are different versions of ClearType, just as there are different Windows rendering engines and different web browsers. These nested components evolve independently, but the latest version of each may not be present in a given web browsing experience. For example, a version of ClearType with y-direction antialiasing, similar to what we see in DirectWrite, was available via another Windows API called Windows Presentation Foundation (WPF). But because no version of Internet Explorer made proper use of WPF, web text viewed with a Windows browser has traditionally lacked y-direction antialiasing.

GDI with Standard antialiasing enabled

Above: GDI rendering of FacitWeb (above) and Minion Pro (below) with Standard antialiasing.

You wouldn’t know it by our survey of text rendering engines thus far, but there was a time when sub-pixel antialiasing was not the most common means of smoothing fonts on screens. Windows Standard antialiasing is in good ol’ grayscale. This is how most Windows XP users see type on the web (unless they browse with Internet Explorer 7 or 8, but we’ll get to that later!), and how most users with CRT monitors see type as well (LCD-based sub-pixel antialiasing doesn’t work when there are no sub-pixels).

Grayscale antialiasing adjusts whole pixels at once, doing its best to approximate the partial presence of a letterform by showing a solid gray representation of the two-dimensional area consumed by the shape’s overlap upon a given pixel. Grayscale text is not sharp enough to be very legible and, combined with Windows’ philosophical preference for snapping to pixel edges, does not adhere to the design of a particular typeface very well.

GDI with no antialiasing

Above: GDI rendering of FacitWeb (above) and Minion Pro (below) with no antialiasing.

While rare because it is not the default choice on any modern Windows OS, aliased text (that is, text without any kind of antialiasing) is what some folks see as they read web text. The most common reasons type is rendered this way are because the user (or computer’s administrator) prefers this style of text rendering and has adjusted the OS antialiasing settings, or because a particular setting within the font file has explicitly disabled antialiasing for the specific font size being used. We’ll talk more about this setting in a future post about font files.

Screenshot review
Here again are each of the screenshots. For extra fun, try opening each image in a new tab and flipping quickly among them.


Above: Core Text rendering of FacitWeb (above) and Minion Pro (below).


Above: DirectWrite rendering of FacitWeb (above) and Minion Pro (below).


Above: GDI rendering of FacitWeb (above) and Minion Pro (below) with ClearType enabled.


Above: GDI rendering of FacitWeb (above) and Minion Pro (below) with Standard antialiasing.


Above: GDI rendering of FacitWeb (above) and Minion Pro (below) with no antialiasing.

In summary, most people reading text on the web view type in one of these five ways. Mac OS X users see Core Text, Windows 7 and Windows Vista users see either DirectWrite or GDI, and Windows XP users see GDI. For now, I have not included details about Linux or Android OS. (If you have any good references for how web browsers on these platforms render text, please link them up in the comments!) But as we will see in future posts, preferences, web browsers, font formats, and CSS properties may each affect the way type is rendered on the web.

         
