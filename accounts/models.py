from typing import List

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    objects = UserManager()

    EMAIL_FIELD: str = "username"
    USERNAME_FIELD: str = "username"
    REQUIRED_FIELDS: List[str] = [
        "first_name",
        "last_name",
    ]

    class Meta:
        ordering = ("-id",)
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
