from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField()
    image = models.ImageField(upload_to="photos/", null=True, blank=True)


    def __str__(self):
        return self.name


    def delete(self, *args, **kwargs):
        import os
        # Delete associated media file before deleting the object
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)





#teacher manager
class TeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(position__in=['senior_teacher', 'junior_teacher'])



class Staff(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField()
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to="photos/", null=True, blank=True)


    objects = models.Manager() # default manager
    teachers = TeacherManager() # custom manager



    def __str__(self):
        return self.name


    def delete(self, *args, **kwargs):
        import os
        # Delete associated media file before deleting the object
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)




class Class(models.Model):
    name = models.CharField(max_length=100)
    type_1 = models.CharField(max_length=100, null=True, blank=True)
    type_2 = models.CharField(max_length=100, null=True, blank=True)
    type_3 = models.CharField(max_length=100, null=True, blank=True)



    students = models.ManyToManyField(Student, related_name="classes", blank=True, through="StudentClass")
    teacher = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name="classes", null=True, blank=True)


    class Meta:
        verbose_name_plural = "Classes"


    def __str__(self):
        return self.name + "-" + self.type_1 + "-" + self.type_2 + "-" + self.type_3




class StudentClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="get_classes")
    classes = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="get_students")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student.name+" - "+self.classes.name