from django.db import models

# This creates a database table.
class Post(models.model):
    title = models.CharField()     # These are columns, find the data type using django docs.
    body = models.TextField()
    date = models.DateTimeField()

    def __str(self):
        return self.title           # Makes sure it returns a string rather than a Post object.
