from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def hello(request):
    movie_data = {'movie_list': [ {
        'title':'Ghodha',
        'summary':'',
        'year':'2028',
        'success':False
    },{
        'title':'mannan',
        'summary':'it is a good movie',
        'year':'2028',
        'success':True
    },{
        'title':'rajav',
        'summary':'it is a good movie',
        'year':'2028',
        'success':True
    },{
        'title':'pattini',
        'summary':'it is a good movie',
        'year':'2028',
        'success':False
    },{
        'title':'saram',
        'summary':'it is a good movie',
        'year':'1990',
        'success':True
    },{
        'title':'pani',
        'summary':'it is a good movie',
        'year':'2028',
        'success':True
    }]}
    return render(request,'hello.html',movie_data)