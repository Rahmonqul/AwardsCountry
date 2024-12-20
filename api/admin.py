from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Award)
admin.site.register(Partner)
admin.site.register(AwardPartner)
admin.site.register(Decision)
admin.site.register(SocialLink)

