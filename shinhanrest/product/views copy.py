from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

class ProductListView(APIView):
    def post(self, request, *args, **kwargs):
        # 전달한 값 받아오기
        name = request.data.get('name')
        price = request.data.get('price')
        product_type = request.data.get('product_type')

        # 객체생성
        product = Product (
            name = name,
            price = price,
            product_type = product_type,
        )

        # 객체의 save() 함수를 이용해서 Database에 저장
        product.save()  # 이때 PK가 생성된다. 

        return Response({
            'id': product.id,   # PK
            'name': product.name,
            'price': product.price,
            'product_type': product.product_type,
        }, status=status.HTTP_201_CREATED)


    def get(self, request, *args, **kwargs):
        ret = []
        # QuerySet
        products = Product.objects.all()    # 이 순간 DB에서 가져오지 않음

        if 'price' in request.query_params:
            price = request.query_params['price']
            products = products.filter(price__lte=price) # __lte : 오른쪽 price 보다 작거나 같다
        
        if 'name' in request.query_params:
            name = request.query_params['name']
            products = products.filter(name__contains=name) # __contain : 포함하는 글자
        
        products = products.order_by('id')

        for product in products:
            p = {
                'id': product.id,   # PK / 이때 DB에서 값을 가져옴
                'name': product.name,
                'price': product.price,
                'product_type': product.product_type,
            }
            ret.append(p)

        return Response(ret)

class ProductDetailView(APIView):
    def put(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)

        # if 'name' in request.data:
        #     product.name = request.data['name']

        # if 'price' in request.data:
        #     product.price = request.data['price']

        # if 'product_type' in request.data:
        #     product.product_type = request.data['product_type']

        dirty = False
        for field, value in request.data.items():
            if field not in [f.name for f in product._meta.get_fields()]:
                continue

            dirty = dirty or (value != getattr(product, field))
            setattr(product, field, value)
        
        if dirty:
            product.save()

        return Response({
            "name": product.name,
            "price": product.price,
            "product_type": product.product_type,
        }, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        # 1. 없으면 지워졌다고 거짓말하기 (204 반환)
        # 2. 없으면 없다고 반환하기 (404 반환) - get에서 처리

        if Product.objects.filter(pk=pk).exist():
            product = Product.objects.get(pk=pk)
            product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, *args, **kwargs):
        # 1. get 하기 전 exist()로 확인하고 가져오기
        # 2. get 할 때 예외처리 하기

        try:
            # 상품가져오기 
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # 하나의 딕셔너리 형태로 반환
        ret = {
            "name": product.name,
            "price": product.price,
            "product_type": product.product_type,
        }
        # return Response({"temp":1})
        return Response(ret)
