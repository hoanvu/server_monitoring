from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm
from .models import Server

# Index view - display name, description and status for all servers
class IndexView(generic.ListView):
	template_name = 'mainApp/index.html'
	context_object_name = 'serverList'

	def get_queryset(self):
		return Server.objects.order_by('servername')

def userLogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/mainApp/')
			else:
				return HttpResponse('Account is disabled.')
		else:
			return HttpResponse('Incorrect username/password.')
	else:
		return render(request, 'mainApp/login.html')

# Log a user out
@login_required
def userLogout(request):
	logout(request)
	return HttpResponseRedirect('/mainApp/')

# Add new server
@login_required
def addServer(request):
	if request.method == 'POST':
		servername = request.POST.get('servername')
		description = request.POST.get('description')

		server = Server(servername=servername, description=description)
		server.save()

		return HttpResponseRedirect('/mainApp/')

# Remove a server from monitoring system
@login_required
def removeServer(request, serverId):
	if request.method == 'POST':

		server = Server.objects.get(id=serverId)
		server.delete()

		return HttpResponseRedirect('/mainApp/')

# List all users available
@login_required
def allUser(request):
	userList = User.objects.order_by('username')
	return render(request, 'mainApp/allUser.html', {'userList': userList})

# Route to add new user to the system
@login_required
def addUser(request):
	if request.method == 'POST':
		# Strip all space in username
		message = ''
		username = request.POST.get('username').strip()
		password = request.POST.get('password')

		userList = User.objects.all()
		usernameList = [user.username for user in userList]

		# Check if username is empty
		if not username:
			message = 'Username can not be empty.'
		# Check if username entered already exists
		elif username in usernameList:
			message = 'Username already exists.'	
		else: # otherwise, add new user to system
			newuser = User(username=username)
			newuser.set_password(password)
			newuser.save()
			return HttpResponseRedirect('/mainApp/allUser/')

		# Render user page with proper message
		return render(request, 'mainApp/allUser.html', {
			'message': message,
			'userList': userList
		})		

@login_required
def removeUser(request, name):
	if request.method == 'POST':
		deleteUser = User.objects.get(username=name)
		deleteUser.delete()

		return HttpResponseRedirect('/mainApp/allUser/')