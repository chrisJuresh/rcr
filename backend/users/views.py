from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer, RoleSerializer
from .models import Role
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.contrib.auth import logout

User = get_user_model()

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            response_data = {'token': token.key}
            return Response(response_data, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.create_user(
                    username=serializer.validated_data['username'],
                    password=serializer.validated_data['password'],
                )
                token, _ = Token.objects.get_or_create(user=user)
                response_data = {'token': token.key}
                return Response(response_data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({'error': 'A user with that username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer



class ValidateToken(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response({
            'user_id': request.user.id,
            'username': request.user.username,
            'email': request.user.email
        }, status=status.HTTP_200_OK)


from django.contrib.auth import logout

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)