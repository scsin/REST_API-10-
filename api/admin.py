from django.contrib import admin

from api.models import LambdaF

from django.utils.html import format_html
from django.urls import reverse

class ListModelAdmin(admin.ModelAdmin):
    def ordered_list(self, obj):
        return f'{obj.lst}'

    def link_list(self, obj):
        href = reverse('admin:lambda', args=(obj.lst.pk))


admin.site.register(LambdaF, ListModelAdmin)
