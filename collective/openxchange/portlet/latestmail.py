from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from collective.openxchange.interfaces import ISessionManager, IOXUtility

import requests
from datetime import datetime

_ = lambda x: x

class ILatestMailPortlet(IPortletDataProvider):
    count = schema.Int(title=_(u'Number of items to display'),
                       description=_(u'How many items to list.'),
                       required=True,
                       default=5)

class Assignment(base.Assignment):
    implements(ILatestMailPortlet)

    def __init__(self, count=5):
        self.count = count

    @property
    def title(self):
        return _(u"Latest mail")

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('latestmail.pt')

    @property
    def available(self):
        return getUtility(ISessionManager).getSession()

    def mails(self):
        oxutil = getUtility(IOXUtility)
        mails = []
        for i in oxutil.get_emails()[:self.data.count]:
            m = {
                'from': i[2][0][0],
                'from_addr': i[2][0][1],
                'subject': i[1],
                'datetime': datetime.fromtimestamp(i[3]/1000)
            }
            mails.append(m)
        return mails

class AddForm(base.AddForm):
    form_fields = form.Fields(ILatestMailPortlet)
    label = _(u"Add Latest Mail Portlet")
    description = _(u"This portlet displays recent emails.")

    def create(self, data):
        return Assignment(count=data.get('count', 5))

class EditForm(base.EditForm):
    form_fields = form.Fields(ILatestMailPortlet)
    label = _(u"Edit Latest Mail Portlet")
    description = _(u"This portlet displays recent emails.")
