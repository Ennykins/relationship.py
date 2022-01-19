from django.contrib import admin

from lead.models import User, Profile, Profile2,Blog, Product, tag

# Register your models here.


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Profile2)
admin.site.register(Blog)
admin.site.register(Product)
admin.site.register(tag)