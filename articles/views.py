from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'articles/index.html')

def detail(request, uuid):
    return render(request, 'articles/article.html')
