from django.shortcuts import render
from .models import UserInfo, Category, Post

def index_view(request):
	user_info = UserInfo.objects.get(id=1)
	categories = Category.objects.all()
	posts = Post.objects.all()
	context ={
		'user': user_info,
		'categories': categories,
		'posts': posts,
	}

	return render(request, 'index.html', context)

def post_details(request, id):
	post = Post.objects.get(id=id)
	context = {
	'post': post,
	}

	return render(request, 'post_detail.html', context)