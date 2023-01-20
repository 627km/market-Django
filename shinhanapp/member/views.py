from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# 로그인페이지
# 기능1 : 로그인 화면출력
# 기능2: 아이디, 비밀번호 입력받아서 로그인 되는 것.
def signin(request):
    if request.method == 'POST':
       user_id = request.POST.get('user_id')
       password = request.POST.get('password')
       user = authenticate(request, username = user_id, password = password)
       if user is not None:
        login(request, user)
        return redirect('/')

    return render(request, 'login.html')


def signout(request):
    logout(request)
    return redirect('/')

# 회원가입 페이지 노출 
# 회원정보 저장 기능
def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            request.POST.get('user_id'),
            request.POST.get('email'),
            request.POST.get('password'),
        )
        return redirect('/member/login/')
    return render(request, 'register.html')