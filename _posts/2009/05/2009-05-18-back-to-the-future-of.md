---
title: "[Back to] The Future of Typography - Presentation Notes"
date: 2009-05-18 03:36:07 +0000
external-url: http://kernest.com/blog/archive/back-to-the-future-of-typography-presentation-notes
hash: 6cde0ee6b39c467be35eef87b6a859a4
annum:
    year: 2009
    month: 05
url-parts:
    scheme: http
    host: kernest.com
    path: /blog/archive/back-to-the-future-of-typography-presentation-notes

---

I just talked with the UofMN’s Web Standards Workgroup about @font-face. Rather than load up a context-less, frozen, presentation, here are my notes.

Fonts are how we express emotion, identity, and personality, visually in text. 

As part of their  2002 print edition redesign the Wall Street Journal redrew 2 of their typefaces; WSJ Scotch Condensed, Franklin Gothic, and added a third - Retina - to the mix. Maintaining the WSJ brand in how news and information is presented.

When WSJ redesigned the online edition in 2008 they, like everyone of us, chose; Georgia, Arial, and Times New Roman. 

The distinction, differentiation, and identity offline designers strive for falls completely apart online when the ability to specify the fonts online in a meaningful way.

We’ve had the technology to support this for 12 years - since 1997.

When Netscape 4 supported TrueDoc and Internet Explorer 4 supported EOT.

Netscape dropped TrueDoc support when it went open-source.

Microsoft.com hasn’t updated their Web Embedding Fonts Tool to create .eot files since 2003.

So, in the mean time, web designers have restricted themselves to the 12 Core fonts for the Web. Another now defunct project containing classic fonts - the most contemporary of which is the 12 year old - Webdings. 

Have we not found new ways of expressing ourselves within the past 12 years?

As of CSS3 - the @font-face declaration is officially a standard way of specifying fonts for used within web pages. 

EXAMPLE

@font-face {
  font-family:‘Fotin-Regular’;
  src: url(‘/fotin.otf’);
}

p {
  font-family:‘Fotin-Regular’;
  font-size: 3.2em;
  letter-spacing: 1px;
  text-align: center;
}


BROWSER SUPPORT
Safari 3+ (current)
Internet Explorer v4+ (still via .eot files)
Firefox 3.5 (expected after Jun 2009)
Opera v10 

EOT was submitted to the W3C in March of 2008. It contains 6 DRM keys. 

EXAMPLES OF @FONT-FACE IN THE WILD
Jon Tan’s @font-face test with Fontin Regular
ElliottCable.name
Richard Rutter’s Clagnut

EMBED-ABLE FONTS
Exljbris Font Foundry
Webfonts.info Wiki Page: Fonts Available for font-face embedding

