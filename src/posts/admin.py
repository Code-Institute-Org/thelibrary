from django.contrib import admin
from .models import Post, PostCategory, PostTag, PostFlag, Bookmark


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(PostTag)
admin.site.register(PostFlag)
admin.site.register(Bookmark)
