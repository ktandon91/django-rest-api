from rest_framework import permissions
from django.contrib.auth.models import Group
from django.contrib.auth import  get_user_model
from rest_framework.response import Response

User = get_user_model()

class FullAcess(permissions.BasePermission):

    def has_permission(self, request, view):
        pass


class LimitedAccess(permissions.BasePermission):

    def has_permission(self, request, view):
        group = request.user.groups.filter(name='limited_access')
        if group.exists():
            return True

        return False
