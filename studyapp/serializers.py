from studyapp.models import Course
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['course_id', 'course_title', 'institute_name', 'course_desc', 'course_image']

