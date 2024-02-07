from django.contrib import admin
from .models import Watch, WatchImage, Testimonial
from django.utils.html import format_html


class WatchImageInline(admin.TabularInline):
    model = WatchImage
    extra = 1     # Добавляем еще одно изображение


class WatchAdmin(admin.ModelAdmin):
    inlines = [WatchImageInline]
    list_display = ['brand', 'model', 'case_material', 'color', 'price', 'release_date', 'movement', 'display_base_image']

    def display_base_image(self, obj):
        if not obj.base_image:
            return 'No image'
        return format_html('<img src="{}" width="80 height="80 />', obj.base_image.url)

    display_base_image.short_description = 'Base Image'

admin.site.register(Watch, WatchAdmin)
admin.site.register(Testimonial)