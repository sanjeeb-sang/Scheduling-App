from django.db import models

# Create your models here.

class Suggestion(models.Model):

    user_name = models.CharField(max_length = 40)

    user_email = models.EmailField(max_length = 40)

    suggestion = models.TextField()

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

    def save_appointment(self, post_values):

        self.professor_name = post_values['professor_name']
        self.professor_email = post_values['professor_email']
        self.user_name = post_values['user_name']
        self.user_email = post_values['user_email']
        self.date = post_values['date']
        self.start_time = post_values['start_time']
        self.end_time = post_values['end_time']

class TimeSlot(models.Model):

    professor_name = models.CharField(max_length = 40)
    professor_email = models.EmailField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def save_data(self, p_name, p_email, start, end, date):
        self.professor_name = p_name
        self.professor_email = p_email
        self.date = date
        self.start_time = start
        self.end_time = end


class Internship(models.Model):

    internship_name = models.CharField(max_length = 200)
    company_name = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    date_posted = models.DateField()

    def save_internship(self, post_values):

        self.internship_name = post_values['internship_name']
        self.company_name = post_values['company_name']
        self.url = post_values['url']
        self.date_posted = post_values['date_posted']


class Job(models.Model):

    job_name = models.CharField(max_length = 200)
    company_name = models.CharField(max_length = 100)
    url = models.CharField(max_length = 200)
    date_posted = models.DateField()

    def save_job(self, post_values):

        self.job_name = post_values['job_name']
        self.company_name = post_values['company_name']
        self.url = post_values['url']
        self.date_posted = post_values['date_posted']
