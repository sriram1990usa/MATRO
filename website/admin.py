from django.contrib import admin
from website.models import *

# Register your models here.
@admin.register(contactus)
class contactAdmin(admin.ModelAdmin):
    list_display=[field.name for field in contactus._meta.get_fields()]

admin.site.register(blogs)
admin.site.register(serch)
# admin.site.register(Shortlist)
admin.site.register(ViewedSearchs)

'''@admin.register(searchs)
class searchAdmin(admin.ModelAdmin):
    list_display=[field.name for field in searchs._meta.get_fields()]'''

admin.site.register(Searchs)    

admin.site.register(showvideo)

admin.site.register(story)