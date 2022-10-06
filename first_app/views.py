from django.shortcuts import render
from . models import Post
from django.db.models import Q

# Create your views here.

def index(request):
    data = Post.objects.all()

    return render(request, 'index.html' ,context = {'data':data})

# def search(request):
#     data = Post.objects.all()
#     # s = request.GET.get('search')
#     # if s:
#     #     data = data.filter(Q(title__icontains=s))
    
#     return render(request, 'index.html', context = {'obj': data})    