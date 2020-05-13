from rest_framework import serializers
from .models import Status

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status

        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']

        def validate_content(self, value):
            if len(value) > 500:
                return serializers.ValidationError("This is way too long.")
            return value

        def validate(self, data):
            content = data.get('content', None)
            if content == "":
                content = None

            image = data.get('image', None)

            if not content and not image:
                raise serializers.ValidationError("Provide either content or image.")

            return data