from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Product
# Create your views here.

def main(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'product.html', {'products': products})

def write(request): # 상품등록하는 페이지를 띄워주고 등록까지해주는 함수
    if not request.user.is_authenticated:  # 로그인 상태가 아니면 상품등록 페이지 접근 불가
        return redirect('/member/login/')

    if request.method == 'POST':
        product = Product(
            user = request.user,    # 로그인 된 사용자가 자동으로 들어감
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            price = request.POST.get('price'),
            location = request.POST.get('location'),
            image=request.FILES.get('image'),
        )
        product.save()
        return redirect('/')
    return render(request, 'writepage.html')

def detail(request, pk):
    product = Product.objects.get(pk=pk)


    ret = {
        'title': product.title,
        'content': product.content,
        'price': product.price,
        'location': product.location,
        'username' : product.user.username,
        'image' : '/static/bg.jpg',
    }

    if product.image:
        ret['image'] = product.image.url
   
        
    return JsonResponse(ret)