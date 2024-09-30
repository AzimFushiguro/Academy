from apps.course.api_endpoints.courseList.views import CourseListAPIView
from apps.course.api_endpoints.courseDetail.views import Co, CourseDetailApiView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("courses/", CourseListAPIView.as_view(), name='course-list'),
    path("courses/", CourseDetailApiView.as_view(), name='course-detail')

]

