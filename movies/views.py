from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


# def moviesDetail(request):
#     data = Movie.objects.all()

#     return render(request, 'movies/movieDetail.html', {'movies':data})
#     # return render(request, 'movies/movies.html', {'movies':data})

def seatSelection(request):
    return render(request, 'movies/seatSelection.html')

def movieList(request):
    return render(request, 'movies/movielist.html')

def register(request):
    return HttpResponse("Register Page")

def login(request):
    return render(request, 'movies/login.html')
