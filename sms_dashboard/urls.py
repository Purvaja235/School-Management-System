from django.urls import path
from . import views

app_name = "sms_dashboard"


urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    #account
    path("accounts/signup/", views.signup_view, name="signup_view"),
    path("accounts/login/", views.login_view, name="login_view"),
    path("accounts/logout/", views.logout_view, name="logout_view"),

    #students
    path("admit/", views.admit, name="admit"),
    path("students/", views.students, name="students"),
    path("students/search/", views.search_student, name="search_student"),
    path("students/edit/<int:pk>/", views.student_edit, name="student_edit"),
    path("students/delete/<int:pk>/", views.student_delete, name="student_delete"),


    #id card
    path("generate_id_card/", views.generate_id_card, name="generate_id_card"),



    #staff
    path("staff/add/", views.staff_add, name="staff_add"),
    path("staff/edit/<int:staff_id>/", views.staff_edit, name="staff_edit"),
    path("staffs/", views.staffs, name="staffs"),
    path("staffs/search/", views.search_staff, name="search_staff"),
    path("staffs/delete/<int:staff_id>/", views.staff_delete, name="staff_delete"),


    #class
    path("class/add/", views.class_add, name="class_add"),
    path("class/edit/<int:class_id>/", views.class_edit, name="class_edit"),
    path("classes/", views.classes, name="classes"),
    path("classes/search/", views.search_class, name="search_class"),
    path("classes/delete/<int:class_id>/", views.class_delete, name="class_delete"),


    #StudentClass
    path("student_class/add/", views.add_student_to_class, name="add_student_to_class"),
    path("students_classes/", views.students_classes, name="students_classes"),



]
