from django.shortcuts import render
from .models import PDF
from django.shortcuts import render_to_response


def index(request):

    posts = PDF.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'posts':posts
    }

    return render(request,'posts/index.html', context)

def home(request):
	return render(request, 'posts/home.html')

def login(request):
    return render(request,'registration/login.html')

def test(request):
    return render(request,'posts/test.html')


def details(request,id):
    post = PDF.objects.get(id=id)

    context = {
        'post':post
    }
    return render(request,'posts/details.html', context)

def pdfview(request,id):
    pdf = PDF.objects.get(id=id)
    context = {
        'pdf': pdf
    }
    return render_to_response('posts/pdfview.html',context)


