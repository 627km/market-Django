from rest_framework import generics, mixins
from .models import Product, Comment, Like
from .serializers import (
    ProductSerializer, 
    CommentSerializer, 
    CommentCreateSerializer,
    LikeCreateSerializer
)
from .paginations import ProductLargePagination

class ProductListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = ProductSerializer
    pagination_class = ProductLargePagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            products = Product.objects.all()
        else:
            products = Product.objects.none()
            
        

        # if 'name' in self.request.query_params:
        #     name = self.request.query_params.get['name']
        #     products products.filter(name__contains = name)
        
        name = self.request.query_params.get('name')
        if name:
            products = products.filter(name__contains=name)
        return products.order_by('id')
        
    def get(self, request, *args, **kwargs):
        print(request.user)
        return self.list(request, args, kwargs) # 부모클래스의 list메소드를 사용할 수 있다. 
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class ProductDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)

class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        if product_id:
            return Comment.objects.filter(product_id=product_id).order_by('-id')
        return Comment.objects.none()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

# 댓글달기 기능
class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

# 좋아요 기능
class LikeCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = LikeCreateSerializer
    def get_queryset(self):
        return Like.object.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)