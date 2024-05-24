from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password', write_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data,username=user_data['email'])
        Token.objects.create(user=user)
        return Customer.objects.create(user=user, **validated_data)


class loginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    allowed_methods = ['GET', 'POST']

    def create(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, requert):
        serializer = loginSerializer(data=requert.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(email=serializer.data['email'])

        if not user or (not user.first().check_password(serializer.data['password'])):
            return Response({'error': 'Invalid email or password'},
                            status=status.HTTP_400_BAD_REQUEST)
        print({'email': user.first().email, 'token': user.first().auth_token.key})
        return Response(
            {'email': user.first().email, 'token': user.first().auth_token.key},
            status=status.HTTP_200_OK,
        )