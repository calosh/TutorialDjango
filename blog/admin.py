from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('autor','titulo','fecha',)
    search_fields = ('titulo',)
    list_filter = ('fecha',)
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)
    fields = ('titulo','autor','fecha',) # orden de presentacion

    #filter_horizontal = ('autor',) ManyToManyFields
    raw_id_fields = ('autor',) # ForeignKey

admin.site.register(Post, PostAdmin)
