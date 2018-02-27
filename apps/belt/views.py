from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from django.contrib import messages
from models import *
import time
today = time.strftime('%b %d')

def index(request):
	return render(request, 'exam/login.html')
def process(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		if request.method == 'POST':
			first_name=request.POST['fname']
			last_name=request.POST['lname']
			email=request.POST['email']
			alias=request.POST['alias']
			hpassword=bcrypt.hashpw(request.POST['pword'].encode(),bcrypt.gensalt())
			user=User.objects.create(first_name=first_name,last_name=last_name,email=email,password=hpassword, alias=alias)
			request.session['id']=user.id
			request.session['alias']=user.alias
		return redirect('/home/'+str(user.id))
def login(request):
	if request.method=='POST':
		pings = User.objects.login_validator(request.POST)
		if len(pings):
			for tag, error in pings.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect('/')
		else:
			user=User.objects.get(email=request.POST['email'])
			request.session['id']=user.id
			print user
			return redirect('/home/'+str(user.id))
def home(request,id):
	users=Friend.objects.filter(from_user=request.session['id'])
	all_users=User.objects.all().exclude(id=request.session['id'])
	yo=User.objects.get(id=id)
	context={
		'get':yo,
		'all':all_users,
		'users':users,	
	}
	return render(request, 'exam/home.html', context)
def logout(request):
	request.session.pop('id')
	return redirect('/')
def view(request,id):
	user=User.objects.get(id=id)
	info={
		'user': user
	}
	return render(request, 'exam/profile.html',info)
def friend(request,id):	 
	b=User.objects.get(id=id)
	name=b.alias
	from_user=User.objects.get(id=request.session['id'])
	to_user= User.objects.get(id=id)
	print to_user
	friend=Friend.objects.create(from_user=from_user, to_user=to_user,name=name)

	return redirect('/home/'+str(request.session['id']))
def remove(request,id):
	bad=Friend.objects.get(id=id)
	bad.delete()
	return redirect('/home/'+str(request.session['id']))