from django.shortcuts import render, redirect, HttpResponse
from app.forms import SuggestionForm, SignUpForm, InternshipForm, JobForm
from app.models import Suggestion, Internship, Job, TimeSlot
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import json
from django.http import JsonResponse

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


def schedule(request):

    if request.method == 'GET':
        # If the method is get, then just display the suggestion page
        return render(request, 'schedule/schedule.html', {'user' : request.user, 'title' : 'Schedule'})
    else:
        # If the method is post, then store the value
        form = InternshipForm(request.POST);
        if form.is_valid():
            internship = Internship()
            internship.save_internship(request.POST)
            internship.save()

            return redirect('/all_schedules/')

    
def all_schedules(request):

    #internships = Internship.objects.all()

    return render(request, 'schedule/all_schedule.html', {"title" : "All Scheduled Appointments"})

def calendar(request):

    #internships = Internship.objects.all()

    return render(request, 'calendar/calendar.html', {"title" : "Calendar"})


def timeslots(request):

    if request.method == 'GET':
        # If the method is get, then just display the suggestion page
        return render(request, 'professor_view/add_time_slot.html', {'title' : 'Add time slot'})
    else:
        # slots = json.loads(request.POST.get("slots", ""))
        startTimes = request.POST.getlist("startTimes[]")
        endTimes = request.POST.getlist("endTimes[]")
        professor_name = request.POST.get("professor_name")
        professor_email = request.POST.get("professor_email")
        date = request.POST.get("date")
        
        for i in range(len(startTimes)):
            start = startTimes[i]
            end = endTimes[i]
            timeslot = TimeSlot()
            timeslot.save_data(professor_name, professor_email, start, end, date)
            timeslot.save()
        
        return JsonResponse({'result' : 'Ok'})

    
def all_timeslots(request):

    slots = TimeSlot.objects.all()

    return render(request, 'professor_view/all_time_slots.html', {'timeslots' : slots, "title" : "All TimeSlots"})


def delete_timeslot(request, id):

    TimeSlot.objects.get(id=id).delete()

    slots = TimeSlot.objects.all();

    return render(request, 'professor_view/all_time_slots.html', {"title"  :"TimeSlots", 'message' : 'One TimeSlot deleted', "timeslots" : slots})

def get_all_timeslots(request):

    slots = TimeSlot.objects.all()

    return render(request, 'professor_view/all_time_slots.html', {'timeslots' : slots, "title" : "All TimeSlots"})

"""
def delete_internship(request, id):

    Internship.objects.get(id=id).delete()

    all = Internship.objects.all();

    return render(request, 'internship/all_internships.html', {"title" : "Internships", 'message' : 'One Intership deleted', 'internships' : all})

    """