<h1 class="header">Archlinux on MacBook</h1>
</br>
*29 December 2014* | [Revision History](https://github.com/sevaivanov/kedfilms/commits/master/frontend/static/frontend/md/quests/archlinux-macbook.md)

> What MacBook? MacBook Pro mid-2011 with Intel CPU & Graphics.

> What ArchLinux? ArchLinux x86_64.


# What are my motivations?

1. Help curious minds to get into something delightful.
2. ArchLinux is one level deeper diving into Linux.
3. MacBook laptops are the most aesthetic in the 2010s market.


# Results

> TODO


# Guide Flow

I know that you are aware of what you are doing and that you have read or are reading the ArchLinux wiki. Hence, there is no one to blame but yourself for the destruction of your system.

Take this as an example and a proof of concept.

The ArchLinux wiki is tremendous and the community on freenode servers is great. 

[ArchLinux Mentality](steps.svg)

You should have had read or have the [ArchLinux MacBook wiki page](https://wiki.archlinux.org/index.php/MacBook) open in a separate tab.


# Table of content

1. [Preparations](#preparations)

	2.1 Determine the device.

	2.2 Erase all of your partitions using cgdisk.

	2.3 Follow the simple partitions model below and adapt it to your needs.

	2.4 Format the partitions.

2. [Installing the base system](#installing)

	2.1 Installing the base system

	2.2 Identifying partitions

	2.3 Connecting to the system

	2.4 Localtime

	2.5 Language

	2.6 Keyboard

	2.7 Hostname

	2.8 Getting a network connection

	2.9 Pacman Time! No gaming allowed.

	2.10 Configuring the early user space enviroment a.k.a. ramdisk

	2.11 Configuring GRUB bootloader

	2.12 Last notes

3. [Configuring with finess using Gnome 3](#configuring)

	3.1 Get your MacBook Arch drivers.
	
	3.2 Get Gnome 3.

	3.3 Create & Configure a New User.

	3.4 Configure the WIFI using AUR & package build.

	3.5 Add transparency to windows.

4. [Problem Solving](#problem-solving)

	* Tweak Tool: Error on Global Dark Theme

	* eog: Can't open jpeg photos

5. [Learn More](#learnmore)

	* MBR VS GPT


<a name="preparations"></a>
# Preparations

## Creating a bootable USB key

Partition: GPT

Filesystem Type: FAT

	dd bs=4m if=arch.iso of=/dev/sdx

## Partitionning

We will use the GPT - UEFI model.

1. Determine the device.

		root@archiso ~ # lsblk

2. Erase all of your partitions using cgdisk.

	X is the letter of your device. I will use this to define your letter, but don’t assume your drive is sdx. It isn’t, most likely. To find your device, write this command and use your logic.

		cgdisk /dev/sdx

3. Follow the simple partitions model below and adapt it to your needs.

	Gdisk, fdisk, cgdisk & parted **(NOT cfdisk)** adds the first starting offset to the physical sector size reported by the disk in order to align it properly. Basically, the starting offset is just there to guarantee that the first partition and the rest start on a proper boundary. You can use + or % instead of G, Mb in older tools to avoid losing alignment. In our case, we will use cgdisk.

	[Read more](http://www.ibm.com/developerworks/library/l-linux-on-4kb-sector-disks/index.html)

	We will encrypt our third root partition sdx3 and we won't use swap space for the hibernation.

	<table>
		<tr>
			<th>Partition</th>
			<th>Size</th>
			<th>Type</th>
			<th>Name</th>
		</tr>
		<tr>
			<td>sdx1</td>
			<td>200MB</td>
			<td>ef00</td>
			<td>/boot/efi</td>
		</tr>
		<tr>
			<td>sdx2</td>
			<td>100MB</td>
			<td>8300</td>
			<td>/boot</td>
		</tr>
		<tr>
			<td>sdx3</td>
			<td>The Rest</td>
			<td>8300</td>
			<td>root</td>
		</tr>
	</table>

		First sector (2048, default = ...): [Enter]
		Size in sectors or {KMGTP} (default = ...): [Size]
		Current type is 8300 (Linux filesystem)
		Hex code or GUID (L to show codes, Enter = 8300): [Type] 
		Current partition name is ''
		Enter new partition name, or  to use the current name: [Name]

	You can always consult the cgdisk [walkthrough](http://www.rodsbooks.com/gdisk/cgdisk-walkthrough.html) to be sure.

	Afterwards, [ verify ] and [ write ] and you are done partitioning.

4. Formatting the partitions

		mkfs.vfat /dev/sdx1
		mkfs.ext2 /dev/sdx2
		mkfs.ext4 /dev/sdx3

	[Read more](https://help.ubuntu.com/community/LinuxFilesystemsExplained)

	Let's set up the dm-crypt (luks) on the entire root sdx3 without lvm.

		cryptsetup -y -v luksFormat /dev/sdx3
		cryptsetup open /dev/sdx3 cryptroot
		mkfs.ext4 /dev/mapper/cryptroot
		mount /dev/mapper/cryptroot /mnt

	*The boot flag is not required with a GPT-UEFI model.*


<a name="installing"></a>
## Installing the base system

As was previously done, the cryptroot is mounted at /mnt. Let's create directories to allow the pacstrap to populate our partitions by using the same directory names as in the /mnt.

	mkdir /mnt/boot && mkdir /mnt/boot/efi
	mount /dev/sdx2 /mnt/boot
	mount /dev/sdx3 /mnt/boot/efi

1. Installing the base system

		pacstrap /mnt base

	There is also a more bare-metal called ‘base-devel’ but you will be missing, nano, mkinitcpio and other useful commands.

	*DO NOT mount your system elsewhere than at /mnt. Pacstrap works with /mnt folder. Otherwise you will get something really weird -> [What Went Wrong? : Pacstrap](#www-pacstrap).

2. Identifying partitions

		genfstab -p /mnt >> /mnt/etc/fstab

	[Read more](https://wiki.archlinux.org/index.php/Fstab#Identifying_filesystems)

3. Connecting to the system

	It’s time to chroot to configure the system we created. Chrooting allows you to connect to the mounted system and make the main process and all its subprocesses to believe that this directory is the root. Thus, we can install everything we need to the system via USB key.

		arch-chroot /mnt /bin/bash

	Arch-chroot is a wrapper of chroot and by default the command without /bin/bash will point to /bin/sh which, in many Linux systems like Arch, will be pointing back to /bin/bash. Still, it’s a bad habit because in the modern systems it won’t always be the case.

	> One doesn’t need to restart from the beginning if something goes wrong from this point. Take some time to think, to read, ask some questions on IRC freenode channels and think again.

	*It’s time to make the first basic configurations on the system. I will present you mine.*

4. Localtime

		ln -s /usr/share/zoneinfo/Canada/Eastern /etc/localtime

5. Language

	> Locales are used by glibc and other locale-aware programs or libraries for rendering text, correctly displaying regional monetary values, time and date formats, alphabetic idiosyncrasies, and other locale-specific standards. - ArchWiki

	Open locale.gen and uncomment the two rows for your keyboard. i.e. en_US...

		nano /etc/locale.gen

	Create the /etc/locale.conf file substituting your chosen locale manually or by issuing

		echo LANG=en_US.UTF-8 > /etc/locale.conf

	Generate your locale configuration

		locale-gen

6. Keyboard

	By default, the keyboard is in English and keys mapping is fine.

	[Language](https://wiki.archlinux.org/index.php/Beginners%27_guide#Change_the_language)
	[Font & Keymap](https://wiki.archlinux.org/index.php/Beginners%27_guide#Console_font_and_keymap)

7. Hostname

		echo "Torvalds" >> /etc/hostname

8. Getting a network connection

	You can use ethernet cable and enable dhcp.

		dhcpcp &
		ping 8.8.8.8

	Otherwise

		wifi-menu

9. Pacman Time! No gaming allowed.

	Let's download a fresh copy of the master package list from the server and force-refresh all packages even if they appear up to date.

		pacman -Syy

	Search for regexp in package database

		pacman -Ss [package]

	Get the package information

		pacman -Si [package]

	Install a package

		pacman -S [package]

	[Read more](https://www.archlinux.org/pacman/pacman.8.html)

	I prefer using [vim] instead of [nano]. It is up to you. Efibootmgr is essential for GRUB, that we will use later, & net-tools have ifconfig and other useful commands.

		pacman -S efibootmgr net-tools vim

	> The pkgfile searches the .files metadata created by repo-add(8) to retrieve file information about packages. By default, the provided target is considered to be a filename and pkgfile will return the package(s) which contain this file.

		pacman -S pkgfile; pkgfile -u

	For instance, you could find

		root@arch ~ # pkgfile -s ifconfig
		core/net-tools


10. Configure the early user space enviroment a.k.a. ramdisk.

		vim /etc/mkinitcpio.conf

	Insert into *HOOKS* between the words *encrypt* and *filesystems* where *encypt* is before *filesystems*.

		HOOKS="...encrypt...filesystems..."

	Initiate ramdisk enviroment

		mkinitcpio -p linux

	[Read more](https://wiki.archlinux.org/index.php/Mkinitcpio)

11. Configure GRUB bootloader

		vim /etc/default/grub

	Change this line to make it look like this

		GRUB_CMDLINE_LINUX="cryptdevice=/dev/sdx3:cryptroot"

	[Read more](https://wiki.archlinux.org/index.php/Dm-crypt/System_configuration#cryptdevice)

	And this line

		GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"

	> The presence of the word **splash** enables the splash screen with condensed text output. Adding the parameter **quiet** will only show the splash screen. In order to enable the *normal* text start up, you should remove both of these.

	[Read more](https://wiki.archlinux.org/index.php/GRUB#Additional_arguments)

	Install the bootloader

		modprobe dm-mod
		grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=arch_grub --recheck --debug
		mkdir -p /boot/grub/locale
		cp /usr/share/locale/en\@quot/LC_MESSAGES/grub.mo /boot/grub/locale/en.mo

	Generate a configuration 

		grub-mkconfig -o /boot/grub/grub.cfg

	[Read more](https://wiki.archlinux.org/index.php/MacBook#Installing_GRUB_to_EFI_partition_directly)

	Find your devices UUID's

		blkid

	Verify by looking for UUID of your cryptroot and root inside. These are simple commands that will be run on boot time. Try to understand the logic in order to find where to look.
		
		vim -R grub.cnf

12. Last notes

	If you're planning to use **wifi-menu** instead of the ethernet cable for further installations after booting into your system, you should install its dependencies right away.

		pacman -S dialog wpa_supplicant

	Now you can safely exit the chroot, unmount your partitions and reboot into your new fresh system.

		exit
		umount /mnt/boot/efi
		umount /mnt/boot
		umount /mnt
		reboot

	Cross your fingers and hold tight, we hope you will enjoy your flight!


<a name="configuring"></a>
## Configuring with finess using Gnome 3

Welcome to your new system!

In this section, I will help you get started with a basic **G**raphical **U**ser **I**nterface and a basic system configuration using Gnome 3.

1. Get your MacBook Arch drivers

	Graphic card
	
		lspci | grep VGA
		pacman -S xf86-video-intel

	Touchpad

		pacman -S xf86-input-synaptics

	Everything else worked out of the box. Otherwise, go to the [post-installation](https://wiki.archlinux.org/index.php/MacBook#Post-installation) section.

		reboot

2. Get Gnome 3

	Living in Bash interpreter is o.k. but it can get a little depressing during the lazy days.

	> GNOME (pronounced /ɡˈnoʊm/ or /ˈnoʊm/) Shell is the graphical shell of the GNOME desktop environment starting with version 3 - Wikipedia

	I suggest you install the **gnome** group instead of *gnome-extra* and you should definetly learn the purpose of each [package](https://www.archlinux.org/groups/x86_64/gnome/) inside. You will be aware of what will be running in your system and it could even save some of your precious ressources on a daily basis. You can always install more of the packages later using pacman.

		pacman -S gnome

	Start Gnome

		systemctl start gdm

	You should be logged in as root, if not then write **root** as username and hit enter.

	[Read More](https://wiki.archlinux.org/index.php/Gnome#Installation)

3. Create & Configure a New User

	Go into *Settings* > *Users* and create a new administrator user.

	To allow this user to run commands we will use the [sudoers](https://wiki.archlinux.org/index.php/Sudo) powers.

			pacman -S sudo

	To open this file you have do the following with the editor of your choice. Mine is vim.

			EDITOR=vim visudo

	Add the last line to this section

			##
			## User privilege specification
			##
			root ALL=(ALL) ALL
			new_awesome_username ALL=(ALL) ALL

	Logout and login as the user that you have created.

4. Configuring the WIFI using AUR & package build

	**You should definitly read the [AUR wiki page](https://wiki.archlinux.org/index.php/Arch_User_Repository).**

	Install this group package to be able to makepkg.

		pacman -S --needed base-devel

	I succeeded with [broadcom-wl](https://aur.archlinux.org/packages/broadcom-wl/) that is in AUR. For other WIFI drivers -> [Read More](https://wiki.archlinux.org/index.php/MacBook#Wi-Fi).

		mkdir ~/Builds && cd ~/Builds

	Under Package Actions > Download tarball , save it to ~/Builds.

		mkdir broadcom-wl
		tar xvf broadcom-wl.tar.gz broadcom-wl/

	Read the PKGBUILD file carefully because shell commands will be executed from it.

		cd broadcom-wl/ && vim -R PKGBUILD

	Makepkg and **-s** will resolve all of its dependecies.

		makepkg -s PKGBUILD

	Install the driver.

		pacman -U broadcom-wl.tar.xz

	Unload other conflicting modules.

		rmmod b43
		rmmod ssd

	Load the wl module.

		modprobe wl

	[Read More](https://wiki.archlinux.org/index.php/Broadcom_BCM4312#Loading_the_wl_kernel_module)

5. Add transparency to windows

	Devilspie is THE tool to use. It works with S-expressions.

	> Devil's Pie can be configured to detect windows as they are created, and match the window to a set of rules. If the window matches the rules, it can perform a series of actions on that window.

		mkdir ~/.devilspie/
		touch ~/.devilspie/gnome-terminal.ds

	Here is an example of **gnome-terminal.ds** to lower the gnome terminal opacity.

		(if
			(is (application_name) "Terminal")
			(begin
				(opacity 85)
			)
		)

	The command below will show you the results with the current window.

		devilspie
		ctrl+C

	You can use it to see the proprieties of the open windows.

	And please remember...

	> A totally crack-ridden program for freaks and weirdos who want precise control over what windows do when they appear - [Gnome-Wiki](https://wiki.gnome.org/Projects/DevilsPie)

	Funny guys!


<a name="problem-solving"></a>
## Problem Solving

Wait. Something went really wrong and you need help?

		echo "Spiderman Days" | curl -F 'sprunge=<-' http://sprunge.us

Get your command output and go to #archlinux on irc.freenode.net and believe in humanbeing goodwill.

### Tweak Tool: Error on Global Dark Theme

A tool to customize advanced GNOME 3 options.

Error On: Enabling Global Dark Theme
Solution:

		touch ~/.config/gtk-3.0/settings.ini

### eog: Can't open jpeg photos

Get the codecs

		pacman -S imlib libjpeg-turbo jasper mjpegtools openjpeg


<a name="learnmore"></a>
## Learn More

### MBR VS GPT

The Master Boot Record (MBR) was developed during the 80’s.

GUID Partition Table (GPT) was developed during the 90’s.
</br>
MBR disks only have one partition table to keep track of all the blocks in the partition and is limited to three primary partitions and one extended partition.

GPT can have many partition tables and is limited to 128 partitions per disk.
</br>
MBR partitions are being limited to 2TB (terabytes) in size. 

GPT partitions are being limited to 18 EB (Exabyte’s) or 1 million terabytes.

<p class="footer">Goodbye dear deer.</p>