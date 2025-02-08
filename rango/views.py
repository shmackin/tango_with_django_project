from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict= {'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}

    # render(users request/template we wanna use, template file name, context dictionary)
    #//The render() function will take this data and mash it together with the template to produce
    # a complete HTML page that is returned with a HttpResponse.//
    return render(request, 'rango/index.html', context=context_dict)

def about(request):

    context_dict= {'boldmessage':'This tutorial has been put together by Aimee'}

    return render(request, 'rango/about.html', context=context_dict)
