from django.shortcuts import render
from . models import MovieInfo
# Create your views here.
def create(request):
    if request.POST:
       title= request.POST.get('title')
       year= request.POST.get('year')
       summary= request.POST.get('summary')
       movie_obj=MovieInfo(title=title,year=year,desc=summary)
       movie_obj.save()

    
    return render(request,'create.html')


def list(request):
    movie_data = MovieInfo.objects.all()
    print(movie_data)

    return render(request,'list.html',{'movie_list':movie_data})


def edit(request):
    return render(request,'edit.html')
