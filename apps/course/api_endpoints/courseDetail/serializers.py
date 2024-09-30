from rest_framework import serializers
from apps.course.models import Course, Lesson, Module, CourseReview


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title']
class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer()
    class Meta:
        model = Module
        fields = ["title","lessons"]
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = ["rating","comment","user. full_name"]

class CourseDetailSerializer(serializers.ModelSerializer):
    rating = ReviewSerializer()
    modules = ModuleSerializer()
    class Meta:
        model = Course
        fields = ["title","description","rating","modules"]