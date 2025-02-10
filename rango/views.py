from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
    
    #retrives top 5 ordered by likes
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = pages_list

    # render(users request/template we wanna use, template file name, context dictionary)
    #//The render() function will take this data and mash it together with the template to produce
    # a complete HTML page that is returned with a HttpResponse.//
    return render(request, 'rango/index.html', context=context_dict)

def about(request):

    context_dict= {'boldmessage':'This tutorial has been put together by Aimee'}

    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):

    context_dict={}

    try:
        category = Category.objects.get(slug=category_name_slug)

        #retrieves all assoiciated pages
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        #use this in the template to verify that the category exists
        context_dict['category'] = category

    except Category.DoesNotExist:

        context_dict['pages']=None
        context_dict['category']=None

    except Page.DoesNotExist:
        context_dict['pages']=None
    
    return render(request, 'rango/category.html', context=context_dict)