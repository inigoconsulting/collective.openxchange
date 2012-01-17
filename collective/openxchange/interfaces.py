from Products.PluggableAuthService import interfaces as ifaces
from zope.interface import Interface

class IOpenXChangeHelper(
        ifaces.plugins.IAuthenticationPlugin,
        ifaces.plugins.IRolesPlugin,
        ifaces.plugins.IPropertiesPlugin,
        ifaces.plugins.IUserEnumerationPlugin
        ):
    pass

class ISessionManager(Interface):
    pass

class IOXUtility(Interface):
    pass
