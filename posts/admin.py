from django.contrib import admin

from .models import *

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(ParentComment)
admin.site.register(Mark)
admin.site.register(Picture)