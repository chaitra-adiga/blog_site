from django.shortcuts import render
from .models import Post

# Create your views here.
'''posts=[
    #dummy data
    {
        'author':'Rahul',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'November 15, 2024'
    },
    {
        'author':'Shahul',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'November 13, 2024'
    }
]'''

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})