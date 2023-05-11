from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from .serializers import *
from .utils import calculateScore

HEADS = [
                "depressedMood",
                "feelingsOfGuilt",
                "suicide",
                "initialInsomnia",
                "insomniaDuringTheNight",
                "delayedInsomnia",
                "workAndInterests",
                "retardation",
                "agitation",
                "psychiatricAnxiety",
                "somaticAnxiety",
                "gastrointestinalSomaticSymptoms",
                "generalSomaticSymptoms",
                "hypochondriasis",
                "weightLoss",
                "insight"
            ]

# Create your views here.
class QuestionareView(viewsets.ModelViewSet):

        queryset = Questionare.objects.all()
        serializer_class = QuestionareSerializerDetail

        def create(self, request, *args, **kwargs):
            data = request.data.values()

            values = {i:j for i,j in zip(HEADS,list(data))}
            print(len(list(data)))
            try:
                score = calculateScore(data)
                my_model = Questionare.objects.create(**values)
                serializer = self.get_serializer(my_model)
                response_data = serializer.data
                response_data['calculatedScore'] = score
                return Response({'calculatedScore':score})
            except:
                return Response({"Error":"OOPS"},status=status.HTTP_501_NOT_IMPLEMENTED)

class GetScore(APIView):

    def post(self,response,format=None):
        data = response.data.values()
        score = calculateScore(data)
        return Response({"calculatedScore":score},status=status.HTTP_200_OK)