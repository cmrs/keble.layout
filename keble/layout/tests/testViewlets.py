import unittest2 as unittest

from plone.app.testing import PLONE_INTEGRATION_TESTING
from plone.app.testing import ploneSite
from plone.app.testing import applyProfile
from plone.app.viewletmanager.interfaces import IViewletSettingsStorage

from zope.component import getAdapters
from zope.component import getUtility
from zope.component import queryMultiAdapter
from zope.interface import alsoProvides
from zope.viewlet.interfaces import IViewletManager, IViewlet

from Products.Five import zcml
from Products.Five.browser import BrowserView

from keble.layout.browser.interfaces import IKebleLayout

from base import KEBLE_LAYOUT_INTEGRATION_TESTING
from base import TestCase

class TestViewlets(unittest.TestCase):
    """Ensure the right viewlets are available"""
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

    def testSearchBox(self):
        context = self.portal
        viewlet_names = self.get_viewlet_manager(context, 'plone.portalheader')
        assert 'keble.layout.searchbox' in viewlet_names
        print viewlet_names
        #assert 'plone.searchbox' not in viewlet_names

    def testGlobalSections(self):
        context = self.portal
        viewlet_names = self.get_viewlet_manager(context, 'plone.portalheader')
        assert 'keble.layout.global_sections' in viewlet_names
        print viewlet_names
        #assert 'plone.global_sections' not in viewlet_names

    def testSectionBanner(self):
        context = self.portal
        viewlet_names = self.get_viewlet_manager(context, 'plone.portalheader')
        assert 'keble.layout.sectionbanner' in viewlet_names

    def testFooter(self):
        context = self.portal
        import pdb;pdb.set_trace()
        viewlet_names = self.get_viewlet_manager(context, 'plone.portalfooter')
        assert 'keble.layout.footer' in viewlet_names
        print viewlet_names
        #assert 'plone.footer' not in viewlet_names
        #assert 'plone.colophon' not in viewlet_names
        #assert 'plone.site_actions' not in viewlet_names
        #assert 'plone.analytics' not in viewlet_names

    def testViewletStorage(self):
        storage = getUtility(IViewletSettingsStorage)
        hidden_viewlets = storage.getHidden('plone.portalheader', 'Keble Default')

