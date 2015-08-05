from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/posts/")
    return render(request, 'site-auth/login.html', {'form': form })

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/posts/')

def register_view(request):
 	if request.method == 'POST':
 		username = request.POST['username'].lower()
 		password = request.POST['password']
 		user = User.objects.create(username=username)
 		user.set_password(password)
 		user.save()
 		user = authenticate(username=username, password=password)
 		if user is not None:
 			login(request, user)
 			return HttpResponseRedirect('/posts/')
 		else:
	 		return HttpResponse("User was none")
 	elif request.method == 'GET':
 		if request.user.is_authenticated():
 			return HttpResponseRedirect('/posts/')
 		else:
			return render(request, 'site-auth/register.html')

#check if username exists on registration form
def username_check(request, username):
	try:
		user = User.objects.get(username=username)
		return HttpResponse("fail");
	except:
		return HttpResponse("success");


