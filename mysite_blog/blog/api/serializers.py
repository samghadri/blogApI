from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from blog.models import Post


class PostSerializer(ModelSerializer):

    url = HyperlinkedIdentityField(
        view_name='blog-api:detail',
        lookup_field='slug'
        )
    delete_url = HyperlinkedIdentityField(
        view_name='blog-api:delete',
        lookup_field='slug'
        )
    class Meta:
        model = Post
        fields =['author','url','title','text','delete_url']


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =['author', 'title', 'text','created_date', 'slug']


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =['author', 'title','text']
