from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm
# Create your views here.
def create(request):
    frm=MovieForm()
    if request.POST:
       frm=MovieForm(request.POST)
       if frm.is_valid:
           frm.save()
       else:
           frm=MovieForm()
    #    title= request.POST.get('title')
    #    year= request.POST.get('year')
    #    summary= request.POST.get('desc')
    #    movie_obj=MovieInfo(title=title,year=year,desc=summary)
    #    movie_obj.save()

    
    return render(request,'create.html',{'frm':frm})


def list(request):
    movie_data = MovieInfo.objects.all()
    print(movie_data)

    return render(request,'list.html',{'movie_list':movie_data})


def edit(request,pk):
    instance_edit=MovieInfo.objects.get(pk=pk)
    frm=MovieForm(instance=instance_edit)
    if request.POST:
        frm=MovieForm(request.POST,instance=instance_edit)
        if frm.is_valid():
            frm.save()
    else:

        # title=request.POST.get('title')
        # year=request.POST.get('year')
        # description=request.POST.get('desc')

        # instance_edit.title=title
        # instance_edit.year=year
        # instance_edit.desc=description

        # instance_edit.save()
        frm=MovieForm(instance=instance_edit)


    return render(request,'create.html',{'frm':frm})


def delete(request,pk):
    Instance=MovieInfo.objects.get(pk=pk)
    Instance.delete()

    Movie_set=MovieInfo.objects.all()


    return render(request,'list.html',{'movie_list':Movie_set})