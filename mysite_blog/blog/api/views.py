from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                    RetrieveUpdateAPIView, DestroyAPIView,
                                    CreateAPIView)
from blog.models import Post, Comment
from .serializers import PostSerializer, PostDetailSerializer, PostCreateUpdateSerializer, CommentSerializer

from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAdminUser,
                                        IsAuthenticatedOrReadOnly,
                                        )
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q
from .pagination import (PostLimitOffsetPagination,
                         PostPageNumberPagination
                         )


class PostApi(ListAPIView):

    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title','author__first_name','text']
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args,**kwargs):
        queryset_list = Post.objects.all()
        # queryset_list = super(PostApi,self).get_queryset(*args,**kwargs)
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(text__icontains=query)|
                    Q(author__first_name__icontains=query)|
                    Q(author__last_name__icontains=query)
                    ).distinct()
        return queryset_list




class PostDetailApi(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostDeleteApi(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class PostUpdateApi(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class PostCreateApi(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]


class CommentDetailApi(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListApi(ListAPIView):

    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['text','author']
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args,**kwargs):
        queryset_list = Comment.objects.all()
        # queryset_list = super(PostApi,self).get_queryset(*args,**kwargs)
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                    Q(text__icontains=query)|
                    Q(author____icontains=query)
                    ).distinct()
        return queryset_list
