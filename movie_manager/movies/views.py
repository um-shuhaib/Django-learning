from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm
# Create your views here.
def create(request):
    frm=MovieForm()
    if request.method == 'POST':
       frm=MovieForm(request.POST,request.FILES)
       if frm.is_valid():
           frm.save()
       else:
           print("Form errors:", frm.errors)
    else:
        frm=MovieForm()
    #    title= request.POST.get('title')
    #    year= request.POST.get('year')
    #    summary= request.POST.get('desc')
    #    movie_obj=MovieInfo(title=title,year=year,desc=summary)
    #    movie_obj.save()

    
    return render(request,'create.html',{'frm':frm})


def list(request):
    recent_visits=request.session.get('recent_visits',[])
    recent_movie_set=MovieInfo.objects.filter(pk__in=recent_visits)
    movie_data = MovieInfo.objects.all()
    print(movie_data)
    visiters=int((request.session.get('visiters',0)))
    visiters=visiters+1
    request.session['visiters']=visiters
    response=render(request,'list.html',{'movie_list':movie_data,'recent_movie_set':recent_movie_set,'visiters':visiters})
    
    return response


def edit(request,pk):
    instance_edit=MovieInfo.objects.get(pk=pk)
    frm=MovieForm(instance=instance_edit)
    if request.POST:
        frm=MovieForm(request.POST,request.FILES,instance=instance_edit)
        if frm.is_valid():
            frm.save()
    else:
        recent_visits=request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits

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