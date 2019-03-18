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
