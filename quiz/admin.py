from django.contrib import admin
from . import models
# Register your models here.
class categoryslug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

admin.site.register(models.Category, categoryslug)
admin.site.register(models.Question)
admin.site.register(models.Quiz)
admin.site.register(models.Choice)
admin.site.register(models.Review)
