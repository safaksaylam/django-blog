from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(yayinlama_tarihi__lte=timezone.now()).order_by('yayinlama_tarihi')
    return render(request, 'blog/post_list.html', {'posts' : posts})
