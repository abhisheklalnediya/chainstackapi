from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from User.models import User, QuotaCredit

admin.site.register(User, UserAdmin)
admin.site.register(QuotaCredit)
