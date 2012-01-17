from collective.openxchange.pas import install

install.register_plugin()

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    install.register_plugin_class(context)
