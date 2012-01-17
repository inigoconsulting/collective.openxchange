from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
import requests
from collective.openxchange.interfaces import ISessionManager
from zope.component import getUtility
import json

class AuthenticationPlugin(BasePlugin):
    security = ClassSecurityInfo()

    security.declarePrivate('authenticateCredentials')
    def authenticateCredentials(self, credentials):

        """ credentials -> (userid, login)

        o 'credentials' will be a mapping, as returned by IExtractionPlugin.

        o Return a  tuple consisting of user ID (which may be different
          from the login name) and login

        o If the credentials cannot be authenticated, return None.
        """

        login = credentials.get('login')
        password = credentials.get('password')

        r = requests.post('http://192.168.122.214/ajax/login?action=login', {
            'name': login,
            'password': password
        })

        data = json.loads(r.content)
        if data.get('session'):
            sm = getUtility(ISessionManager)
            sm.setSessionData(login, data, r.cookies)
            return (login, login)
