from django.contrib import admin

from .models import Workers
from .models import Professions
from .models import WorkerProfession


class WorkersInstanceInline(admin.TabularInline):
    model = WorkerProfession


class ProfessionsInstanceInline(admin.TabularInline):
    model = WorkerProfession


class WorkersModelAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'created_at', 'updated']
    inlines = [WorkersInstanceInline]

    class Meta:
        model = Workers


class ProfessionsModelAdmin(admin.ModelAdmin):
    list_display = ['profession']
    inlines = [ProfessionsInstanceInline]

    class Meta:
        model = Professions


class WorkerProfessionModelAdmin(admin.ModelAdmin):
    list_display = ['worker', 'prof']

    class Meta:
        model = WorkerProfession


admin.site.register(Workers, WorkersModelAdmin)
admin.site.register(Professions, ProfessionsModelAdmin)
admin.site.register(WorkerProfession, WorkerProfessionModelAdmin)
