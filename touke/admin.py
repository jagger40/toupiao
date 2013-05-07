from django.contrib import admin
from touke.models import Choice,Poll,Comment,UserProfile

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra=1

class CommentInline(admin.TabularInline):
    model = Comment
    extra=1

class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline,CommentInline]


# admin.site.register(UserProfile)
# admin.site.register(Choice)
admin.site.register(Poll,PollAdmin)
# admin.site.register(Comment)
