---
title: "37signals ID begins rolling out"
date: 2009-12-14 03:14:45 +0000
external-url: http://productblog.37signals.com/products/2009/12/37signals-id-whats-new.html
hash: 6c487e995bb8f11d3c0d709f5aacea0c
---

37signals ID, our new single sign-in system is beginning to roll out to customers (starting with our Max and Premium plan customers). Over the next week we'll roll it out to more and more people. By the end of the week (around the 18th) we expect the upgrades to be rolled out to everyone.


Here's a list of many of the major changes that come along with the 37signals ID username and password system upgrade. We'll be providing more detail on some of these in the coming week.


Launchpad (global)


Introduced Launchpad. Visible to anyone with multiple accounts tied to a 37signals ID or Open ID. The Launchpad shows up when someone signs in from 37signals.com or a product marketing site home page. Also linked from the in-app Launchbar.
The Launchpad displays all accounts linked to your 37signals ID. Each product gets a column, and each account gets a row. Drag and drop reorder columns and rows. Single click sign-in to any listed account.
Edit Identity: Edit your 37signals ID name, email, avatar, username, and password. Switch between OpenID and 37signals ID username and password.
Settings: Assign nicknames to each product account. Hide accounts you don't want displayed on the Launchpad or Launchbar.


Launchbar (global)


Renamed Launchbar (was called Openbar for OpenID users).
Everyone with more than one account attached to their 37signals ID sees the Launchbar at the top of the screen when they're in an app.
Horizontal application order, and vertical account order, mirrors the layout on the Launchpad. User configurable via drag and drop reordering on the Launchpad.


Sign-in screens (global)


Resetting your password asks for your email address instead of your username.
Introduced temporary tokenized sign-in link if your OpenID provider is down. This allows you to still access your accounts if your OpenID provider is offline or unavailable for any reason.
Modernized the design of the in-app login screens with the rounded edges tablet design. Otherwise the same.
Customers who have custom sign-in screens on their own site can update their forms with this new form code.


Edit user (global)


Everyone's "My Info" screen shows 37signals ID card (with a user's real avatar) and a link to edit info in the light blue header. Note: Basecamp clients don't see "37signals ID" branding.
Avatars are now global. Upload an avatar to your identity and it's updated across all your accounts that use the same 37signals ID.


Reset password (global)


New reset password screens. Enter email and get password recovery link sent via email. Actual passwords not sent though email.
Username and password can't be the same for security purposes.
Legacy users (users who haven't gone through transition) continue get old password email.


RSVP - accepting an invitation to create an account (global)


New invitation emails include a link to choose a username and password.
New create an identity screen (pick a username and password).
People can choose to use their OpenID, create a new 37signals ID, or link to an existing 37signals ID they already set up.
Special Basecamp client-view of the RSVP create a username and password screen doesn't show 37signals ID name/branding.
New success screen overlay replaces the old "bookmark this page" message above the sign-in screen. Newly designed success email as well.
Live username and password validation.



In Basecamp


Added a link on the edit person screen that allows admins to fire off a "here's how you recover your username/password" to any user. Admins can use this if one of their users forgets their username or password.
Added a link to edit person to resend the original "set up your account" email.
Users pick their own username and password. Admins create users by entering their first name, last name, email address, and any contact information they want. The system then sends an invite to the email address with a link to the new user to create a username and password.


In Highrise


Added extra email fields to the dropbox email screen. This allows someone to tell Highrise other email addresses they may use so Highrise recognizes them when they forward an email to their dropbox.
Separated users from contacts. A user can be a user without also being a contact.
Export data link moved from edit contact to edit user.
"Import from Basecamp" feature now uses an API token instead of username/password fields. Changed to improve security.


In Campfire


Added support for OpenID.


Thanks again for your patience during this long-term project. This upgrade addresses a variety of top customer requests and lays the foundation for us to deliver even more good stuff in 2010. Stay tuned!


