from django.shortcuts import render

# Create your views here.
def create(request):
    if request.POST:
        print(request.POST.get('title'))
        print(request.POST.get('year'))
        print(request.POST.get('summary'))
    
    return render(request,'create.html')


def list(request):
    movie_data = {'movie_list': [ {
        'title':'Ghodha',
        'summary':'',
        'year':'2028',
        'success':False,
        'img':'music.png'
    },{
        'title':'mannan',
        'summary':'it is a good movie',
        'year':'2028',
        'success':True,
        'img':'real.jpg'
    },{
        'title':'rajav',
        'summary':'it is a good movie',
        'year':'2028',
        'success':True,
        'img':'real.jpg'
    },{
        'title':'pattini',
        'summary':'it is a good movie',
        'year':'2028',
        'success':False,
        'img':'music.png'
    },{
        'title':'saram',
        'summary':'it is a good movie',
        'year':'1990',
        'success':True,
        'img':'real.jpg'
    },{
        'title':'pani',
        'summary':'it is a good movie',
        'year':'2028',
        'success':True,
        'img':'music.png'
    }]}

    return render(request,'list.html',movie_data)


def edit(request):
    return render(request,'edit.html')
