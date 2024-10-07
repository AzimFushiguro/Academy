from rest_framework import serializers
from apps.course.models import Course, Lesson, Module, CourseReview


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title']


class ModuleSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ["title", "lessons"]

    def get_lessons(self, obj):
        return LessonSerializer(obj.lessons, many=True).data


class ReviewSerializer(serializers.ModelSerializer):
    user_full_name = serializers.SerializerMethodField()
    class Meta:
        model = CourseReview
        fields = ["rating", "comment", "user_full_name"]

    def get_user_full_name(self, obj):
        return obj.user.full_name

    def get_user(self,obj):
        return
class CourseDetailSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    modules = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["title", "description", "rating", "modules"]

    def get_rating(self, obj):
        return ReviewSerializer(obj.ratings, many=True).data

    def get_modules(self, obj):
        return ModuleSerializer(obj.moduless, many=True).data
