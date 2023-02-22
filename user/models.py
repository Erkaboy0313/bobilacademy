from gettext import NullTranslations
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from eduspace.managers import StudentManager, TeacherManager

class CustomUser(AbstractUser):
    TEACHER = 'Teacher'
    STUDENT = 'Student'
    ADMIN = "Admin"

    USER_TYPE = [
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (ADMIN, 'Admin'),
    ]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13, unique=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(
        max_length=7, choices=USER_TYPE, default=STUDENT)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        null=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    @property
    def get_full_name(self) -> str:
        return super().get_full_name()

    def __str__(self):
        return f"{self.first_name}" or f"{self.username} this is admin"


DEKABR = 'Dekabr'
YANVAR = 'Yanvar'
FEVRAL = 'Fevral'
MART = 'Mart'
APREL = 'Aprel'
MAY = 'May'
IYUN = 'Iyun'
IYUL = 'Iyul'
AVGUST = 'Avgust'
SENTYABR = "Sentyabr"
OKTYABR = "Oktyabr"
NOYABR = 'Noyabr'

MONTHS = [
    (YANVAR, 'Yanvar'),
    (FEVRAL, 'Fevral'),
    (MART, 'Mart'),
    (APREL, 'Aprel'),
    (MAY, 'May'),
    (IYUN, 'Iyun'),
    (IYUL, 'Iyul'),
    (AVGUST, 'Avgust'),
    (SENTYABR, "Sentyabr"),
    (OKTYABR, "Oktyabr"),
    (NOYABR, 'Noyabr'),
]


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, default='Bio')
    image = models.ImageField(
        upload_to='Student_images', blank=True, null=True)
    free_months = models.CharField(max_length=10, blank=True, choices=MONTHS, default="NO")
    blocked = models.BooleanField(default=False)

    student = StudentManager()
    
    objects = models.Manager()

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
    @property
    def get_full_name(self):
        return self.user.get_full_name

    @property
    def block_user(self):
        if self.blocked:
            self.blocked = False
        else:
            self.blocked = True
        self.save()
        return self.blocked

    @property
    def add_free_month(self, month):
        if not month in self.free_months:
            self.free_months.append(month)
            self.save()

    def __str__(self):
        return f'{self.user.username} {self.user.last_name}'


class Teacher(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, blank=True, default='Bio')
    image = models.ImageField(
        upload_to='Teacher_images', blank=True, null=True)
    specialization = models.CharField(
        max_length=100, blank=True, default='Jamoa Azosi')
    
    teacher = TeacherManager()
    
    objects = models.Manager()
    
    @property
    def get_full_name(self):
        return self.user.get_full_name
    
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
