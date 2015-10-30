__author__ = 'gmena'
from django.shortcuts import render_to_response


class PermissionRequired(object):
    """
    Handle Permission for the views
    :var failure_perm_template // The default not authorized view
    :var permission_requires // The permission needed for view
    """
    failure_perm_template = 'layout/error/permission_denied.html'
    permission_required = None

    def check_permission(self, usr):
        """
        Check for user permission
        :param usr:
        :return:
        """
        if type(self.permission_required) == list:
            return usr.has_perms(self.permission_required)
        return False

    def custom_permission_handle(self):
        """
        Abstract method
        Check form custom permission handler
        :return:
        """
        return True

    def dispatch(self, request, *args, **kwargs):
        """
        Inherit dispatch from generic view
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # Not permission?
        if not self.check_permission(request.user) \
                or not self.custom_permission_handle():
            context = dict()
            context['error'] = '403'
            context['message'] = 'You do not have permission to access this area'
            return render_to_response(self.failure_perm_template, context)

        return super(PermissionRequired, self).dispatch(request, *args, **kwargs)
