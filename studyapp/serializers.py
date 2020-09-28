from studyapp.models import Course
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'course_title', 'institute_name', 'course_desc']

