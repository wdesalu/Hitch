from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, redirect

from models import *
from forms import *

#from hitch.models import Driver, Client

# ------------Define webpages-------------
def index(request):
    return render(request,'hitch/index.html')


def client(request):
	print "client method starts"
	context = {}

	allDrivers = Driver.objects.all()
	print allDrivers

	context['drivers'] = allDrivers
	return render(request,'hitch/client.html',context)

def driver(request):

	print "--got into driver!"

	context = {}

	if(request.method == "GET"):
		context = {'form': RegistrationForm()}
		return render(request,'hitch/driver.html',context)
	elif request.method == "POST":
		print "POST WOOWOWOWOWOWO"

		form_new = RegistrationForm(request.POST)
		context['form'] = form_new

	if not form_new.is_valid():	
		return render(request,'hitch/driver.html',context)


	# code reaching here means the form is valid
	username = form_new.cleaned_data['username']
	emailGiven = form_new.cleaned_data['emailGiven']
	clientNumber = form_new.cleaned_data['clientNumber']
	ppm = form_new.cleaned_data['ppm']
	bagCapacity = form_new.cleaned_data['bagCapacity']
	departureGiven = form_new.cleaned_data['departureGiven']
	destinationGiven = form_new.cleaned_data['destinationGiven']

	new_driver = Driver(name=username, email = emailGiven, client_capacity = clientNumber, pricepermile = ppm, bag_capacity = bagCapacity, departure = departureGiven, destination = destinationGiven)

	new_driver.save()
	print "SAVED YU$$$$$$$$"
	print Driver.objects.all()
	return redirect("/hitch/accept")



def accept(request):
	print "--got into accept!"
	return render(request,'hitch/accept.html')


# -------- Client Side --------------------


