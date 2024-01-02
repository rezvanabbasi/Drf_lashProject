from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from apps.users.models import Profile


class IsAdminOrStaffPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        profile = Profile.objects.get(user_id=request.user.id)
        if profile.user_type.title != 'پرسنل':
            raise PermissionDenied('You are not staff!')
        return True
