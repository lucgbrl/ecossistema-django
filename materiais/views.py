from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Material
from django.utils import timezone
from django.http import HttpResponse
from .forms import PostForm, MaterialForm


# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'html/index.html', {'posts' : posts})

def usuarios(request):
    return render(request, 'html/usuarios.html', {})
    
def lista(request):
    materiais_count = Material.objects.count()
    materiais = Material.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'html/lista.html' , {'materiais' : materiais, 'materiais_count' : materiais_count})

def detalhes(request, pk):
    materiais = get_object_or_404(Material, pk=pk)
    return render(request, 'html/detalhes.html', {'materiais' : materiais})

def new(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit = False)            
            material.published_date = timezone.now()
            material.save()
            return redirect('index')
    else:
            form = MaterialForm()
    return render(request, 'html/material_edit.html', {'form' : form})

def login(request):
    return render(request, 'html/login.html', {})
"""
def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('index')
     else:
         form = PostForm()
     return render(request, 'html/post_edit.html', {'form': form})

"""
