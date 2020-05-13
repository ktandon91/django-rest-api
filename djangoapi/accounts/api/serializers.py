from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]

        extra_kwargs = { 'password': {'write_only':True}}

        def valide(self, data):
            password1 = data.get('password')
            password2 = data.get('password2')

            if password1 != password2:
                raise serializers.ValidationError("Password must match")
            #this will give error since django will try to create user with password2 as an argument
            #either remove password2 here or overwrite create method.
            return data

        def create(self, validated_data):
            user_obj = User.objects.create(username=validated_data.get('username'),
                                           email=validated_data.get('email'))
            user_obj.set_password(validated_data.get('password'))
            user_obj.save()
            return user_obj