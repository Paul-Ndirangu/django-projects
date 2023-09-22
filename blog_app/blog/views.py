from django.http import HttpResponse
from django.template import loader
from .models import Post

# Create your views here.
#
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))


def post(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)

