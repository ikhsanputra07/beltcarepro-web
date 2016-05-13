from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import json

def index(request):
	context = {}
	template = "index.html"
	return render (request,template,context)


def dashboard(request):
	context = {} 
	template = "content/dashboard.html"
	return render (request,template,context)

def data_conveyor(request):
	context = {"range":range(100)}
	template = "content/data_conveyor.html"
	return render (request,template,context)

def view_conveyor(request):
	context = {"range":range(100)}
	template = "content/view_conveyor.html"
	return render (request,template,context)

def add_conveyor(request):
	context = {"range":range(8)}
	template = "content/add_conveyor.html"
	return render (request,template,context)

def data_customer(request):
	context = {"range":range(100)}
	template = "content/data_customer.html"
	return render (request,template,context)

def view_customer(request):
	context = {"range":range(10)}
	template = "content/view_customer.html"
	return render (request,template,context)

def add_customer(request):
	context = {}
	template = "content/add_customer.html"
	return render (request,template,context)

def data_site(request):
	context = {"range":range(100)}
	template = "content/data_site.html"
	return render (request,template,context)

def view_site(request):
	context = {"range":range(10)}
	template = "content/view_site.html"
	return render (request,template,context)

def add_customer_site(request):
	context = {}
	template = "content/add_customer_site.html"
	return render (request,template,context)

def data_area(request):
	context = {"range":range(100)}
	template = "content/data_area.html"
	return render (request,template,context)

def view_area(request):
	context = {"range":range(5)}
	template = "content/view_area.html"
	return render (request,template,context)

def add_area(request):
	context = {"range":range(4)}
	template = "content/add_area.html"
	return render (request,template,context)

def detail_conveyor_condition(request):
	context = {"part":["Belt Conveyor","SECTION SPLICE BELT","Pulley","ROLLER","PRIMARY Cleaners","Secondary Cleaners"]}
	template = "content/detail_conveyor_condition.html"
	return render (request,template,context)

def login(request):

	if request.method == 'POST':   
		username = request.POST['username']
  		password = request.POST['passwd']                                                                                                                                                                                                        
		login_form =  authenticate(username=username, password=password)
		response_data = {}                                                                              
		if login_form is not None:
			if login_form.is_active:
				response_data['accessGranted'] = 'Success!'
				response_data['result'] = 'Success!'
				response_data['message'] = 'You"re logged in' 		
		else:
			response_data['result'] = 'failed'
			response_data['message'] = 'You messed up'   
		print response_data['result'],"<<<<<<<<<<<<<<<"
		return HttpResponse(json.dumps(response_data), content_type="application/json")  