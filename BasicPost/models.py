'''
2018 DAIA HOME PAGE PROJECT
(Dongguk Artificial Inteligence Association)
For security, Some codes have been removed.
Copyright(c) DAIA_HanSeonung All rights reserved.
Contributor : See the following link
https://github.com/winty95/DAIAweb
'''
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.ImageField(upload_to='%Y/%m/%d/orig', null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Post, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title

# 프로젝트 게시판 table
class ProjectBoard(models.Model):
    title = models.CharField(db_column='Project_title', max_length=100,default="")
    content = models.TextField()
    project_member = models.CharField(db_column='Project_Member', max_length=200,default="")
    origin_date = models.DateTimeField(db_column='Origin_date', blank=True, null=True)
    final_date = models.DateTimeField(db_column='Final_date', blank=True, null=True)
    writer_name = models.CharField(db_column='Writer_name', max_length=10, blank=True, null=True)
    writer_id = models.IntegerField(db_column='Writer_id', blank=True, null=True)
    process = models.BooleanField()
    image = models.ImageField(upload_to='project/%Y/%m/%d/img', null=True, blank=True)
    file=models.FileField(upload_to='project/%Y/%m/%d/file', null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.file.delete()
        super(ProjectBoard, self).delete(*args, **kwargs)

# 세미나 자료 게시판 table
class SeminarBoard(models.Model):
    title = models.CharField(db_column='Title', max_length=100,default="")
    content = models.TextField()
    origin_date = models.DateTimeField(db_column='Origin_date', blank=True, null=True)
    final_date = models.DateTimeField(db_column='Final_date', blank=True, null=True)
    writer_name = models.CharField(db_column='Writer_name', max_length=10, blank=True, null=True)
    writer_id = models.IntegerField(db_column='Writer_id', blank=True, null=True)
    image = models.ImageField(upload_to='seminar/%Y/%m/%d/img', null=True, blank=True)
    file = models.FileField(upload_to='seminar/%Y/%m/%d/file', null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.file.delete()
        super(SeminarBoard, self).delete(*args, **kwargs)

class NoticeBoard(models.Model):
    title = models.CharField(db_column='Title', max_length=100,default="")
    origin_date = models.DateTimeField(db_column='Origin_date', blank=True, null=True)
    final_date = models.DateTimeField(db_column='Final_date', blank=True, null=True)
    writer_name = models.CharField(db_column='Writer_name', max_length=10, blank=True, null=True)
    writer_id = models.IntegerField(db_column='Writer_id', blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='notice/%Y/%m/%d/img', null=True, blank=True)
    file = models.FileField(upload_to='notice/%Y/%m/%d/file', null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.file.delete()
        super(NoticeBoard, self).delete(*args, **kwargs)