import unittest
from zope.component import getUtility
from zope.component import getMultiAdapter
from ploneintranet.invitations.interfaces import ITokenUtility

from ploneintranet.invitations.testing import \
    PLONEINTRANET_INVITATIONS_INTEGRATION_TESTING


class TestViews(unittest.TestCase):

    layer = PLONEINTRANET_INVITATIONS_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.util = getUtility(ITokenUtility)

    def test_accept_token_view(self):
        token_id, token_url = self.util.generate_new_token(usage_limit=1)
        self.assertTrue(self.util.valid(token_id))

        view = getMultiAdapter((self.portal, self.request),
                               name=u'accept-token')
        view.publishTraverse(self.request, token_id)()
        self.assertFalse(self.util.valid(token_id))
        events = eventtesting.getEvents(ITokenAccepted)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].token_id, token_id)
