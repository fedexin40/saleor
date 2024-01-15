import logging

from ...permission.enums import get_permissions_codename
from ..openid_connect.client import OAuth2Client
from ..openid_connect.const import SALEOR_STAFF_PERMISSION
from ..openid_connect.plugin import OpenIDConnectPlugin
from . import PLUGIN_ID

logger = logging.getLogger(__name__)


class OpenIDConnectPluginFacebook(OpenIDConnectPlugin):
    PLUGIN_ID = PLUGIN_ID
    PLUGIN_NAME = "OpenID Connect Facebook"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_oauth_session(self):
        scope = "openid email"
        if self.config.use_scope_permissions:
            permissions = [f"saleor:{perm}" for perm in get_permissions_codename()]
            permissions.append(SALEOR_STAFF_PERMISSION)
            scope_permissions = " ".join(permissions)
            scope += f" {scope_permissions}"
        if self.config.enable_refresh_token:
            scope += " offline_access"
        return OAuth2Client(
            client_id=self.config.client_id,
            client_secret=self.config.client_secret,
            scope=scope,
        )
