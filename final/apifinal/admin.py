from django.contrib import admin

# Register your models here.
from .models import Story, Comment, UserProfile

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'story', 'created_at')
    list_filter = ('story',)
    search_fields = ('content',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'karma_points')
    search_fields = ('username', 'email')

admin.site.register(Story, StoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
