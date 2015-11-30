from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from MrJeevesApp.models import ROSActionOutput
from django.http import JsonResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'MrJeevesApp/index.html', context_dict)

def GetActionData(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    data_list = ROSActionOutput.objects

    # Render the response and send it back!
    return JsonResponse({'data': data_list})

