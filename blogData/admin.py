from django.contrib import admin

from blogData.models import Article, Comment, Concessionnaire, Vehicule

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)


@admin.register(Concessionnaire)
class ConcessionnaireAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom']  # Masquer siret dans la liste
    list_filter = ['nom']
    search_fields = ['nom']
    fields = ['nom', 'siret']  # Siret reste accessible en édition
    
    def get_readonly_fields(self, request, obj=None):
        # Siret en lecture seule après création pour éviter les erreurs
        if obj:  # Si c'est une modification
            return ['siret']
        return []


@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ['id', 'marque', 'type', 'chevaux', 'prix_ht', 'concessionnaire']
    list_filter = ['type', 'concessionnaire', 'marque']
    search_fields = ['marque', 'concessionnaire__nom']
    fields = ['type', 'marque', 'chevaux', 'prix_ht', 'concessionnaire']
    
    def get_queryset(self, request):
        # Optimisation pour éviter les requêtes N+1
        return super().get_queryset(request).select_related('concessionnaire')