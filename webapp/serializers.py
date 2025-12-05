from accounts.serializers import UserNestedSerializer
from webapp.models import Major, Type, University
from rest_framework import serializers


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)
    major = MajorSerializer(read_only=True, many=True)

    class Meta:
        model = University
        fields = ('id', 'name', 'description', 'min_unt_score', 'tuition_fee', 'city', 'major', 'type', 'image_url', 'languages', 'scholarships', 'internships')
