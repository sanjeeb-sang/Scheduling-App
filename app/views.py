from django.shortcuts import render, redirect
from app.forms import SuggestionForm, SignUpForm, InternshipForm, JobForm
from app.models import Suggestion, Internship, Job
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):

    return render(request, 'index.html', {'title' : 'Home', 'message' : 'Hello, and welcome to my site'})


def contact(request):

    return render(request, 'contact.html', {'title' : 'Contact', 'message' : 'This page contains my contact info'})


def courses(request):

    return render(request, 'courses.html', {'title' : 'Courses', 'message' : 'View some of my courses'})


def suggestions(request):

    if request.method == 'GET':
        # If the method is get, then just display the suggestion page
        return render(request, 'suggestions.html', {'title' : 'Suggestions', 'form' : SuggestionForm(), 'message' : 'Suubmit a new Suggestion'})
    else:
        # If the method is post, then store the value
        form = SuggestionForm(request.POST);
        if form.is_valid():
            suggestion = Suggestion()
            suggestion.save_suggestion(request.POST)
            suggestion.save()

            return redirect('/all_suggestions/')
   

def all_suggestions(request):

    suggestions = Suggestion.objects.all()

    return render(request, 'all_suggestions.html', {'suggestions' : suggestions, 'title' : "All Suggestions"})


def delete_suggestion(request, id):

    Suggestion.objects.get(id=id).delete()

    all = Suggestion.objects.all();

    return render(request, 'all_suggestions.html', {"title" : "Suggestions", "suggestions" : all, 'message' : 'One Suggestion deleted'})


def legal_information(request):

    return render(request, 'legal_information.html', {'title' : 'Legal Information'})


def about(request):

    return render(request, 'about.html', {'title' : 'About'})


def help(request):

    return render(request, 'help.html', {'title' : 'Help'})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user);
            return redirect('index');
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, "title" : "Sign Up"})


def profile(request):

    return render(request, 'profile.html', {'user' : request.user, "title" : "Profile"})




def internships(request):

    if request.method == 'GET':
        # If the method is get, then just display the suggestion page
        return render(request, 'internship/internships.html', {'title' : 'Internships', 'form' : InternshipForm()})
    else:
        # If the method is post, then store the value
        form = InternshipForm(request.POST);
        if form.is_valid():
            internship = Internship()
            internship.save_internship(request.POST)
            internship.save()

            return redirect('/all_internships/')
   

def all_internships(request):

    internships = Internship.objects.all()

    return render(request, 'internship/all_internships.html', {'internships' : internships, "title" : "All Internships"})


def delete_internship(request, id):

    Internship.objects.get(id=id).delete()

    all = Internship.objects.all();

    return render(request, 'internship/all_internships.html', {"title" : "Internships", 'message' : 'One Intership deleted', 'internships' : all})


def jobs(request):

    if request.method == 'GET':
        # If the method is get, then just display the suggestion page
        return render(request, 'job/jobs.html', {'title' : 'Jobs', 'form' : JobForm()})
    else:
        # If the method is post, then store the value
        form = JobForm(request.POST);
        if form.is_valid():
            job = Job()
            job.save_job(request.POST)
            job.save()

            return redirect('/all_jobs/')
   

def all_jobs(request):

    jobs = Job.objects.all()

    return render(request, 'job/all_jobs.html', {'jobs' : jobs, "title" : "All Jobs"})


def delete_job(request, id):

    Job.objects.get(id=id).delete()

    all = Job.objects.all();

    return render(request, 'job/all_jobs.html', {"title"  :"Jobs", 'message' : 'One Job deleted', "jobs" : all})
