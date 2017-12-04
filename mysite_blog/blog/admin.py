from django.contrib import admin
from .models import Post, Comment, ContactRequest, UserProfileInfo

admin.site.register(Comment)
admin.site.register(ContactRequest)
admin.site.register(UserProfileInfo)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_per_page = 25

admin.site.register(Post, PostAdmin)
