from apps.course.models import Course
from rest_framework.generics import ListAPIView
from .serializers import CourseListSerializer

class CourseListAPIView(ListAPIView):
    queryset = Course.objects.filter(is_startted  = True)
    serializer_class = CourseListSerializer
