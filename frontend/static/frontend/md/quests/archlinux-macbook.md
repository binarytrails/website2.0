<h1 class="header">Archlinux on MacBook</h1>
</br>
*29 December 2014* | [Revision History](https://github.com/sevaivanov/kedfilms/commits/master/frontend/static/frontend/md/quests/archlinux-macbook.md)

> What MacBook? Pro mid-2011 with Intel CPU & Graphics

> What ArchLinux? ArchLinux x86_64

# Table of content

1. <a href="#preparations">Preparations</a>
2. <a href="#installing">Installing the base system</a>
3. <a href="#configuring">Configuring with finess using Gnome 3</a>
4. <a href="#learnmore">Learn More</a>

# What are my motivations?

1. I was confronted to limitations with Debian.
2. ArchLinux is one level deeper diving into Linux.
3. Honestly, MacBook laptops are the most aesthetic in the 2014 market.

# Results

> TODO


# Guide Flow

I know that you are aware of what you are doing and that you have read or are reading the ArchLinux wiki. Hence, there is no one to blame but yourself for the destruction of your system.

Take this as an example and a proof of a concept.

The ArchLinux wiki is tremendous and the community on freenode servers is great. 

[ArchLinux Mentality](steps.svg)

You should have had read or have the [ArchLinux MacBook wiki page](https://wiki.archlinux.org/index.php/MacBook) open in a separate tab.


<a name="preparations"></a>

# Preparations

## Creating a bootable USB key

Partition: GPT

Filesystem Type: FAT

	dd bs=4m if=arch.iso of=/dev/sdx

## Partitionning

We will use the GPT - UEFI model.

1. Determine the device

		root@archiso ~ # fdisk -l

2. Erase all of your partitions using cgdisk.

	X is the letter of your device. I will use this to define your letter, but don’t assume your drive is sdx. It isn’t, most likely. To find your device, write this command and use your logic.

		cgdisk /dev/sdx

3. Follow the simple partitions model below and adapt it to your needs.

	Gdisk, fdisk, cgdisk & parted **(NOT cfdisk)** adds the first starting offset to the physical sector size reported by the disk in order to align it properly. Basically, the starting offset is just there to guarantee that the first partition and the rest start on a proper boundary. You can use + or % instead of G, Mb in older tools to avoid losing alignment. In our case we will use cgdisk.

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

	Let's setup the dm-crypt (luks) on the entire root sdx3 without lvm.

		cryptsetup -y -v luksFormat /dev/sdx3
		cryptsetup open /dev/sdx3 cryptroot
		mkfs.ext4 /dev/mapper/cryptroot
		mount /dev/mapper/cryptroot /mnt

	*The boot flag is not required with a GPT-UEFI model.*


<a name="installing"></a>

## Installing the base system

Considering cryptroot is mounted at /mnt as previously done. Let's create directories to allow the pacstrap to populate our partitions by using the same directory names as in the /mnt.

	mkdir /mnt/boot && mkdir /mnt/boot/efi
	mount /dev/sdx2 /mnt/boot
	mount /dev/sdx3 /mnt/boot/efi

1. Install the [base] system.

		pacstrap /mnt base

	There is also a more bare-metal called ‘base-devel’ but you will be missing, nano, mkinitcpio and other useful commands.

2. Identifying partitions

		genfstab -p /mnt >> /mnt/etc/fstab

	[Read more](https://wiki.archlinux.org/index.php/Fstab#Identifying_filesystems)

3. Connecting to the system

	It’s time to chroot to configure the system we created. Chrooting allows you to connect to the mounted system and make the main process and all its subprocesses to believe that this directory is the root. Thus, we can install everything we need to the system via USB key.

		arch-chroot /mnt /bin/bash

	Arch-chroot is a wrapper of chroot and by default the command without /bin/bash will point to /bin/sh which, in many Linux systems like Arch, will be pointing back to /bin/bash. Still, it’s a bad habit because in the modern systems it won’t always be the case.

	> One doesn’t need to restart from the beginning if something goes wrong from this point. Take some time to think, to read, ask some questions on IRC freenode channels and think again.

	*It’s time to make the first basic configurations on the system. I will present you mine.*

4. Getting a network connection

	You should use ethernet cable and enable dhcp.

		dhcpcp &
		ping 8.8.8.8

5. Pacman Time! No gaming allowed.

	Let's download a fresh copy of the master package list from the server and force-refresh all packages even if they appear up to date.

		pacman -Syy

	Search for regexp in package database

		pacman -Ss [package]

	Get a package information

		pacman -Si [package]

	Install a package

		pacman -S [package]

	[Read more](https://www.archlinux.org/pacman/pacman.8.html)

	I prefer using [vim] instead of [nano]. It is up to you. Efibootmgr is essential for GRUB that we will use later & net-tools have ifconfig and other usefull commands.

		pacman -S efibootmgr net-tools vim

6. Keyboard

	By default, the keyboard is in English and keys mapping is fine.

	[Language](https://wiki.archlinux.org/index.php/Beginners%27_guide#Change_the_language)
	[Font & Keymap](https://wiki.archlinux.org/index.php/Beginners%27_guide#Console_font_and_keymap)

7. Hostname

		echo "Torvalds" >> /etc/hostname

8. Configure the early user space enviroment a.k.a. ramdisk.

		vim /etc/mkinitcpio.conf

	Insert into *HOOKS* between the words *encrypt* and *filesystems* where *encypt* is before *filesystems*.

		HOOKS="...encrypt...filesystems..."

	Initiate ramdisk enviroment

		mkinitcpio -p linux

	[Read more](https://wiki.archlinux.org/index.php/Mkinitcpio)

9. Configure GRUB bootloader

		vim /etc/default/grub

	Change this line to make it look like this

		GRUB_CMDLINE_LINUX="cryptdevice=/dev/sdx3:cryptroot"

	[Read more](https://wiki.archlinux.org/index.php/Dm-crypt/System_configuration#cryptdevice)

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

	Now you can safely exit the chroot, unmount your partitions and reboot into your new fresh system.

		exit
		umount /mnt/boot/efi
		umount /mnt/boot
		umount /mnt
		reboot

	Cross your fingers and hold tight, we hope you will enjoy your flight!


<a name="configuring"></a>

## Configuring with finess using Gnome 3

> TODO

<a name="learnmore"></a>

## Learn More

### MBR VS GPT

The Master Boot Record (MBR) was developed during the 1980’s.

GUID Partition Table (GPT) was developed during the 1990’s.
</br>
MBR disks only have 1 partition table to keep track of all the blocks in the partition and is limited to 3 primary partitions and 1 extended partition.

GPT can have many partition tables and is limited to 128 partitions per disk.
</br>
MBR partitions are being limited to 2TB (terabytes) in size. 

GPT partitions are being limited to 18 EB (Exabyte’s) or 1 million terabytes.
