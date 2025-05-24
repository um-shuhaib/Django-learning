from django.db import models

# Create your models here.
class CensorInfo(models.Model):
    rating=models.CharField(max_length=20,null=True)
    certify_by=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.rating

class Directors (models.Model):
    name=models.TextField(max_length=250)

    def __str__(self):
        return self.name

class Actors(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MovieInfo (models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    desc=models.TextField()
    poster=models.ImageField(upload_to='image/',null=True)
    censor_details=models.OneToOneField(CensorInfo,on_delete=models.SET_NULL,related_name='movie',null=True)
    directed_by=models.ForeignKey(Directors,null=True,related_name='movie_director',on_delete=models.CASCADE)
    actors=models.ManyToManyField(Actors,related_name='movie_actors')


    def __str__(self):
        return self.title

