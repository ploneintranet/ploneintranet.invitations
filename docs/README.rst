Plone Intranet Invitations
==========================


Build status
------------

Unit tests
~~~~~~~~~~

.. image:: https://travis-ci.org/ploneintranet/ploneintranet.invitations.svg?branch=master
   :target: https://travis-ci.org/ploneintranet/ploneintranet.invitations
.. image:: https://coveralls.io/repos/ploneintranet/ploneintranet.invitations/badge.png?branch=master
   :target: https://coveralls.io/r/ploneintranet/ploneintranet.invitations?branch=master
.. image:: http://jenkins.ploneintranet.net/buildStatus/icon?job=Plone%20Intranet%20Notifications
    :target: http://jenkins.ploneintranet.net/job/Plone%20Intranet%20Notifications/

Robot tests for Plone Intranet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://jenkins.ploneintranet.net/buildStatus/icon?job=Plone%20Intranet%20Suite%20Master
    :target: http://jenkins.ploneintranet.net/job/Plone%20Intranet%20Suite%20Master/badge/


This package provides the following:

Invite users via email
----------------------

Ability to invite users to a plone site using a unique URL, rather than a username and password

- Invites are linked to an email address
- Unique login URL is sent via email
- Accessing unique login URL will create a user account and authenticate them
- Subsequent use of login URL will authenticate

Generic token framework
-----------------------

- Provides a unique url (used to accept the token)
- Fires an event when a token is accepted
- Optionally redirect to a custom path when token is accepted
- Optionally provide limits to tokens
  - Expiry time
  - Number of uses

Installation
------------

- Add ploneintranet.invitations to your buildout eggs
- Activate ploneintranet.invitations via plone control panel

Invitation Usage
----------------

- Control panel -> ploneintranet.invitations
 
Using the token framework
-------------------------

To create a new token:

.. code:: python

    from zope.component import getUtility
    from ploneintranet.invitations.interfaces import ITokenUtility
    
    token_util = getUtility(ITokenUtility)
    token_id, token_url = token_util.generate_new_token()

You can then register an event subscriber that will be trigged when the 
token url is visited:

.. code:: xml

    <subscriber
        for="ploneintranet.invitations.events.ITokenAccepted"
        handler=".subscribers.handle_token_accepted" />
    
.. code:: python

    def handle_token_accepted(event):
        token_id = event.token_id
        # do something cool

Copyright (c) Plone Foundation
------------------------------

This package is Copyright (c) Plone Foundation.

Any contribution to this package implies consent and intent to irrevocably transfer all 
copyrights on the code you contribute, to the `Plone Foundation`_, 
under the condition that the code remains under a `OSI-approved license`_.

To contribute, you need to have signed a Plone Foundation `contributor agreement`_.
If you're `listed on Github`_ as a member of the Plone organization, you already signed.

.. _Plone Foundation: https://plone.org/foundation
.. _OSI-approved license: http://opensource.org/licenses
.. _contributor agreement: https://plone.org/foundation/contributors-agreement
.. _listed on Github: https://github.com/orgs/plone/people
