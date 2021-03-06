from rest_framework import serializers
from facebook_recipes.models import Video, Facebook_Page, LANGUAGE_CHOICES, STYLE_CHOICES

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('created', 'created_ms', 'image_url', 'fbid', 'page_url', 'recipe_text', 'description', 'host_id', 'name')

class FbPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facebook_Page
        fields = ('name', 'fbid', 'image_url')