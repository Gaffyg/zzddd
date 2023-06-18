from django.contrib import admin
from .models import *


class ConcertAdmin(admin.ModelAdmin):
    list_display = ('city', 'place', 'date')
    list_display_links = ('city', 'place')
    search_fields = ('city', 'place')
    prepopulated_fields = {'slug': ('city', 'place')}


class LinksAdmin(admin.ModelAdmin):
    pass
    # list_display = ('platform', 'link')
    # list_display_links = ('platform', 'link',)


class ClipsAdmin(admin.ModelAdmin):
    pass
    # list_display = ('link', 'image')
    # list_display_links = ('link', 'image')


class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'count_bilet', 'data_time_buy', 'city', 'place')
    list_display_links = ('name', 'email')
    list_filter = ('city', 'place', 'name', 'email', 'data_time_buy')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'text', 'image')
    list_display_links = ('post_id', 'text')


admin.site.register(Concert, ConcertAdmin)
admin.site.register(Group)
admin.site.register(Clips, ClipsAdmin)
# admin.site.register(Links, LinksAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(News, NewsAdmin)
