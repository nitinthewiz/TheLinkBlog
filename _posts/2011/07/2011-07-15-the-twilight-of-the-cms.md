---
title: "The Twilight of the CMS | TPM Media Labs"
date: 2011-07-15 20:27:04 +0000
external-url: http://labs.talkingpointsmemo.com/2011/07/the-twilight-of-the-cms.php
hash: 050211de6e585cd98331ad13fcf8a893
annum:
    year: 2011
    month: 07
hostname: labs.talkingpointsmemo.com
---

Instead of revolving around a monolithic central piece of software, we have adopted the paradigm of feature-as-app. Our frontpage: an app. Our slideshow: a different app. Article publishing: yet another app. You get the picture. At the heart is a simple and flexible API that digests manifold requests from the different applications. For example, Moveable Type is great at publishing entries and updating its database accordingly. Our new system will simply wrap the MT database in a cached layer and incorporate its content. Our new gallery app — currently active on the site — creates slideshows, writing its changes to central datastore as well. The frontpage maker reads from the API and is made aware of MT updates, galleries, and all other content that has passed through the system.
