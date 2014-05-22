Plone Intranet Invitations
==========================

.. image:: https://travis-ci.org/ploneintranet/ploneintranet.invitations.svg?branch=master
    :target: https://travis-ci.org/ploneintranet/ploneintranet.invitations

Generic invitation framework for use with ploneintranet

Installation
------------

- Add ploneintranet.invitations to your buildout eggs

Usage
-----

To use the provided invitation view::

    def do_something():
        return True

To

 - Generate tokens
 - Store token details (hash, limits and current usages)
 - Provides a view (to consume the token)
 - Fires an event when a token is consumed
 - Optionally provide limits to tokens which can be queried for a given token
    - Expiry time
    - Number of uses
 - As an example, also provides a view to invite people to Plone site by email
   creating a user for them
