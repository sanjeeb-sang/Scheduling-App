from django.core.mail import send_mail
from Scheduling_Website import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import datetime
from app.models import Appointment
from django.utils import formats

CONFIRM_EMAIL_URL = "http://www.ulm-scheduler.herokuapp.com/confirm/";

class MassEmailSender(object):

    def sendAllEmails(self):
        date = datetime.date.today()
        date = str(date.year) + "-" + str(date.month) + "-" + str(date.day + 1)
        appointments = Appointment.objects.filter(date = date)
        for appointment in appointments:
            self.sendEmails(appointment)
            
    def sendEmails(self, appointment):
        emailSender = EmailSender()
        emailSender.sendEmail(appointment.user_email, appointment.user_name, appointment.professor_name, appointment)
        emailSender.sendEmail(appointment.professor_email, appointment.professor_name, appointment.user_name, appointment)

class ConfirmationEmailSender(object):

    def sendConfirmationalEmail(self, user) :
     
        p = user.get_profile();
        title = "Ulm Scheduler Email account confirmation";
        content = "Hi, " + user.username + "\n\n\nHope you like our application.\nFor additional security, we require users to verify email. Please click on the link below to verify your email.\n\n" + CONFIRM_EMAIL_URL + str(p.confirmation_code) + "/" + user.username + "\n\nSincerely,\nULM Scheduler App team";
        EmailSender().sendEmail(title, content, user.email);


class EmailSender(object):

    def sendEmail(self, one_email, one_name, another_name, appointment):

        print("Starting sending email to " + one_email);

        self.sendTextEmail(one_email, one_name, another_name, appointment)

        print("Sent email to " + one_email)


    def sendTextEmail(self, one_email, one_name, another_name, appointment):

        greeting = "\nHi " + one_name + ",\n\n"

        remainderText = "This is a remainder for your appointment with " + another_name 
        start = getTime(appointment.start_time);
        end = getTime(appointment.end_time);

        print(start)

        timeText = " today from " + start + " to " + end

        ending = "\n\n\nSincerely,\nULM Scheduling Website"

        body = greeting + remainderText + timeText + ending 

        send_mail('About appointment with ' + another_name,
            body,
            settings.EMAIL_HOST_USER,
            [one_email],
            fail_silently=False,)

    def sendHtmlEmail(self, email):

        subject, from_email, to = 'Welcome to Keepr', settings.EMAIL_HOST_USER, email

        html_content = render_to_string('email_template.html', {'user': to}) # render with dynamic value
        text_content = strip_tags(html_content) # Strip the html tag.  So people can see the pure text at least.

        # create the email, and attach the HTML version as well.
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

def getTime(timeList):
    hour = int(timeList[0]);
    mins = int(timeList[1]);
    amOrPm = "am."
    if (hour > 12):
        hour -= 12;
        amOrPm = "pm.";
    if (mins == 0):
        return str(hour) + " " + amOrPm;
    else:
        return str(hour) + ":" + str(mins) + " " + amOrPm; 

def getTime(time):
    hour = time.hour;
    mins = time.minute;
    amOrPm = "am."
    if (hour > 12):
        hour -= 12;
        amOrPm = "pm.";
    if (mins == 0):
        return str(hour) + " " + amOrPm;
    else:
        return str(hour) + ":" + str(mins) + " " + amOrPm; 