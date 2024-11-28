from django.contrib import admin

# Register your models here.

from .models import Question, Choice


class ChoiceInline(admin.TabularInline[Choice]):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin[Question]):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
