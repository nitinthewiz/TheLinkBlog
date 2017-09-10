---
title: "Weblog Tools Collection: Gravatars and WordPress 2.5"
date: 2008-03-04 05:30:10 +0000
external-url: http://weblogtoolscollection.com/archives/2008/03/03/gravatars-and-wordpress-25/
hash: 072700de0c05fa67d672a293f396f7d9
year: 2008
month: 03
scheme: http
host: weblogtoolscollection.com
path: /archives/2008/03/03/gravatars-and-wordpress-25/

---

Several commenters mentioned on yesterday’s post regarding Gravatars without a plugin that WordPress 2.5 would be having built-in Gravatar support.

And indeed WordPress 2.5 will come with Gravatar (aka, Avatar) support.  Within this post I will demonstrate how Gravatars will be used with WordPress 2.5.  As a side note, 2.5 has yet to be released as of this writing.

Gravatars in the WordPress Admin Panel
WordPress 2.5 marries theme authors and casual WordPress users together with support for Gravatars in the WordPress admin panel.

WordPress users can access the Gravatars settings in the Settings->Reading panel.

If a theme author has decided to use the WordPress 2.5 function, then WordPress users can easily control their Gravatar usage in the admin panel.

In the admin panel, WordPress users can change:


Whether Avatars (aka, Gravatars) are displayed or not.
Which rating of Avatars are shown.


Avatars in the WP Admin Panel

Please keep in mind these settings will have no effect if the theme author didn’t make use of the WordPress 2.5 function.

And what is the functon you ask?

Theme Authors:  Adding Gravatars to Your Theme
The function to add Gravatars to your theme is called:  get_avatar.  The function returns a complete <img> tag of the Avatar.

The function get_avatar is setup as follows:

function get_avatar( $id_or_email, $size = '64', $default = '' )


id_or_email: The author’s User ID (an integer or string) or an E-mail Address (a string)
size: The size of the Avatar to display (max is 80).
default: The absolute location of the default Avatar.

Some things to note here:


The default Avatar size is 64×64.
The default Avatar is 
The Avatars will show only if the user allows them in the WP Admin Panel (enabled by default).
The Avatars will only show based on the rating the user has selected in the WordPress admin panel.

Here are some examples of the function in use:

Example 1 with a default Avatar
echo get_avatar( 1, '80', 'http://mysite.com/avatar/avatar.gif' )

In this example I used a user ID of ‘1‘ and specified the location of a default location.  This example is useful if you want to display an Avatar outside of the comment’s section and you have an idea of the person’s User ID.

Example 2 with an e-mail address and size
echo get_avatar( 'myname@mysite.com', '60' )

This example is useful if you want to display the Avatars within the Comments Loop.

If calling Avatars from the Comments Loop (in comments.php), you will want to use the get_comment_author_email function in place of the above e-mail address.

echo get_avatar( get_comment_author_email(), '80' )

Backwards Compatibility
If you wish to develop a theme that displays Avatars for 2.5 and below, I recommend using a combination of the code mentioned here and the code from Connor Wilson’s post on using Gravatar without a plugin.

Your code would look something along the lines of:

 


if (function_exists('get_avatar')) {
 //2.5 code
 } else {
 //alternate gravatar code for < 2.5
 }

Further Reading
For more reading on the get_avatar function, please read Ryan Boren’s Avatars in WordPress 2.5, which he covers several additional points not mentioned here.

Conclusion
The inclusion of the get_avatar function is a nice addition to WordPress 2.5, but it relies on theme authors to include it.  If you are comfortable editing your own theme, you can easily add the function into your own theme when 2.5 is released.

