from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoryModel(models.Model):
    cat = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    def __str__(self):
        return self.cat



class TasksModel(models.Model):
    tname = models.CharField(max_length=30)
    desc = models.TextField(max_length=200)
    tadded_at = models.DateTimeField(auto_now_add=True)
    tstatus = models.BooleanField(default=False)
    cat = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.tname


