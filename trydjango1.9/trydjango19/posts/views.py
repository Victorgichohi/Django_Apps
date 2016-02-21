from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post

# Create your views here.
def post_create(request):
	form = PostForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absoulute_url())
	context={
		"form":form,
	}
	return render(request, "post_form.html" ,context)

def post_detail(request, id=None):
	# return HttpResponse("<h1>detail</h1>")
	instance=get_object_or_404(Post, id=id)
	context={
		"title": instance.title,
		"instance":instance,
		}

	
	return render(request, "post_detail.html" ,context)

def post_list(request):
	queryset=Post.objects.all()
	context={
	"object_list":queryset
	}

	return render(request,"index.html",context)
	# return HttpResponse("<h1>list</h1>")

def post_update(request, id=None):
	instance=get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absoulute_url())
	
	context={
		"title": instance.title,
		"instance":instance,
		"form":form,
		}

	
	return render(request, "post_form.html" ,context)

def post_delete(request):
	return HttpResponse("<h1>delete</h1>")