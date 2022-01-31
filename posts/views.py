from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Post

def index(request):
  
  posts = Post.objects.order_by('-publish_date').filter(is_published=True)
  
  paginator = Paginator(posts, 6)
  
  # get param from URL
  page = request.GET.get('page')
  paged_posts = paginator.get_page(page)
  
  context = {
    'posts': paged_posts
  }
  
  return render(request, 'posts/posts.html', context)


def post(request, post_id):
  post = get_object_or_404(Post, pk=post_id).filter(is_published=True)
  context = {
    'post': post
  }
  return render(request, 'posts/post.html', context)
