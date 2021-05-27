from django.contrib import admin
from .models import phq9test
from .models import generalized_anxiety
from .models import panicdisorder
from .models import post_traumaticstress
from .models import major_depressive
from .models import manic_episodes

class phq9_date(admin.ModelAdmin):
    readonly_fields = ('date_taken',)

class generalized_anxiety_date(admin.ModelAdmin):
    readonly_fields = ('date_taken',)

class panicdisorder_date(admin.ModelAdmin):
    readonly_fields = ('date_taken',)

class post_traumaticstress_date(admin.ModelAdmin):
    readonly_fields = ('date_taken',)

class major_depressive_date(admin.ModelAdmin):
    readonly_fields = ('date_taken',)

class manic_episodes_date(admin.ModelAdmin):
    readonly_fields = ('date_taken',)

admin.site.register(phq9test,phq9_date)
admin.site.register(generalized_anxiety,generalized_anxiety_date)
admin.site.register(panicdisorder,panicdisorder_date)
admin.site.register(post_traumaticstress,post_traumaticstress_date)
admin.site.register(major_depressive,major_depressive_date)
admin.site.register(manic_episodes,manic_episodes_date)
