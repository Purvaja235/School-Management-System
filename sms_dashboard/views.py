from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST

from django.contrib.auth.models import User
from django.contrib import messages
from . import models
# from . import utils


#for id card pdf generation
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import utils
from io import BytesIO



@login_required
def dashboard(request):

    total_students = models.Student.objects.count()
    total_staffs = models.Staff.objects.count()
    total_classes = models.Class.objects.count()

    context = {
        "total_students": total_students,
        "total_staffs": total_staffs,
        "total_classes": total_classes
    }
    return render(request, "sms_dashboard/dashboard.html", context)



def signup_view(request):

    if request.method == 'POST':
        post_data = request.POST
        username = post_data.get('username')
        password = post_data.get('password')
        password_confirm = post_data.get('password_confirm')

        if len(str(password)) < 8:
            context = {
                'error': "Password must be at least 8 characters"
                
            }
            return render(request, "sms_dashboard/signup/index.html", context)
        
        if password != password_confirm:
            context = {
                'error': "Password and Confirm Password doesn't match"

            }
            
            return render(request, "sms_dashboard/signup/index.html", context)


        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully for " + user.username)

        return redirect("sms_dashboard:login_view")


        

    return render(request, "sms_dashboard/signup/index.html")




def login_view(request):

    if request.method == 'POST':
        post_data = request.POST
        username = post_data.get('username')
        password = post_data.get('password')

        if len(str(password)) < 8:
            context = {
                'error': "Password must be at least 8 characters"
                
            }
            return render(request, "sms_dashboard/login/index.html", context)
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            

            return redirect("sms_dashboard:dashboard")
        
        
        context = {
            'error': "Username or password is incorrect"
                
        }

        return render(request, "sms_dashboard/login/index.html", context)


        

    return render(request, "sms_dashboard/login/index.html")



def logout_view(request):
    logout(request)
    return redirect("sms_dashboard:login_view")


@login_required
def admit(request):

    if request.method=="POST":

        post_data = request.POST

        name = post_data.get('name')
        address = post_data.get('address')
        phone_no = post_data.get('phone_no')
        gender = post_data.get('gender')
        email = post_data.get('email')
        dob = post_data.get('dob')

        # print(name, address, phone_no, gender, email, dob)
        # print(gender)
        student = models.Student.objects.create(name=name, address=address, phone_no=phone_no, gender=gender, email=email, dob=dob)
        messages.success(request, "Student admitted successfully")

        return redirect("sms_dashboard:dashboard")
        # return render(request, "sms_dashboard/admission.html")


    return render(request, "sms_dashboard/admission.html")



@login_required
def students(request):

    if request.session.get('student_name'):
        student_name = request.session.get('student_name')
        print(student_name)
        students = models.Student.objects.filter(name__icontains=student_name)
        request.session['student_name'] = None
    else:
        students = models.Student.objects.all()


    classes = models.Class.objects.all()
    context = {
        "students": students,
        "classes": classes
    }
    return render(request, "sms_dashboard/students.html", context)






@login_required
def search_student(request):
    student_name = request.GET.get('search_name')
    request.session['student_name'] = student_name

    
    return redirect("sms_dashboard:students")



@login_required
def student_edit(request, pk):
    if request.method=="POST": 

  
       
        student = models.Student.objects.get(pk=pk)
        for key, value in request.POST.items():
            if len(value) != 0:
                setattr(student, key, value)

        
        image = request.FILES.get('student_photo')
        if image is not None:
            student.image = image
        
        student.save()
        messages.success(request, "Student updated successfully")

        return redirect("sms_dashboard:students")
    
    else:
        student = models.Student.objects.get(pk=pk)
        context = {
            "student": student
        }

        return render(request, "sms_dashboard/student_edit.html", context)



@login_required
def student_delete(request, pk):
    student = models.Student.objects.get(pk=pk)

    student.delete()
    messages.success(request, "Student deleted successfully")

    return redirect("sms_dashboard:students")



@login_required
def generate_id_card(request):

    student_name = request.GET.get("search_name")

    if student_name:
        students = models.Student.objects.filter(name__icontains=student_name)

        # import os
        # absolute_uri = os.path.abspath(settings.MEDIA_ROOT)

        # print(absolute_uri)
    


        context = {
            "students": students,
        }
        return render(request, "sms_dashboard/generate_id_card.html", context)

    else:
        return render(request, "sms_dashboard/generate_id_card.html")        

    

@login_required
def staff_add(request):

    if request.method=="POST":
        data = request.POST

        name = data.get('name')
        address = data.get('address')
        phone_no = data.get('phone_no')
        gender = data.get('gender')
        email = data.get('email')
        dob = data.get('dob')
        position = data.get('position')

        # print(name, address, phone_no, gender, email, dob, position)

        staff = models.Staff.objects.create(name=name, address=address, phone_no=phone_no, gender=gender, email=email, dob=dob, position=position)
        messages.success(request, "Staff added successfully")

        return redirect("sms_dashboard:dashboard")




    return render(request, "sms_dashboard/staff_add.html")





