from rest_framework.permissions import BasePermission
from .models import Address

class IsVerified(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_verified()
    
class IsValidUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        add_ids = [i['id'] for i in Address.objects.filter(user = request.user.id).values()]
        if obj.id not in add_ids:
            return False
        return True