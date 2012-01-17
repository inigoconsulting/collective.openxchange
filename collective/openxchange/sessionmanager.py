from zope.interface import implements
from collective.openxchange.interfaces import ISessionManager
from zope.globalrequest import getRequest

import pprint
import json

class SessionManager(object):

    implements(ISessionManager)

    def setSessionData(self, sessiondata, cookies):
        request = getRequest()

        sessiondata = json.dumps(sessiondata)
        cookies = json.dumps(cookies)
        request.RESPONSE.setCookie('openxchange-session', sessiondata)
        request.RESPONSE.setCookie('openxchange-cookies', cookies)

    def getSession(self):
        request = getRequest()
        value = json.loads(request.get('openxchange-session', "{}"))
        session = value.get('session', None)
        if session:
            session = str(session)
        return session

    def getCookies(self):
        request = getRequest()
        cookies = json.loads(request.get('openxchange-cookies', "{}"))
        return dict([(str(k), str(v)) for k,v in cookies.items()])
