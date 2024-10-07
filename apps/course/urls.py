from apps.course.api_endpoints.courseList.views import CourseListAPIView
from  apps.course.api_endpoints.courseDetail.views import CourseDetailApiView
from apps.course.api_endpoints.courseComment.views import CourseReviewView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("courses/", CourseListAPIView.as_view(), name='course-list'),
    path("course-detail/<int:pk>/", CourseDetailApiView.as_view(), name='course-detail'),
    path("course-comment", CourseReviewView.as_view(), name= 'course-comment' )
]

