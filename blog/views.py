from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
import utils
# Create your views here.


def index(request):
    tpl_name = 'index.html'
    return render(request,tpl_name)

def detail(request):
    pass

class blog(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(blog, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        start,end = utils.custompaginator(paginator.num_pages,page.number, 3)
        context.update(
            {
                'page_range' : range(start,end + 1)
            }
        )
        return context