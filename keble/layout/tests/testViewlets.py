import unittest2 as unittest

from plone.app.testing import PLONE_INTEGRATION_TESTING
from plone.app.testing import ploneSite
from plone.app.testing import applyProfile

from zope.component import getAdapters
from zope.component import queryMultiAdapter
from zope.interface import alsoProvides
from zope.viewlet.interfaces import IViewletManager, IViewlet

from Products.Five import zcml
from Products.Five.browser import BrowserView

from keble.layout.browser.interfaces import IKebleLayout

from base import KEBLE_LAYOUT_INTEGRATION_TESTING
from base import TestCase

class TestViewlets(unittest.TestCase):
    """Ensure product is properly installed"""
    layer = KEBLE_LAYOUT_INTEGRATION_TESTING

    def setUp(self):                                
        self.portal = self.layer['portal'] 

    def get_viewlet_manager(self, context, manager_name):
        request = self.portal.REQUEST
        alsoProvides(request, IKebleLayout)
        view = BrowserView(context, request)
        manager = queryMultiAdapter(
            (context, request, view),
            IViewletManager,
            name=manager_name)
        manager.update()
        viewlet_names = [v.__name__ for v in manager.viewlets]
        return viewlet_names

    def testSectionBanner(self):
        context = self.portal
        viewlet_names = self.get_viewlet_manager(context, 'plone.portalheader')
        assert 'keble.layout.sectionbanner' in viewlet_names
