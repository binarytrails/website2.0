<h1 class="header">Server tools</h1>

Basic utilities for monitoring

*27 October 2014*

## Run-level a.k.a. boot manager

		sysv-rc-conf


## What is going on?

[top] is a great tool but a little fade on colors and interactivity...

		htop


## Disk space

Filesystems disk space usage

		df -h

Estimate directories space usage in [h]uman & [s]ummarized

		du -hs


## Ip information

		traceroute www.google.com
		  whois www.google.com | less


## Network statistics

Network statistics of upload & download rates

		vnstat -i wlan0


## Mount ssh directory

[mount]

		sshfs roger@ipaddr:/home/toto /mnt/roger/

[umount]

		fusermount -u mountpoint

<p class="footer">The happiest ending</p>