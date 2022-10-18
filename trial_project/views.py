
# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse

# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def hello_name (request) :
 
    # This will return "Hello Nimish, this is view from project"
    # string as HttpResponse
    return HttpResponse("Hello Nimish, this is view from project")
