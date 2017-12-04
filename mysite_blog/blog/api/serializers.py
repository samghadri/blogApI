from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedIdentityField,
                                        SerializerMethodField
                                        )
from blog.models import Post, Comment


class PostSerializer(ModelSerializer):

    url = HyperlinkedIdentityField(
        view_name='blog-api:detail',
        lookup_field='slug'
        )
    delete_url = HyperlinkedIdentityField(
        view_name='blog-api:delete',
        lookup_field='slug'
        )
    author = SerializerMethodField()
    class Meta:
        model = Post
        fields =['author','url','title','text','delete_url']

    def get_author(self,obj):
        return str(obj.author.username)



class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =['author', 'title', 'text','created_date', 'slug']

    def get_author(self,obj):
        return str(obj.author.username)


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =['author', 'title','text']



class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields =[
        'author',
        'text',
        'created_date',
        'post',
        ]
