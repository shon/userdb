Usage
=====

Create `settings.py` with following variables


- SESSION_KEY_SEP
- SESSION_KEY_PREFIX
- SESSION_KEYS
- SESSION_TTL (seconds)
- SESSIONS_DB_HOST
- SESSIONS_DB_PORT
- SESSIONS_DB_NO

Example

.. code-block:: python

    SESSION_KEY_SEP = ':'
    SESSION_KEY_PREFIX = 'sid'
    SESSION_KEYS = ['prefs', 'last_seen']
    SESSION_TTL = 30 * 24 * 60 * 60  # (seconds)
    SESSIONS_DB_HOST = 'localhost'
    SESSIONS_DB_PORT = 6379
    SESSIONS_DB_NO = 1



Development Setup
=================

Ubuntu 16.04
--------------


.. code-block:: bash

    mkvirtualenv -p /usr/bin/python3 myenv
    pip install -r pip-requirements.txt
    pip install -r dev_pip-requirements.txt

    # hug -f service.py

Run tests
=========

nose2 tests
