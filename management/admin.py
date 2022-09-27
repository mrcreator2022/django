from django.contrib import admin
from .models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date')


# Register your models here.

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)


