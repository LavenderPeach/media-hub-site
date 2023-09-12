from rest_framework import serializers
from ..mediaSITE.models import movie
from ..mediaSITE.models import television
from ..mediaSITE.models import book
from ..mediaSITE.models import videogame


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = '__all__'


class TelevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = television
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'



class VideoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = videogame
        fields = '__all__'