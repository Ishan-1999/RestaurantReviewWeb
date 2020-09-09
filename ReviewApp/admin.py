from django.contrib import admin
from .models import Review, Querie, Dishe, TodaysSpecial


admin.site.site_header = 'KokaniKitchen Administration'

# Register your models here.
admin.site.register(Review)
admin.site.register(Querie)
admin.site.register(Dishe)
admin.site.register(TodaysSpecial)