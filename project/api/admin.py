from django.contrib import admin
from .models import Client, Project

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'created_at', 'created_by', 'updated_at')
    search_fields = ('client_name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'client', 'created_at', 'created_by')
    search_fields = ('project_name', 'client__client_name')
    filter_horizontal = ('users',)  # To use a better UI for ManyToMany fields

# Alternatively, you can use the following approach if you prefer:
# admin.site.register(Client, ClientAdmin)
# admin.site.register(Project, ProjectAdmin)
