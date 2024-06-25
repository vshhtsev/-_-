from django.db import models
from tasks.models import Task, Project


class BugReport(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    project = models.ForeignKey(
        Project,

        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,

        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
        ]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    PRIORITY_CHOICES = [
        ('1', 'очень важно'),
        ('2', 'важно'),
        ('3', 'нормально'),
        ('4', 'ничего страшного'),
        ('5', 'потом сделаем')
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default='1',
    )


class FeatureRequest(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    project = models.ForeignKey(
        Project,
        related_name='feature_requests',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='feature_requests',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    STATUS_CHOICES = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    PRIORITY_CHOICES = [
        ('1', 'очень важно'),
        ('2', 'важно'),
        ('3', 'нормально'),
        ('4', 'ничего страшного'),
        ('5', 'потом сделаем')
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Accepted',
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default='1',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
