from django.contrib import admin

# Register your models here.

from .models import Article

class AdminArticle(admin.ModelAdmin):
    list_display= ['title','slug','author','body','created_date']
    prepopulated_fields = {"slug":('title',)}
admin.site.register(Article,AdminArticle)

#rohan -->Rohan@123