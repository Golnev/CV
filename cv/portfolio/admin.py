from django.contrib import admin

from .models import Education, WorkExperience, Contact


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'years_work', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message')
