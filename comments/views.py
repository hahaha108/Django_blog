from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse

from blog.models import Post
from .forms import CommentForm
# Create your views here.


def post_comment(request, post_pk):

    # 根据传入的post_pk获取post对象
    post = get_object_or_404(Post, pk=post_pk)
    # 判断form提交方法是否是post方法
    if request.method == 'POST':
        # 如果是post方法，那么获取POST中的所有数据，并以此数据实例化CommentForm

        if request.user.is_authenticated:
            current_user = request.user
            form = CommentForm(request.POST)
            # 判断form中的数据是否合法。
            if form.is_valid():
                # 如果合法，则创建comment实例，先不保存
                comment = form.save(commit=False)
                # 把post赋值给comment
                comment.post = post
                # 数据已到位，可以保存。
                comment.author = current_user

                comment.save()
                # redirect传一个对象的话，会直接调用对象的get_absolute_url方法。
                return redirect(post)
            else:
                comment_list = post.comment_set.all()
                context = {
                    'post': post,
                    'form': form,
                    'comment_list': comment_list
                }
                return render(request, 'blog/detail.html', context=context)
        else:

            return redirect(reverse('login'))
    # 如果提交方法不是post，那么重定向到原页面。
    return redirect(post)