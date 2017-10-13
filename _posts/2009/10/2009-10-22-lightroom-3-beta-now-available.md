---
title: "Lightroom 3 beta now available"
date: 2009-10-22 04:25:49 +0000
external-url: http://blogs.adobe.com/lightroomjournal/2009/10/lightroom_3_beta_now_available.html
hash: a9fafe1baa4cb4c1fa84518c1321d839
year: 2009
month: 10
scheme: http
host: blogs.adobe.com
path: /lightroomjournal/2009/10/lightroom_3_beta_now_available.html

---

The Lightroom team is proud to introduce the third public beta program of our application designed by and for digital photographers.  We've come a long way since our very first public beta on January 9th 2006 at MacWorld.(We didn't even have a crop tool in the first release!)   For this latest release we went back to the drawing board and revisited what we believe are the fundamental priorities of our customers:  Performance and Image Quality.  Lightroom has been stripped down to the "engine block" in order to rebuild a performance architecture that meets the needs of photographers with growing image collections and increasing megapixels.  The raw processing engine has also received an overhaul right down to the fundamental demosaic algorithms that now allows unprecedented sharpening and noise reduction results.   


Revisiting the success of the first Lightroom public beta, we want to provide photographers with early access to this new technology so that we have adequate time to respond to feedback.   While we're not going all the way back to a 14 month, 4 version public beta like we did for Lightroom 1, we do want more flexibility than we had in our public beta for Lightroom 2.   Here are a few key details on what we're looking for feedback on:


Import
We've redesigned the Lightroom import experience to make it much easier to visualize how Lightroom allows you to manage your files.  You'll be able to see exactly where you've asked Lightroom to copy your files off your card and then use import presets in compact mode to get fast repeatable results every time.  You can also quickly browse your hard drive to find exactly the right file you need to work on.


Publish Collections
We live in a connected world so you need direct access to publish your photos on your favorite sharing site from directly within the Lightroom Library.  In the Lightroom 3 public beta we're providing direct access to the Flickr photo sharing site so that adding images to your Photostream is as simple as a drag and drop.  You can see all of your uploaded images and if you make any changes to those images you can have them updated on Flickr automatically.(Pro accounts only)  When a visitor comments on your images, Lightroom can pull that comment right back into the Library so that you can see feedback on your files where it belongs, next to the image in your Lightroom library.  We've built this functionality with the same extensibility designed for our Export Plug-ins so if Flickr isn't your cup of tea we're working hard to support developers who can create connections to any of the popular photo sharing sites.  Publish collections can do more than just publish to a photo sharing site.  You can have a publish collection that allows you to publish images to my iPhone sync folder with drag and drop simplicity.  


Image Quality
Sharpening and Noise Reduction
In the Develop module we've focused on tuning our raw processing algorithms to extract incredible detail and quality from your images.  Capture sharpening and Color Noise Reduction improvements work together to give you incredible noise reduction results without losing that fine detail.  We're only halfway through our noise reduction efforts but believe that you will be very pleased with the results so far.  We've actually disabled the previous Luminance Noise Reduction so that you can focus on evaluating the Color Noise reduction implementation.


Grain
While Lightroom's improved noise reduction will give you incredibly smooth images, sometimes you want a little texture or grain in your images.  We've added a grain tool that can add a natural film-style grain to your images to get that perfect look for your photo.


Vignette
The Lightroom team received quite a bit of feedback on our post-crop vignette tool in Lightroom 2 that allows photographers to apply beautifully styled vignettes after cropping is applied.  While the tool was received quite well, we found that photographers wanted a more natural vignette that utilized an exposure or brightness effect rather than just painting black and white on the edges of images.  We've added two vignette modes in Lightroom 3 beta, Color Priority and Highlight Priority that attempt to provide the natural vignette that photographers have requested. Let's not get hung up on the technical details of these models but rather focus on which you prefer for your images and why.


Process Version
The changes above are so significant that for the first time since the Camera Raw plug-in was introduced in 2003, we've needed to add the concept of a process version.   The process version specifies which version of certain Camera Raw image processing elements should be used when rendering and editing files. Process version can affect raw, DNG, TIFF, JPEG, and PSD files. The process version is incremented only when major changes to the raw processing or features are changed. In Lightroom 3, the demosaicing, noise reduction, sharpening, and post crop vignette were all updated.  Depending on what is applied to the image, different image characteristics will change more dramatically than others (i.e. sharpening should change sharpening characteristics etc.), but the demosaic changes apply across the board, so there will always be some change.  By default, we'll leave your images just as they were but if you want to take advantage of the latest processing technology, just update to the current process version.  You can update to the latest process version by selecting the notification triangle that includes an exclamation point above the left hand side of the histogram. (Or from the Settings -> Process Version file menu available in the Develop module)  By default, all new files in Lightroom 3 beta will receive the latest process version.


