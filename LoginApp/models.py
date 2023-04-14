from django.db import models

# Create your models here.
class City(models.Model):
    CityName = models.CharField(max_length=50)

    def __str__(self):
        return self.CityName
class Course(models.Model):
    CourseName= models.CharField(max_length=50)

    def __str__(self):
        return self.CourseName
class Student(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=45)
    CityName = models.ForeignKey(City,on_delete=models.CASCADE)
    CourseName = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname