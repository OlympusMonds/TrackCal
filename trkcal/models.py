from django.db import models
from django.utils import timezone


# Three types - daily, recurring, due


class Task(models.Model):

    name = models.CharField(max_length = 50)
    description = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)

    class Meta:
        abstract = True


class Recurring(Task):
    start_date = models.DateTimeField(blank = True, null = True)
    end_date = models.DateTimeField(blank = True, null = True)
    frequency = models.IntegerField()  # Days, for now


class Daily(Task):
    # TODO: This guy could very easily inherit from recurring, and just set 
    # frequency to be 1 (day). Deal with that later.
    start_date = models.DateTimeField(blank = True, null = True)
    end_date = models.DateTimeField(blank = True, null = True)


class Due(Task):
    due_date = models.DateTimeField(blank = True, null = True)
