<h1 class="header">Host Django Website</h1>
</br>
*31 October 2014*

# Cloud hosting

## [Gandi](https://www.gandi.net)

### Why choose it? 

1. They have a great history of supporting freedoom and privacy on the internet. They [support](https://www.gandi.net/supports/) many projects, either financially, technically, administratively, or morally. 

2. The documentation is almost perfect.

3. The prices and discounts are just amazing.

4. They do not store your credit card information.


### How do I get started ?

Well their documentation covers pretty much everything. I struggled in a few sections. This Quick Tip should help you get going after painful hours of misunderstanding!

1. Buy a domain name

2. Take a [Simple Hosting](https://www.gandi.net/hosting/simple?language=python&db=mysql&grid=A) free testing instance for 5 days.

	Afterwards, you can renew it for a year with 5$/month -> 30$/1st year = 60$ - 30$ with a first use discount.

3. Configure your instance

	To enter your server via ssh, you have to activate via the web pannel.

		ls web/vhosts/default/

	Here will be hosted your instance project. From this point you can read their [django-simple-hosting](http://wiki.gandi.net/en/simple/instance/python) documentation. It is important that you read it carefully. This part is crutial...

	> You must use Git to commit and push this file to the instance for it to be used.

	It means that you have to create a repository with Git [git-simple-hosting](http://wiki.gandi.net/en/simple/git) that will push the code to a Git repository **associated by name** to your default [vhost] folder seen earlier.

		mkdir -p gandi/roger/default
		  cd gandi/roger/default
		  git init
		  git remote add origin ssh+git://12345@git.alien.gpaas.net/default.git
		  echo "hi" > test
		  git add test
		  git commit -m "test" test
		  git push origin master


	One important thing to understand is that right now Gandi does not support Git submodules. It means that you can't create a repository for your simple hosting instance and put your github external repository with the [.git/] folder inside. Otherwise, it will commit an empty folder to your Gandi repository. I know, it means it is a sync party! You will have to sync your external Github repository to your local Gandi one by hand. You can achieve that with [rsync].

		rsync -az source/ destination/

	Add delete option to remove everything that is in [destination/] but not in the [source/].

		rsync -az --delete source/ destination/


	For some reason, deploying code didn't work via the admim web pannel. Hence, to deploy your code from your Gandi Git repository to your web server, you must do it by handy hand.

		ssh 12345@git.alien.gpaas.net 'deploy default.git'


	Assuming you /vhost/default looks like

		default
		  ├── requirements.txt
		  ├── wsgi.py
		  ├── myproject
		  │   ├── myapp
		  │   ├── manage.py
		  │   ├── myproject
		  │   │   ├── __init__.py
		  │   │   ├── settings.py
		  │   │   ├── urls.py

	Your *wsgi.py* file should be

		import os, sys

		  django_project = os.path.abspath(os.path.join(os.path.dirname(__file__), 'myproject'))
		  sys.path.append(django_project)

		  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
		  from django.core.wsgi import get_wsgi_application
		  application = get_wsgi_application()

	</br>
	[Domain-as-website](http://wiki.gandi.net/en/domains/management/domain-as-website)

	It is important that you understand how to connect your domain name to your website. There are three ways to do it. I suggest you the third one: *Configuring your zone file at Gandi*. It can take up to a few hours before it spreads in the World Wide Web. It's a great occasion to take a cup of tea and read a book!


<p class="footer">Everything else is explained very clearly in the Gandi.net documentation.</p>