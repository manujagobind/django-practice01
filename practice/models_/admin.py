from django.contrib import admin

from .models import Person, Group, Membership, Restaurant, Place


admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)

admin.site.register(Place)
admin.site.register(Restaurant)