---
title: "Installing CrashPlan on a PogoPlug Pro"
date: 2011-07-16 09:47:24 -0500
external-url: http://www.opticality.com/blog/2011/07/16/installing-crashplan-on-a-pogoplug-pro/
hash: 039dc141953356a9f511b0ff9c4def40
year: 2011
month: 07
scheme: http
host: www.opticality.com
path: /blog/2011/07/16/installing-crashplan-on-a-pogoplug-pro/

---

PogoPlug Pro is an amazing device (coupled with an amazing service). CrashPlan is an amazing piece of software (and also provides a fee-based amazing service). I’ve had both for a while and think very highly of them.

To solve a number of my own problems (not caused by either service!), I decided to investigate marrying them (the PogoPlug device, with the CrashPlan software). To be slightly more accurate, I wanted the device to perform an additional function (beyond backups). I wanted it to be my primary DLNA server.

Caution: none of what follows is supported by either company. You will be voiding your PogoPlug warranty and CrashPlan does not support this configuration of their Linux software. Proceed at your own risk!

My primary reason for installing CrashPlan on this device is to compensate for the pathetic upload speed provided by Time Warner, all of 485Kbps, shared with my wife, for normal Internet use, VoIP calls and backups. In other words, not really a useful real-time backup solution. Since we are often at other, very high-speed locations, I still believe that paying for the CrashPlan online backup service is the way to go (and gives me great comfort), but when I’m home, I wanted a local solution (that didn’t involve plugging in a hard drive to my laptop).

Since I was able to do this, successfully, the instructions can be found on the Net. Since it took me way longer to find the various pieces, let alone get them to work, than I felt it should have, I’m writing this (for myself, as well as for others who might give up more easily than I did). None of the credit goes to me, I’m just collecting the wisdom of others in one place, hopefully an easy one to find.

There are a number of Linux distributions available for the PogoPlug Pro (an ARM-based device). I chose Arch Linux because it was the most prominent one I found and because it has a very good reputation independent of the PogoPlug. The specific ARM implementation has it’s own site, which is where I started my odyssey.

After reading the overview on that page, I clicked on the Installation tab. The instructions there are extremely clear. The first time I followed them, the formatting of my external drive failed. I ended up formatting the drive while it was connected to a laptop running Linux, but all of the other instructions on that page worked. I will repeat them here, so that anyone who doesn’t want to link off of this page can simply follow all the way through.

You have to register your PogoPlug at my.pogoplug.com. This is required, even though we will shortly be disabling the service, since this is the only way to get SSH access to the device. You will be able to reverse the process, returning the device to a full PogoPlug in the future, should you desire that, but it’s not a dual-boot situation where you decide which version you want it to be.

Once you’ve enabled SSH on the device, you can set your own password. The username will be root. The default password for a PogoPlug Pro is ceadmin (as noted, you can change it via the website, or once you log in, with the passwd command. Change it!

One of the steps that they don’t cover is discovering the IP address of your PogoPlug, so that you can SSH to it. In a home environment, this is relatively easy (for the geeks among us). You login to your router, look at the list of attached devices and easily spot it.

I’m installing the software on a second device as I type along. I’m in an office environment and don’t have access to the router. There are hundreds of devices in the office. I had to write down the MAC address of the PogoPlug, go over to a system administrator and ask him to search the DHCP log files for that MAC address. He did and I found out the address that was assigned to it. Whew.

I successfully logged into the device, just to make sure it worked, while it was still an official PogoPlug. That step was optional, but comforting. Since the next step is to power down the device (which you can safely do by just pulling the power cord, especially if you have no hard drives attached yet), since I’m logged in as root, I typed /sbin/halt instead, to be a little safer. Wait 60 seconds (for added safety), then pull the power cord.

We’re going to install Arch Linux on an external drive. The only thing that will be changed on the PogoPlug itself is the boot sector, which will now point to the external drive (that’s what would need to be reversed to restore the PogoPlug functionality).

With the PogoPlug powered down, attach only the drive that you intend to install Arch Linux on. This way there will be no confusion or errors. Later on, if you want multiple drives attached (for backups and/or media files) it will be easy to add them. I am using a 2TB Fantom Drives to do my install.

Once the drive is attached (and turned on), plug the power cord back into the PogoPlug and wait for it to boot. Then SSH back on to it (the root password will be what you set it to, or ceadmin if you didn’t change it). The box is still running the PogoPlug software, with your drive attached to it.

Type: killall hbwd

That will stop the PogoPlug software from running on the box. We don’t want it to interfere with the installation of Arch Linux. You might have to wait a bit for the service to stop. If you want to check, type the following:

ps | grep hb

The only result should your grep process. Then, you can type:

/sbin/fdisk –l

The last line of output should start with /dev/sda1. That means your disk drive was found and has a partition on it (it’s likely formatted already). We are about to erase everything on the disk, so be absolutely sure that you want to continue with this adventure before doing that! If you’re ready, type:

/sbin/fdisk /dev/sda

That will bring up the fdisk program on the entire drive (sda as opposed to sda1 which is the first partition). You will now have a prompt that is directly from the fdisk program. We will type a number of one character commands. Right after you type the character and press enter, fdisk will go off and do what you asked it to.

Type: o

That will clear the partition table so that the disk will become unusable (for the moment). As you can see from the messages, nothing has been committed in stone as yet (very soon). This has modified an in-memory copy of the partition table.

Type: p (to verify the above, that there are now no partitions)

Type: n (press Enter, this will create a new partition)

Type: p (to make it a Primary partition. At this point, I’ll stop saying “Press Enter”, but you still have to!)

Type: 1 (to make this partition #1)

At the next two prompts (First and Last cylinders), just Press Enter to accept the defaults (you are making the entire disk available as the first and only partition).

Now comes the destructive part. This will actually wipe out any data you had on the disk (but still doesn’t modify the PogoPlug in any way!).

Type: w (this writes the partition table back out to the disk)

You are now back at the command line. If you’re a paranoid type (or just careful), you can verify that things worked by repeating the fdisk command and listing out the partition table, all in one shot:

/sbin/fdisk –l

This is the output on my system:

Device Boot      Start         End      Blocks  Id System
/dev/sda1               1      243201  1953512001  83 Linux

2TB, in one partition, marked for use by a Linux system. Now we need to actually create the filesystem, which in our case will be an ext3 one. This will require downloading some commands that will need to be executed. Here are the steps:

Type: sync (to flush any filesystem changes)

Type: cd /tmp (to change to a temporary, writable working directory)

Type: wget http://archlinuxarm.org/os/pogoplug/mke2fs (to retrieve the program mke2fs)

Type: chmod 755 mke2fs (to make it executable)

Type: ./mke2fs -j /dev/sda1 (the leading dot is critical. This will format the partition to an ext3 filesystem)

The above command can take quite a while, depending on the size of your external drive. This is the command that failed for me on my first PogoPlug, so I ended up having to detach the drive, connect it to a Linux laptop, perform the same exact command as above (which was already available, I didn’t need the wget part) and then reattach the drive to the PogoPlug.

Note: it failed for me again. I was able to format it using the built-in /sbin/mkfs.ext2 command (passing in the “-j” flag), but I didn’t trust that it was building a true ext3 filesystem (ext2 + journal). So, I disconnected the drive from the PogoPlug, attached it to a VirtualBox VM on my Win7 laptop, and formatted it there as a real ext3. Took forever, but it worked.

Whether the mke2fs command worked for you or whether you had to format the drive separately, like I had to on two separate installations, you’re now ready to install Arch Linux on the external drive. You should already (still) be in /tmp, but to make sure, feel free to type: cd /tmp

Type: wget http://archlinuxarm.org/os/oxnas/oxnas-install.sh (that retrieves the install script)

Type: chmod 755 oxnas-install.sh (this makes the script executable)

Type: ./oxnas-install.sh (this starts the script, which will send lots of messages to your terminal window. It also downloads the root filesystem image, which is roughly 129MB, so it can take a while if you don’t have a fast network connection.)

When it’s finally done (took between 5-10 minutes on a very high speed connection in the office), the output should look like this if it succeeded (at the very end):

#############################
## Looks good!
# Sync …
# Unmount
# Reboot to enter into Arch Linux ARM

Note the looks good! and then the instructions to reboot. That’s what we’re going to do next.

Type: /sbin/reboot (cross fingers!) 

This will immediately disconnect you from the terminal window you were in. You need to wait a few minutes for the orderly shutdown of the PogoPlug, followed by the booting up of Arch Linux ARM. You can watch the lights on your external drive to see when there is activity on it, indicating that the booting has begun. When the light settles down, the boot is complete.

We’re ready to log back in (this time to the new operating system), and the password has been changed to a new default one. The user is still root, but now so is the password (root), which you should change right away with the passwd command. It’s quite possible that the IP address of the box has changed during the reboot, so please verify the new (or existing) one, before SSH’ing back on.

If the IP address did not change, then you might have to remove the old key associated with it, or ssh might refuse to connect, thinking it’s a security violation. If you get the same IP address again, you may need to run the following command first (on your local machine, the one you are SSH’ing from):

Type: ssh-keygen -R 192.168.1.123 # (using your device’s IP, which won’t likely be 192.168.1.123)

The following First Steps page on the Arch Linux ARM Wiki explains the above, and gives you a number of other useful tips. I followed them religiously the first time through, but I changed the order a bit this time around and it saved a bit of typing (or I think it did).

Instead of going through the above, this time I updated all of the packages right away. I believe that it installed openntpd and updated the /etc/rc.conf file (one of the first steps that I performed manually the last time). You can do what I did, then check if openntpd is installed and running.

Type: pacman –Scc (clear out old packages. I said YES to the first, and NO to remove unused repositories)

Type: pacman –Syu (this will do a large update, first syncing the repositories, then updating all packages)

Now comes a crazy part. I say crazy because by the time you read this, perhaps the maintainers of Arch Linux ARM will have updated the repositories and this will no longer be necessary. Then people will think I’m an idiot, so be it, I’m putting it in here because it can’t hurt!

Type: pacman –Sy udev-compat (to fix a problem with udev + syslog-ng taking up 100% of your CPU)

The 100% cpu problem might be happening as you read this (if you’ve done the previous steps already). It might be filling up your disk in /var/log as well. We can check that in a minute (here’s the thread that helped me: there’s a typo in that thread, “sleep3” should be “sleep 3”), but first, let’s do a few more things and then reboot.

Let’s create a swapfile:

Type: dd if=/dev/zero of=/swapfile.img bs=1M count=1024 #for a 512MB swapfile, use count=512

Type: mkswap /swapfile.img (to turn the file we just created into a valid swapfile)

Type: swapon /swapfile.img (to see whether you get any errors, you shouldn’t)

Now we’ll edit /etc/rc.local (use your favorite editor, I use “vi”, you might prefer “nano”) to add exactly four lines after the comments:

swapon /swapfile.img
kill $(pidof udevd)
sleep 3
udevd &

The first line turns the swap on after each reboot. The next three lines kill the bad udev (even after updating the udev-compat the process sometimes misbehaves at boot), then sleeps for three seconds and restarts udev, which makes it seem to behave correctly so far.

OK, time to reboot and see if we have a stable system:

Type: sync (flushes the memory to disk)

Type: reboot (you should lose your ssh connection right away)

Wait until the disk activity settles down a bit, then ssh back in.

Type: top (to see what processes are running. If udev and/or syslog-ng are at the top, something isn’t good)

Type: q (to exit top, whenever you’re done looking around)

You can follow any of the additional instructions for setting up a user, adding sudo, changing TimeZone settings, etc. All are linked from the First Steps above.

Since the reason I did this was to install DLNA, I’ll cover that first (it’s really short), then we’ll move on to the heavier CrashPlan setup. Skip the next few lines if you have no interest in DLNA.

Type: pacman -Sy minidlna jack (this names two packages, but will install something closer to 44, with dependencies)

You should edit the file /etc/minidlna.conf and change any variables (where the files are stored, where to store the DB, what you want to call your DLNA server, etc.). You can read the Wiki page (linked above) to see the more important entries.

Then add the word minidlna at the end of the DAEMONS= line, which should be at the bottom of the /etc/rc.conf file. This will auto-start the DLNA server every time the PogoPlug is booted. To start it right now, type: /etc/rc.d/minidlna start

Whew. Finally ready for the very tricky and long installation of CrashPlan. This is not for the faint of heart, nor is it in any way supported by CrashPlan. It works for me (and obviously others), but you’ll have to be the judge as to whether the hassle is worth it for you.

Let’s start with crediting the place that got me unstuck, the CrashPlan support forums! Kudos to CrashPlan for allowing this type of discussion on their forums, even though they don’t support this configuration. Here’s the thread, but all of the interesting bits are in the long comment by Torbjorn. It was really hard for me to find, because I was searching for the word PogoPlug. This solved the problem for Sheeva (the baseline of the Pogo), but it’s not quite identical.

Type: pacman –Sy openjdk6 cpio (we need to get a working Java installed and CrashPlan will require the cpio package separately)

The next step (according to Torbjorn) is to download an ancient (2005) libjtux source package, apply a patch and compile it. He supplies a pointer to the source (amazingly, still available) and the patch file is available as an attachment to his comment. You can grab both from the the thread linked above. If you do, you will likely have to download a bunch of development packages (using pacman), starting with gcc.

Instead, I will attach the completed libjtux.so that I built (following those instructions), to save you time, effort and potential errors. I also just grabbed it from my first build and applied it to my second, for the same reasons.

Now we need to install CrashPlan itself by heading to the download page for Linux. I right-clicked on the download button (currently version 3.0.3, but the software auto-updates after the first install). I copied the link location. Back on the PogoPlug:

Type: wget http://download.crashplan.com/installs/linux/install/CrashPlan/CrashPlan_3.0.3_Linux.tgz (that should work, but starting at the http part, just paste in the link you copied if it’s newer than 3.0.3)

Type: cd /tmp

Type: tar –xzf WHEREVER_YOU_DOWNLOADED_THE_CRASHPLAN_FILE (which could be /tmp to simplify matters)

Type: cd CrashPlan-install

Type: ./install.sh (all of the defaults seem reasonable to me, though I did put my archives in another directory. You will need to page through the license file with the space bar and accept that as well. The init scripts on Arch are in /etc/rc.d, which is the other thing I changed from the default.)

When this is done, it will report that it has successfully started the CrashPlan service. It did not. That’s because we haven’t yet replaced the libjtux.so that comes with CrashPlan. The problem is that it was compiled with an Intel i386 architecture.

Type: cd /usr/local/crashplan

Type: mv libjtux.so libjtux.so-ORIGINAL (no real need to save it, other than to memorialize the changes we’re making)

Type: cp WHERE_YOU_DOWNLOADED/libjtux.so . (this copies my version from wherever you downloaded it, or you can right click my link above, and wget directly from my website to this directory)

Torjborn mentions editing a file to add jna.jar to it. I didn’t need to do that, and the directory he references doesn’t exist. I think it’s from a different installation of Java (for the original Sheeva) and not necessary when using the openjdk6 package.

We’re ready to start CrashPlan (at least to see if it comes up and stays up). We can do it by hand, but I am going to add it to the DAEMONS list at the end of /etc/rc.conf (like we did with minidlna) and reboot the machine to ensure that it comes up on it’s own. The daemon name to add right after minidlna is crashplan (lower case).

Type: /sbin/reboot

If you did everything above correctly, when you log back in, there should be a java process running, with CrashPlan as the application. It can a few minutes to completely initialize. In that case, we’re done, right? Wrong! CrashPlan is indeed sitting there, waiting to go to work, but it needs to be configured to allow your machine(s) to start backing up to it. Under normal circumstances, this would be trivial to do, but since the PogoPlug is a headless server, we have to jump through a few final hoops.

Once again, CrashPlan support to the rescue (again, for a completely unsupported feature). If you want to understand the details, or are enough of a techy to prefer the theory, I urge you to just read the CrashPlan document and skip to the final section of this post. If you want fewer steps (and warnings) to follow, I’ll give you the bare necessary steps here.

They key is that on every machine that has CrashPlan installed, there are two programs: 1) the server that does all the work and 2) the GUI (graphical user interface) that connects to the server when launched, and allows you to configure and monitor the server process. On the PogoPlug, we only have #1. The good news is that the GUI speaks to the server over the network. By default, that network is local to the machine that the server is running on, but with some ssh magic (and a little editing of a configuration file), we can make that a remote connection.

