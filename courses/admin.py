from django.contrib import admin
from .models import Course, Lesson, UserProgress


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ('order', 'title', 'youtube_url')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    ordering = ('course', 'order')


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'completed', 'completed_at')
    list_filter = ('completed', 'lesson__course')
    search_fields = ('user__username', 'lesson__title')
