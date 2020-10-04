from django.shortcuts import render
from studyapp import models
from django.http import HttpResponseRedirect
from django.urls import reverse	
from django.http import HttpResponseBadRequest
import json
import requests
from studyapp.models import Course
from math import ceil
import io
import base64
from PIL import Image
from django.core.files.storage import FileSystemStorage

# Create your views here.
def get_base64_encoded_image(image_path):
	with open(image_path, "rb") as img_file:
		return base64.b64encode(img_file.read()).decode('utf-8')
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
	return render(request,'index.html',{'page_num':page_num, 'next_page_link':next_page_link, 'previous_page_link':previous_page_link, 'result_data':result_data,'course_list':course_list, 'next_page':str(next_page), 'previous_page':str(previous_page)})

def update(request):
	"""
	This function modifies courses.
	"""
	course_id = request.GET.get('course_id')
	if request.method == 'POST':
		course_title = request.POST['course_title']
		institute_name = request.POST['institute_name']
		course_desc = request.POST['course_desc']
		image_data = request .FILES ['photo']
		current_data = Course.objects.get(course_id = course_id)
		current_data.course_title = course_title
		current_data.institute_name = institute_name
		current_data.course_desc = course_desc
		current_data.save()
		return HttpResponseRedirect(reverse('courseapp:index'))
	data = Course.objects.get(course_id = course_id)
	return render(request,'update.html',{'data':data})

def create(request):
	

	"""
	This function creates new courses.
	"""
	if request.method == 'POST':
		
		
		course_title = request.POST['course_title']
		institute_name = request.POST['institute_name']
		course_desc = request.POST['course_desc']
		image_data = request .FILES.FILES['photo']

		
		# def get_base64_encoded_image(image_path):
		#     with open(image_path, "rb") as img_file:
		#         return base64.b64encode(img_file.read()).decode('utf-8')
		# print(get_base64_encoded_image(image_data))
		# # up_img = str(image_data.read())
		# conv_data = base64.b64decode(up_img)
		# print(conv_data)

		# with open(request.FILES['photo'],"rb") as image_file:
		# 	encode_string = base64.b64decode(image_file.read())

		# print(encode_string)


		data = models.Course(course_title=course_title,institute_name=institute_name,
								course_desc=course_desc,course_image = image_data)
		data.save()
		image_datas = 'media/images/' + image_data.name
		return_data = get_base64_encoded_image(image_datas)
		# print(get_base64_encoded_image(image_datas))
		current_data = Course.objects.all().last()
		current_data.course_image = return_data
		return HttpResponseRedirect(reverse('courseapp:index'))
	return render(request,'add.html')

def image_page(request):
	
	return render(request,'image_page.html')