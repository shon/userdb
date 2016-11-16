Usage
=====

Create `settings.py` with following variables


- SESSIONS_KEY_SEP

  - eg. `-`
- SESSION_KEYS

  - eg. ```['key-1', 'key-2']```

- SESSION_TTL (seconds)

  - eg. `30 * 24 * 60 * 60`

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
