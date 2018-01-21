---
title: "Recovering Photos from a Corrupt Memory Card with PhotoRec"
slug: recovering-photos-from-a-corrupt-memory-card-with-photorec
date: 2008-12-03 07:03:34 -0600
category: 
external-url: http://regex.info/blog/2008-12-03/1016
hash: 14bdb1068eadb5f2b5a893cb5ec3283d
year: 2008
month: 12
scheme: http
host: regex.info
path: /blog/2008-12-03/1016

---


Nikon D700 + Nikkor 85mm f/1.4 — 1/6400 sec, f/2.2, ISO 200 —
full exif & map — nearby photos
Almost Lost
Brilliant Orange at the Nanzenji Temple, Kyoto Japan


I accepted an invite the other day from my friend Shimada-san to visit the
Nanzen'in temple/gardens located in a sequestered back corner of the large
Nanzenji temple complex. It was my first visit to that sub-temple, and I'll
post more about it later, but suffice to say that it was
spectacular. I took a bazillion pictures, which I found totally
missing when I got home and tried to load them onto my PC. The card was
corrupt and Windows hung trying to read it. Yikes!



Nikon D700 + Nikkor 24-70mm f/2.8 @ 55 mm — 1/200 sec, f/6.3, ISO 2500 —
full exif & map — nearby photos
Enjoying the Nanzen'in Gardens
at the Nanzenji Temple, Kyoto Japan


It's the first time I've had a problem like this in the 10+ years I've
been shooting digital, so I finally had to pay attention to the
image-recovery talk that often comes up in online photography forums.


I recovered all the photos... the pictures on this post are from among
them.


In the hope that it might prove useful to someone, I'll recount how I
did it. Having run into the problem on my Windows XP box, I decided to try
the recovery on my Mac.


I used the most-excellent PhotoRec software to
recover the files. It's a command-line program that can run on many
different operating systems (DOS, Windows, Linux, Mac OS X, FreeBSD...), so
I did the recovery within a Mac Terminal window.




First, I mounted the damaged card, and used the df command to see its raw device name:




% df
Filesystem              512-blocks      Used   Avail Capacity  Mounted on
/dev/disk0s2             155367520 148986336 5869184    96%    /
devfs                          208       208       0   100%    /dev
<volfs>                       1024      1024       0   100%    /.vol
/dev/disk1s1               7536512       704 7535808     0%    /Volumes/NIKON D700



The details of what you see would be different on your system, but the
important thing here is to be able to identify the line with the memory
card (in my example, the last line), and to then identify the “raw device
name” at the start of that line. The raw device name will always start with
“/dev/” and in my example, it's “/dev/disk1s1”.


(If there's a way to connect a memory card without OSX mounting it, I'd
like to know, because that would be safer.)


You then need to tell OS X to pretend that the memory card is no longer mounted while actually leaving it physically connected to the computer.
Thus, without disconnecting it, run the following (using the raw device name you find in the first step):




% sudo umount /dev/disk1s1



You'll have to be an administrator, and will have to enter your password.


Now, run photorec. The Mac version is in the “darwin” subfolder
of the download folder, so after changing directories to the download
folder, here's what I ran (again, you'll want to change the raw device name
to whatever you found):




% darwin/photorec /dev/disk1s1
PhotoRec 6.10, Data Recovery Utility, July 2008
Christophe GRENIER <grenier@cgsecurity.org>
http://www.cgsecurity.org

PhotoRec is free software, and comes with ABSOLUTELY NO WARRANTY.

Select a media (use Arrow keys, then press Enter):
Disk /dev/disk1s1 - 8152 MB / 7775 MiB (RO)

[Proceed ]  [  Quit  ]

Note: Some disks won't appear unless you're root user.
Disk capacity must be correctly detected for a successful recovery.
If a disk listed above has incorrect size, check HD jumper settings, BIOS
detection, and install the latest OS patches and disk drivers.



I made sure that the raw device name was highlighted, then pressed
enter. It'll progress through a few more screens where you tell it that the
card has an Intel/PC partition-table type, that you want to do the
“whole disk”, that the filesystem is “Other”, and where you
want to save whatever files it can recover. (I had just created a “found”
folder on my Desktop, and used that.)


Make sure, of course, that you have at least enough free space on the
disk as the size of the card.


PhotoRec took about two hours to process My Transcend 8GB “300×”
compact-flash card, and recovered all the pictures from the day, and
hundreds of random other shots going back more than a month. I reformat the
card each time I go out, but that just marks the disk's table of contents as
empty, without actually clearing out any data, so the data for random old
pictures remained on the card for PhotoRec to find.



Nikon D700 + Nikkor 24-70mm f/2.8 @ 70 mm — 1/200 sec, f/6.3, ISO 220 —
full exif & map — nearby photos


PhotoRec does not recover the original filename with a recovered file,
so whatever images it finds have names filled with apparently random
numbers, like “f1535616.jpg”. If your digital-photo workflow involves
renaming images based on, say, the image-capture date and time, you don't
care what the in-camera filename was, but my workflow keeps the
in-camera filename, so i wanted to rename the files to what they would have
been.


I used this magic incantation, which requires exiftool:




exiftool -q -p 'mv $&#123;filename&#125; JF7_00$&#123;filenumber&#125;.NEF;'  *.nef  | sh



I don't know about other kinds of cameras, but Nikon SLRs include in the
image file a “FileNumber” bit of metadata that tells what number was used
in the in-camera filename. I use exiftool to reference that number,
insert it into the pattern for the kind of filename I want, then combine
that with a file-rename command.


Spiffy.



It's probably overkill, but I then used the built-in Mac “Disk Utility”
to zero-fill the entire memory card, then re-formatted it in my camera.
Good as new.



Nikon D700 + Nikkor 24-70mm f/2.8 @ 70 mm — 1/250 sec, f/6.3, ISO 200 —
full exif & map — nearby photos


The pictures I recovered are nice, but it's not like I couldn't have
just walked down there again today to take most of them. I'm happy to have
recovered them, but I'm most happy about having this experience under my
belt, so that these techniques will be at my disposal should I ever be
faced with the loss of important pictures.


In thanks for making this experience possible, I sent €25 to the guy who wrote
PhotoRec, Christophe Grenier. Thanks, Christophe!

