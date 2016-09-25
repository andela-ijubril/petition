from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Petition, Signature
from .serializers import PetitionSerializer, SignatureSerializer


class PetitionList(APIView):
    """
    List all Petition or create new petition
    """
    def get(self, request, format=None):
        petitions = Petition.objects.all()
        serializer = PetitionSerializer(petitions, many=True)
        return Response(serializer.data)


# TODO: Add a form of authhentication
# TODO: Automated deploy
#
