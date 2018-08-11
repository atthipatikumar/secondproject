from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from myproject.models.user1 import Users1, Details
#from myproject.models.user import Details

class UserResource(ModelResource):
	class Meta:
		collection_name="data"
		queryset = Users1.objects.all()
		resource_name = 'user79'
		authorization = Authorization()
		
'''class PageResource(ModelResource):
	class Meta:
		collection_name="data"
		queryset = DetailsUsers.objects.all()
		resource_name = 'user45'
		authorization = Authorization()'''
		
class PagesResource(ModelResource):
	class Meta:
		collection_name="data"
		queryset = Details.objects.all()
		resource_name = 'user456'
		authorization = Authorization()