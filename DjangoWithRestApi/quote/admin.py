from django.contrib import admin

from . models import Quote,QuoteCategory



admin.site.site_header="My Dashboard"


admin.site.register(Quote)
admin.site.register(QuoteCategory)
