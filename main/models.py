from django.db import models
from django.contrib.auth.models import User

class Questionary(models.Model):
    activeuser = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    questions= models.TextField(null=True)
    option1 = models.TextField(null=True)
    option2 = models.TextField(null=True)
    option3 = models.TextField(null=True)
    option4 = models.TextField(null=True)
    correct_ans = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.title
