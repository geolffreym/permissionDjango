from django.views.generic import ListView
from pHandler.models import PHandler
from mixin.Permission import PermissionRequired


# Agencies
class List(PermissionRequired, ListView):
    """
    Class-based views needed
    https://docs.djangoproject.com/en/1.8/topics/class-based-views/
    """
    # Test Model
    model = PHandler
    # Has the user pHandler.view_phandler?
    # Fill the list with required permissions to access this view..
    permission_required = ['pHandler.view_phandler']
    # The failure perm template!! default ~ 'layout/error/permission_denied.html'
    failure_perm_template = 'error.html'
    # The main template
    template_name = 'pHandler.html'

    def custom_permission_handle(self):
        """
        Custom permission shall be verified, on par with the permissions list
        :return: bool
        """
        # Need a custom permission?
        return 1 == 1
