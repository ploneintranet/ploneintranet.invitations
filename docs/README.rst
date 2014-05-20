.. image:: https://travis-ci.org/ploneintranet/ploneintranet.invitations.svg?branch=master :target:  https://travis-ci.org/ploneintranet/ploneintranet.invitations
.. image:: https://coveralls.io/repos/ploneintranet/ploneintranet.invitations/badge.png :target: https://coveralls.io/r/ploneintranet/ploneintranet.invitations
Introduction
============

Generic invitation framework for use with ploneintranet
 - Generate tokens
 - Store token details (hash, limits and current usages)
 - Provides a view (to consume the token)
 - Fires an event when a token is consumed
 - Optionally provide limits to tokens which can be queried for a given token
    - Expiry time
    - Number of uses
