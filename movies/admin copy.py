from .models import Member, Movie, UserProfile

from django.contrib import admin


admin.site.register(Movie)
admin.site.register(Member)
admin.site.register(UserProfile)