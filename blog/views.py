from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
