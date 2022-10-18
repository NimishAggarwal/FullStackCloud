#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from .forms import InputForm,NimishForm, NimishForm1, My_Form
from .models import My_Model
 
def index(request):
  return HttpResponse("Hello Nimish, this is view from app")

# Create your views here.
def home_view(request):
	#context ={}
	#context['form']= InputForm()
  ##print(request.GET)
	#return render(request, "home.html", context)
  ##print(request.POST)
  ##return render(request, "home.html")
	context = {}
	form = My_Form(request.POST or None)
	context['form'] = form
	return render(request, "home.html", context)
 
def home_view1(request):
    context ={}

 
    # create object of form
    # using Model through form as a medium
    form = My_Form(request.POST or None, request.FILES or None)
    # or other way is directly fetching values from model as below:
    '''
    data=User.objects.all()
    
    #for passing or showing the object values(values of fields), we just pass the collected data to our html file

    return render(request,'page1.html'),{'form':form,'dataset':data}

    # here form is used to make a structure as per data being collected
    # and dataset is used to display the actual data collected.(not mandatory, just for display)
    '''
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
 
    context['form']= form
    return render(request, "home.html", context)

# create a function
def home_view2(request):
	# create a dictionary to pass
	# data to the template
	context ={
		"data":"Gfg is the best",
		"list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	}
	# return response with template and context
	return render(request, "page1.html", context)

def show_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = My_Model.objects.all()
		
	return render(request, "show_view.html", context)

# pass id attribute from urls
def detail_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["data"] = My_Model.objects.get(id = id)
		
	return render(request, "detail_view.html", context)

# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(My_Model, id = id)
 
    # pass the object as instance in form
    form = My_Form(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    #context ={"tag":"Nimish"}
    context={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(My_Model, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)