from django.contrib import admin

from survey.models import Questions, Choice

admin.site.register(Questions)
admin.site.register(Choice)