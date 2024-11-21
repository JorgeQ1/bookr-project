from django.contrib import admin
from reviews.models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Contributor)
admin.site.register(Review)
admin.site.register(BookContributor)
admin.site.register(Publisher)