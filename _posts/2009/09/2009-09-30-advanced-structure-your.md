---
title: "Advanced: Structure Your Account With Roll Up Reporting And More"
date: 2009-09-30 04:30:27 +0000
external-url: http://analytics.blogspot.com/2009/09/advanced-structure-your-account-with.html
hash: 8ecfe64a9e715d074c0a33596738982c
annum:
    year: 2009
    month: 09
url-parts:
    scheme: http
    host: analytics.blogspot.com
    path: /2009/09/advanced-structure-your-account-with.html

---

Guest post by the team at E-Nor, a Google Analytics Authorized ConsultantFor the analytics ninjas out there, you know that data accuracy is probably one of the most challenging aspects of analytics across all solutions and platforms, and you learn to apply best practices and establish processes to improve data collection and reporting. But for the rest of us, how do we help marketers, business owners, and webmasters have confidence in their data? Analytics is all about clarity. It should help you see actionable statistics clearly and quickly. However, when you have a website structure with multiple domains and subdomains - which is often the case - sometimes things can get jumbled. For instance, you are a CMO or a Director of Marketing at the enterprise and you are responsible for the performance and ROI of a large number of web proprieties. You look at your analytics reports and you can't find your ecommerce data from site A, site B is referring traffic to itself (definitely not a good thing!), and conversion data from your marketing campaign microsite is no where to be found.This image sums up the feeling.No need to panic. This post aims to offer an approach to help you plan your Google Analytics accounts setup in a structured fashion to help with clarity. I hope that by following the approach and the technical steps, you will be able to collect and manage all your data, make more sense of it, and most importantly, ensure what you are reporting on, trending, dashboarding and analyzing is based on accurate data.There are two distinct sections of this post:
The Strategy (non-technical)The How (technical)The StrategyThere are many ways to structure your Google Analytics profiles when you have multiple domains and subdomains. But in this post I will limit myself to the one that I like the most and I believe is the least confusing.Before I go into details of the solution, and for simplification, let us assume we are dealing with a project that has the following requirements:A business with 3 domains (www.a.com, www.b.com, and www.c.com)1 domain (a.com) links to a 3rd party shopping cart (www.mystore.com)2 domains (a.com and b.com) have multiple sub-domainsHere is a graphical representation of the structure:Measurement RequirementsTrack each domain and sub-domain separately (e.g. www.a.com, news.a.com, and blog.b.com)Track the rollup/overall traffic for all domains and sub-domainsTrack full e-commerce transactionsSolutionCreate a Google Analytics account for each domain (www.a.com, www.b.com, and www.c.com)Customize the tracking code to link the multiple sub-domains with their main domainsLink the third party shopping cart with the main domain and install Google Analytics tracking code in all shopping pagesCreate a rollup Google Analytics account and add its code to all domains and sub-domainsGraphical example of a well-planned Analytics Account Structure:Now on to the technical stuff.  If you don't enjoy javascript and regular expressions, you may stop here and ask your webmaster or technical analyst to read further :-)

The How:I will try to illustrate the technical implementation in 10 simple steps:1- Create a unique Google Analytics account for each domain www.a.com, www.b.com, and www.c.com and then use the account number UA-AAAAAAAA-1 in the code in step 3 and use the accounts UA-BBBBBBBB-1 for www.b.com and UA-CCCCCCCC-1 for www.c.com in the code in step 8.
2- Create a Google Analytics account for the a rollup account that will oversee all domains and sub-domains (use the GA account number UA-XXXXXXXX-1 in the code used in step 3 and 8)
3- Add the following Google Analytics tracking code to the main site (www.a.com) and its sub-domains (blog.a.com, news.a.com, images.a.com, and media.a.com)
About the following code: We have a regular pageTracker object to track activity on each particular subdomain and a rollupTracker to track activity across all subdomains and the third party checkout site. (Click here to learn more about the customizations we made to the standard Google Analytics tracking code)
 <script type="text/javascript">var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));</script><script type="text/javascript">try {var pageTracker = _gat._getTracker("UA-AAAAAAAA-1");pageTracker._setAllowHash(false);pageTracker._setDomainName(".a.com");pageTracker._setAllowLinker(true);pageTracker._trackPageview();var rollupTracker = _gat._getTracker("UA-XXXXXXXX-1");rollupTracker._setAllowHash(false);rollupTracker._setDomainName(".a.com");rollupTracker._setAllowLinker(true);rollupTracker._trackPageview();}catch(err) {}</script>
4- Enable E-Commerce Reporting


Analytics Settings > Profile Settings > Edit Profile Information
5- Add the following code* to all shopping cart pages on the store site (www.mystore.com)*Make sure to add this code to the top of the pages.
<script type="text/javascript">var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));</script><script type="text/javascript">try {var pageTracker = _gat._getTracker("UA-AAAAAAAA-1");pageTracker._setDomainName("none");pageTracker._setAllowLinker(true);pageTracker._trackPageview();var rollupTracker = _gat._getTracker("UA-XXXXXXXX-1");rollupTracker._setDomainName("none");rollupTracker._setAllowLinker(true);rollupTracker._trackPageview();}catch(err) {}</script>
6- Add the e-commerce tracking code to the confirmation page after the GATC.
Read more about "How to track e-commerce transactions?"
7- Change the links to the store site (www.mystore.com) on the main site (www.a.com) to use _link as following:
If the current link looks like:
<a href="https://www.mystore.com">Buy Now</a>
Change it to:
<a href="https://www.mystore.com" onclick="pageTracker._link(this.href); return false;">Buy Now</a>
8- Repeat step number 3 for domains www.b.com and www.c.com after updating the Google Analytics account number UA-AAAAAAAA-1 and the setDomainName value.
To view the entire code for www.b.com and its sub-domains (click here)To view the entire code for www.c.com (click here)9- Create a profile for each sub-domain (only if needed)
In order to track a sub-domain (ex. blog.b.com) in its own profile, follow the following three steps:
a- Create a filter that include only traffic from Hostname=blog.b.comb- Create a profile and name it "Blog"
c- Apply the sub-domain filter to the new profile10- As you might have noticed from the codes that we added so far to all pages, we added an extra Google Analytics account to track all pageviews across domains and sub-domains to one Google Analytics account. We call this account “rollup account”.
var rollupTracker = _gat._getTracker("UA-XXXXXXXX-1");rollupTracker._trackPageview();
Since in the rollup account, we will track pages from different sites and many of these pages might share the same naming convention, I suggest that you create an advanced filter that adds the hostname to the page name to differentiate between pages with same URI.

Once you apply the filter, the upcoming data will appear as following:
Note, in the example above if we didn’t apply the “Add Hostnames” filter, all home.aspx pages will appear as one page with 2685 pageviews.If you have been with us so far, you are now ready to conduct your analysis based on clean and much more accurate data :)To review each domain by itself and for deep-dive analysis, use the domain profilesTo get an overview and to see how the business is doing across all sites, use the “Rollup Account”Related Posts
Google Analytics - Accounts and ProfilesAccount Rollup in Google AnalyticsGoogle Analytics for the EnterprisePosted by Allaedin Ezzeidin, Analytics Specialist @ E-Nor, a Google Analytics Authorized Consultant


