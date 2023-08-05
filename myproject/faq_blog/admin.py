from django.contrib import admin
from .models import FAQ, Blog, Review, ContactUs

# Register your models here.
admin.site.register(Blog)
admin.site.register(FAQ)
admin.site.register(Review)
admin.site.register(ContactUs)