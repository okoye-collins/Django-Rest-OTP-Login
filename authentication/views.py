from django.shortcuts import render

from .serializers import UserRegistrationSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.


class UserRegistration(GenericAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'message': "User account was created successly"}, status=status.HTTP_201_CREATED)