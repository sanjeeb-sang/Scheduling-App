from django.shortcuts import render, redirect, HttpResponse
from app.forms import SuggestionForm, SignUpForm
from app.models import Suggestion, TimeSlot, Appointment, Professor, Student, ProfessorStudent
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import json
from django.http import JsonResponse
from app.helpers.email_helper import MassEmailSender 

# Create your views here.

def index(request):
    data = {'title' : 'Home'}
    status = request.session['status'];
    data['status'] = status
    if (status == 'student'):
        data['professor_email'] = request.session['professor_email']
    return render(request, 'index.html', data)
 
def contact(request):
    return render(request, 'contact.html', {'title' : 'Contact'})

def send_remainder_emails(request):

    massEmailSender = MassEmailSender();
    massEmailSender.sendAllEmails();

    return JsonResponse({"result" : "Ok"})

def suggestions(request):

    if request.method == 'GET':
        # If the method is get, then just display the suggestion page
        return render(request, 'suggestions.html', {'title' : 'Suggestions', 'form' : SuggestionForm()})
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

    return render(request, 'all_suggestions.html', {"title" : "Suggestions", "suggestions" : all})


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


def timeslots(request):

    if request.method == 'GET':
        slots = TimeSlot.objects.order_by("-date", "-start_time")
        # If the method is get, then just display the suggestion page
        return render(request, 'professor_view/add_time_slots_2.html', {'title' : 'Add time slot', "timeslots" : slots})
    else:
        # slots = json.loads(request.POST.get("slots", ""))
        startTimes = request.POST.getlist("startTimes[]")
        endTimes = request.POST.getlist("endTimes[]")
        professor_email = request.POST.get("professor_email")
        prof = None
        try:
            prof = Professor.objects.get(email = professor_email);
        except Professor.DoesNotExist:
            return JsonResponse({'result' : "Erro"})
        date = request.POST.get("date") 
        professor_name = request.user.first_name + " " + request.user.last_name;      
        if prof != None:
              professor_name = prof.title + " " + professor_name
        for i in range(len(startTimes)):
            start = startTimes[i]
            end = endTimes[i]
            timeslot = TimeSlot()
            timeslot.save_data(professor_name, professor_email, start, end, date)
            timeslot.save()
        
        return JsonResponse({'result' : 'Ok'})

    
def all_timeslots(request):

    slots = TimeSlot.objects.order_by("-date", "-start_time")

    return render(request, 'common/all_time_slots_2.html', {'timeslots' : slots, "title" : "All TimeSlots"})


def delete_timeslot(request, id):

    TimeSlot.objects.get(id=id).delete()

    return redirect('/all_timeslots/')

def get_all_timeslots(request):

    slots = TimeSlot.objects.order_by('start_time')

    return render(request, 'common/all_time_slots.html', {'timeslots' : slots, "title" : "All TimeSlots"})
   

def appointments(request):

    if request.method == 'GET':
        return redirect("/all_appointments/")

    else:
        # slots = json.loads(request.POST.get("slots", ""))
        appointments = Appointment.objects.filter(user_email = request.user.email);
        if (appointments.count() > 0):
            return JsonResponse({"result" : "Error"});
        appointment = Appointment();
        profRel = ProfessorStudent.objects.get(student_email = request.user.email);
        prof = Professor.objects.get(email = profRel.professor_email);
        profUser = User.objects.get(email = profRel.professor_email)
        appointment.save_data(request.POST, request.user, profUser, prof);
        appointment.save();
        TimeSlot.objects.get(id=request.POST['timeslot_id']).delete()
        return JsonResponse({'result' : 'Ok'})

    
def all_appointments(request):
    a = []
    if (request.session['status'] == "student"):
        a = Appointment.objects.filter(user_email=request.user.email)
    if (request.session['status'] == "professor"):
        a = Appointment.objects.filter(professor_email = request.user.email)
    return render(request, 'common/all_appointments.html', {'appointments' : a, "title" : "All Appointments"})


def delete_appointment(request, id):

    app = Appointment.objects.get(id=id)
    app.delete()
    slot = TimeSlot()
    slot.save_data(app.professor_name, app.professor_email, app.start_time, app.end_time, app.date)
    slot.save()

    return redirect('/all_appointments/')