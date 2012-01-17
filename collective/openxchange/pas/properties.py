from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PlonePAS.sheet import MutablePropertySheet

class PropertiesPlugin(BasePlugin):
    """ Return a property set for a user.
    """
    security = ClassSecurityInfo()

    security.declarePrivate('getPropertiesForUser')
    def getPropertiesForUser(self, user, request=None):
        """ user -> {}

        o User will implement IPropertiedUser.

        o Plugin should return a dictionary or an object providing
          IPropertiesPlugin.

        o Plugin may scribble on the user, if needed (but must still
          return a mapping, even if empty).

        o May assign properties based on values in the REQUEST object, if
          present
        """

        if isinstance(user, basestring):
            user_id = user
        else:
            user_id = user.getId()

        properties = {'fullname': '',
                      'email': ''}

        return MutablePropertySheet(self.id, **properties)

