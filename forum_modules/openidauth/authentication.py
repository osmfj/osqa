from consumer import OpenIdAbstractAuthConsumer
from forum.authentication.base import ConsumerTemplateContext

class OSMJPAuthConsumer(OpenIdAbstractAuthConsumer):
    def get_user_url(self, request):
        return 'http://openstreetmap.jp/user/1/identity'

class OSMJPAuthContext(ConsumerTemplateContext):
    mode = 'BIGICON'
    type = 'DIRECT'
    weight = 200
    human_name = 'OSM Japan'
    icon = '/media/images/openid/osm_icon16x16.gif'

