import unittest2 as unittest

from zope.component import getSiteManager

from plone.app.testing import PLONE_INTEGRATION_TESTING
from plone.app.testing import ploneSite
from plone.app.testing import applyProfile
from plone.browserlayer.utils import registered_layers

from base import KEBLE_LAYOUT_INTEGRATION_TESTING

class TestInstallation(unittest.TestCase):
    """Ensure product is properly installed"""
    layer = KEBLE_LAYOUT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testBrowserLayerRegistered(self):
        sm = getSiteManager(self.portal)
        layers = [o.__name__ for o in registered_layers()]
        assert 'IKebleLayout' in layers

    def testSkinLayer(self):
        portal_skins = getattr(self.portal, 'portal_skins')
        assert 'Keble Default' in portal_skins.getSkinSelections()

    def testCurrentSkinLayer(self):
        current_skin = self.portal.getCurrentSkinName()
        assert 'Keble Default' == current_skin

    def testCssInstalled(self):
        css_ids = self.portal.portal_css.getResourceIds()
        assert '++resource++keble.layout.stylesheets/main.css' in css_ids
