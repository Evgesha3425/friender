from django.contrib import admin
from .models import User, Establishment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'date_of_birth', 'gender', 'looking_gender')  # Поля, которые отображаются в приложении
    list_filter = ('gender', 'looking_gender')  # Поля, по которым можно фильтровать
    # fields = ('name', 'age')  # Поля, которые можно будет изменять при вхождении в профиль


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    pass


# admin.site.register(User, UserAdmin)
# admin.site.register(Establishment, EstablishmentAdmin)
# admin.site.register(User)
# admin.site.register(Establishment)

