from django.contrib import admin
# Register your models here.
from .models import Doubts

class DoubtsAdmin(admin.ModelAdmin):
    list_display=('Ques_ID','Q_Type')
    list_display_links=['Ques_ID']
    search_fields=['Ques_ID','Student']
    list_per_page=25


admin.site.register(Doubts,DoubtsAdmin)