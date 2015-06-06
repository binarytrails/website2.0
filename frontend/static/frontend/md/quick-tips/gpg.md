<h1 class="header">GNU Privacy Guard</h1>

[Public-key cryptography](http://en.wikipedia.org/wiki/Public-key_cryptography)

*27 October 2014* | [View On Github](https://github.com/sevaivanov/kedfilms/blob/master/frontend/static/frontend/md/quick-tips/gpg.md#gnu-privacy-guard) | [Revision History](https://github.com/sevaivanov/kedfilms/commits/master/frontend/static/frontend/md/quick-tips/gpg.md)

Driving your car is a privilege not your privacy.

Almost every email client i.e. Icedove & Thunderbird supports [gpg].
This can make it very transparent in a daily based routine with some per-recipient rules.


## How secure?

As far as I know, there are acoustic cryptanalysis guys that managed to decrypt it by listening to the computer sounds from a short distance with a smartphone or a more sophisticate software. It is called a side channel attack because it is not direct and unconventional, hence often unsecured. You can find more in the world wide internet on this subject.

In that case, someone has to be physically close to you while you are performing your daily [gpg] duties. If you are this deep in the rabbit hole then I suggest you to change your keys very frequently or to be never close to anything technological while performing your tasks.

Take a little breath... You will probably never get that far.


## Generating your key

I have to advise you to choose the RSA and RSA (for signing and encrypting) with a 4096 bit long key for an optimal security. Your name, email & comment can be anything you want depending on your needs. It is important to know that you won't be able to change them once your key is created.

		gpg --gen-key


## Encrypting

The fastest way is to use echo directly.

		echo "dear deer" | gpg --encrypt --armor --recipient "Roger"

Another way is to use [more] to pass the file content to [gpg].

		more message | gpg -e -a -r "Roger"

In case you are using this method, it is very important that you understand 
how to efficiently destroy your history file or the file. Do not use [rm], use [shred].


## Decrypting

In this case you don't have to worry about file destruction (it is encrypted).

		echo "-----BEGIN PGP MESSAGE-----
		Version: GnuPG v1.4.12 (GNU/Linux)

		hQIMA8LsxNwWC0LgARAAhZgg+SyNc2SW2GHIclRNbl6534wnWmdrMkBK5LZXvirP
		y1jbCMjSCcGY8kzkuQZ07KfFYv7uwCDcs7RFxgYUwV1O71egLnslG+FYAAA/EY0f
		z4wJBJBtToIN/Ii83pvOvxchwKgynMyQ5/5mT8CFhuRsLrYrS/zxI7bnbAhETDep
		jh3WTVTpg6Bz/rRGqyHVADSXJdrALNzd0fZG5yP+rksgB01SljjhIIAn9vvEzpTS
		QAE26eH2Uz99e2xoRONU4Whs/+Jul9r3v8XLuGlyTIq5thLyCFqdaPQyNp7rFgPM
		tsfiPEo94XJ4z+TFqanNjG8=
		=L9Js
		-----END PGP MESSAGE-----" | gpg --decrypt



You can always export it to file by adding [> output]

		echo "encrypted message" | gpg -d > output


## Exporting

		gpg --export -a "Roger" > public.key
		gpg --export-secret-key -a "Roger" > private.key


## Importing

		gpg --import public.key
		gpg --allow-secret-key-import --import private.key


## Deletion

		gpg --delete-key "Name"
		gpg --delete-secret-key "Name"


## Compress & Encrypt

		tar czvpf - dir/ | gpg --symmetric --cipher-algo aes256 -o backup.tar.gz.gpg


## Decrypt & Extract

		gpg -d backup.tar.gz.gpg | tar xzvf -


<p class="footer">I haven't covered the key revocation topic. </br>For more privacy, go ahead and read about Tor, I2P & Tails operative system</p>