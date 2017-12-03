from rest_framework import permissions



class IsOwnerOrReadOnly(permissions.BasePermission):
    message ='you dont have persmission body'

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
