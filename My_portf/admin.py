from django.contrib import admin
from .models import Opinion,Blog,Education,Experience,Contact,Portfolio
# Register your models here.
admin.site.register(Experience)
admin.site.register(Blog)
admin.site.register(Portfolio)
admin.site.register(Contact)
admin.site.register(Education)
admin.site.register(Opinion)