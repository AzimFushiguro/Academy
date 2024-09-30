from rest_framework import serializers
from apps.course.models import Course


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title','description','price','cover']