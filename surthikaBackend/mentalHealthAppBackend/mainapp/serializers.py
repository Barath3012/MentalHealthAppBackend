from rest_framework.serializers import Serializer,ModelSerializer
from .models import *




class QuestionareSerializerDetail(ModelSerializer):

	class Meta:
		model=Questionare
		fields='__all__'