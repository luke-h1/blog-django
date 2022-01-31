from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25
  
admin.site.register(Author, AuthorAdmin)
