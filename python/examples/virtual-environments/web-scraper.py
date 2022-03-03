# Please make sure to read all of the instructions below before
# attempting to run this example.
#
# We are going to learn how to create a virtual environment and
# install 3rd party Python libraries using pip.
#
# If you are using Python 3 (which you definitely should), there
# is a built-in feature that allows you to create a sandbox for
# your python project. This sandbox includes a full version of
# the current Python installation and a few scripts to help you
# activate and deactivate this environment. Now, a question might
# arise such as "Why would I want this virtual environment thing?"
# A perfectly reasonable question. When we are working on a project
# sometimes we might be using a specific version of Python, or of a
# library necessary for our project. However, we are busy people, and
# this might not be the only project we are working on. It is also
# possible that different projects we are working on might use the
# same library, but be compatible with different versions of that
# library. This poses a problem because the default behavior when
# installing new packages for use in Python is to install them
# in a way such that all of our projects would need to use the
# same version. This is where virtual environments can help as
# our whole python install and packages in the virtual environment
# is isolated for a single directory where our project resides.
#
# Let's explore this. Open your VS Code terminal and make sure that
# your terminal is inside this virtual-environments directory on
# Mac you can run the pwd command or on Windows you can run the
# cd command. The end of the path should say "virtual-environments"
#
# Once you have that verified run the following command:
# On Mac: python3 -m venv env
# On Windows: python -m venv env
# Make sure to be patient in might take a bit to setup. 
# This command tells the python interpreter to run a module (-m) named
# venv (short for virtual environment). When it finishes you should
# notice that you have a new folder called env which contains all the
# important virtual environment stuff.
#
# This is just the first part, we need to activate this environment so
# we aren't using our normal Python install. You can do this with the 
# following command:
# On Mac: source env/bin/activate
# On Windows: env\Scripts\activate
# If all goes well you should see the text (env) in your terminal window.
# You are now using the Python that is inside the virtual environment.
# From here everything behaves normally with the exception that on MacOS
# you no longer need to type python3, just python will do in this
# environment.
#
# Now this program is going to use a third-party library called requests
# to access websites (and more). To install it, you will use the package
# manager that comes with Python3 called pip. Let's install requests with
# the command: pip install requests
# Pip will download and install the package for you and when it's done you
# are all set to import it. To help us make sense of the webpage content
# that requests can download, we are going to also use Beautiful Soup.
# Install that too using: pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# This is the web address we are going to access. Go ahead and open this up
# in a webbrowser tab.
URL = "https://realpython.github.io/fake-jobs/"

# Requests will visit the page and get us some information
page = requests.get(URL)

# We can access the HTML code that makes up the webpage like
# this. The problem is we don't want to have to manually process
# the page data like a big string...we have a better way.
# print(page.text)

# Beautiful soup can parse the text for us and give us a nice
# object to work with with convenient methods.
soup = BeautifulSoup(page.content, "html.parser")

# On this page, I want to find all the job titles listed on this page
# and print them all. I know that on this page, they are contained in
# a tag <h2> with the class name "title is-5". You can find this
# information using your webbrowsers developer tools (specifically the
# inspector and element selector tools). Let's try and find them all.
job_names = soup.find_all("h2", class_="title is-5")
for job_name in job_names:
    print(job_name.text)

# When you are done using this program you might want to leave the virtual
# environment. To do so, you can use the command: deactivate
# You should notice that your terminal no longer contains the (env) text
# and at this time you are now using your "normal" version of python.

# I'm not going to try and cover all of requests or beautiful soup here,
# but you can find more documentation on how these libraries work at their
# websites:
# * Requests - https://docs.python-requests.org/en/latest/
# * Beautiful Soup - https://beautiful-soup-4.readthedocs.io/en/latest/
#
# You can also get a jump start with this nice tutorial from RealPython:
# * https://realpython.com/beautiful-soup-web-scraper-python/
#
# There is also a book on O'Reilly if you are interested in this topic:
# * https://learning.oreilly.com/library/view/python-web-scraping/9781786462589/
#
# PLEASE DO KEEP SOME THINGS IN MIND.
# * Bandwidth does cost money, so do not over request resources from a website
# * If you make too many requests too rapidly, you can limit a site's ability
#       to service other visitors. Be kind about how many requests you make
#       per second (limit it to only a few tops).
# * Beware of bugs/errors that might cause you to accidentally make too many
#       requests
# * Respect the robots.txt file on a site. You can learn more about that here
#       (https://developers.google.com/search/docs/advanced/robots/intro) or
#       from doing some googling.
# * If you intend to build a website crawling application or scraper, make
#       sure to follow webscraping guidelines and etique.
# * Violating some of these above bullet points might get your IP address
#       blocked by the site as they may think you are running malicious
#       software, so play nice and be careful.
