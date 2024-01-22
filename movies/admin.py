from .models import Member, Movie, UserProfile, Movies

from django.contrib import admin

# class JaribuAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image')


admin.site.register(Movie)
admin.site.register(Movies)
admin.site.register(Member)
admin.site.register(UserProfile)
# admin.site.register(Jaribu, JaribuAdmin)

# admin.py
from django.contrib import admin

admin.site.site_header = 'Your Site Admin'
admin.site.site_title = 'Your Site Admin'

