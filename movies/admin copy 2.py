from .models import Member, Movie, UserProfile, Theater

from django.contrib import admin


# class TheaterAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location')

# class TheaterInline(admin.TabularInline):  # or admin.StackedInline for a different layout
#     model = Movie.theaters.through  # the intermediate model for the ManyToManyField
#     extra = 1  # number of inline forms to show


# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('title', 'genre', 'language', 'release_date', 'price', 'category', 'theater_places')
#     search_fields = ('title', 'genre', 'language', 'category')
#     filter_horizontal = ('theaters',)
#     inlines = [TheaterInline]

#     def theater_places(self, obj):
#         return ", ".join([theater.name for theater in obj.theaters.all()])


# admin.site.register(Movie, MovieAdmin)
# admin.site.register(Movies, MoviesAdmin)
admin.site.register(Member)
admin.site.register(UserProfile)
# admin.site.register(Theater, TheaterAdmin)
# admin.site.register(Jaribu, JaribuAdmin)

# admin.py
from django.contrib import admin

admin.site.site_header = 'Your Site Admin'
admin.site.site_title = 'Your Site Admin'






from django.contrib import admin
from .models import Theater, Screen, Movie

class ScreenInline(admin.TabularInline):
    model = Screen
    extra = 4  # Assuming 4 screens per theater

class TheaterAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    inlines = [ScreenInline]

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'price', 'category', 'display_screens')

    def display_screens(self, obj):
        return ", ".join([f"{screen.theater.name} - Screen {screen.number}" for screen in obj.screens.all()])


class ScreenAdmin(admin.ModelAdmin):
    list_display = ('theater', 'number')

admin.site.register(Theater, TheaterAdmin)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(Movie, MovieAdmin)