All of the work is going to be done on your desktop or laptop, where you already (presumably) have CrashPlan running. This is likely the machine that you want to backup to the PogoPlug. Let’s just call it laptop so that it’s obvious it isn’t the PogoPlug.

On laptop, make sure that the CrashPlan GUI isn’t running. If it is, exit the application. Find the conf directory associated with CrashPlan on your system. On my Windows 7 x64 machine, it’s this directory: “c:\Program Files\CrashPlan\conf”. In that directory is a file called ui.properties. Edit that file. The following line is in that file: “#serviecPort=4243”. This line is commented (#), because 4243 is the default value. You can leave that line commented and add a line below it:

servicePort=4200

(You could also remove the comment and replace 4243 with 4200, but I recommend adding a new line.)

Save the file to disk. While still on laptop, open a terminal window and execute the following SSH command (if you’re using Putty to do this on Windows, rather than cygwin, I recommend reading the post back on the CrashPlan site).

ssh -L 4200:localhost:4243 user@192.168.5.71

In the above command, substitute your username (or root) where I put in “user” and the IP address of your PogoPlug where I put in the “192.168.5.71”. This command makes port 4200 on laptop magically redirect to port 4243 on the PogoPlug, which is where the CrashPlan server is listening by default already.

Now launch the CrashPlan GUI on laptop by double-clicking the icon (on Windows, it’s probably in your system tray). You should see a request to create a new CrashPlan account (free) or log in to an existing one. Since I already have one (and presumably you do too), just put in your email address and password. It took quite a while for it to log in and download the configuration, but it worked. I think when I first tried it on my first PogoPlug it actually timed out, but worked the second time.

