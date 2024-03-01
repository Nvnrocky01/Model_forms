from django.contrib import admin

# Register your models here.
from app.models import *

class Custmizewebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_display_links=['url']
    list_editable=['name']
    list_filter=['name']
    list_per_page=1
    search_fields=('name',)


class Custmizeaccessrecord(admin.ModelAdmin):
    list_display=['name','author','date']


admin.site.register(Topic)
admin.site.register(Webpage,Custmizewebpage)
admin.site.register(AcessRecord,Custmizeaccessrecord)