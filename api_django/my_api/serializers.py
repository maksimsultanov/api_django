from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        Model = News
        fields = ('title', 'url')
