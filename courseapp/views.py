from django.shortcuts import render
from studyapp import models
from django.http import HttpResponseRedirect
from django.urls import reverse	
from django.http import HttpResponseBadRequest
import json
import requests
from studyapp.models import Course
from math import ceil
import base64



# Create your views here.

def index(request):

	"""
	This function is used to fetch all the data from API.
	"""

	course_list=[]
	next_page = 0
	page = request.GET.get('page')
	if page is None:
		page_num = "1"
	else:
		page_num = page
	next_page = int(page_num)+1
	previous_page = int(page_num)-1
	course_api_url= "http://127.0.0.1:8000/myapi/Course/?page=" + page_num
	course_api_data=requests.get(course_api_url)
	if course_api_data is None:
		return HttpResponseBadRequest("400 Bad Request Error")

	data=course_api_data.json()
	if 'next' in data:
		next_page_link=data['next']
	if 'previous' in data:
		previous_page_link=data['previous']
	if 'count' in data:
		new_count=data['count']
	count=ceil(new_count/8)
	for item in range(count):
		course_list.append(item+1)
	result_data=data['results']
<<<<<<< HEAD
	return render(request,'index.html',{'page_num':page_num, 'next_page_link':next_page_link, 'previous_page_link':previous_page_link, 'result_data':result_data,'course_list':course_list, 'next_page':str(next_page), 'previous_page':str(previous_page)})
=======
	database_course= models.Course.objects.all()
	return render(request,'index.html',{'database_course':database_course, 'page_num':page_num, 'next_page_link':next_page_link, 'previous_page_link':previous_page_link, 'result_data':result_data,'course_list':course_list, 'next_page':str(next_page), 'previous_page':str(previous_page)})
>>>>>>> 72f4279497219059a43c826018757ae80f00e4b1

def update(request):
	"""
	This function modifies courses.
	"""
<<<<<<< HEAD

=======
>>>>>>> 72f4279497219059a43c826018757ae80f00e4b1
	name = request.GET.get('name')
	if request.method == 'POST':
		course_title = request.POST['course_title']
		institute_name = request.POST['institute_name']
		course_desc = request.POST['course_desc']
		current_data = Course.objects.get(course_title = name)
		current_data.course_title = course_title
		current_data.institute_name = institute_name
		current_data.course_desc = course_desc
		current_data.save()
		return HttpResponseRedirect(reverse('courseapp:index'))
	data = Course.objects.get(course_title = name)
	return render(request,'update.html',{'data':data})

<<<<<<< HEAD
def create(request):
	

=======
def create(request): 
>>>>>>> 72f4279497219059a43c826018757ae80f00e4b1
	"""
	This function creates new courses.
	"""
	if request.method == 'POST':
<<<<<<< HEAD
		# import pdb
		# pdb.set_trace()
		
		course_title = request.POST['course_title']
		institute_name = request.POST['institute_name']
		course_desc = request.POST['course_desc']
		# image_data = request.FILES['image']
		data = models.Course(course_title=course_title,institute_name=institute_name,
								course_desc=course_desc)
=======
		course_title = request.POST['course_title']
		institute_name = request.POST['institute_name']
		course_desc = request.POST['course_desc']
		data = models.Course(course_title=course_title,institute_name=institute_name,course_desc=course_desc)
>>>>>>> 72f4279497219059a43c826018757ae80f00e4b1
		data.save()

		return HttpResponseRedirect(reverse('courseapp:index'))
	return render(request,'add.html')
