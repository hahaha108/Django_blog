from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.urls import reverse

# Create your views here.

def register_user(request):
    # 获取next的值
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    # 判断提交方法是否是post
    if request.method == 'POST':
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
        form = RegisterForm()
    return render(request, 'user/register.html', {'form':form,'next':redirect_to})

