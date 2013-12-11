from django import forms

from django.contrib.auth.models import User
from models import *

# ---------- Driver Registration ----------------
class RegistrationForm(forms.Form):
	username = forms.CharField(max_length=200,
								widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name','required':'on','autofocus':'on'}))
	emailGiven = forms.EmailField(max_length=200,
								widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email','required':'on','autofocus':'on'}))
	clientNumber = forms.IntegerField(
								widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Client Capacity','required':'on','autofocus':'on'}))
	ppm = forms.IntegerField(
								widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Price Per Mile','required':'on','autofocus':'on'}))
	bagCapacity = forms.IntegerField(
								widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Bag Capacity','required':'on','autofocus':'on'}))
	departureGiven = forms.DateTimeField(
								widget=forms.DateTimeInput(attrs={'class':'form-control','placeholder':'Departure Date','required':'on','autofocus':'on'}))
	destinationGiven = forms.CharField(max_length=200,
								widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Destination','required':'on','autofocus':'on'}))

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()

		username = cleaned_data['username']
		email = cleaned_data['emailGiven']
		clientNumber = cleaned_data['clientNumber']
		ppm = cleaned_data['ppm']
		bagCapacity = cleaned_data['bagCapacity']
		departureGiven = cleaned_data['departureGiven']
		destinationGiven = cleaned_data['destinationGiven']

		if not (username and email and clientNumber and ppm and bagCapacity and departureGiven and destinationGiven):
			raise forms.ValidationError("Not Enough Information")

		return cleaned_data