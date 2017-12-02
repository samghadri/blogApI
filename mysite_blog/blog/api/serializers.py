from rest_framework.serializers import ModelSerializer
from blog.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =['author','title','text','slug']


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =['author','title','text','slug']


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =['author','title','text']
