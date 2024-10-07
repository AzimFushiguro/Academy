from rest_framework.generics import CreateAPIView
from apps.course.models import CourseReview
from .serializers import CourseReviewSerializer


class CourseReviewView(CreateAPIView):
    serializer_class = CourseReviewSerializer
    queryset = CourseReview
