from django.contrib import admin
from .models import Review, Contact, Menu


admin.site.site_header = 'KokaniKitchen Administration'

# Register your models here.
admin.site.register(Review)
admin.site.register(Contact)
admin.site.register(Menu)