# Create your views here.
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializers_class = UserSerializer







