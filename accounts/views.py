from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import logout
from accounts import serializers
from rest_framework import views, status, permissions, generics


class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Logout(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class CurrentUserView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CurrentUserSerializer

    def get_object(self):
        return self.request.user


def profile(request):
    return render(request, 'accounts/profile.html')

def login(request):
    return render(request, 'accounts/login.html')
