from django.db import models
import os

# Create your models here.
class Course (models.Model):
	"""
	table for courses having field course_id, course title, institute_name, course_dedc, course_image.
	"""
	course_id = models.AutoField(primary_key=True)
	course_title = models.CharField(max_length=100)
	institute_name = models.CharField(max_length=100)
	course_desc = models.CharField(max_length=300)
	course_image =models.ImageField(upload_to="images",default="")

