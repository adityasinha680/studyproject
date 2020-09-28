from django.db import models


# Create your models here.
class Course (models.Model):
	course_title = models.CharField(max_length=100)
	institute_name = models.CharField(max_length=100)
	course_desc =models.CharField(max_length=300)
