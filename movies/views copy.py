import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Jaribu, Movie, UserProfile
from .forms import LoginForm, MemberForm, RegistrationForm
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def jaribu(request, item_id):
    item = Jaribu.objects.get(pk=item_id)
    return render(request, 'movies\jaribu.html', {'item': item})


def login_or_register(request):
    if request.method == 'POST':
        # Check if the form is for login or registration
        if 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # Handle login logic
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']


# Query the database to check credentials
            try:
                user = UserProfile.objects.get(username=username, password=password)
                return redirect('list')
            except UserProfile.DoesNotExist:
                # Authentication failed, display an error message
                # You can customize this part based on your requirements
                login_form.add_error(None, 'Invalid username or password')
                registration_form = RegistrationForm()
                return render(request, 'registration/login.html', {'login_form': login_form, 'registration_form': registration_form})
            


                # user = authenticate(request, username=username, password=password)
                # if user is not None:
                #     login(request, user)
                #     return redirect('list')  # Redirect to the dashboard or another page after login
                    
                # else:
                #     print(username)
                #     print(password)
                #     return redirect('seat')
                    # Authentication failed, display an error message
                    # login_form.add_error(None, 'Invalid username or password')
                
        elif 'register' in request.POST:

            registration_form = RegistrationForm(request.POST)

            if registration_form.is_valid():
                # Handle registration logic
                username = registration_form.cleaned_data['username']
                password = registration_form.cleaned_data['password']
                confirm_password = registration_form.cleaned_data['confirm_password']

                if password == confirm_password:
                    # Create a new user profile
                    user_profile = UserProfile(username=username, password=password)

                    user_profile.save()

                    return redirect('login_or_register')  # Redirect to the same page or a login page after registration
                
                else:
                    login_form = LoginForm()
                    registration_form.add_error(None, 'Unmatched passwords')  # Redirect to the same page or a login page after registration
                    return render(request, 'registration/login.html', {'login_form': login_form, 'registration_form': registration_form})


    else:
        # Render the page with both forms for GET requests
        login_form = LoginForm()
        registration_form = RegistrationForm()
        return render(request, 'registration/login.html', {'login_form': login_form, 'registration_form': registration_form})







def movieDetails(request, title_id):
    try:
        import requests

        url = "https://netflix54.p.rapidapi.com/title/details/"

        querystring = {"ids": title_id,"lang":"en"}

        headers = {
            "X-RapidAPI-Key": "d36244c78bmsh748fd1611f4f5c8p149ad2jsn0c2dbce20a66",
            "X-RapidAPI-Host": "netflix54.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)


        response=response.json()
        print(response)
        return render(request, 'movies/movieDetails.html', {'response':response})
    
    except requests.exceptions.RequestException as e:
         return render(request, 'movies/movieDetails.html')
 
    


def seatSelection(request):
    return render(request, 'movies/seatSelection.html')

def movieList(request):
    movies = Jaribu.objects.all()
    return render(request, 'movies/movielist.html', {'movies': movies})

# def register(request):
#     return HttpResponse("Register Page")

def login(request):
    return render(request, 'movies/login.html')


def index(request):
    form = MemberForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)


def netflixDisplay(request):
    try:
        url = "https://netflix54.p.rapidapi.com/search/"
        querystring = {"query":"stranger","offset":"5","limit_titles":"5","limit_suggestions":"20","lang":"en"}
        headers = {
            "X-RapidAPI-Key": "d36244c78bmsh748fd1611f4f5c8p149ad2jsn0c2dbce20a66",
            "X-RapidAPI-Host": "netflix54.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        print(response.json())
        response=response.json()
        return render(request, 'movies/movielist.html', response)
    
    except requests.exceptions.RequestException as e:
         return render(request, 'movies/movielist.html')




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
