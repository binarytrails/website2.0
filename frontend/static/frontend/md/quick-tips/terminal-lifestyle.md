<h1 class="header">Terminal Lifestyle</h1>

Ascii, wine & a keyboard

*27 October 2014* | [Revision History](https://github.com/sevaivanov/kedfilms/commits/master/frontend/static/frontend/md/quick-tips/terminal-lifestyle.md)

## Music on Console

		apt-get install moc
        
Copy and edit the configuration

        cd ~/.moc && cp /usr/share/doc/moc/examples/config.example.gz ./ && gunzip config.example.gz && mv config.example config

Start it

        mocp -T transparent-background


## Command line dictionnary

Download dictionnaries at [web.archive.org](https://web.archive.org/web/20140917131745/http://abloz.com/huzheng/stardict-dic/dict.org/)

		mkdir -p /usr/share/stardict/dic/
		tar -xvjf downloaded_dictionnary.tar.bz2 -C /usr/share/stardict/dic
		tar -xvzf downlaoded_dictionnary.tar.gz -C /usr/share/stardict/dic
		sdcv word


## Midnight Commander
Text base file navigator

		mc -b


## Dynamic Virtual Terminal Manager

[vim] output can get messy but hey, give it a try!

		dvtm

Here are some commands to help you start up

		ctrl+G		Mod command, you type it before every below command

		Mod-c  		Create a new shell window. Ex: (ctrl+G, c)
		Mod-x  		Close focused window.
		Mod-j  		Focus next window.
		Mod-k  		Focus previous window.
		Mod-Space  	Toggle between defined layouts (affects all windows).
		Mod-t  		Change to vertical stack tiling layout.
		Mod-g  		Change to grid layout.
		Mod-q  		Quit dvtm.

<p class="footer">The happiest ending</p>
