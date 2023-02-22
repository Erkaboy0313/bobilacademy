from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from .managers import ProjectManager, CourseManager
# Create your models here.


class Course(models.Model):
    slug = models.SlugField(unique=True,blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='Course_images', blank=True, null=True)
    price = models.PositiveIntegerField()
    desciption = models.TextField(blank=True, null=True)

    course = CourseManager()
    objects = models.Manager()

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-id"]


class Module(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='Course_images/Modul_images')
    description = models.TextField(blank=True, null=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return f"{self.course.name}--{self.name}"

    class Meta:
        ordering = ["-id"]


class Theme(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.module.id}--{self.name[0:15]}"

    class Meta:
        ordering = ["-id"]


class AboutUs(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='AboutUs', blank=True, null=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'AboutUs'


class Contact(models.Model):
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=50)
    phone1 = models.CharField(max_length=13, blank=True, null=True)
    phone2 = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.email


class Project(models.Model):
    slug = models.SlugField(unique=True,blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="Projects", blank=True, null=True)
    url = models.URLField(max_length=150, blank=True, null=True)

    project = ProjectManager()
    
    objects = models.Manager()

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('project_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-id"]


class News(models.Model):
    slug = models.SlugField(unique=True,blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="News", blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):

        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('News_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'News'
        ordering = ["-id"]

class Sugession(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=13, null=True)
    subject = models.CharField(max_length=100, null=True)
    body = models.TextField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ["-time"]

class Register(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=13, null=True)
    course = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}-{self.course}'