from .models import Todo
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Todo Serializer
# Serializers take one thing and turn it into another thing...this is going to turn the Django model object we normally get into a more friendly-looking/familiar JSON object
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model that will be serialized by this class
        model = Todo
        # The fields that should be included in the serialized output:
        fields = ['id', 'subject', 'details']
