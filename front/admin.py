from django.contrib import admin

# Register your models here.
from front.models import Nav, Download, Contact, Aboutus


class NavAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'path', 'level', 'priority')

# class DownloadAdmin(admin.ModelAdmin):
#     list_display = ('type', 'download_img', 'qrcode_img', 'url', 'gmt_create')
#
#     def add_view(self, request, form_url='', extra_context=None):
#         pass
#
#     def save_form(self, request, form, change):
#         pass
#
#     def save_model(self, request, obj, form, change):
#         pass

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'content', 'gmt_create', 'status')

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('content','title')

class ProductAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(Nav, NavAdmin)
# admin.site.register(Download, DownloadAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Aboutus, AboutUsAdmin)