from django.contrib import admin

from .models import Ad
from .models import Country
from .models import Gender
from .models import Users

admin.site.register(Ad)
admin.site.register(Country)
admin.site.register(Gender)
admin.site.register(Users)

