from django.contrib import admin
from shop import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

