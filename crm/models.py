from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )
    group = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.group})"


class Document(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Черновик"
        REVIEW = "review", "На проверке"
        APPROVED = "approved", "Одобрено"

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="documents"
    )
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/")
    status = models.CharField(
        max_length=32,
        choices=Status.choices,
        default=Status.DRAFT
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
