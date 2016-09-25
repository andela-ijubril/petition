# from petition.models import Petition
from rest_framework import serializers
from .models import Petition, Signature


class PetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Petition
        fields = ('name', 'description')


class SignatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Signature
        fields = ('petition', 'time_signed')
