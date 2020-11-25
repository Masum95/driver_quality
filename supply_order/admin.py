from django.contrib import admin
from supply_order import models

admin.site.register(models.SupplyOrder)

#
# @admin.register(models.SupplyOrder)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_filter = ('author', )
#
# @admin.register(models.FeedbackReact)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_filter = ('post', )