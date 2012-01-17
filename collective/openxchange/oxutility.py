import requests
from zope.component import getUtility
from zope.interface import implements
from collective.openxchange.interfaces import ISessionManager, IOXUtility
from collective.openxchange import const
import json
import urllib

class OXUtility(object):
    implements(IOXUtility)

    server = 'http://192.168.122.214/'

    @property
    def sessionmanager(self):
        return getUtility(ISessionManager)

    @property
    def session(self):
        return self.sessionmanager.getSession()

    @property
    def cookies(self):
        return self.sessionmanager.getCookies()

    def authenticate(self, user, password):
        r = requests.post('%s/ajax/login?action=login' % self.server, {
            'name': user,
            'password': password
        })

        data = json.loads(r.content)
        if data.get('session'):
            self.sessionmanager.setSessionData(data, r.cookies)
            return True
        return False


    def get_root_folders(self, columns=[const.FolderColumns.TITLE]):
        r = requests.post('%s/ajax/folders?action=root' % self.server, {
            'session': self.session,
            'columns': ','.join([str(i) for i in columns])
        },
        cookies=self.cookies)
        return json.loads(r.content)

    def get_emails(self, folder='INBOX', columns=[const.MailColumns.ID,
                                                  const.MailColumns.SUBJECT,
                                                  const.MailColumns.FROM,
                                                  const.MailColumns.RECEIVED_DATE]):
        query = urllib.urlencode({
            'action': 'all',
            'session':self.session,
            'folder': folder,
            'columns': ','.join([str(x) for x in columns]),
            'sort': const.MailColumns.RECEIVED_DATE,
            'order':'desc'
        })
        r = requests.get('%s/ajax/mail?%s' % (self.server, query),
            cookies=self.cookies)
        
        return json.loads(r.content)['data']


