from datetime import datetime
from django.db import models

class Entry(models.Model):
    time = models.DateTimeField(default=datetime.now())
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    tags = models.ManyToManyField('EntryTag', blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-time']

class EntryTag(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']