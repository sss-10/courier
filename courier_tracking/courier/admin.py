from django.contrib import admin

# Register your models here.
from courier.models import Login, Signup, Orders

admin.site.register(Login)
admin.site.register(Signup)
admin.site.register(Orders)