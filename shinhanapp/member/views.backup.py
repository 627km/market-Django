from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Member
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.

# 로그인페이지
# 기능1 : 로그인 화면출력
# 기능2: 아이디, 비밀번호 입력받아서 로그인 되는 것.
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        if Member.objects.filter(user_id = user_id).exists():
            # get함수는 없거나 두개이상있으면 에러발생한다. 하지만 user_id는 unique속성때문에 무조건 하나이다. 
            member = Member.objects.get(user_id = user_id)

            if check_password(password, member.password):
                request.session['user_pk'] = member.id # 로그인 성공 (세션은 딕셔너리이다.)
                request.session['user_id'] = member.user_id # (세션은 딕셔너리이다.)
                
                return redirect('/')

        # 로그인 실패


    return render(request, 'login.html')

def logout(request):
    if 'user_pk' in request.session:
        del(request.session['user_pk'])
    if 'user_id' in request.session:
        del(request.session['user_id'])

    return redirect('/')

# 회원가입 페이지 노출 
# 회원정보 저장 기능
def register(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        name = request.POST.get('name')
        age = request.POST.get('age')

        if not Member.objects.filter(user_id=user_id).exists():
            member = Member(
                user_id = user_id,
                password = make_password(password),
                name = name,
                age = age,
        )
        member.save()
        redirect('/member/login/')
    return render(request, 'register.html')