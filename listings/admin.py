from django.contrib import admin
 
from .models import Listing

# //TO show the fields in the admin we need to do like below
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
#to make clickable teh column or the field in the admin
    list_display_links =('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields =('title','description','address','city','state','price')
    list_per_page =25


admin.site.register(Listing,ListingAdmin)