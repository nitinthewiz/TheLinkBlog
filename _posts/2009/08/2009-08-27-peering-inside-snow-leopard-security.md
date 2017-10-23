---
title: "Peering Inside Snow Leopard Security"
slug: peering-inside-snow-leopard-security
date: 2009-08-27 21:57:10 -0500
external-url: http://tidbits.com/article/10509
hash: 3910e50e9e3135ef24e2986dd478bf15
year: 2009
month: 08
scheme: http
host: tidbits.com
path: /article/10509

---

From the beginning, Apple made it clear that Mac OS X 10.6 Snow Leopard was focused on improving the performance of the operating system and providing developers with new tools for harnessing the power of modern hardware and multiprocessor systems. The included security updates are no different, and for the most part are completely invisible to the user. 
 
 
These updates provide new tools to assist programmers in producing more secure applications and harden the core operation system, which result in a safer computing experience for most Mac users, even if they aren't overly noticeable.
 
 
Despite these improvements, Apple missed a major opportunity to include a key operating system feature that could nearly wipe-out a entire category of attack.
 
 
Securing Memory and the Power of 64-Bit Security -- The changes I describe here are fairly subtle and technical, so those of you who don't care about things like stack vs. heap memory might want to skip to the next section.
 
 
The most significant single improvement is that the operating system has now been compiled with stack memory protection by default. Essentially, this places what's known as "canaries" in stack memory; fixed values in fixed locations that are pushed around if an attacker uses a buffer overflow attack, allowing the operating system or program to detect the attack. 
 
 
(Buffer overflows happen when input values to a program - something as simple as a URL entered in the Location field of a browser - is larger than the expected set of data. The data that overflows can be used to crash software or a system, or gain privileged access.)
 
 
This makes an entire class of buffer overflow attacks much more difficult to exploit, even when a software vulnerability is present. Developers will need to enable this for their own applications, but by default, Apple uses this feature everywhere it can to limit attacks.
 
 
A second kind of gestalt upgrade is the migration to 64-bit applications and components throughout Snow Leopard. While this is touted as a boost in speed, the Intel architecture offers substantial hardware security capabilities that generally aren't available in 32-bit environments. (While Snow Leopard includes both 32-bit and 64-bit kernels, only the Xserve boots into a 64-bit kernel, Gizmodo reports. Security features are available to programs in 64-bit mode even when the kernel is not.)
 
 
Wherever possible, Apple appears to try and use these technologies for Snow Leopard on 32-bit systems, but most of the real security advantages are only possible when running 64-bit software on 64-bit hardware.
 
 
One of the key areas in which this prevents trouble is in the heap memory, where Apple uses a combination of technologies: one leverages 64-bit hardware, while the others are software enhancements. (The heap is a pool of free memory that applications can dynamically use on a temporary basis, as opposed to the more-structured and static stack memory.)
 
 
When programming an application, heap memory locations that should only accept data can be marked as non-executable, and this will be enforced by the 64-bit processor (similar hardware protection has been used since Mac OS X 10.4 Tiger for stack memory on 32-bit processors). This, again, increases the difficulty of heap-based memory exploits, which are a common form of attack.
 
 
Apple further hardened the heap through use of stronger heap checksums to detect when someone has tried to modify a portion of memory. This is combined with a related feature that will terminate processes if it detects double null bytes where they shouldn't be. This combination doesn't eliminate all heap based memory attacks, but makes the life of the attacker much more difficult.
 
 
A final advantage of the move to 64-bit code is that applications now move data around more securely, skipping the stack completely. Function arguments are passed via registers, which, again, severely complicates the life of an attacker trying to attack your Mac using memory corruption techniques.
 
 
Sandboxing and Safari Enhancements -- Sandboxing is the process of restricting what kinds of activities an application can perform. For example, you can sandbox an application so it can read files, but not write them, or restrict it from ever accessing the network. It's a great way to limit the damage if an attacker exploits an application on your Mac, since they'll be stuck in the sandbox.
 
 
Apple provides sandboxing services that any developer can use, and has slowly been increasing the number of Apple applications that implement sandboxing through software updates. Apple continued this trend with Snow Leopard, sandboxing a number of new applications and features. One example is the x264  codec for handling H.264 video, which will make it harder for attackers to build malicious video files designed to corrupt your video player and allow them to exploit your Mac (a not-uncommon attack vector).
 
 
There's been discussion over increased sandboxing in Safari, but that's not quite how Apple improved browser security and stability. Instead of trying to sandbox browser plugins within Safari, Snow Leopard now runs them as separate processes. That way if a plugin crashes, it doesn't crash your entire browser.
 
 
This improves security better than just increasing sandboxing, because Safari includes support for a legacy requirement that allows the use of a somewhat less-secure version of a common programming function called malloc that's important for memory management. These plugins now run using the more secure version of malloc used by the rest of Snow Leopard. As separate processes developers potentially have more opportunities to add sandboxing to their plugins. 
 
 
Some WebKit-based plugins still run within the main Safari process, but most of the major plugins have migrated to this new architecture, improving security and stability.
 
 
A New Firewall Setting -- With Leopard, Apple introduced a new firewall capable of restricting inbound access to specific applications, not just network ports and protocols (see "Leopard Firewall Takes One Step Forward, Three Steps Back," 2007-11-05). In Snow Leopard, Apple implemented a minor default usability change some users will want to disable. 
 
 
You can find the settings in the Security system preference pane in the Firewall view. The main view now has just a Start or Stop button in it. If you click the Advanced button, the settings are nearly identical to those in Leopard - but with one minor change: a new checkbox that allows signed software to receive incoming connections automatically.
 
 
This setting allows applications signed by a valid certificate authority - the same authorities that sign Web pages for secure SSL/TLS sessions - to receive incoming connections with no additional steps. Previously, you would have had to add the application or approve a firewall exception when Leopard noted the application trying to set up the incoming connection.
 
 
This bypass was likely included to reduce the number of dialog boxes users need to click when installing software from known companies. Don't worry: even if a program is allowed by default you can still manually change the setting to block access.
 
 
Users who want more control over their security should disable this setting since anyone willing to pay the money can purchase a code signing certificate. Just because a program is signed doesn't necessarily mean you want it to accept incoming connections.
 
 
New Malicious Software Protection -- Back in Mac OS X 10.4 Tiger, Apple introduced a new File Quarantine feature. Enhanced again in Leopard, you receive a warning the first time you run any file that was downloaded using common Internet programs like Mail, Safari, and iChat. 
 
 
In Snow Leopard, File Quarantine now checks these programs to see if they contain certain malicious software, which is sometimes hidden in downloads to trick users into installing them. If the file is infected, you'll see a new warning that explicitly warns you the file is dangerous.
 
 
Right now, according to reports on the Internetthe feature only checks for two known types of malicious software. Apple has stated that additional checks can be added using the normal Software Update program if ever needed.
 
 
This doesn't mean that Apple has added antivirus software to your Mac. Using File Quarantine will protect you from running a limited number of infected files you download using standard programs, but won't catch other malicious files, such as one transferred off a USB drive. The feature also won't necessarily protect you if an attacker exploits your Mac, such as through a web browser vulnerability, and then uses that toehold to install additional malicious software. And it can't remove the infection from compromised files.
 
 
The initial version offers Apple a great capability to quickly push out protection to users in case a larger infection starts to propagate. (For detailed information on how the enhanced File Quarantine feature works, we recommend Dan Moren's excellent article at Macworld.
 
 
A Missed Opportunity -- One major disappointment in the midst of all these security enhancements is that Apple did not improve the Library Randomization feature introduced in Leopard. Known as ASLR, and found in Windows Vista and Windows 7, it's a powerful operating system security technology that nearly wipes out the memory-based attacks we've spent so much time talking about. 
 
 
Library Randomization and ASLR pick different memory locations for key operating system components each time the system starts up. Even if an attacker exploits a vulnerability on your system, it is nearly impossible for them to tie into the operating system and actually do anything malicious (or otherwise) because they can't rely on where the hook can be found.
 
 
Library Randomization in Leopard and Snow Leopard does shift around some important pieces of the operating system, but leaves the memory location of one key component static across all Macs (dyld_ the dynamic loader). With dyld in place, an attacker has a roadmap to continue their exploitation and potentially take over your system.
 
 
Randomizing the location of dyld is no small task, but Apple had a perfect opportunity to make the change with Snow Leopard since so many other important parts of the operating system were being updated. Combined with the 64-bit enhancements, it would make memory exploitation of any type extremely difficult and provide years of worry-free Mac computing.
 
 
Continually Improving Security -- Snow Leopard also includes a few other small changes. Users concerned with privacy can disable location services in the Security preference pane (in the General view, check Disable Location Services). As on the iPhone and iPod touch, Location services allow your current coordinates - derived via Wi-Fi signals as well as future compatible GPS hardware - to be used by system components and third-party software. Date & Time, for instance, now uses Wi-Fi signal snapshots to set your time zone automatically.
 
 
Apple also increasingly phased out the use of the setuid function in the operating system, which reduces security by running processes under administrative or other user accounts.
 
 
It's important to remember that Apple has been slowly enhancing security, sometimes with major enhancements, through Software Update long before the release of Snow Leopard. Sandboxing, increased stack memory protection, reducing use of setuid, adding anti-phishing to Safari, and a series of other changes have found their way onto our Macs outside of major operating system version updates.
 
 
Overall, Snow Leopard is a more-secure operating system than Leopard itself, although Mac users on 32-bit processors won't see all the same benefits.
 
 
Still, I am extremely disappointed that Apple failed to complete Library Randomization. Microsoft has experienced significant real-world security benefits with their adoption of ASLR, and had Apple taken this step they would have practically eliminated memory-based attacks like buffer overflows.
 
 
Although most of the security enhancements in Snow Leopard are hidden deep within the operating system, they should provide practical benefits to all Mac users on 64-bit architectures. While the only true test of security is how effective it is in the real world, on paper it looks like life is now at least a little harder for any potential Mac attackers.

 
Read and post comments about this article | Tweet this article

Fetch Softworks: Fetch 5.5 makes FTP and SFTP easy!Upload, download, mirror, and manage your Web site. Dozens ofnew features to make file transfers easier and more reliable.Get your free trial version at <http://fetchsoftworks.com/>!

 
Copyright © 2009 Rich Mogull. TidBITS is copyright © 2009 TidBITS Publishing Inc. If you're reading this article on a Web site other than TidBITS.com, please let us know, because if it was republished without attribution, by a commercial site, or in modified form, it violates our Creative Commons License.

