import datetime
import logging

import os
import random
import string
import threading

from django.conf import settings
from django.shortcuts import render, redirect
from django.core.cache import cache
from . import verify_code
from .forms import RegisterForm
from django.urls import reverse
from .forms import PubilcationForm
from .models import User
# Create your views here.

logger = logging.getLogger("django")

def register_user(request):
    # 生成验证码
    err_msg = None
    today_str = datetime.date.today().strftime("%Y%m%d")
    verify_code_img_path = os.path.join(settings.VERIFICATION_CODE_IMGS_DIR,today_str)
    if not  os.path.isdir(verify_code_img_path):
        os.makedirs(verify_code_img_path,exist_ok=True)
    random_filename = "".join(random.sample(string.ascii_lowercase,5))
    random_code = verify_code.gene_code(verify_code_img_path,random_filename)
    print(verify_code_img_path)
    img_path = 'verify_code/'+ today_str + '/' + random_filename + '.png'
    # 验证码写入缓存字典中，并设置60秒过期时间
    cache.set(random_filename,random_code,60)
    print(os.path.join(verify_code_img_path,random_filename+'.png'))
    threading.Thread(target=verify_code.del_img,args=(os.path.join(verify_code_img_path,random_filename+'.png'),)).start()

    # 获取next的值
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    # 判断提交方法是否是post
    if request.method == 'POST':
        _verify_code = request.POST.get('verify_code')
        _verify_code_key = request.POST.get('verify_code_key')

        if cache.get(_verify_code_key) == _verify_code:

            # 接收post中的数据，并以此数据实例化modelform
            form = RegisterForm(request.POST, request.FILES)

            # 判断数据是否合法有效。
            if form.is_valid():
                # 数据有效，保存。
                form.save()

                # 判断是否需要跳转到之前的页面
                if redirect_to:
                    return redirect(redirect_to)
                else:
                    # 跳转到登录。
                    return redirect(reverse('login'))
        else:
            form = RegisterForm(request.POST, request.FILES)
            err_msg = '验证码输入错误'
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form':form,'next':redirect_to,'img_path':img_path,'filename':random_filename,'err_msg':err_msg})

def index(request):
    return render(request,'user/index.html')

def pubilcation(request):
    form = PubilcationForm()
    if request.method == 'POST':
        form = PubilcationForm(request.POST,request.FILES,)
        logger.warning('POST请求成功')
        current_user = request.user
        if form.is_valid():
            logger.warning('表单提交成功')
            post = form.save(commit=False)
            post.author = current_user
            post.save()
            form.save_m2m()
            return redirect(reverse('users:publication_done'))

    return render(request,'user/publication.html',{'form':form })

def pubication_done(request):
    return render(request,'user/pubication_done.html')