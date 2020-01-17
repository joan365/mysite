from django.shortcuts import render, get_object_or_404
from .models import Post    #importem els model Post del directori acu¡tual
from django.utils import timezone

# Create your views here.
def post_list(request):
    # El resultat (queryset) que amagatzemat a la variable posts
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #dins les {} relacionem la variable calculada amb la que cal mostrar a la plantilla
    return render(request, 'blog/post_list.html', {'paltilla_posts': posts})

def post_detail (request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