Slideshow Export
One of the most elegant ways to present your images is in a slideshow accompanied by music.  But until now, you could only share that slideshow with music when playing it directly from within the Lightroom application.  But with Lightroom 3 we've added the ability to export high quality movie files that include your detailed layout and the music track you've selected.  By utilizing the popular H.264 movie format you can share these movies on many popular video sharing sites or optimize it for mobile media!


Custom Print Package
Lightroom 3 adds a new custom layout option for photographers who need complete control over their print layouts.  Add as many different images in whatever configuration you desire on a single or multiple pages.  


Watermarking
Lightroom 3's new watermarking function lets you embed your identity or other information in your images themselves. You can apply text or graphic watermarks to a photograph with adjustable size, position, and opacity.  Available in the Print and Web modules as well as the Export dialog, your identity can now travel with all of your images.


What's Next?
We're not even close to finished in terms of features, performance or image quality but we want early feedback on our improvements so that we have time to make sure Lightroom 3 is your ideal workflow assistant.


Additional Details
GeneralOn Mac, the 'hit zone' for the right scroll bar in the grid view has been expanded so that a closed right hand panel doesn't automatically open too easily.  The automatic panel opening experience has been modified so that it takes a longer amount of time for the panel to open in cases of overshooting the scrollbar. (Mouse towards the white triangle for instant opening) Please provide feedback on this new behavior so that it can be modified or added to the Windows version of Lightroom.Images can be sorted by aspect ratioThe catalog selection dialog has been expanded and improved

Library
You can backup your catalog when you quit Lightroom instead of on launchA volume can be ejected or un-mounted from your system directly from the volume browser in the Library module.Collections can be created directly within a collection set by right-clicking on the collection setImages can be sorted by aspect ratioThe name of a collection is displayed when an image is added to a target collectionStack badges can now be toggled on or off independently in the filmstrip via an interface preferenceErasing with the spray paint tool now requires the use of the Alt keySelect a folder in the Library module and choose a new option "Import to here" to launch the import dialog with that folder preselected as the destinationThe import dialog provides source folder and destination volume capacity informationThe option to include items from subfolders has been included in the primary Folder panel drop down menuChoose Library -> Show Missing Images to locate offline or missing filesA lock icon has been added to the metadata filter bar in the Library module to make filter selections "global" across folders or collectionsAn icon has been added to grid thumbnails to indicate that an image is part of a collection.  Click on that icon to view and/or visit the collectionFavorite sources can be added to the filmstrip source pop-up menu for quick access to specific collections or foldersFlash state is now included as part of the smart collection filter criteriaWhen the 'spray can' is used to add an image to a collection, the collection name is now displayed upon applicationThe optimize catalog feature is now available in the File menuLightroom now imports CMYK files.  Any output, with the exception of export original, or adjustments to these images will take place in an RGB color spaceFilters are now longer automatically "sticky" on folders or collections

DevelopCrop presets choices have been edited for clarityA checkbox has been added to the toolbar to turn on/off overlay visibilityAll adjustment brush and graduated filter sliders can be reset by holding down Option/Alt and clicking on AmountThe color setting for the adjustment brush and graduated filter clearly display an 'x' overlay when no color is selectedThe Collections panel is now available in the Develop ModuleThe targeted adjustment tool is deactivated when switching to a new Develop panelThe local adjustment brush and graduated filter panel have been simplified to a single mode (Previously there was a button and slider 'mode')
SlideshowThe music selection in the Slideshow module has been decoupled from iTunes on the MacClick the track duration to sync the length of the slideshow to the length of the music track
PrintBlack or a custom color can be selected for a print layout backgroundThe Identity Plate can be moved in small increments by selecting it and using the arrow keysMatch photo aspect ratio is now a persistent option in the Cell panel
ExportThe file extension case(UPPER/lower) can be selected in the export dialog

Full release notes are located here:  http://labs.adobe.com/technologies/lightroom3/releasenotes.pdf

