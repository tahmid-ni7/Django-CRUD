from django.contrib import admin
from .models import Member
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone', 'designation', 'is_active')
    list_display_links = ('name','id')
    list_editable = ('is_active',)
    search_fields = ('name', 'email', 'phone', 'designation')
    list_per_page = 25

admin.site.register(Member, MemberAdmin)
