from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db.models import TextChoices
from redis.commands.search.document import Document


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="name of course")
    description = RichTextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Price")
    is_startted = models.BooleanField("Has course the started?", default=False)
    cover = models.ImageField(upload_to="covers/")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField("Name of Module", max_length=255)
    description = RichTextField()
    duration = models.DateField("Duration")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    class LessonTypes(models.TextChoices):
        VIDEO = "video", "Video"
        AUDIO = "audio", "Audio"
        DOCUMENT = "document", "Document"

    title = models.CharField(max_length=255, verbose_name="Name of Lesson")
    file = models.FileField(upload_to="media/", null=True, blank=True)
    _type = models.CharField(max_length=255, verbose_name="Type of lesson", choices=LessonTypes.choices,
                             default=LessonTypes.DOCUMENT)
    body = RichTextField(null=True, blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons")


class CourseReview(models.Model):
    class Rating(models.TextChoices):
        R1 = "1", "1"
        R2 = "2", "2"
        R3 = "3" ,"3"
        R4 = "4", "4"
        R5  ="5", "5"

    user =  models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,null=True,blank=True)
    # course= models.ForeignKey(Course, on_delete=models.CASCADE)
    # modules = models.ForeignKey(Module,on_delete=models.CASCADE)
    comment=RichTextField()
    rating  =  models.CharField(choices=Rating.choices,default=Rating.R5 , max_length=6)
    is_confirmed = models.BooleanField(default=False)
    class Meta:
        verbose_name = "Comment of course"
        verbose_name_plural = "Comment of courses"

    def __str__(self):
        return self.comment

    # Create your models here.
