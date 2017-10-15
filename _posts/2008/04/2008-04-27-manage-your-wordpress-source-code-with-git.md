---
title: "Manage your Wordpress source code with Git"
date: 2008-04-27 22:45:15 -0500
external-url: http://whereslou.com/2008/04/27/manage-your-wordpress-source-code-with-git
hash: dd863bd28c7aad361ae4d06421871e43
year: 2008
month: 04
scheme: http
host: whereslou.com
path: /2008/04/27/manage-your-wordpress-source-code-with-git

---

I was just thinking of posting an article about using ReSharper and MbUnit together, but before doing that I was going to make sure the source control of the blog was up to date. Then I thought, hey, why don’t I write about that instead.

So this is about using the new Git fast version control system on Ubuntu Gutsy 7.10. to add version control to your Wordpress installation.



So why bother? Especially if you copy your wordpress structure periodically? Well, obviously you can get by with that or frequently zipping into dated snapshots after you make changes. There are advantages though. Usually you’ll get rid of the oldest zip files because you’ll probably never need them, and you probably won’t be taking a snapshot after every change you make. You’re also missing some nice extras like providing comments about changes you’ve made.

So first you’ll want to install git. One way to do that is sudo apt-get install git, but as various blogs will point out git is being developed pretty actively and the packages typically trail a few versions. Piku describes the steps you would take to install 1.5.5 which is what I did. You can also browse http://kernel.org/pub/software/scm/git/ to see which is the highest available version.

From Piku’s Blog Updating git on ubuntu:

mkdir ~/build
cd ~/build
wget http://kernel.org/pub/software/scm/git/git-1.5.5.1.tar.bz2
sudo apt-get build-dep git-core
tar xjf git-1.5.5.1.tar.bz2
cd git-1.5.5.1/
./configure
make
sudo make install

And now you can git stuff. Next go to your wordpress directory, create a git repository there, and commit the current version of your code.

cd /path/to/your/site/wordpress
git init
git add .
git commit -m "initial import"

That’s it. If you want to ls -la you will see there is now a hidden .git directory inside the wordpress directory. It contains all information you would need to restore all of the contents to this state at any time.

Also assuming your Wordpress directory is being published by something like Apache, you’ll want to adjust the security. The following line will take away any read-only access the www-data Apache user would have by default. If you don’t do this, then you’re probably publishing your repository for the rest of the world to download. Very, very bad since your mysql password is probably in the wp-config.php file.

chmod -R og-rwd .git

You can also check the history with git log, or check to see if any files have been added or modified with git status.

Now whenever you make changes you can update your own private version control system with the following:

git status
git add .
git commit -m "changed blah blah for yadda reasons"
git log

The next thing you’re probably going to want to do is push a copy of this hidden git repository onto another location, or even better onto another machine. You may also have a situation where you will make some local changes and decide you simply want to revert to the most recent commit. At this point I think the responsible thing for me to do is leave you searching the git site itself because I would hate to throw a command-line out there someone with more experience will say is completely wrong.

Ah, what the heck. I’ll throw one out there and hopefully someone who knows what they’re doing will correct it.

git reset --hard will force the current directory to return to the state which was last committed. The exception will be new files that have never been added, but you can git status to see which extra files that would be. If you’re feeling especially brave, or potentially foolish, you could do the following:

sudo rm -rf *
git reset --hard
git status

Of course you’ll want to be absolutely certain your current directory is the correct one. Do a “ls -la” first to make sure there’s the .git folder present before you rm. I’ve verified the “sudo rm -rf *” line will not remove the hidden .git folder at the same time. Still it’s such a scary thing to do I’d recommend just using “git status” and removing the extras after you reset.

(As always any corrections in comments are greatly appreciated.)

