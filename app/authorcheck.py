from rest_framework import permissions

class IsAuthor(permissions.BasePermission):				#incomplete
	def check_permission(self, request, view, obj):
		return True