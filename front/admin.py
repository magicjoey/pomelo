from django.contrib import admin

# Register your models here.
from front.models import Nav


class NavAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'path', 'level', 'priority')

# admin.site.register(User, UserAdmin)
# admin.site.register(UserStatus, UserStatusAdmin)
# admin.site.register(UserInfo)
# admin.site.register(AuthGroup)
# admin.site.register(AuthMenu,AuthMenuAdmin)
# admin.site.register(AuthPrivilege)
# admin.site.register(AuthRole)
# admin.site.register(AuthRolePrivilege)
# admin.site.register(AuthUserPrivilege)
admin.site.register(Nav, NavAdmin)