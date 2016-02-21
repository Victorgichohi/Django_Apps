from django.http import HttpResponse

from django.shortcuts import render

from .models import Post

# Create your views here.
def post_create(request):
	return HttpResponse("<h1>create</h1>")

def post_detail(request):
	# return HttpResponse("<h1>detail</h1>")

	
	return render(request, "index.html" ,{})

def post_list(request):
	queryset=Post.objects.all()
	context={
	"object_list":queryset
	}

	return render(request,"index.html",context)
	# return HttpResponse("<h1>list</h1>")

def post_update(request):
	return HttpResponse("<h1>update</h1>")

def post_delete(request):
	return HttpResponse("<h1>delete</h1>")