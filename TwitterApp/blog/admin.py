from django.contrib import admin
from .models import Twitt
# Register your models here.
class TwittAdmin(admin.ModelAdmin):
    # list_display = ["name","email"]
    list_display = [field.name for field in Twitt._meta.fields]
    search_fields = ['title']
    class Meta:
        model = Twitt


admin.site.register(Twitt, TwittAdmin)
