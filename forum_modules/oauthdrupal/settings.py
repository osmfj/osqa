from forum.settings import EXT_KEYS_SET
from forum.settings.base import Setting
from django.utils.translation import ugettext_lazy as _

OAUTH_CONSUMER_KEY = Setting('OAUTH_CONSUMER_KEY', '', EXT_KEYS_SET, dict(
label = _("OAuth consumer key"),
help_text = _("""
"""),
required=False))

OAUTH_CONSUMER_SECRET = Setting('OAUTH_CONSUMER_SECRET', '', EXT_KEYS_SET, dict(
label = _("OAuth consumer secret"),
help_text = _("""
"""),
required=False))

OAUTH_AUTO_CALLBACK_REDIRECT = Setting('OAUTH_AUTO_CALLBACK_REDIRECT', True, EXT_KEYS_SET, dict(
label = _("provider's auto-callback redirect"),
help_text = _("""
Automatically redirect to the authentication done page, pass the oauth_callback parameter.
"""),
required=False))

OAUTH_SERVER_URL = Setting('OAUTH_SERVER_URL', '', EXT_KEYS_SET, dict(label = _("OAuth provider's service URL"), help_text = _("""
OAuth provider's server URL such as twitter.com
"""),
required=False))

OAUTH_REQUEST_TOKEN_URL = Setting('OAUTH_REQUEST_TOKEN_URL', '', EXT_KEYS_SET, dict (label = _("OAuth request token URL"), help_text = _("""
"""),
required=False))

OAUTH_ACCESS_TOKEN_URL = Setting('OAUTH_ACCESS_TOKEN_URL', '', EXT_KEYS_SET, dict (label = _("OAuth access token URL"), help_text = _("""
"""),
required=False))

OAUTH_AUTHORIZE_URL = Setting('OAUTH_AUTHORIZE_URL', '', EXT_KEYS_SET, dict (label = _("OAuth authorize URL"), help_text = _("""
"""),
required=False))

OAUTH_USER_CREDENTIALS = Setting('OAUTH_USER_CREDENTIALS', '', EXT_KEYS_SET, dict (label = _("OAuth User Credentials get url"), help_text = _("""
"""),
required=False))
