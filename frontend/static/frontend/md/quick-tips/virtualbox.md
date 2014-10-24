<h1 class="header">Virtualbox</h1>

[www.virtualbox.org](https://www.virtualbox.org/)

I am assuming you know what are the magnificent sudo powers.

## Install Guest Additions via terminal

1. Devices menu > Install Guest Additions CD Image

2. In the server

		mount /dev/cdrom /media/cdrom
		  cd /media/cdrom && ls -l

3. Install

		./VBoxLinuxAdditions.run

4. If you got missing build tools or dependencies

		apt-get install -y dkms build-essential linux-headers-generic linux-headers-$(uname -r)


## Boot from usb

You must boot virtualbox as root to have access to sdX or play with priviledges

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

<p class="footer">The happy end</p>