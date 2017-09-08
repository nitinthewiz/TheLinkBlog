---
title: "Weblog Tools Collection: First Look At WordPress 2.7"
date: 2008-09-02 12:15:07 +0000
external-url: http://weblogtoolscollection.com/?p=4040
hash: 0535f9e7a10371379def0e07c603cddf
annum:
    year: 2008
    month: 09
hostname: weblogtoolscollection.com
---

Although tentatively scheduled for November, WordPress 2.7 looks to be as big of a release since WordPress 2.5, perhaps even bigger. Before reading the rest of this post, please keep in mind that what you see in the following screenshots is by no means a representation of the final product. Also keep in mind that WordPress 2.7 should not be used on a live blog as 2.7 is no where near stable. What you see here is not necessarily what you’ll get. This post will highlight WordPress 2.7 at its current stage of development. Please keep this in mind as you read through the post and make comments. Also, click on any of the thumbnails to see the full size of the image.

Back End User Interface:


Right from the get go, you’ll notice that just about every facet of the dashboard has been changed. There is now a left hand side navigational column. This column is displayed no matter which part of the administration panel you are viewing. From what I have read on the WP-Hackers mailing list, the decision to go with a side column for navigation was to cut down on the amount of vertical scrolling. This will also allow plugin authors more room to use the top navigation column. After using this version of WordPress, I have noticed that I don’t scroll up or down as much as I used to. One thing worthy of noting is that, when a navigational item contains child elements, clicking on the parent initiates a smooth drop down animation. While this means some elements of the administration area will require an extra mouse click, I don’t find it to be that big of a deal. I imagine if people raise a ruckus about this, the team may decide to initiate the drop down effect during a mouse over.

Although this feature was not available in this prototype, each content block within the dashboard contains an edit link. I’m not sure if these will be drag and drop-able like Widgets but at least you’ll be able to edit their contents or configure them. Speaking of the dashboard, you’ll notice in the screenshot that there is a new block labeled QuickPress. QuickPress is a quick and easy way to publish posts. Although in this iteration, it does not give you the chance to attach a category. So far, it seems to me as though QuickPress could serve to be a quick and easy draft manager/creator.

On the left hand side, we have a box labeled InBox. Again, I am not sure what the plans are for this area of the dashboard. Any details for this feature are speculative at this point. However, I think it would be pretty cool if it served as a private messaging area. A simple way to contact other WordPress site administrators. Sure, we could use email or IM to accomplish this goal, but doing it from within WordPress sounds pretty good to me.

As an aside, the black headers for the various blocks in the dashboard appear more stylish to me versus the light blue colored ones in the current implementation.

Before we move on, we need to acknowledge the WordPress admin bar at the top of the administration area. This bar looks and works similar to the way in which the WordPress.com admin bar works. My Account acts as a profile link as it takes you directly to your account profile. New Post takes you straight to the Write Panel and of course, you can see how many new comments you have in the moderation queue which will take you to the comment management panel when clicked on.

Last but not least, it is important to notice that some of the naming conventions have changed in terms of navigation. For example, Templates have taken the place of Design. There is also a brand new menu item called Utilities. So far, this link houses the following items: InBox, Tags, Categories, Link Categories, Users, Import, and Export. This addition seems pretty logical to me. Instead of clicking on the Management tab where you would then gain access to manage content, there is now a parent navigational menu item called Content. Underneath of this element you’ll find links for Posts, Comments, Media Library, Links, and Pages.

I’ve had discussions with a few people already about why the change from Design to Template has taken place as I don’t understand why it has changed. Templates seem like they would be a good fit underneath Design. Now, we have the possibility of Themes showing up underneath Templates.

The Write Panel:


The Write Panel in WordPress 2.7 has gone through an overhaul as well. I think you’ll really enjoy the fact that drag and drop elements are back. You can now drag elements to the sidebar or to the bottom of the panel. I am thoroughly excited for this element alone. We can now configure the write panel so it is best suited for our needs instead of using a static configuration. There is a cool new tab on the right-hand sidebar called settings.



If you click on this tab, you’ll be able to select which elements are displayed and which ones are hidden. An extra bonus in terms of configuring the write panel! Not only can you configure the layout to your liking, you can even exclude the non used items from showing up. With todays average monitor resolutions being as big as they are, these two changes to the write panel may end the need for vertical scrolling. This was a major complaint with the WordPress 2.5 write panel.

Here is what the Write Panel looks like with all of the settings turned off:



