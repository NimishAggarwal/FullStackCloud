#from django import forms

'''class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()'''

# import the standard Django Forms
# from built-in library
from django import forms
from django.shortcuts import render
#from .forms import InputForm
   
# creating a form 
class InputForm(forms.Form):
   
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput())

'''# Create your views here.
def home_view(request):
	context ={}
	context['form']= InputForm()
	return render(request, "home.html", context)
'''
# import form class from django
from django import forms

# import My_Model from models.py
from .models import My_Model

# create a ModelForm
class My_Form(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = My_Model
		fields = "__all__"

#creating a django form using a form directly-if possible
class NimishForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField()
	views = forms.IntegerField()
	#date = forms.DateField()
	date = forms.DateField(widget = forms.SelectDateWidget)
    #available = forms.BooleanField()


class NimishForm1(forms.Form):
	title = forms.CharField(widget = forms.Textarea)
	description = forms.CharField(widget = forms.CheckboxInput)
	views = forms.IntegerField(widget = forms.TextInput)
	available = forms.BooleanField(widget = forms.Textarea)


