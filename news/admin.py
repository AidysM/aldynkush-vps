from django.contrib import admin

from .models import Author, Rubric, New, AdditionalImage, Comment


admin.site.register(Author)
admin.site.register(Rubric)
admin.site.register(New)
admin.site.register(AdditionalImage)
admin.site.register(Comment)
