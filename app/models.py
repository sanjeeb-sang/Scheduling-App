from django.db import models

# Create your models here.

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class Suggestion(models.Model):

    user_name = models.CharField(max_length = 40)

    user_email = models.EmailField(max_length = 40)

    suggestion = models.TextField()

    def __str__(self):
        return self.user_email

    def save_suggestion(self, post_values):

        self.user_name = post_values['user_name']
        self.user_email = post_values['user_email']
        self.suggestion = post_values['suggestion']


class Appointment(models.Model):

    professor_name = models.CharField(max_length = 40)
    professor_email = models.EmailField()
    user_email = models.EmailField()
    user_name = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def clean_date (self, date):
        list = date.split(" ")
        month = list[0]
        day = list[1].replace(",", "")
        year = list[2]
        return str(year) + "-" + str(MONTHS.index(month) + 1) + "-" + str(day)

    def clean_time (self, time):
        time = time.replace("noon", "12:00 p.m")
        list = time.split(" ");
        t = list[0]
        timeList = t.split(":")
        hour = int(timeList[0])
        mins = "00"
        if len(timeList) > 1:
            mins = timeList[1]
        pmOrAm = list[1]
        if "p.m" in pmOrAm:
            hour += 12;
        if hour == 24:
            hour -= 12;
        return str(hour) + ":" + mins
    
    def __str__(self):
        return self.professor_name + " at " + self.user_email
    def save_data(self, post_values, user, prof_user, prof_object):
        self.professor_name = prof_object.title + " " + prof_user.first_name + " " + prof_user.last_name;
        self.professor_email = prof_user.email;
        self.user_name = user.first_name + " " + user.last_name
        self.user_email = user.email
        self.date = self.clean_date(post_values['date'])
        self.start_time = self.clean_time(post_values['start_time'])
        self.end_time = self.clean_time(post_values['end_time'])

class TimeSlot(models.Model):

    professor_name = models.CharField(max_length = 40)
    professor_email = models.EmailField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.professor_name

    def save_data(self, p_name, p_email, start, end, date):
        self.professor_name = p_name
        self.professor_email = p_email
        self.date = date
        self.start_time = start
        self.end_time = end

class Professor(models.Model):

    email = models.EmailField();
    title = models.CharField(max_length = 10, default = "Dr. ");

    def __str__(self):
        return self.email

class Student(models.Model):

    email = models.EmailField();

    def __str__(self):
        return self.email

class ProfessorStudent(models.Model):

    student_email = models.EmailField();
    professor_email = models.EmailField();

    def __str__(self):
        return "Professor - " + self.professor_email + " Student - " + self.student_email;