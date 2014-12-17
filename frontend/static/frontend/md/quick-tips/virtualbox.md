<h1 class="header">Virtualbox</h1>

[www.virtualbox.org](https://www.virtualbox.org/)

*27 October 2014* | [Revision History](https://github.com/sevaivanov/kedfilms/commits/master/frontend/static/frontend/md/quick-tips/virtualbox.md)

 I am assuming you know what are the magnificent [sudo] powers.

## Guest Additions would not work !!!

Install the dependencies

        apt-get install -y dkms build-essential linux-headers-generic linux-headers-$(uname -r)

*Unable to run them or they are nowhere to be found?*

Sadly, they never worked for me out of the box.

        Devices menu > Install Guest Additions CD Image

If it throws an error it means that in most of the cases that they are already inserted.

In the vbox machine, open a terminal and locate them. They should be at [sr0].

        lsblk

If they are mounted at [/dev/cdrom]

        umount /dev/cdrom

Afterwards, whenever they were mounted or not

        mkdir /dev/vboxguests
          mount /dev/sr0 /dev/vboxguests
          ls -l /dev/vboxguests

They should be mounted as [read-only] and you should only be able to execute them as a normal user with sudoer powers.

        sudo ./VBoxLinuxAdditions.run
          reboot

## Boot from usb

You must boot virtualbox as root to have access to [sdX] or play with privileges.

	VBoxManage internalcommands createrawvmdk -filename usb_sdc.vmdk -rawdisk /dev/sdc


## Debian Guess Additions image location

	ls -l /usr/share/virtualbox/VboxGuestAdditions.iso


## Usb not detected

1. Install the extension pack
2. Add your user to vboxusers

		groups roger
		  adduser roger vboxusers


## Kernel driver not installed (rc=-1908)

	apt-get install dkms
	  /etc/init.d/vboxdrv setup


## Resize screen dimentions by hand

	vboxmanage setextradata "roger-vm" "CustomVideoMode1" "1366x768x32"

<p class="footer">The happiest ending</p>
