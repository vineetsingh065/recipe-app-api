from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):

	"""Create new user"""
	serializer_class = UserSerializer


class CreateToken(ObtainAuthToken):

	serializers = AuthTokenSerializer
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES