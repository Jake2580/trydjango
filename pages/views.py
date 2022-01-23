from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(f'request: {request.user}, args: {args}, kwargs: {kwargs}')
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_context = {
        "title": "abc this is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [2424, 4231, 312, 'Abc'],
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request, 'about.html', my_context)

def social_view(*args, **kwargs):
    html = "<h1>Social Page</h1>"
    return HttpResponse(html)
