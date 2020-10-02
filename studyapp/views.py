from rest_framework import viewsets
from rest_framework import permissions
from studyapp.serializers import UserSerializer
from studyapp.models import Course





class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