@login_required
def staffs(request):

    if request.session.get('staff_name'):
        staff_name = request.session.get('staff_name')
        staffs = models.Staff.objects.filter(name__icontains=staff_name)
        request.session['staff_name'] = None
    else:
        staffs = models.Staff.objects.all()

    context = {
        "staffs": staffs
    }
    return render(request, "sms_dashboard/staffs.html", context)




@login_required
def search_staff(request):
    staff_name = request.GET.get('search_name')
    request.session['staff_name'] = staff_name

    
    return redirect("sms_dashboard:staffs")





@login_required
def staff_edit(request, staff_id):
    if request.method=="POST": 

       
        staff = models.Staff.objects.get(pk=staff_id)
        for key, value in request.POST.items():
            if len(value) != 0:
                setattr(staff, key, value)

        
        image = request.FILES.get('staff_photo')
        if image is not None:
            staff.image = image
        
        staff.save()
        messages.success(request, "Staff updated successfully")

        return redirect("sms_dashboard:staffs")
    
    else:
        staff = models.Staff.objects.get(pk=staff_id)
        context = {
            "staff": staff
        }

        return render(request, "sms_dashboard/staff_edit.html", context)




@login_required
def staff_delete(request, staff_id):
    staff = models.Staff.objects.get(pk=staff_id)

    staff.delete()
    messages.success(request, "Satff deleted successfully")

    return redirect("sms_dashboard:staffs")






#class
@login_required
def class_add(request):

    if request.method=="POST":
        data = request.POST

        name = data.get('name')
        type_1 = data.get('type_1')
        type_2 = data.get('type_2')
        type_3 = data.get('type_3')
        teacher_id = data.get('teacher')

        teacher = models.Staff.objects.get(pk=teacher_id)

        models.Class.objects.create(name=name, type_1=type_1, type_2=type_2, type_3=type_3, teacher=teacher)

        messages.success(request, "Class added successfully")

        return redirect("sms_dashboard:dashboard")


    
    teachers = models.Staff.teachers.all()

    context = {
        "teachers": teachers
    }


    return render(request, "sms_dashboard/class_add.html", context)




@login_required
def classes(request):

    if request.session.get('class_name'):
        class_name = request.session.get('class_name')
        classes = models.Class.objects.filter(name__icontains=class_name)
        request.session['class_name'] = None
    else:
        classes = models.Class.objects.all()

    context = {
        "classes": classes
    }
    return render(request, "sms_dashboard/classes.html", context)



@login_required
def search_class(request):
    class_name = request.GET.get('search_name')
    request.session['class_name'] = class_name

    
    return redirect("sms_dashboard:classes")



@login_required
def class_delete(request, class_id):
    class_ = models.Class.objects.get(pk=class_id)

    class_.delete()
    messages.success(request, "Class deleted successfully")

    return redirect("sms_dashboard:classes")



@login_required
def class_edit(request, class_id):
    if request.method=="POST": 

       
        class_ = models.Class.objects.get(pk=class_id)
        for key, value in request.POST.items():
            if len(value) != 0:
                if key == "teacher":
                    teacher = models.Staff.objects.get(pk=value)
                    setattr(class_, key, teacher)
                else:
                    setattr(class_, key, value)

        
      
        class_.save()
        messages.success(request, "Class updated successfully")

        return redirect("sms_dashboard:classes")
    
    else:
        class_ = models.Class.objects.get(pk=class_id)
        teachers = models.Staff.teachers.all()
        print(class_.teacher)


        context = {
            "class": class_,
            "current_teacher":class_.teacher,
            "teachers": teachers.exclude(id=class_.teacher.id)
        }

        return render(request, "sms_dashboard/class_edit.html", context)



@require_POST
@login_required
def add_student_to_class(request):

    student_id = request.POST.get("student_id")
    class_id = request.POST.get("class_id")

    student = models.Student.objects.get(pk=student_id)
    class_ = models.Class.objects.get(pk=class_id)

    models.StudentClass.objects.create(student=student, classes=class_)
    messages.success(request, f"{student.name} added to {class_.name} class successfully")

    return redirect("sms_dashboard:dashboard")




@login_required
def students_classes(request):

    if request.GET.get('student_name'):
        student_name = request.GET.get('student_name')
        print(student_name)
        students_classes = models.StudentClass.objects.filter(student__name__icontains=student_name)
       

    elif request.GET.get('class_name'):
        class_name = request.GET.get('class_name')
        print(class_name)
        students_classes = models.StudentClass.objects.filter(classes__name__icontains=class_name)

    else:  
        students_classes = models.StudentClass.objects.all().order_by('-date')

    context = {
        "students_classes": students_classes
    }
    
    return render(request, "sms_dashboard/students _classes.html", context)