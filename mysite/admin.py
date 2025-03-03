from django.contrib import admin
from .models import Survey, Question, Journal


class QuestionInline(admin.TabularInline):  # Inline form to add questions within the survey
    model = Question
    extra = 1  # Number of empty question fields to show

class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]  # Attach inline questions

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question)