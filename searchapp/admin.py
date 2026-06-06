from django.contrib import admin

from .models import (
    SiteVisit,
    bagmodel,
    bagmodel_english_json,
    pantsmodel,
    pantsmodel_english_json,
    shoesmodel,
    shoesmodel_english_json,
    tshirtmodel,
    tshirtmodel_english_desc,
    tshirtmodel_english_json,
)

admin.site.register(SiteVisit)
admin.site.register(tshirtmodel_english_json)
admin.site.register(pantsmodel_english_json)
admin.site.register(bagmodel_english_json)
admin.site.register(shoesmodel_english_json)
admin.site.register(tshirtmodel)
admin.site.register(pantsmodel)
admin.site.register(bagmodel)
admin.site.register(shoesmodel)
admin.site.register(tshirtmodel_english_desc)
