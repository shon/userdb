Setup
======

Ubuntu 16.04
--------------

mkvirtualenv -p /usr/bin/python3 myenv
pip install -r pip-requirements.txt
pip install -r dev_pip-requirements.txt

# hug -f service.py

Run tests
=========

nose2 tests
