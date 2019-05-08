

class TimeslotsHandler ():

    def handle(self, request):
            # slots = json.loads(request.POST.get("slots", ""))
            startTimes = request.POST.getlist("startTimes[]")
            endTimes = request.POST.getlist("endTimes[]")
            professor_email = request.POST.get("professor_email")
            prof = None
            try:
                prof = Professor.objects.get(email = professor_email);
            except Professor.DoesNotExist:
                return JsonResponse({'result' : "Error"})
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