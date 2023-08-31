from django.contrib import admin
from .models import Post, Comment, Gallery, News
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'post', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ('body',)

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured_image', 'created_on',)
    search_fields = ['title', 'content']


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'user', 'website', 'external_link',)
    search_fields = ['title', 'website']