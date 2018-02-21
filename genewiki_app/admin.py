from django.contrib import admin
from genewiki_app.models import Gene, GO, ExpDB, Project#, ProjectAdmin
# Register your models here.

#class ProjectAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Gene)
admin.site.register(GO)
admin.site.register(Project)
admin.site.register(ExpDB)
