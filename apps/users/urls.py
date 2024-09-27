from tkinter.font import names

from apps.users.api_endpoints.loginRequirets import LoginRequestAPIView
from apps.users.api_endpoints.loginVerify import LoginVerifyAPIView
from apps.users.api_endpoints.registerEntry import RegisterEntryAPIView
from apps.users.api_endpoints.registerVerify import RegisterVerifyAPIView
from apps.users.api_endpoints.updateProfile import UserProfileUpdateView
from apps.users.api_endpoints.updateProfileAvatar import UserProfileUpdateAvatarView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #loginb
    path("login-request/", LoginRequestAPIView.as_view(), name = 'login-request'),
    path("login-verify/", LoginVerifyAPIView.as_view(),name = 'login-verify'),

    #register
    path("register-entry/", RegisterEntryAPIView.as_view(), name='register-entry'),
    path("register-verify/", RegisterVerifyAPIView.as_view(), name='register-verify'),


    #Profile Update
    path("profile-update/", UserProfileUpdateView.as_view(), name='profile-update'),
    path("profile-avatar/", UserProfileUpdateAvatarView.as_view(), name='profile-avatar'),

]

urlpatterns += [
    # boshqa URL lar
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)