Once that’s done, you can exit the GUI, as all of the defaults are exactly what we want/need. The only exception to that is if you want to let others (that aren’t part of your account) backup to your PogoPlug. Then you will need to write down the CODE to enable that (it’s toward the bottom of the front page on the GUI and also on a Settings tab).

You can now exit from the ssh session that was started above (Type: exit or hit Ctrl-d in that terminal window).

Once the GUI is shut down, edit the ui.properties file again and delete the extra line we added with “servicePort=4200” (or place the comment “#” back in front of it). Save the file.

Launch the GUI again. This time it will connect to the local CrashPlan server on laptop. Now click on Destinations (bottom left entry on the left-hand navigation). Then click on the icon labeled Computers in the center (the PogoPlug is a real computer!). Whatever you called your device should be in your list, no code necessary, since you should have used the same account on both machines. If you didn’t name your device, then Arch Linux ARM defaults your host name to alarm (get it? ArchLinuxARM?).

Now you’re truly done. If you have a large amount to backup, it could take a couple of days to complete the first backup, even though it’s on a LAN. It will also alternate between the various backup locations (including CrashPlan Central), which is one of the reasons it will be somewhat slowed down.

For reasons I can’t explain, it can take a very long time to start the initial backup, even if you pause the other locations. The GUI correctly communicates with the server instantly, since I can see the correct directory created on the PogoPlug, but the destination still shows up as unavailable for some period of time. Eventually, it gets going, and appears to be quite reliable from that point on.

