import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Movie
from .forms import MemberForm
import requests

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


def index(request):
    form = MemberForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)



def netflixDisplay(request):
    url = "https://netflix54.p.rapidapi.com/search/"
    querystring = {"query":"stranger","offset":"30","limit_titles":"5","limit_suggestions":"20","lang":"en"}
    headers = {
        "X-RapidAPI-Key": "d36244c78bmsh748fd1611f4f5c8p149ad2jsn0c2dbce20a66",
        "X-RapidAPI-Host": "netflix54.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    response=response.json()
    return render(request, 'movies/movielist.html', response)



def netflixToJson(request):
    url = "https://netflix54.p.rapidapi.com/search/"
    querystring = {"query":"stranger","offset":"0","limit_titles":"200","limit_suggestions":"20","lang":"en"}
    headers = {
        "X-RapidAPI-Key": "d36244c78bmsh748fd1611f4f5c8p149ad2jsn0c2dbce20a66",
        "X-RapidAPI-Host": "netflix54.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    response=response.json()

 # Convert the JSON data to a string
    json_string = json.dumps(response, indent=2)

        # Specify the file path where you want to save the JSON
    file_path = "netflix_json2.json"

        # Write the JSON string to the file
    with open(file_path, "w") as file:
        file.write(json_string)

    return JsonResponse({"status": "JSON saved to file successfully"})


def read_json_from_file(request):
    # Specify the file path where you saved the JSON
    file_path = "netflix_json.json"

    # Read the JSON from the file
    with open(file_path, "r") as file:
        json_data = json.load(file)

    return render(request, 'movies/netflix.html', json_data)


def cardPayment(request):
    return render(request, 'movies/cardPayment.html')
