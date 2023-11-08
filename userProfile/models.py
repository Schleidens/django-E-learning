from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.


# validator for bio length
def validate_bio_length(value):
    if len(value) > 2000:
        raise ValidationError('Content is too long, 1000 character max')


class teacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=(
        "Teacher"), related_name="teacher", on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, validators=[validate_bio_length])
    qualifications = models.CharField(max_length=50)
    profile_picture = models.ImageField(
        upload_to="profile/", blank=True)

    def __str__(self):
        return self.user.username


class studentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=(
        "Student"), related_name="student", on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="profile/", blank=True)

    def __str__(self):
        return self.user.username
