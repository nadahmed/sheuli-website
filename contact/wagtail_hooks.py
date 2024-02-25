from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Contact
from wagtail.contrib.modeladmin.helpers import PermissionHelper

class ContactAdminPermissionHelper(PermissionHelper):

    def user_can_delete_obj(self, user, obj):
        if user.is_superuser:
            return True
        return False

    def user_can_edit_obj(self, user, obj):
        return False

    def user_can_create(self, user):
        return False
    
    def user_can_list(self, user):
        return True

@modeladmin_register
class ContactAdmin(ModelAdmin):
    model = Contact
    permission_helper_class = ContactAdminPermissionHelper
    menu_label = 'Contact'
    menu_icon = 'mail'
    menu_order = 200
    inspect_view_enabled = True
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)