from StringIO import StringIO

from zope.component import getUtility

from plone.app.viewletmanager.interfaces import IViewletSettingsStorage

def hideViewlets(portal, out):
    """Hide the default viewlets that are overridden
    """
    storage = getUtility(IViewletSettingsStorage)
    hidden_viewlets = storage.getHidden('plone.portalheader', 'Keble Default')
    storage.setHidden('plone.portalheader', 'Keble Default', (u'plone.footer', u'plone.colophon', u'plone.site_actions'))

def setupVarious(context):

    if context.readDataFile('keble.layout_various.txt') is None:
        return

    site = context.getSite()
    out = StringIO()

    hideViewlets(site, out)
