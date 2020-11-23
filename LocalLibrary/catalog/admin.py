from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
admin.site.register(Genre)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')
  def display_genre(self, genre):
    return ', '.join(genre.name for genre in self.genre.all()[:3])

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  pass