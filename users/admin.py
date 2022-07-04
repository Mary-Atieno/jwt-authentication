from pyexpat import model
from django.contrib import admin

from users.models import User

# Register your models here.
# admin.register(models.User)
admin.site.register(User)
