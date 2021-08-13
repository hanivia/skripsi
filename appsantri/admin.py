from django.contrib import admin
from .models import Santri, Pesan
from import_export.admin import ImportExportModelAdmin
from import_export import resources

admin.site.register(Pesan)

# Mengatur yang di import dan export
class SantriResource(resources.ModelResource):
    class Meta:
        model = Santri
        exclude = ('foto')
# Mengatur yang di import dan export


class SantriAdmin(ImportExportModelAdmin):
    resource_class = SantriResource
admin.site.register(Santri, SantriAdmin)
