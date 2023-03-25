from django.contrib import admin

from .models import BlockedDay, Building, Room, Room_Type

# Register your models here.

admin.site.register(Building)

admin.site.register(Room_Type)

admin.site.register(Room)

class BlockedDayAdmin(admin.ModelAdmin):  
  list_display = ("Day",)

admin.site.register(BlockedDay, BlockedDayAdmin)



