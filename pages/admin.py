from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('nombre1', 'order')

    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)