One last thing about the write panel that I noticed. Instead of the add media buttons that are present within todays WordPress write panel, this version showcases a single Add Media button. For now, this only supports the addition of images into posts but I imagine the other media functionality will be added before its release.



Another item worthy of mentioning is that the Publish tab now includes an additional option that will allow you to stick a post to the front page. Subsequent posts will be published underneath of this sticky post until the sticky option item is unchecked.

Even More Plugin Goodness:
Browsing and installing plugins from the respository looks to become even more convenient now that you can do both from the WordPress back end.



WordPress 2.7 essentially brings all of the features of the plugin repository and makes them accessible in the back end. The plugin installation area presents you with a myriad of different ways in which to search the respository for plugins. For example, you can search by Term, Tag, or Author. I tested the search function by selecting Term and then looking for WP Ajax Edit Comments which is a plugin written by our own Ronald Huereca. The search was fast but didn’t show the plugin I searched for as the first result. In fact, the plugin was listed on page four at the bottom. This is a good example as to why the Plugin repository search needs to be improved. There is no reason why a plugin should not be listed as the first result if you type in its exact name into the search field.



Each search result provides a version number, rating, description and an install link. When I clicked on the install link, the detailed plugin information page opened in a Lightbox sort of fashion providing me with a button from which to install from. Clicking the install link from the detailed information page will initiate the download of the plugin. The plugin will automatically be unpacked and installed into WordPress. This is what a successful plugin installation screen looks like in 2.7.



If the plugin was installed successfully, the only thing you’ll have left to do is activate and then configure it.

Although this is great for end users, plugin authors will be pleased to know that they will be able to upload plugins to the repository from the WordPress back end. The Upload Plugin feature in the backend will allow the uploading of plugin archives to your own site while installing them directly from the zip file. This feature was not present in the prototype version but it appears as though the uploading will utilize SwfUpload if available and will unzip .zip packages.

The whole idea of being able to install and upgrade plugins automatically from within WordPress is cool but to see it become a reality is awesome. We can thank the team for building a quality plugin repository API for allowing much of this to happen. I have a feeling that the theme repository and the back end of WordPress will end up going down a similar route with a future version of WordPress.

More Image Settings:
Within the Miscellaneous section of settings, there are now a few more options for customizing the display of images within posts. You can now configure a large image size, default image size, default image alignment, and default image links. Very nice, time saving options.



Plugin Users/Authors:
If you happen to test WordPress 2.7 either on a live site or a local install, please check to see which plugins you have installed work or break with the new version. Then, add your results to the WordPress 2.7 Plugin Compatibility page within the Codex.  Note to contributors: Please include the version number of the plugin you tested. This will help both WordPress users and plugin developers determine what needs to be addressed.

Make This The Best Release Ever:
There are a number of ways in which you can help make this the best release of WordPress thus far. First, there are the mailing lists which you can subscribe and participate in.

WP-Testers Mailing List - You can download the pre-releases of WordPress and test them, so that the WordPress developers can fix problems before the new version is made available to the public. If you would like to get involved in this effort, join this mailing list, where new releases are announced and discussed.

WP-Hackers Mailing List -  All contributions, ideas and suggestions are welcome at the mailing list. Sometimes, requests are also made on the list asking for the help of volunteers to assist in the improvement and development of specific functionality.

Occasionally there are also bug days on the #wordpress-bugs IRC channel. You can read about what happens in a bug day in WordPress Bug Hunts, and subscribe to either the wp-hackers or wp-testers mailing list to find out when they happen.

Also, bookmark this Codex page dedicated to WordPress 2.7. It will be updated as the day of release gets closer.

Conclusion:
Considering WordPress 2.5 was released not too long ago, seeing another User Interface design in the administration panel frustrated me a little at first. I was just beginning to get used to the way the 2.5 admin area looks and feels. However, I must admit that the more I use this new design, the more I enjoy using it. There might be a few users who are upset with the left hand navigation column being displayed on every page. I know I was, especially on the Write panel where I felt squeezed in. However, after using the test version for a little while, I am actually starting to appreciate the vertical navigational column as I don’t need to scroll my mouse wheel up and down as much as I used to. The re-introduction of drag and drop elements within the Write panel is a huge sigh of relief.

Overall, I really like what I’ve seen thus far in this very, very early build of WordPress 2.7. There is still a lot of time before 2.7 is released. Things can and probably will change from now until then but as of right now, things are looking really good.

