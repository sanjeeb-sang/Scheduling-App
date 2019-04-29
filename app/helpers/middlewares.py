from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from app.helpers.professor_student import *
from app.models import ProfessorStudent

dontRedirectOn = ["accounts", "signup"]

class AuthRequiredMiddleware(MiddlewareMixin):

    def process_view(self, request, view, args, kwargs):
       
        for url in dontRedirectOn:
            if url in request.path:
                return None

        if request.user is None or not request.user.is_authenticated:
            return redirect("/accounts/login/")

        return None

class ProfessorStudentRelationMiddleware(MiddlewareMixin):

    def process_view(self, request, view, args, kwargs):
        status = getStatus(request.user)
        request.session['status'] = status
        if status == 'student':
            try:
                rel = ProfessorStudent.objects.get(student_email=request.user.email)
                request.session['professor_email'] = rel.professor_email
            except ProfessorStudent.DoesNotExist:
                print("User is not assigned a professor yet.")
            
        return None