
from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic import ListView,DetailView

from comments.forms import CommentForm
from .models import Post
import utils
# Create your views here.


def index(request):
    return render(request,'index.html', context={'my_page': 'index'})

class detail(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self,request,*args,**kwargs):
        response = super().get(request,*args,**kwargs)
        self.object.increase_views()
        return response


    def get_context_data(self, **kwargs):
        # 调用父类的get_context_data，获取原始的context对象
        context = super().get_context_data(**kwargs)
        post = self.object
        # 添加额外的上下文对象
        form = CommentForm()
        comment_list = post.comment_set.all()
        # 更新context
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


class blog(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(blog, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        start,end = utils.custompaginator(paginator.num_pages,page.number, 10)
        context.update(
            {
                'page_range' : range(start,end + 1),
                'my_page':'blog'
            }
        )
        return context

