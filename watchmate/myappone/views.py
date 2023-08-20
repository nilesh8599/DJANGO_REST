from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from myappone.models import Movie


# def movie_list(request):
#     movies = Movie.objects.all()
#     return HttpResponse(movies.values())


def movie_list(request):
    movies = Movie.objects.all()

    data ={
        'movies':list(movies.values())
    }

    return JsonResponse(data)

