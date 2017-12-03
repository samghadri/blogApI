from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                    RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView)
from blog.models import Post
from .serializers import PostSerializer, PostDetailSerializer, PostCreateUpdateSerializer
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAdminUser,
                                        IsAuthenticatedOrReadOnly,
                                        )

from .permissions import IsOwnerOrReadOnly


class PostApi(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetailApi(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostDeleteApi(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'



class PostUpdateApi(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class PostCreateApi(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
