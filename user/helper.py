from django.shortcuts import render,redirect

from .models import User

def check_perm(perm_name):
    def wrap1(view_func):
        def wrap2(request,*args,**kwargs):
            uid = request.session.get('uid')
            if uid is None:
                url = '/user/login'
                request = redirect(url)
            else:
                user = User.objects.get(pk = uid)
                if user.has_perm(perm_name):
                    request = view_func(request,*args,**kwargs)
                else:
                    tpl_name = 'user/permission_denied.html'
                    request = render(request,tpl_name)
            return request
        return wrap2
    return wrap1