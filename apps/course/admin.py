from django.contrib import admin

from apps.course.models import Course, Module, Lesson, CourseReview


@admin.register(Course)
class CourseRegisterAdmin(admin.ModelAdmin):
    list_display = ("id", "get_custom_price", "is_startted")
    search_fields = ("title",)
    list_filter = ("is_startted",)

    def get_custom_price(self, obj):
        if obj:
            return f"$ {obj.price}"
        return obj

    get_custom_price.short_description = "price"


@admin.register(Module)
class ModuleRegisterAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "duration", "course")
    search_fields = ("title",)
    list_filter = ("course",)
    autocomplete_fields = ("course",)


@admin.register(Lesson)
class LessonRegisterAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "_type", "module")
    search_fields = ("title",)
    list_filter = ("module", "module__course")
    autocomplete_fields = ("module",)


@admin.register(CourseReview)
class CoursereviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "rating", "is_confirmed", "comment")
    list_editable = ("is_confirmed",)
    search_fields = ("user.fullname", "comment")
    list_filter = ("is_confirmed", "rating")

    # def has_add_permission(self,request):
    #     return False
    def has_delete_permission(self,request, obj=None):
        return False

# Register your models here.
