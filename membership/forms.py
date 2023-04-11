from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.forms import CharField, PasswordInput
# from .models import User
# from django.contrib.auth.password_validation import validate_password
# from django.core import validators

# class UserForm(forms.ModelForm):

# 	email = forms.EmailField()
# 	first_name = forms.TextInput()
# 	middle_name = forms.TextInput()
# 	last_name = forms.TextInput
# 	# password = CharField(widget=PasswordInput())
# 	password = forms.CharField(widget=forms.PasswordInput)
# 	confirm_password = forms.CharField(widget=forms.PasswordInput)

# 	class Meta:
# 		model = User
# 		fields = ("email", "first_name", "middle_name", "last_name", "password", "confirm_password")
	

# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user
	    