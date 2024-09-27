# views.py
from rest_framework.generics import UpdateAPIView
from apps.users.models import User # or your custom user model
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfileUpdateSerializer

class UserProfileUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Override this method to return the logged-in user
        return self.request.user
