from zope.interface import implements
from collective.openxchange.interfaces import ISessionManager

_sessions = {}
_cookies = {}

class SessionManager(object):
    """ Memory based cookie storage """

    implements(ISessionManager)

    def setSessionData(self, user, sessiondata, cookies):
        _sessions[user] = sessiondata,
        _cookies[user] = cookies

    def getSession(self, user):
        _sessions.setdefault(user, {})
        return _sessions[user].get('session', None)

    def getCookies(self, user):
        _cookies.setdefault(user, {})
        return _cookies[user]
