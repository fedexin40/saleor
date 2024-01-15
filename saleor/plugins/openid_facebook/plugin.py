import logging

from django.conf import settings
from ..openid_connect.plugin import OpenIDConnectPlugin
from ..openid_connect.dataclasses import OpenIDConnectConfig

from . import PLUGIN_ID

logger = logging.getLogger(__name__)


class OpenIDConnectPluginFacebook(OpenIDConnectPlugin):
    PLUGIN_ID = PLUGIN_ID

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Convert to dict to easier take config elements
        self.config = OpenIDConnectConfig(
            client_id=settings.CLIENT_ID_FACEBOOK,
            client_secret=settings.CLIENT_SECRET_FACEBOOK,
            enable_refresh_token=settings.ENABLE_REFRESH_TOKEN_FACEBOOK,
            json_web_key_set_url=settings.JSON_WEB_KEY_SET_URL_FACEBOOK,
            authorization_url=settings.AUTHORIZATION_URL_FACEBOOK,
            token_url=settings.TOKEN_URL_FACEBOOK,
            user_info_url=settings.USER_INFO_URL_FACEBOOK,
            audience = '',
            use_scope_permissions = False,
            staff_user_domains = '',
            default_group_name = '',
            logout_url = '',
        )

        # Determine, if we have defined all fields required to use OAuth access token
        # as Saleor's authorization token.
        self.use_oauth_access_token = bool(
            self.config.user_info_url and self.config.json_web_key_set_url
        )

        # Determine, if we have defined all fields required to process the
        # authorization flow.
        self.use_authorization_flow = bool(
            self.config.json_web_key_set_url
            and self.config.authorization_url
            and self.config.token_url
        )

        # Activating the plugin manually
        self.active = True
