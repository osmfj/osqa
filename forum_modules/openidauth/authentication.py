from consumer import OpenIdAbstractAuthConsumer
from forum.authentication.base import ConsumerTemplateContext

class OSMJPAuthConsumer(OpenIdAbstractAuthConsumer):
    def get_user_url(self, request):
        user_id = request.POST['input_field']
        return 'http://openstreetmap.jp/user/%s/identity' % user_id

class OSMJPAuthContext(ConsumerTemplateContext):
    mode = 'SMALLICON'
    type = 'SIMPLE_FORM'
    simple_form_context = {
        'your_what': 'OSM Japan User ID'
    }
    weight = 200
    human_name = 'OSM Japan'
    icon = '/media/images/openid/osm_icon16x16.gif'

