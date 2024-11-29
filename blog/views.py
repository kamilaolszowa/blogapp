from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .pagination import DefaultPagination
from .models import Post, Blogger
from .serializers import PostSerializer, BloggerSerializer
from .permissions import IsAuthenticatedOrPostReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticatedOrPostReadOnly]


class BloggerViewSet(ModelViewSet):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (blogger, created) = Blogger.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = BloggerSerializer(blogger)
            return Response(serializer.data)
        elif request.method == ['PUT']:
            serializer = BloggerSerializer(blogger, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
