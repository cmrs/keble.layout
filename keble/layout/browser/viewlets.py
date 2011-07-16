from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_base, aq_inner
from random import choice

class OxfordEmblem(ViewletBase):
    render = ViewPageTemplateFile('templates/oxford_emblem.pt')

class KebleSectionBanner(ViewletBase):
    render = ViewPageTemplateFile('templates/keble_section_banner.pt')

    def get_banner_image(self):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        home_pages = portal_catalog(portal_type='HomePage')
        if not home_pages:
            print 'none found'
            return
        home_page = home_pages[0].getObject()
        return home_page.getRandomHomeImage()
