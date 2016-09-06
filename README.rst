==============
discord_simple
==============

.. image:: https://img.shields.io/pypi/v/discord_simple.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/discord_simple
   :alt: PyPi Package Version

.. image:: https://img.shields.io/pypi/pyversions/discord_simple.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/discord_simple
   :alt: Supported python versions

.. image:: https://travis-ci.org/askovpen/discord_simple.svg?branch=master
   :target: https://travis-ci.org/askovpen/discord_simple
   :alt: Travis CI Status

----------
Installing
----------

.. code:: shell

    $ pip install discord_simple --upgrade

-----
Usage
-----

.. code:: python

    import discord_simple

    bot=None

    def on_connect(user):
      print("connected as "+user)
    def on_message(message):
      print("message from {}: {}".format(message.author,message.content))

    bot = discord_simple.Bot("your token",on_connect=on_connect,on_message=on_message)
    bot.forever_loop()
---
API
---

User
----

* ``id``
* ``avatar``
* ``username``                                                                                                                                                           
* ``discriminator``

Message                                                                                                                                                            
-------

* ``author`` : `User`_                                                                                                                                             
* ``content`` : Message text                                                                                                                                             
* ``timestamp``                                                                                                                                                         

Methods                                                                                                                                                           
-------
* ``send_message('username#discriminator','message')``  
