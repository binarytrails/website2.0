<h1 class="header">OWASP Security Shepherd</h1>

*17 december 2014* | [Revision History](https://github.com/sevaivanov/kedfilms/commits/master/frontend/static/frontend/md/hacks/owaspshepherd.md)

</br>

>   Security Shepherd is a computer based training application for web and mobile application security vulnerabilities. This project strives to herd the lost sheep of the technological world back to the safe and sound ways of secure practices. Security Shepherd can be deployed as a CTF (Capture the Flag) game or as an open floor educational server. **-[www.owasp.org](https://www.owasp.org/index.php/OWASP_Security_Shepherd)**

# Installation

1. [Download it](http://sourceforge.net/projects/owaspshepherd/files/)

2. Setup Host Only network

    Fire up the virtualbox manager

        File > Preferences > Network > Host-only Networks
        Click on add

    The default configuration is fine

3. Remove the NAT to keep host-only.

4. The networking auto-configuration failed for me.

    *Tested with v2.11 on Debiana amd64 in Virtualbox 4.3.20*

    Login into the virtual machine

        login: securityshepherd
        password: owaspSecurityShepherd

    Find the interface name

        ifconfig -a

    Add it to the interfaces for the boot setup, i.e. [eth4].

        echo "
            auto eth4
            iface eth4 inet dhcp
        " >> /etc/network/interfaces

    Reboot and find your ip

          sudo reboot
          ifconfig

5. Go to the web interface from the host machine and log in.

        Username: admin
        Password: password

    Change the [core] & [exposed] addresses to your virtual machine ip addresses

        http://<VM IP Address>/
        http://<VM IP Address>/Exposed/

Have fun!
