from django.db import models


class ToDo(models.Model):
    title = models.CharField('Title', max_length=64, null=False, blank=False)
    description = models.CharField('Description', max_length=255, null=False, blank=False)
    completed = models.BooleanField('Completed', null=False, blank=False, default=False)
    start_date = models.DateTimeField('Start Date',null=True, blank=True)
    end_date = models.DateTimeField('End Date',null=True, blank=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)
    deleted_at = models.DateTimeField('Deleted At', null=True, blank=True)

    class Meta:
        db_table = 'todo'
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDo'

    def __str__(self):
        return f'{self.id} - {self.title} - {self.description} - {self.completed}'
