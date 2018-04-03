from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist

from .models import User
from .helper import check_perm

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        if User.objects.filter(nickname__exact=nickname).exists():
            info = {'error':'"昵称"已存在'}
            tpl_name = 'user/register.html'
            return render(request,tpl_name,info)

        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            info = {'error':'两次密码输入不一致'}
            tpl_name = 'user/register.html'
            return render(request,tpl_name,info)

        age = request.POST.get('age')
        sex = request.POST.get('sex')
        f_in = request.FILES.get('icon')
        user = User(nickname = nickname,password = password,age = age,sex = sex)
        if f_in:
            user.icon.save(f_in.name,f_in,save=False)
        user.set_password(password)
        user.save()
        request.session['uid'] = user.id
        request.session['nickname'] = user.nickname
        url = '/user/info/?uid={}'.format(user.id)
        return redirect(url)
    else:
        tpl_name = 'user/register.html'
        info = {'error':'test'}
        return render(request,tpl_name,info)


@check_perm('admin')
def info_user(request):
    uid = request.session['uid']
    user = User.objects.get(pk = uid)
    info = {'user':user}
    tpl_name = 'user/info.html'
    return render(request,tpl_name,info)


def login(request):
    info = {}
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        print('nickname:{},password:{}'.format(nickname,password))
        user = User.objects.filter(nickname__exact=nickname).first()
        if user is None:
            info = {'error':'用户名错误'}
        elif not user.check_password(password):
            info = {'error':'密码错误','nickname':nickname}
        else:
            request.session['uid'] = user.id
            request.session['nickname'] = user.nickname
            url = '/user/info/?uid={}'.format(user.id)
            return redirect(url)
    tpl_name = 'user/login.html'
    return render(request,tpl_name,info)


def logout(request):
    request.session.flush()
    tpl_name = 'user/login.html'
    return render(request,tpl_name)