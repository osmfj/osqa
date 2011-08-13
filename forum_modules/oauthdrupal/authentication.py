from consumer import OAuthAbstractAuthConsumer
from forum.authentication.base import ConsumerTemplateContext

try:
    import json as simplejson
except ImportError:
    from django.utils import simplejson

from lib import oauth2
import settings

class OAuthConsumer(OAuthAbstractAuthConsumer):
    def __init__(self):
        OAuthAbstractAuthConsumer.__init__(self,
                str(settings.OAUTH_CONSUMER_KEY),
                str(settings.OAUTH_CONSUMER_SECRET),
		str(settings.OAUTH_SERVER_URL),
		str(settings.OAUTH_REQUEST_TOKEN_URL),
		str(settings.OAUTH_ACCESS_TOKEN_URL),
		str(settings.OAUTH_AUTHORIZE_URL),
        )

    def get_user_data(self, key):
        json = self.fetch_data(key, str(settings.OAUTH_USER_CREDENTIALS))
        
        if 'screen_name' in json:
            creds = simplejson.loads(json)

            return {
                'username': creds['screen_name']
            }
        
        
        return {}

class OAuthContext(ConsumerTemplateContext):
    mode = 'BIGICON'
    type = 'DIRECT'
    weight = 150
    human_name = 'Twitter'
    icon = '/media/images/openid/twitter.png'
