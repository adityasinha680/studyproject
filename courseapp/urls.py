from django.urls import path
from courseapp import views

app_name = 'courseapp'

urlpatterns=[
	path('',views.index,name='index'),
	path('update/',views.update, name='update'),
	path('create/',views.create, name='create'),

]