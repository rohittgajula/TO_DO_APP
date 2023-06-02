from rest_framework import serializers

from .models import Task, Tag

class TaskSerializer(serializers.ModelSerializer):
    #timestamp = serializers.DateTimeField(format="%H:%M:%S")

    class Meta:
        model = Task
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'