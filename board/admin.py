from django.contrib import admin

from .models import Master, Customer
# Register your models here.

class CustomerInLine(admin.TabularInline):
	model = Customer
	extra = 0

class MasterAdmin(admin.ModelAdmin):
	inlines = [CustomerInLine]

admin.site.register(Master, MasterAdmin)
# admin.site.register(Customer, CustomerInLine)

