from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Newsletter
from wagtail.contrib.modeladmin.helpers import PermissionHelper


@modeladmin_register
class ContactAdmin(ModelAdmin):
    model = Newsletter
    menu_label = 'Newsletter'
    menu_icon = 'mail'
    menu_order = 200
    inspect_view_enabled = True
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('email', 'ip', 'created_at')
    search_fields = ('email', 'ip')
    list_filter = ('created_at',)