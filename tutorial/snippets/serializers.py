from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, User

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id','title','code','lineons','language','style')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','birthday')