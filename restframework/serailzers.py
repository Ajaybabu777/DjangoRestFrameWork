from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class StudentSerailzer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self,data):
        if data['age'] < 18:
            raise serializers.ValidationError({"error":"age should be greater than 18"})
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error":"name only in alphabets"})
        return data
    
class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self,validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user