from django.db import models
from users.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_projects'
    )

    members = models.ManyToManyField(
        User,
        related_name='member_projects'
    )

    def __str__(self):
        return self.name