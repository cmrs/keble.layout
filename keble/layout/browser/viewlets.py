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

    def get_banner_images(self, obj):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        banner_images_folder = getattr(obj, 'banner-images', None)
        if banner_images_folder:
            banner_images = banner_images_folder.objectValues('ATBlob')
            if not banner_images:
                if self.isPortalRoot(obj):
                    return
                banner_images = self.get_banner_images(obj.aq_parent)
        else:
            if self.isPortalRoot(obj):
                return
            banner_images = self.get_banner_images(obj.aq_parent)
        return banner_images

    def get_banner_image(self):
        portal = getToolByName(self.context, 'portal_url').getPortalObject()
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        banner_images = self.get_banner_images(self.context)

        if not banner_images:
            return

        if banner_images:
            return choice(banner_images)
        else:
            banner_images = portal_catalog.searchResults(portal_type='Image', path={'query':'/'.join(portal.getPhysicalPath()) + '/banner-images', 'level':0})
            if banner_images:
                return choice(banner_images)
            else:
                return

    def isPortalRoot(self, obj=None):
        if not obj:
            obj = self.context
        context_state = getMultiAdapter((obj, self.request),
                                       name=u'plone_context_state')
        return context_state.is_portal_root()

