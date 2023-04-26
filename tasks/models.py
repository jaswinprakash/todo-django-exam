from django.db import models


class ToDo(models.Model):
    username = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    add_task = models.CharField(blank=False, null=False, max_length=255)
    is_deleted = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "ToDo"
        verbose_name_plural = "ToDo"

    def __str__(self):
        return self.add_task