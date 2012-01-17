from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
import requests
from collective.openxchange.interfaces import ISessionManager, IOXUtility
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

        if not login:
           return 

        oxutil = getUtility(IOXUtility)

        if oxutil.authenticate(login, password):
            return (login, login)
