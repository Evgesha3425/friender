from django.contrib import admin
from .models import User, Establishment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'gender', 'looking_gender')


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    pass


# admin.site.register(User, UserAdmin)
# admin.site.register(Establishment, EstablishmentAdmin)
# admin.site.register(User)
# admin.site.register(Establishment)

