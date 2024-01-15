import logging

from ..openid_connect.plugin import OpenIDConnectPlugin
from . import PLUGIN_ID

logger = logging.getLogger(__name__)


class OpenIDConnectPluginGoogle(OpenIDConnectPlugin):
    PLUGIN_ID = PLUGIN_ID
    PLUGIN_NAME = "OpenID Connect Google"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
