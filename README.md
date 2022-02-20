![Supported Python version](https://img.shields.io/badge/python-3.7+-blue.svg)

# Description:
 
Like Skiptracer but for the uk.
SkiptracerUK peforms recon attacks and finds information about a target. SkiptracerUK mainly uses basic python webscraping.


# What can it do:

Skiptracer will alow you to search with the following queries:

* UK car plate search
* Usernames
* IP addresses

More search queries coming soon!

# How to install and use SkiptracerUK:

* Download the repository with `git clone https://github.com/Samuel20354/SkiptracerUK.git`
* run `cd SkiptracerUK`
* then run `python3 -m pip install -r requirements.txt`
* and finaly run `python3 SkiptracerUK.py`

Done, enjoy SkiptracerUK!

# What I hope to add:

* UK name search
* ~VIN finder to the plate search~ (Turns out that it is illegal to get a car's VIN without a cause. Read more [here](https://www.gov.uk/data-requests-dvla))
* Phone number look up

# Bugs that I know of and how to fix them:

* `FileNotFoundError: [Errno 2] No such file or directory: 'plugins/'` try just run SkiptracerUK again, and it should be fixed. Idk why it happens.
* When exiting using the method in the script it some times doesn't exit just use the same method again and it will exit. 
* Some times when running plate or ip search it wont return you back to the menu just run the script again.

#### Credit to Critical-Function956 over at reddit for helping me out
