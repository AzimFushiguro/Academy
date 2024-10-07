from apps.course.models import Course
from rest_framework.generics import RetrieveAPIView
from .serializers import CourseDetailSerializer

class CourseDetailApiView(RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course


