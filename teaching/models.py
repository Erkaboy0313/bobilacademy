from django.db import models
from user.models import Student, Teacher
from django.utils.text import slugify
from eduspace.managers import PaymentManager

class Group(models.Model):
    slug = models.SlugField(unique=True,blank=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=True, null=True)
    students = models.ManyToManyField(Student)
    image = models.ImageField(upload_to="Groups", blank=True, null=True)
    cost = models.IntegerField(default=0,blank=True)
    data_created = models.DateField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return f"{self.name}--{self.teacher.user.first_name}"

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class GroupModul(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='GroupModul', blank=True, null=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.name


class GroupTheme(models.Model):
    modul = models.ForeignKey(
        GroupModul, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    task = models.FileField(upload_to='Group/Files',blank=True, null=True)
    file = models.FileField(upload_to='Group/Files', blank=True, null=True)
    video = models.URLField(null=True)

    def __str__(self):
        return f"{self.modul.id} | {self.name}"

    @property
    def get_url(self):
        try:
            return self.video
        except:
            return ''
    
    @property
    def get_task(self):
        try:
            return self.task.url
        except:
            return ''
    
    @property
    def get_file(self):
        try:
            return self.file.url
        except:
            return ''

class Payment(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.PositiveIntegerField()
    time = models.DateTimeField(auto_now_add=True)

    payment = PaymentManager()
    
    objects = models.Manager()

    def __str__(self):
        return f"{self.id} | {self.student.user.first_name}"
