from rest_framework.serializers import Serializer,ModelSerializer
from .models import *


class EnquirySerializer(ModelSerializer):
	class Meta:
		model=Enquiry
		fields=['income','transactions','equity']

class EnquirySerializerDetail(ModelSerializer):

	class Meta:
		model=Enquiry
		fields='__all__'