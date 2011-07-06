import unittest2 as unittest

from plone.app.testing import PLONE_INTEGRATION_TESTING
from plone.app.testing import ploneSite
from plone.app.testing import applyProfile

from base import KEBLE_LAYOUT_INTEGRATION_TESTING

class TestInstallation(unittest.TestCase):
    """Ensure product is properly installed"""
    layer = KEBLE_LAYOUT_INTEGRATION_TESTING

    def testSkinLayer(self):
        portal = self.layer['portal']
        with ploneSite() as portal:
            applyProfile(portal, 'keble.layout:default')
        portal_skins = getattr(portal, 'portal_skins')
        #assert 'cmrs' in portal_skins.getSkinSelections()
