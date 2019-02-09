from django.contrib import admin
from django.contrib.auth.models import Group

from . models import Quote
from . models import QuoteCategory


admin.site.site_header="My Dashboard"

class ContactAdmin(admin.ModelAdmin):
    list_display = ('quote','author')
    list_filter = ('created')



admin.site.register(Quote)
admin.site.register(QuoteCategory)
#admin.site.unregister(Group)
