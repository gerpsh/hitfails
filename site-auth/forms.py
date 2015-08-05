from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
	username = forms.CharField(max_length=16, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Username'}))
	password = forms.CharField(required=True, widget=forms.PasswordInput())

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("Username or password incorrect")
		return self.cleaned_data

	def login(self, request):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		return user