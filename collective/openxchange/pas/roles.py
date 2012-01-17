from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin

from Acquisition import aq_get

class RolesPlugin(BasePlugin):
    """Determine the (global) roles which a user has.
    """
    security = ClassSecurityInfo()

    security.declarePrivate('getRolesForPrincipal')
    def getRolesForPrincipal(self, principal, request=None):
        """principal -> (role_1, ... role_N)

        o Return a sequence of role names which the principal has.

        o May assign roles based on values in the REQUEST object, if present.
        """

        if isinstance(principal, basestring):
            principal_id = principal
        else:
            principal_id = principal.getId()

        request = aq_get(self, 'REQUEST', None)
        if request and request.get('__ignore_direct_roles__', False):
            return ()

        return ('Manager',)
