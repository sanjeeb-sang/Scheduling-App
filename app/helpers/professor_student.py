from app.models import Professor, Student, ProfessorStudent

def getStatus(user):
    if user == None or user.is_authenticated == False or user.email == None:
        return "none"
    status = "none"
    prof = Professor.objects.filter(email=user.email)
    if (prof.exists()):
        status = 'professor'
    student = Student.objects.filter(email=user.email)
    if (student.exists()):
        status = 'student'

    return status;