---
title: "An Update on Encrypted UIDs"
date: 2010-11-23 19:25:00 +0000
external-url: http://developers.facebook.com/blog/post/431
hash: 4e2bf25c22a5eb51dd9cd828a10dc5ea
year: 2010
month: 11
scheme: http
host: developers.facebook.com
path: /blog/post/431

---

Last month, we outlined an initial proposal to address the inadvertent sharing of User IDs (UIDs) via the HTTP Referral header.  Further, we announced our intention to provide a unique, but anonymous mechanism that developers can use with third-party service providers.  Over the past few weeks, we have received feedback from the developer community, which we have used to refine our proposals.  Today, we are providing an updated proposal for handling inadvertent UID sharing and releasing a new mechanism for legitimate and anonymous sharing with third-parties.


Iframe POST Proposal
Currently, we pass iframe applications the ‘fb_sig_user’ query string parameter in the URL.  This allows the application to identify the user and create customized, social experience.  Due to the way browsers work, this information in the URL can be inadvertently passed in the HTTP Referrer header when someone clicks a link within the iframe.


Our initial proposal to address this issue  used encryption as a means to protect against this inadvertent sharing, but still passed this encrypted UID in the URL.  After talking with the community, we have updated our proposed solution to use a different mechanism that provides better protection for users while minimizing the impact on existing applications and eliminates the need to use encryption libraries. 


In short, this new proposal embeds the UID in a HTTP POST body ensuring that it will not be exposed in any HTTP Referrer header whatsoever (encrypted or otherwise).  We do this by creating a <form/> element targeted at the application Canvas URL:


<form target="canvas_iframe" action="http://example.com/" id="canvas_form">
<input name="fb_sig_user" value="1234" type="hidden" />
</form>
<iframe name="canvas_iframe"></iframe>
<script>
document.getElementById("canvas_form").submit()
</script>


This change will require minimal effort for developers and addresses the feedback that we have received to date.  You can learn more about this change on the POST for Canvas page.


This is still a proposal from us and we welcome feedback on the approach.  We have, however, implemented this change, so developers can understand how this proposal will impact their applications.  You can test this change by turning on the “POST for Canvas (Beta)” migration on the Advanced tab of the Developer Application.  We plan on gathering feedback over the next two weeks and then determine if/when to require this mechanism for all applications.


Third-Party IDs
Facebook has never and will never sell user information, and we expressly prohibit Platform developers from passing any data from Facebook to data brokers.  There are, however, practical reasons that developers will need to share information with a legitimate third party.  For example, a game developer might need a way to identify that a user has taken an action on a partner website (e.g., completed an offer) so that the person can receive virtual goods.  For this reason, we have developed a mechanism for developers to obtain an anonymous but unique identifier for their users, which we call a third-party identifier.


Developers can obtain a third-party identifier through either the Graph API or FQL:


Graph API
Get the third-party identifier from my User object:  http://graph.facebook.com/dmp?fields=third_party_id&access_token=[access_token]


Get the third-party identifier for two users: 
http://graph.facebook.com/?ids=dmp,vernal&fields=third_party_id&access_token=[access_token]


FQL
Get the third-party identifier from the user table: https://api.facebook.com/method/fql.query?query=select third_party_id from user where username ="dmp"&access_token=[access_token]


Get the third-party identifier for two users:
https://api.facebook.com/method/fql.query?query=select third_party_id from user where (username ="dmp" or username="vernal")&access_token=[access_token]


These identifiers may be shared with permitted third parties, but like all data from Facebook, they are also prohibited from sharing with data brokers.  We encourage developers to move to this mechanism quickly, and we will require it as of January 1, 2011.


If you have comments or questions about either the iframe POST proposal or our third-party identifier feature, please use the comments found below.


Mike Vernal is Director of Engineering for Facebook Platform.

