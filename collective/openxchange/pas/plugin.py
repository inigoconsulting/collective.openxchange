"""Class: SqlalchemyHelper
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from App.class_init import default__class_init__ as InitializeClass

from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PluggableAuthService.utils import classImplements

from collective.openxchange import interfaces
from collective.openxchange.pas import (
        authentication, roles, properties,
        user_enumeration
)

class OpenXChangeHelper(
        authentication.AuthenticationPlugin,
        roles.RolesPlugin,
        properties.PropertiesPlugin,
        user_enumeration.UserEnumerationPlugin
        ):

    meta_type="OpenXChange Authentication Helper"

    security = ClassSecurityInfo()

    def __init__( self, id, title=None ):
        self._setId( id )
        self.title = title


classImplements(OpenXChangeHelper, interfaces.IOpenXChangeHelper)

InitializeClass(OpenXChangeHelper)
